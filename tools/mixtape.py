#!/usr/bin/env python3
"""Render one continuous mix per band or playlist, with a tracklist.

Usage:
  tools/mixtape.py --list                              # sources available locally
  tools/mixtape.py playlists/laundry                   # plain 4s crossfades
  tools/mixtape.py playlists/laundry --beat-align      # (1) crossfades a whole number of beats
  tools/mixtape.py playlists/laundry --tempo-match     # (2) nudge tempos together over the blend
  tools/mixtape.py playlists/the-bell --harmonic       # (3) reorder by key compatibility
  tools/mixtape.py playlists/cherry --beat-align --tempo-match --harmonic     # combine freely

The three modes are independent and compose. Pick per source: rhythmic material
(laundry, cherry, slg) takes 1+2 well; rubato material (the-bell) is better
served by 3 alone. That choice is yours per source — there is no auto-detection,
because a beat tracker reports a confident grid for free-time accordion too.

Needs tools/analyse.py to have been run for anything except plain crossfades.

Honest about what this is: beat-*aligned*, not phase-locked. Crossfades last a
whole number of beats and tracks start on a beat, which removes the worst of the
drift, but it is not sample-accurate beatmatching of the kind a DJ does by ear.
"""

import argparse
import json
import random
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
AUDIO = REPO / "audio"
MIXES = AUDIO / "mixes"
CACHE = AUDIO / "analysis.json"

# No automatic "is this rhythmic enough" gate: two attempts at one (inter-beat
# regularity, then beat salience) failed to separate programmed drums from solo
# accordion — librosa reports a confident grid either way. You pick the modes per
# playlist instead, which is both honest and what was asked for. The stretch
# clamp below is kept because it is arithmetic rather than inference.
MAX_STRETCH = 0.12         # never shift tempo by more than ±12%


def duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(path)],
        capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def hms(seconds, force_hours=False):
    """YouTube chapter format: M:SS under an hour, H:MM:SS above."""
    s = int(seconds)
    if s >= 3600 or force_hours:
        return f"{s // 3600}:{(s % 3600) // 60:02d}:{s % 60:02d}"
    return f"{s // 60}:{s % 60:02d}"


def clip_id(path):
    return path.stem.rsplit("--", 1)[-1]


def sources():
    """Keyed by path under audio/: 'laundry' (by band) or 'playlists/laundry'
    (your Suno playlist, whose NN- filename prefix preserves your running order)."""
    if not AUDIO.exists():
        return {}
    out = {}
    for d in sorted(AUDIO.iterdir()):
        if not d.is_dir() or d.name == "mixes":
            continue
        if d.name == "playlists":
            for p in sorted(d.iterdir()):
                if p.is_dir() and any(p.glob("*.wav")):
                    out[f"playlists/{p.name}"] = sorted(p.glob("*.wav"))
        elif any(d.glob("*.wav")):
            out[d.name] = sorted(d.glob("*.wav"))
    return out


def camelot_distance(a, b):
    """0 = same key, 1 = neighbour or relative major/minor, higher = rougher."""
    if not a or not b or a == "?" or b == "?":
        return 3
    if a == b:
        return 0
    na, ma = int(a[:-1]), a[-1]
    nb, mb = int(b[:-1]), b[-1]
    if na == nb:
        return 1                                    # relative major/minor
    step = min((na - nb) % 12, (nb - na) % 12)
    return step if ma == mb else step + 1


def harmonic_order(tracks, info):
    """Greedy nearest-neighbour walk around the Camelot wheel, tempo as tiebreak."""
    remaining = list(tracks)
    ordered = [remaining.pop(0)]
    while remaining:
        cur = info.get(clip_id(ordered[-1]), {})
        def cost(t):
            a = info.get(clip_id(t), {})
            d = camelot_distance(cur.get("camelot"), a.get("camelot"))
            bpm_gap = abs(a.get("bpm", 0) - cur.get("bpm", 0)) / 100.0
            return (d, bpm_gap)
        remaining.sort(key=cost)
        ordered.append(remaining.pop(0))
    return ordered


