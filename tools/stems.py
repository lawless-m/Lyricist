#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["librosa", "soundfile", "numpy", "essentia"]
# ///
"""Separate stems via the Demucks server, then derive the bar grid the mixer needs.

Usage:
  tools/stems.py playlists/laundry            # separate + analyse anything uncached
  tools/stems.py playlists/laundry --force    # redo everything
  tools/stems.py playlists/laundry --limit 3  # try a few first
  tools/stems.py --show playlists/laundry     # print what's cached

Needs the Demucks server running:
  cd /home/matt/Git/Demucks && .venv/bin/python run_server.py

Stems land in audio/stems/<clipid>/ and the derived analysis in audio/stems.json,
kept separate from audio/analysis.json so the existing tooling is untouched.

Why this exists rather than extending analyse.py: bar arithmetic needs a beat grid
you can extrapolate, and librosa's per-frame beat list drifts and contains inserted
and dropped beats. Here the period comes from essentia's PercivalBpmEstimator and
only the phase is fitted, against an isolated drum stem rather than a full mix. That
isolation is what makes downbeat detection possible at all — kick-on-one is a strong
signal once the guitars are gone and a hopeless one before.

Tempo is the part that fought back; see the comment on PERCIVAL below for the two
approaches that were tried and thrown away before this one.
"""

import argparse
import json
import shutil
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
AUDIO = REPO / "audio"
STEMS = AUDIO / "stems"
CACHE = AUDIO / "stems.json"
DEMUCKS = "http://127.0.0.1:8766"
START_HINT = ("Demucks is not answering on 127.0.0.1:8766. Start it with:\n"
              "  cd /home/matt/Git/Demucks && .venv/bin/python run_server.py")

HOP = 512
WANT = ("drums", "vocals", "other")   # bass is unused; see the design doc
MODEL = "htdemucs_ft"                 # slower than htdemucs, cleaner stems, one-off cost

# Tempo. Three sources disagreed and none could be trusted alone: librosa read
# part-it-out as 129 (its grid scores 1.08, i.e. noise) but scroll-up correctly at
# 152; tempo-cnn read part-it-out correctly at 98 but halved scroll-up to 76, and
# read finna-retard as 184 against a hand check of 93.
#
# Octave error is not cosmetic. At 184 instead of 92 the period is 0.33s, so a "bar"
# is 1.3s of a real 2.6s bar: filler lengths halve, the downbeat search finds
# half-bars, and ordering flings the track to the fast extreme and manufactures a
# cliff either side of it.
#
# Settled by using the same estimator the user's reference tool uses. tunebat.com's
# Analyzer has no upload API because it runs entirely in the browser; its worker is
# fifteen lines and calls essentia's PercivalBpmEstimator at these exact parameters.
# So we run the identical algorithm locally instead of posting anything anywhere.
# It returns 91.5 where tunebat showed 93, and settles the other two disputes in
# opposite directions.
#
# Two earlier attempts were thrown away and are recorded so they are not retried:
# folding into a canonical band (cannot tell a real 76 from a halved 152, and cannot
# reach the 3:2 error in finna-retard), and scoring a kick-on-1-and-3 backbeat over
# candidate octaves (scored 0.24-0.45 against 0.25 for chance — this material puts
# the kick on one class, not two, so the test measured nothing).
PERCIVAL = dict(frameSize=1024, frameSizeOSS=2048, hopSize=128, hopSizeOSS=128,
                maxBPM=210, minBPM=50, sampleRate=16000)
OVERRIDES = AUDIO / "bpm-overrides.json"   # {clip_id: bpm}, wins over everything

# Vocal activity thresholds. Tuned so a held note and the gap before the next line
# stay in one span, rather than shattering every phrase into fragments.
VOX_DB = -35.0        # below the track's own 99th-percentile vocal level
VOX_GAP = 0.40        # merge spans closer together than this (seconds)
VOX_MIN = 0.30        # drop spans shorter than this


def clip_id(path):
    return path.stem.rsplit("--", 1)[-1]


