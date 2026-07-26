#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["librosa", "soundfile", "numpy"]
# ///
"""Analyse local WAVs for tempo, beat grid and musical key; cache to audio/analysis.json.

Usage:
  tools/analyse.py                 # analyse anything not already cached
  tools/analyse.py --force         # re-analyse everything
  tools/analyse.py --show laundry  # print what's known about a source

Deps are declared inline (PEP 723) so uv fetches them on first run: ./tools/analyse.py
or `uv run tools/analyse.py`. Nothing to install by hand, no venv to keep in sync.

Feeds tools/mixtape.py's beat-align, tempo-match and harmonic-order modes. Cached
because a full pass over 130 tracks takes minutes and the audio never changes —
keyed by clip id, so a re-download or a re-link doesn't invalidate anything.

The confidence field matters: beat tracking on rubato accordion is confident
nonsense, so mixtape refuses to tempo-match anything below a threshold rather
than stretching a ballad to fit a grid.
"""

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
AUDIO = REPO / "audio"
CACHE = AUDIO / "analysis.json"

# Krumhansl-Schmuckler profiles, the standard correlation approach to key finding.
MAJOR = [6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88]
MINOR = [6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17]
NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# Camelot wheel: adjacent numbers or the same number in the other mode mix cleanly.
CAMELOT = {
    ("B", "maj"): "1B", ("F#", "maj"): "2B", ("C#", "maj"): "3B", ("G#", "maj"): "4B",
    ("D#", "maj"): "5B", ("A#", "maj"): "6B", ("F", "maj"): "7B", ("C", "maj"): "8B",
    ("G", "maj"): "9B", ("D", "maj"): "10B", ("A", "maj"): "11B", ("E", "maj"): "12B",
    ("G#", "min"): "1A", ("D#", "min"): "2A", ("A#", "min"): "3A", ("F", "min"): "4A",
    ("C", "min"): "5A", ("G", "min"): "6A", ("D", "min"): "7A", ("A", "min"): "8A",
    ("E", "min"): "9A", ("B", "min"): "10A", ("F#", "min"): "11A", ("C#", "min"): "12A",
}


def beat_salience(onset, beats):
    """How much stronger the onset signal is ON the predicted beats than overall.

    NOT the regularity of the beat grid — librosa fits a tempo and emits a near
    uniform grid whatever you feed it, so grid regularity scores ~0.97 for solo
    accordion and tells you nothing. Salience actually separates programmed drums
    (onsets spike on the grid) from rubato playing (they don't).
    """
    import numpy as np
    if len(beats) < 4 or onset.size == 0:
        return 0.0
    mean_all = float(np.mean(onset))
    if mean_all <= 0:
        return 0.0
    on_beat = float(np.mean(onset[np.clip(beats, 0, len(onset) - 1)]))
    ratio = on_beat / mean_all
    return round(float(np.clip((ratio - 1.0) / 1.0, 0.0, 1.0)), 3)


def analyse(path):
    import librosa
    import numpy as np

    y, sr = librosa.load(str(path), mono=True)
    onset = librosa.onset.onset_strength(y=y, sr=sr)
    tempo, beats = librosa.beat.beat_track(onset_envelope=onset, sr=sr, trim=False)
    beat_times = librosa.frames_to_time(beats, sr=sr).tolist()

    confidence = beat_salience(onset, beats)

    chroma = librosa.feature.chroma_cqt(y=y, sr=sr).mean(axis=1)
    best, best_r = ("C", "maj"), -2.0
    for i in range(12):
        rolled = np.roll(chroma, -i)
        for mode, profile in (("maj", MAJOR), ("min", MINOR)):
            r = float(np.corrcoef(rolled, profile)[0, 1])
            if r > best_r:
                best_r, best = r, (NOTES[i], mode)

    return {
        "bpm": round(float(np.atleast_1d(tempo)[0]), 2),
        "beats": [round(b, 4) for b in beat_times],
        "confidence": round(confidence, 3),
        "key": f"{best[0]} {best[1]}",
        "camelot": CAMELOT.get(best, "?"),
        "duration": round(float(len(y) / sr), 3),
    }


def clip_id(path):
    return path.stem.rsplit("--", 1)[-1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--reconfidence", action="store_true",
                    help="recompute confidence only (skips the slow key detection)")
    ap.add_argument("--show", metavar="SOURCE", help="print cached analysis for a source dir")
    args = ap.parse_args()

    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}

    if args.show:
        d = AUDIO / args.show
        if not d.is_dir():
            sys.exit(f"no such source: audio/{args.show}")
        print(f"{'track':44} {'bpm':>7} {'conf':>5}  key")
        for f in sorted(d.glob("*.wav")):
            a = cache.get(clip_id(f))
            if not a:
                print(f"{f.stem[:44]:44} {'—':>7} {'—':>5}  (not analysed)")
                continue
            print(f"{f.stem[:44]:44} {a['bpm']:7.1f} {a['confidence']:5.2f}  {a['key']} ({a['camelot']})")
        return

    if args.reconfidence:
        import librosa
        seen = set()
        files = [f for f in sorted(AUDIO.rglob("*--*.wav"))
                 if clip_id(f) in cache and not (clip_id(f) in seen or seen.add(clip_id(f)))]
        for i, f in enumerate(files, 1):
            y, sr = librosa.load(str(f), mono=True)
            onset = librosa.onset.onset_strength(y=y, sr=sr)
            _, beats = librosa.beat.beat_track(onset_envelope=onset, sr=sr, trim=False)
            cache[clip_id(f)]["confidence"] = beat_salience(onset, beats)
            if i % 20 == 0:
                print(f"  {i}/{len(files)}", flush=True)
                CACHE.write_text(json.dumps(cache, indent=1))
        CACHE.write_text(json.dumps(cache, indent=1))
        print(f"refreshed confidence for {len(files)} tracks")
        return

    todo = [f for f in sorted(AUDIO.rglob("*--*.wav"))
            if args.force or clip_id(f) not in cache]
    # Hardlinked duplicates share a clip id; analysing one covers the rest.
    seen, unique = set(), []
    for f in todo:
        if clip_id(f) not in seen:
            seen.add(clip_id(f))
            unique.append(f)

    print(f"{len(cache)} cached; {len(unique)} to analyse")
    for i, f in enumerate(unique, 1):
        print(f"[{i}/{len(unique)}] {f.stem}", flush=True)
        try:
            cache[clip_id(f)] = analyse(f)
        except Exception as e:
            print(f"    failed: {e}", file=sys.stderr)
        if i % 10 == 0:
            CACHE.write_text(json.dumps(cache, indent=1))
    CACHE.write_text(json.dumps(cache, indent=1))
    print(f"wrote {CACHE.relative_to(REPO)} ({len(cache)} tracks)")


if __name__ == "__main__":
    main()
