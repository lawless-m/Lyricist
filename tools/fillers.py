#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["librosa", "soundfile", "numpy"]
# ///
"""Cut a bank of loopable breakbeats from the isolated drum stems.

Usage:
  tools/fillers.py                      # cut the bank
  tools/fillers.py --per-track 2        # take two from each track, not one
  tools/fillers.py --bars 4             # shorter loops
  tools/fillers.py --show               # print the bank without recutting

Reads audio/stems.json (needs tools/stems.py to have run) and writes
audio/fillers/<bpm>-<clip>-b<bar>.wav plus an index at audio/fillers/index.json.

Drums only, deliberately. Bass and pads are pitched, so a filler carrying them has
a key and can clash with whatever it is bridging. A keyless filler bridges any
harmonic jump, which is the whole point of having one — and it matters more here
than usual, because 21 of the 37 laundry tracks are in F minor, so the harmonic
term has almost nothing to say and the filler is doing the joining.

Scoring is cheap because tools/stems.py already cached per-bar drum RMS, so window
selection never touches the audio — only the winning window is decoded and written.
"""

import argparse
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
AUDIO = REPO / "audio"
STEMS_CACHE = AUDIO / "stems.json"
FILLERS = AUDIO / "fillers"
INDEX = FILLERS / "index.json"

SEAM_MS = 10.0          # micro-fade each end so the loop point doesn't click
TARGET_RMS = 0.10       # level-match the bank; fillers come from tracks mastered apart
EDGE_BARS = 2           # ignore the first and last couple of bars of a track


def score_windows(bars, n):
    """Rank every n-bar window on being busy, steady, and self-similar across halves.

    Busy alone picks the loudest bar of the loudest chorus, which is usually a fill
    or a crash rather than a groove. Steady alone picks silence. Self-similarity
    across the two halves is what makes it survive repetition — a window whose second
    half differs from its first announces the seam every time round.
    """
    import numpy as np
    a = np.asarray(bars, dtype=float)
    out = []
    peak = float(a.max()) or 1e-9
    half = n // 2
    for i in range(EDGE_BARS, len(a) - n - EDGE_BARS + 1):
        w = a[i:i + n]
        m = float(w.mean())
        if m <= 0:
            continue
        busy = m / peak
        steady = 1.0 - min(1.0, float(w.std()) / m)
        h1, h2 = float(w[:half].mean()), float(w[half:].mean())
        similar = 1.0 - min(1.0, abs(h1 - h2) / max(h1, h2, 1e-9))
        out.append((busy * steady * similar, i, busy, steady, similar))
    out.sort(key=lambda r: -r[0])
    return out


def cut(drums_path, start_s, length_s, sr_out=None):
    """Decode just the winning window, level-match it, and micro-fade the seam."""
    import librosa
    import numpy as np
    y, sr = librosa.load(str(drums_path), mono=True, offset=start_s, duration=length_s)
    if y.size == 0:
        return None, 0
    rms = float(np.sqrt(np.mean(y ** 2))) or 1e-9
    y = y * min(TARGET_RMS / rms, 0.99 / (float(np.abs(y).max()) or 1e-9))
    seam = max(1, int(sr * SEAM_MS / 1000.0))
    ramp = np.linspace(0.0, 1.0, seam)
    y[:seam] *= ramp
    y[-seam:] *= ramp[::-1]
    return y, sr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bars", type=int, default=8)
    ap.add_argument("--per-track", type=int, default=1)
    ap.add_argument("--show", action="store_true")
    args = ap.parse_args()

    if args.show:
        if not INDEX.exists():
            raise SystemExit("no bank yet — run tools/fillers.py")
        bank = json.loads(INDEX.read_text())
        print(f"{'bpm':>6} {'bars':>4} {'secs':>6}  {'busy':>5} {'stdy':>5} {'sim':>5} "
              f"{'score':>5}  source")
        for f in sorted(bank, key=lambda f: f["bpm"]):
            print(f"{f['bpm']:6.1f} {f['bars']:4} {f['seconds']:6.2f}  {f['busy']:5.2f} "
                  f"{f['steady']:5.2f} {f['similar']:5.2f} {f['score']:5.2f}  {f['source']}")
        print(f"\n{len(bank)} fillers, "
              f"{min(f['bpm'] for f in bank):.0f}-{max(f['bpm'] for f in bank):.0f}bpm")
        return

    if not STEMS_CACHE.exists():
        raise SystemExit("no audio/stems.json — run tools/stems.py first")
    cache = json.loads(STEMS_CACHE.read_text())
    FILLERS.mkdir(parents=True, exist_ok=True)

    import soundfile as sf

    bank = []
    for cid, a in sorted(cache.items(), key=lambda kv: kv[1]["bpm"]):
        bars = a.get("bar_energy") or []
        if len(bars) < args.bars + 2 * EDGE_BARS + 1:
            continue
        drums = REPO / a["stems"]["drums"]
        if not drums.exists():
            continue

        bar_s = a["grid"]["period"] * 4
        ranked = score_windows(bars, args.bars)
        taken = []
        for score, i, busy, steady, similar in ranked:
            if len(taken) >= args.per_track:
                break
            if any(abs(i - j) < args.bars for j in taken):   # don't take overlaps
                continue
            taken.append(i)

            start = a["first_downbeat"] + i * bar_s
            length = args.bars * bar_s
            y, sr = cut(drums, start, length)
            if y is None:
                continue
            name = f"{a['bpm']:06.2f}-{args.bars:02d}bar-{cid}-b{i:03d}.wav"
            sf.write(str(FILLERS / name), y, sr)
            bank.append({
                "file": name, "clip": cid, "bpm": a["bpm"], "bars": args.bars,
                "bar": i, "seconds": round(length, 3), "score": round(score, 3),
                "busy": round(busy, 3), "steady": round(steady, 3),
                "similar": round(similar, 3),
                "source": drums.parent.name if drums.parent.name != cid else cid,
            })

    # Label each filler with its track's slug rather than the clip id, which is
    # unreadable in a table. Looked up from the playlist filenames.
    slugs = {}
    for w in (AUDIO / "playlists" / "laundry").glob("*.wav"):
        slugs[w.stem.rsplit("--", 1)[-1]] = w.stem.split("--")[0]
    for f in bank:
        f["source"] = slugs.get(f["clip"], f["clip"])

    # The bank holds several loop lengths at once — 4-bar for bridges, 8-bar for rests
    # and the drag — so merge rather than overwrite, replacing only this length.
    existing = json.loads(INDEX.read_text()) if INDEX.exists() else []
    merged = [f for f in existing if f.get("bars") != args.bars] + bank
    INDEX.write_text(json.dumps(merged, indent=1))
    lengths = sorted({f["bars"] for f in merged})
    print(f"cut {len(bank)} x {args.bars}-bar fillers into {FILLERS.relative_to(REPO)} "
          f"({len(merged)} in the bank, lengths {lengths})")


if __name__ == "__main__":
    main()