def sources():
    """Same keying as mixtape.py: 'laundry' or 'playlists/laundry'."""
    out = {}
    if not AUDIO.exists():
        return out
    for d in sorted(AUDIO.iterdir()):
        if not d.is_dir() or d.name in ("mixes", "stems", "fillers"):
            continue
        if d.name == "playlists":
            for p in sorted(d.iterdir()):
                if p.is_dir() and any(p.glob("*.wav")):
                    out[f"playlists/{p.name}"] = sorted(p.glob("*.wav"))
        elif any(d.glob("*.wav")):
            out[d.name] = sorted(d.glob("*.wav"))
    return out


def post(path, payload, timeout):
    req = urllib.request.Request(
        DEMUCKS + path, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def separate(track, model):
    """-> ({stem name: Path}, bpm). Stem names come from the returned filenames."""
    r = post("/separate", {"path": str(track), "model": model}, timeout=1800)
    found = {}
    for f in r.get("stems", []):
        p = Path(f)
        low = p.stem.lower()
        for name in ("drums", "vocals", "bass", "other"):
            if name in low:
                found[name] = p
    return found, r.get("bpm")


GRID_WIN = 0.05        # +/- seconds around a beat that counts as "on the grid"


def fit_grid(onset, sr, bpm, duration):
    """Period comes in decided; fit only the phase, maximising on-grid onset energy.

    Returns (t0, period, score, contrast).

    Score is *enrichment*: the share of total onset energy landing near a beat, over
    the share of the timeline those windows occupy. 1.0 means the grid explains no
    more than random placement would.

    Enrichment rather than mean-onset-on-beat, which looks like the obvious metric
    and is not: it rewards coarse grids for sampling fewer but stronger points, so
    a half-time grid outscores the true one (measured 5.27 at 49bpm against 4.39 at
    the correct 98).

    NEITHER number may be used to choose a tempo. Enrichment still prefers 49 over
    the true 98 (1.97 vs 1.66), and always will: a half-time grid is a subset of the
    real one in which every point is a strong downbeat, so precision-style metrics
    reward it for the beats it never has to explain. Percival owns the tempo.

    Contrast is best-phase over median-phase enrichment at the *same* period, which
    is scale-fair because it never compares two tempos. It answers the only question
    the fit can honestly answer: does this period have a phase it prefers? Near 1.0
    means it does not, so treat the grid as untrustworthy however high the score.
    """
    import numpy as np
    period = 60.0 / bpm
    frames_per_sec = sr / HOP
    win = max(1, int(round(GRID_WIN * frames_per_sec)))
    total = float(onset.sum()) or 1e-9

    best, all_scores = (0.0, -1.0), []
    for t0 in np.arange(0.0, period, 0.005):
        idx = np.round(np.arange(t0, duration, period) * frames_per_sec).astype(int)
        idx = idx[(idx >= 0) & (idx < len(onset))]
        if idx.size < 4:
            continue
        mask = np.zeros(len(onset), dtype=bool)
        for d in range(-win, win + 1):
            j = idx + d
            mask[j[(j >= 0) & (j < len(onset))]] = True
        covered = mask.sum() / len(onset)
        if covered <= 0:
            continue
        score = (float(onset[mask].sum()) / total) / covered
        all_scores.append(score)
        if score > best[1]:
            best = (float(t0), score)
    median = float(np.median(all_scores)) if all_scores else 1e-9
    return best[0], period, round(best[1], 3), round(best[1] / max(median, 1e-9), 3)


KICK_HZ = (0, 120)          # kick fundamental
def kick_band(y, sr):
    """Kick onset envelope from an isolated drums stem."""
    import librosa
    import numpy as np
    mel = librosa.feature.melspectrogram(y=y, sr=sr, hop_length=HOP, n_mels=96, fmax=4000)
    freqs = librosa.mel_frequencies(n_mels=96, fmax=4000)

    def env(lo, hi):
        band = mel[(freqs >= lo) & (freqs < hi)].sum(axis=0)
        return np.maximum(0.0, np.diff(band, prepend=band[0]))

    return env(*KICK_HZ)


def downbeat_phase(kick, sr, t0, period, duration):
    """Which beat class mod 4 carries the kick, from the isolated drums.

    Plain kick concentration. This part works and works decisively — part-it-out
    profiles as [0.21, 0.59, 0.02, 0.19], an unambiguous winner. It is only the
    tempo octave that resisted every measurement; the downbeat never did, and the
    two are separable problems.
    """
    import numpy as np
    idx = np.round(np.arange(t0, duration, period) * sr / HOP).astype(int)
    idx = idx[(idx >= 0) & (idx < len(kick))]
    if idx.size < 8:
        return 0, [0.0] * 4
    k = np.array([kick[idx[n::4]].mean() for n in range(4)])
    k = k / (k.sum() or 1e-9)
    return int(np.argmax(k)), [round(float(x), 3) for x in k]


def percival_bpm(path):
    """tunebat.com/Analyzer's estimator, at tunebat.com/Analyzer's parameters."""
    import essentia.standard as es
    audio = es.MonoLoader(filename=str(path), sampleRate=PERCIVAL["sampleRate"])()
    return float(es.PercivalBpmEstimator(**PERCIVAL)(audio))


def essentia_key(path):
    """-> (key, scale, strength). Replaces the Krumhansl correlation in analyse.py."""
    import essentia.standard as es
    audio = es.MonoLoader(filename=str(path), sampleRate=16000)()
    k, scale, strength = es.KeyExtractor(sampleRate=16000)(audio)
    return k, scale, round(float(strength), 3)


def vocal_spans(y, sr):
    """Contiguous stretches where the vocal stem is actually sounding."""
    import librosa
    import numpy as np
    rms = librosa.feature.rms(y=y, hop_length=HOP)[0]
    ref = float(np.percentile(rms, 99)) or 1e-9
    db = 20.0 * np.log10(np.maximum(rms, 1e-9) / ref)
    active = db > VOX_DB
    hop_s = HOP / sr

    spans, start = [], None
    for i, a in enumerate(active):
        if a and start is None:
            start = i
        elif not a and start is not None:
            spans.append([start * hop_s, i * hop_s])
            start = None
    if start is not None:
        spans.append([start * hop_s, len(active) * hop_s])

    merged = []
    for s in spans:
        if merged and s[0] - merged[-1][1] <= VOX_GAP:
            merged[-1][1] = s[1]
        else:
            merged.append(s)
    return [[round(a, 3), round(b, 3)] for a, b in merged if b - a >= VOX_MIN]


def bar_energy(y, sr, t0, period, phase):
    """RMS of the drums stem per bar, from the first downbeat. Feeds filler picking."""
    import numpy as np
    bar = period * 4
    first = t0 + phase * period
    out = []
    t = first
    while t + bar <= len(y) / sr:
        seg = y[int(t * sr):int((t + bar) * sr)]
        out.append(round(float(np.sqrt(np.mean(seg ** 2))), 5))
        t += bar
    return first, out


def analyse(stem_paths, bpm, cnn_bpm=None):
    """Tempo is decided before we get here; fit the phase and the bar to it."""
    import librosa

    drums, sr = librosa.load(str(stem_paths["drums"]), mono=True)
    duration = len(drums) / sr
    kick = kick_band(drums, sr)

    # Fit the phase to the KICK, not the general onset envelope. On dense electronic
    # material the onset envelope has energy on every 8th and 16th, so sliding the
    # grid half a beat still lands on hits and the fit barely peaks — contrast sat at
    # 1.04-1.15 on 28 of 37 tracks. The kick is sparse and decisive. Switching lifted
    # part-it-out from 1.06 to 1.61 and moved its phase 130ms; the-app-says-im-resting
    # moved 390ms, two thirds of a beat, i.e. the old grid was simply in the wrong
    # place. Fall back to onsets only where the kick is too quiet to fit.
    onset = librosa.onset.onset_strength(y=drums, sr=sr, hop_length=HOP)
    envelope, basis = (kick, "kick") if kick.sum() > 0 else (onset, "onset")
    t0, period, score, contrast = fit_grid(envelope, sr, bpm, duration)
    if contrast < 1.05 and basis == "kick":
        t0b, _, scoreb, contrastb = fit_grid(onset, sr, bpm, duration)
        if contrastb > contrast:
            t0, score, contrast, basis = t0b, scoreb, contrastb, "onset"
    phase, phase_scores = downbeat_phase(kick, sr, t0, period, duration)
    first_downbeat, bars = bar_energy(drums, sr, t0, period, phase)

    vox, _ = librosa.load(str(stem_paths["vocals"]), mono=True)
    spans = vocal_spans(vox, sr)
    sung = sum(b - a for a, b in spans)

    return {
        "bpm": round(float(bpm), 2),            # what the mixer uses
        "bpm_cnn": round(float(cnn_bpm), 2) if cnn_bpm else None,   # kept for comparison
        "duration": round(duration, 3),
        "grid": {"t0": round(t0, 4), "period": round(period, 6)},
        "grid_score": score,
        "grid_contrast": contrast,
        "grid_basis": basis,
        "downbeat_phase": phase,
        "kick_profile": phase_scores,
        "first_downbeat": round(first_downbeat, 4),
        "vocal_spans": spans,
        "vocal_density": round(sung / duration, 3) if duration else 0.0,
        "bar_energy": bars,
    }


def run_analysis(cid, track, kept, cnn_bpm, overrides):
    """Override wins, else Percival on the original mix. -> (analysis, note)."""
    if cid in overrides:
        bpm, note = float(overrides[cid]), f"override {float(overrides[cid]):.0f}"
    else:
        bpm = percival_bpm(track)
        note = f"cnn said {cnn_bpm:.0f}" if cnn_bpm and abs(bpm - cnn_bpm) > 1.0 else ""
    a = analyse(kept, bpm, cnn_bpm=cnn_bpm)
    a["key"], a["scale"], a["key_strength"] = essentia_key(track)
    return a, note


def suspect(cid, a, librosa_bpm):
    """Why this track is worth pasting into tunebat.com/Analyzer. '' if it isn't."""
    reasons = []
    if a["grid_contrast"] < 1.3:
        reasons.append(f"weak grid ({a['grid_contrast']:.2f})")
    if abs(a["bpm"] - a["bpm_cnn"]) > 0.5:
        reasons.append(f"cnn said {a['bpm_cnn']:.0f}")
    old = librosa_bpm.get(cid)
    if old:
        r = a["bpm"] / old
        if not any(abs(r - k) < 0.04 for k in (0.25, 0.5, 1.0, 2.0, 4.0)):
            reasons.append(f"librosa said {old:.0f}")
    return "; ".join(reasons)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", nargs="?", default="playlists/laundry")
    ap.add_argument("--model", default=MODEL)
    ap.add_argument("--keep", default=",".join(WANT))
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--show", metavar="SOURCE")
    ap.add_argument("--reanalyse", action="store_true",
                    help="redo the analysis from cached stems; no GPU, no Demucks")
    ap.add_argument("--check", action="store_true",
                    help="list tracks whose tempo is worth verifying by hand")
    args = ap.parse_args()

    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    overrides = json.loads(OVERRIDES.read_text()) if OVERRIDES.exists() else {}
    old_cache = AUDIO / "analysis.json"
    librosa_bpm = {k: v["bpm"] for k, v in json.loads(old_cache.read_text()).items()
                   if v.get("bpm")} if old_cache.exists() else {}

    if args.check:
        tracks = sources().get(args.source) or sys.exit(f"no such source: {args.source}")
        rows = [(t, cache[clip_id(t)]) for t in tracks if clip_id(t) in cache]
        flagged = [(t, a, r) for t, a in rows if (r := suspect(clip_id(t), a, librosa_bpm))]
        print(f"{len(rows)} analysed, {len(flagged)} worth checking on tunebat.com/Analyzer\n")
        for t, a, r in flagged:
            print(f"  {a['bpm']:6.1f}bpm  {t.stem[:44]:44}  {r}")
        if flagged:
            print(f"\nPut corrections in {OVERRIDES.relative_to(REPO)} as "
                  '{"<clipid>": 93.0} then: tools/stems.py --reanalyse')
        return

    if args.reanalyse:
        tracks = sources().get(args.source) or sys.exit(f"no such source: {args.source}")
        done = 0
        for t in tracks:
            cid = clip_id(t)
            a = cache.get(cid)
            if not a or "stems" not in a:
                continue
            kept = {k: REPO / v for k, v in a["stems"].items()}
            if not kept.get("drums", Path("/nonexistent")).exists():
                print(f"  ! stems missing for {t.stem}", file=sys.stderr)
                continue
            new, note = run_analysis(cid, t, kept, a.get("bpm_cnn"), overrides)
            new["stems"] = a["stems"]
            cache[cid] = new
            done += 1
            print(f"  {t.stem[:44]:44} {new['bpm']:6.1f}bpm  grid {new['grid_score']:.2f}/"
                  f"{new['grid_contrast']:.2f}  db {new['downbeat_phase']}"
                  + (f"  {note}" if note else ""))
        CACHE.write_text(json.dumps(cache, indent=1))
        print(f"reanalysed {done} tracks from cached stems (no GPU touched)")
        return

    if args.show:
        tracks = sources().get(args.show)
        if not tracks:
            sys.exit(f"no such source: {args.show}")
        print(f"{'track':40} {'bpm':>6} {'grid':>5} {'ctr':>5} {'db':>3} {'vox%':>6} spans")
        for t in tracks:
            a = cache.get(clip_id(t))
            if not a:
                print(f"{t.stem[:40]:40}  (not separated)")
                continue
            print(f"{t.stem[:40]:40} {a['bpm_cnn']:6.1f} {a['grid_score']:5.2f} "
                  f"{a['grid_contrast']:5.2f} {a['downbeat_phase']:3} "
                  f"{a['vocal_density']*100:5.1f}% {len(a['vocal_spans']):5}")
        return

    tracks = sources().get(args.source)
    if not tracks:
        sys.exit(f"no such source: {args.source}")

    try:
        urllib.request.urlopen(DEMUCKS + "/healthz", timeout=5).read()
    except (urllib.error.URLError, OSError):
        sys.exit(START_HINT)

    keep = [k.strip() for k in args.keep.split(",") if k.strip()]
    todo = [t for t in tracks if args.force or clip_id(t) not in cache]
    if args.limit:
        todo = todo[:args.limit]
    print(f"{args.source}: {len(tracks)} tracks, {len(todo)} to do "
          f"(model {args.model}, keeping {'+'.join(keep)})")

    STEMS.mkdir(parents=True, exist_ok=True)
    for i, track in enumerate(todo, 1):
        cid = clip_id(track)
        print(f"[{i}/{len(todo)}] {track.stem}", flush=True)
        try:
            produced, bpm = separate(track, args.model)
        except urllib.error.URLError as e:
            sys.exit(f"{START_HINT}\n\n(lost the server mid-run: {e})")
        if "drums" not in produced or "vocals" not in produced:
            print(f"    skipped: got only {sorted(produced)}", file=sys.stderr)
            continue
        if not bpm:
            print("    skipped: no bpm from the tempo sidecar", file=sys.stderr)
            continue

        dest = STEMS / cid
        dest.mkdir(parents=True, exist_ok=True)
        kept = {}
        for name, src in produced.items():
            if name in keep:
                target = dest / f"{name}.wav"
                shutil.move(str(src), target)
                kept[name] = target
            else:
                src.unlink(missing_ok=True)

        try:
            a, _ = run_analysis(cid, track, kept, bpm, overrides)
        except Exception as e:
            print(f"    analysis failed: {e}", file=sys.stderr)
            continue
        a["stems"] = {k: str(v.relative_to(REPO)) for k, v in kept.items()}
        cache[cid] = a
        CACHE.write_text(json.dumps(cache, indent=1))
        flag = suspect(cid, a, librosa_bpm)
        print(f"    {a['bpm']:.1f}bpm  grid {a['grid_score']:.2f}/{a['grid_contrast']:.2f}  "
              f"downbeat {a['downbeat_phase']}  vox {a['vocal_density']*100:.0f}%"
              + (f"  [{flag}]" if flag else ""))

    try:
        post("/request-unload", {}, timeout=60)
        print("asked Demucks to unload (VRAM back to ComfyUI)")
    except Exception:
        pass
    print(f"wrote {CACHE.relative_to(REPO)} ({len(cache)} tracks)")


if __name__ == "__main__":
    main()