def prepare(track, info, target_bpm, tmpdir, beat_align, tempo_match):
    """Optionally trim to the first beat and stretch toward the target tempo."""
    a = info.get(clip_id(track))
    filters, notes = [], []
    start = 0.0

    if beat_align and a and a["beats"]:
        start = a["beats"][0]
        if start > 0.001:
            notes.append(f"trim {start:.2f}s to first beat")

    if tempo_match and a and target_bpm and a["bpm"] > 0:
        ratio = target_bpm / a["bpm"]
        if abs(ratio - 1.0) <= MAX_STRETCH:
            if abs(ratio - 1.0) > 0.001:
                filters.append(f"atempo={ratio:.5f}")
                notes.append(f"{a['bpm']:.0f}->{target_bpm:.0f}bpm")
        else:
            notes.append(f"{a['bpm']:.0f}bpm left alone (>{int(MAX_STRETCH*100)}% away)")

    if not filters and start == 0.0:
        return track, notes

    out = Path(tmpdir) / f"prep-{track.stem}.wav"
    cmd = ["ffmpeg", "-nostdin", "-loglevel", "error", "-y"]
    if start:
        cmd += ["-ss", f"{start:.4f}"]
    cmd += ["-i", str(track)]
    if filters:
        cmd += ["-filter:a", ",".join(filters)]
    cmd += ["-c:a", "pcm_s16le", "-f", "wav", str(out)]
    subprocess.run(cmd, check=True)
    return out, notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", nargs="?")
    ap.add_argument("--crossfade", type=float, default=4.0, help="seconds (default 4)")
    ap.add_argument("--beats", type=int, default=8,
                    help="crossfade length in beats when --beat-align (default 8)")
    ap.add_argument("--beat-align", action="store_true", help="mode 1")
    ap.add_argument("--tempo-match", action="store_true", help="mode 2")
    ap.add_argument("--harmonic", action="store_true", help="mode 3")
    ap.add_argument("--shuffle", type=int, metavar="SEED")
    ap.add_argument("--wav", action="store_true", help="write WAV instead of 320k mp3")
    ap.add_argument("--suffix", default="", help="tag the output filename")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()

    available = sources()
    if args.list or not args.source:
        if not available:
            sys.exit("No local audio — run tools/suno-download.py first.")
        info = json.loads(CACHE.read_text()) if CACHE.exists() else {}
        for name, tracks in available.items():
            got = [info[clip_id(t)] for t in tracks if clip_id(t) in info]
            total = sum(duration(t) for t in tracks)
            extra = ""
            if got:
                bpms = sorted(a["bpm"] for a in got)
                conf = sum(a["confidence"] for a in got) / len(got)
                extra = f"  {bpms[len(bpms)//2]:5.0f} bpm med  conf {conf:.2f}"
            print(f"  {name:34} {len(tracks):3} tracks  {hms(total)}{extra}")
        return

    tracks = available.get(args.source)
    if not tracks:
        sys.exit(f"No WAVs in audio/{args.source} — have: {', '.join(available) or 'nothing'}")

    info = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    if (args.beat_align or args.tempo_match or args.harmonic) and not info:
        sys.exit("No analysis yet — run: uv run tools/analyse.py")

    if args.shuffle is not None:
        random.Random(args.shuffle).shuffle(tracks)
    if args.harmonic:
        tracks = harmonic_order(tracks, info)

    target_bpm = None
    if args.tempo_match:
        steady = [info[clip_id(t)]["bpm"] for t in tracks if clip_id(t) in info]
        if not steady:
            sys.exit("No analysis for this source — run: uv run tools/analyse.py")
        target_bpm = sorted(steady)[len(steady) // 2]

    tags = "".join(t for t, on in
                   [("-beat", args.beat_align), ("-tempo", args.tempo_match),
                    ("-harmonic", args.harmonic)] if on)
    name = args.source.replace("/", "-") + tags + args.suffix
    out = MIXES / f"{name}.{'wav' if args.wav else 'mp3'}"
    MIXES.mkdir(parents=True, exist_ok=True)

    print(f"{args.source}: {len(tracks)} tracks"
          + (f", target {target_bpm:.0f} bpm" if target_bpm else "")
          + f" -> {out.relative_to(REPO)}")

    tmpdir = tempfile.mkdtemp(prefix="mixtape-")
    try:
        prepared, notes = [], []
        for t in tracks:
            p, n = prepare(t, info, target_bpm, tmpdir, args.beat_align, args.tempo_match)
            prepared.append(p)
            notes.append(n)

        durations = [duration(p) for p in prepared]

        # Crossfade length per join. In beat-align mode it is a whole number of
        # beats at the outgoing track's tempo, so the blend starts and ends on a
        # beat rather than at an arbitrary second.
        fades = []
        for i in range(len(prepared) - 1):
            xf = args.crossfade
            a = info.get(clip_id(tracks[i]))
            if args.beat_align and a and a["bpm"] > 0:
                bpm = target_bpm if (args.tempo_match and target_bpm) else a["bpm"]
                xf = args.beats * 60.0 / bpm
            fades.append(min(xf, durations[i] - 1, durations[i + 1] - 1))

        cmd = ["ffmpeg", "-nostdin", "-loglevel", "error", "-y"]
        for p in prepared:
            cmd += ["-i", str(p)]
        if len(prepared) == 1:
            cmd += ["-c", "copy", str(out)]
        else:
            steps, prev = [], "[0]"
            for i in range(1, len(prepared)):
                label = f"[a{i}]"
                steps.append(f"{prev}[{i}]acrossfade=d={fades[i-1]:.4f}:c1=tri:c2=tri{label}")
                prev = label
            cmd += ["-filter_complex", ";".join(steps), "-map", prev]
            cmd += ["-c:a", "pcm_s16le"] if args.wav else ["-c:a", "libmp3lame", "-b:a", "320k"]
            cmd += [str(out)]
        subprocess.run(cmd, check=True)

        titles_path = AUDIO / "titles.json"
        titles = json.loads(titles_path.read_text()) if titles_path.exists() else {}

        chapters, detail_lines, clock = [], [], 0.0
        for i, (t, d) in enumerate(zip(tracks, durations)):
            a = info.get(clip_id(t), {})
            title = titles.get(clip_id(t)) or t.stem.split("--")[0].replace("-", " ").title()
            chapters.append(f"{hms(clock)} {title}")
            det = f"{hms(clock)} {title}"
            if a:
                det += f"  [{a.get('bpm', 0):.0f}bpm {a.get('camelot', '?')} conf {a.get('confidence', 0):.2f}]"
            if notes[i]:
                det += "  " + "; ".join(notes[i])
            detail_lines.append(det)
            clock += d - (fades[i] if i < len(fades) else 0)

        head = f"{args.source} — {len(tracks)} tracks, {hms(clock, force_hours=True)}"
        if tags:
            head += f" ({tags.strip('-').replace('-', ' + ')})"
        # Top block pastes straight into a YouTube description as chapters;
        # everything technical sits below the marker so it can be dropped.
        out.with_suffix(".txt").write_text(
            head + "\n\n" + "\n".join(chapters)
            + "\n\n--- notes (not for the description) ---\n"
            + "\n".join(detail_lines) + "\n")
        print(f"  {hms(clock)} total; tracklist at {out.with_suffix('.txt').relative_to(REPO)}")
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


if __name__ == "__main__":
    main()
