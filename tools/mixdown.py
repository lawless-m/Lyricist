#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Plan and render a DJ mix. This half plans; nothing is rendered yet.

Usage:
  tools/mixdown.py --plan                    # the running order, as a table
  tools/mixdown.py --plan --order tempo      # compare against a plain tempo sort
  tools/mixdown.py --plan --peak 0.6         # move the arc's peak earlier
  tools/mixdown.py --plan --w-trope 0        # what the order looks like ignoring tropes

Needs tools/stems.py to have run. See docs/superpowers/specs/2026-07-27-dj-mixdown-design.md.

Ordering has three terms, and on this material they are very unequally useful:

  tempo   29 of 37 laundry tracks sit in 82-104bpm, so tempo can barely order the
          middle of the set at all. It matters at the edges — the climb to the peak
          and the drag back down — and almost nowhere else.
  key     21 of 37 are F minor. camelot_distance is 0 for most pairs. Near vestigial,
          kept for the F#/Eb minority.
  trope   this is the one doing the work. The playlist is chronological, so every
          song written before the trope library clusters at the front: tracks 1&2
          share a mantra, 3&4 the fold/buckle collapse, 4&5 an arbitrary-day marker,
          5&6 the inventory-of-loss couplet. Six tracks daisy-chained. A continuous
          mix amplifies repetition that scattered listening hides, and no amount of
          beatmatching touches it.
"""

import argparse
import json
import re
import sys
from difflib import get_close_matches
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
AUDIO = REPO / "audio"
STEMS = AUDIO / "stems.json"
TROPES = REPO / ".claude" / "tropes" / "banned-patterns.tsv"

# The three terms are NOT in the same units and the defaults account for it. Tempo
# cost is |log2(ratio)|, which is under 0.1 between two plateau tracks and only 0.67
# for 96->153; trope repulsion is a raw shared-count, so one collision in the adjacent
# slot is 1.0. At w_tempo=1 the tempo term never got a vote and the arc came out as
# noise. At 8 a big tempo jump (~5.4) outweighs any plausible trope cost, while the
# plateau — where log2 differences are tiny — stays free for trope spacing to order.
# That split is the intent: tempo governs the climb and the drag, tropes govern the
# middle, because on this material tempo cannot order the middle at all.
W_TEMPO, W_KEY, W_TROPE = 8.0, 0.15, 2.0
TROPE_WINDOW = 6          # how many previously-placed tracks a new one is repelled by

CAMELOT = {
    ("B", "major"): "1B", ("F#", "major"): "2B", ("C#", "major"): "3B", ("G#", "major"): "4B",
    ("D#", "major"): "5B", ("A#", "major"): "6B", ("F", "major"): "7B", ("C", "major"): "8B",
    ("G", "major"): "9B", ("D", "major"): "10B", ("A", "major"): "11B", ("E", "major"): "12B",
    ("G#", "minor"): "1A", ("D#", "minor"): "2A", ("A#", "minor"): "3A", ("F", "minor"): "4A",
    ("C", "minor"): "5A", ("G", "minor"): "6A", ("D", "minor"): "7A", ("A", "minor"): "8A",
    ("E", "minor"): "9A", ("B", "minor"): "10A", ("F#", "minor"): "11A", ("C#", "minor"): "12A",
}
ENHARMONIC = {"Db": "C#", "Eb": "D#", "Gb": "F#", "Ab": "G#", "Bb": "A#"}


def camelot(key, scale):
    return CAMELOT.get((ENHARMONIC.get(key, key), scale), "?")


def camelot_distance(a, b):
    """0 same, 1 neighbour or relative major/minor, higher rougher."""
    if not a or not b or "?" in (a, b):
        return 3
    if a == b:
        return 0
    na, ma = int(a[:-1]), a[-1]
    nb, mb = int(b[:-1]), b[-1]
    if na == nb:
        return 1
    step = min((na - nb) % 12, (nb - na) % 12)
    return step if ma == mb else step + 1


def load_tropes():
    pats = []
    if not TROPES.exists():
        return pats
    for line in TROPES.read_text().splitlines():
        if line.startswith("#") or not line.strip():
            continue
        f = line.split("\t")
        if len(f) < 4:
            continue
        try:
            pats.append((f[0], re.compile(f[2], re.I), f[3]))
        except re.error:
            pass
    return pats


def trope_sets(tracks, band):
    """{clip_id: {trope index}} by running the banned-pattern regexes over lyrics.

    Audio slugs come from Suno titles and lyric filenames are hand-made, so a
    close-match fallback covers drift between them. A track that silently fails to
    match scores as trope-free and gets placed next to something it echoes — an
    invisible failure, so the fallback is cheaper than the bug.
    """
    pats = load_tropes()
    lyrics = {p.stem: p for p in (REPO / band).glob("*.txt")
              if not p.name.endswith(".style.txt")}
    out, unmatched = {}, []
    for t in tracks:
        slug = t["slug"].partition("-")[2] or t["slug"]
        p = lyrics.get(slug)
        if not p:
            c = get_close_matches(slug, lyrics, 1, 0.85)
            p = lyrics[c[0]] if c else None
        if not p:
            unmatched.append(t["slug"])
            out[t["clip"]] = set()
            continue
        text = p.read_text()
        out[t["clip"]] = {i for i, (_, rx, _) in enumerate(pats) if rx.search(text)}
    return out, unmatched, pats


def arc_targets(bpms, peak):
    """Tempo target per position: rise to a peak, then fall back to the bottom.

    Both legs are dealt a spread across the WHOLE tempo range, then the up-leg is
    sorted ascending and the down-leg descending. The obvious alternative — dealing
    ranks outward from the peak — is wrong when the legs are unequal: the short leg
    exhausts, the long one absorbs every remaining value, and the set ends at a mid
    tempo instead of coming down. That leaves the drag with nothing to drag to.

    Targets are dealt from the actual tempos rather than interpolated along a curve,
    because a curve demands tempos this catalogue does not contain: 31 tracks inside
    a 22bpm band with six above it is a plateau with one excursion, not a rise.
    """
    n = len(bpms)
    asc = sorted(bpms)
    down_n = max(1, n - max(1, round(n * peak)))
    up, down = [], []
    for r, v in enumerate(asc):
        (down if (r * down_n) % n < down_n else up).append(v)
    return sorted(up) + sorted(down, reverse=True)


def order_tracks(tracks, tropes, args):
    import math
    if args.order == "playlist":
        return list(tracks)
    if args.order == "tempo":
        return sorted(tracks, key=lambda t: t["bpm"])

    targets = arc_targets([t["bpm"] for t in tracks], args.peak)
    n = len(targets)
    median = sorted(targets)[n // 2]

    # Fill the tempo extremes first, plateau last. Filling left-to-right strands them:
    # the fastest track has only a couple of slots that suit it, trope repulsion pulls
    # the others into those slots, and whatever is left lands wherever the last free
    # position happens to be — which put a 153bpm track at position 37, after the set
    # had already come down to 81. A plateau track fits almost anywhere, so it can
    # afford to wait; an extreme cannot.
    fill = sorted(range(n), key=lambda i: -abs(math.log2(targets[i] / median)))

    slots = [None] * n
    remaining = list(tracks)
    for pos in fill:
        target = targets[pos]
        best, best_cost = None, None
        for t in remaining:
            tempo = abs(math.log2(t["bpm"] / target))
            key, rep = 0.0, 0.0
            for j in range(max(0, pos - TROPE_WINDOW), min(n, pos + TROPE_WINDOW + 1)):
                other = slots[j]
                if other is None or j == pos:
                    continue
                gap = abs(j - pos)
                rep += len(tropes[t["clip"]] & tropes[other["clip"]]) / gap
                if gap == 1:
                    key = max(key, camelot_distance(other["camelot"], t["camelot"]) / 12.0)
            cost = args.w_tempo * tempo + args.w_key * key + args.w_trope * rep
            if best_cost is None or cost < best_cost:
                best, best_cost = t, cost
        remaining.remove(best)
        slots[pos] = best
    return improve(slots, targets, tropes, args)


def total_cost(slots, targets, tropes, args):
    import math
    n = len(slots)
    c = 0.0
    for i, t in enumerate(slots):
        c += args.w_tempo * abs(math.log2(t["bpm"] / targets[i]))
        if i + 1 < n:
            c += args.w_key * camelot_distance(t["camelot"], slots[i + 1]["camelot"]) / 12.0
        for j in range(i + 1, min(n, i + TROPE_WINDOW + 1)):
            shared = len(tropes[t["clip"]] & tropes[slots[j]["clip"]])
            if shared:
                c += args.w_trope * shared / (j - i)
    return c


def improve(slots, targets, tropes, args, passes=40):
    """Pairwise-swap hill climb over the whole arrangement.

    Greedy placement cannot undo an earlier choice, and that strands scarce tempos:
    both 153bpm slots went to a 153 and a 147 that was nearly as good there, so the
    second 153 had nowhere left and landed at position 33, mid-descent, between two
    94bpm tracks. Filling extremes first moved the failure without removing it —
    the arrangement has to be repairable after the fact, not merely built in a
    smarter order.
    """
    best = total_cost(slots, targets, tropes, args)
    for _ in range(passes):
        improved = False
        for i in range(len(slots)):
            for j in range(i + 1, len(slots)):
                slots[i], slots[j] = slots[j], slots[i]
                c = total_cost(slots, targets, tropes, args)
                if c < best - 1e-9:
                    best, improved = c, True
                else:
                    slots[i], slots[j] = slots[j], slots[i]
        if not improved:
            break
    return slots


def collisions(order, tropes, within):
    """Pairs sharing a trope that end up within `within` positions of each other."""
    out = []
    for i, a in enumerate(order):
        for j in range(i + 1, min(i + within + 1, len(order))):
            shared = tropes[a["clip"]] & tropes[order[j]["clip"]]
            if shared:
                out.append((i + 1, j + 1, len(shared), j - i))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--band", default="laundry")
    ap.add_argument("--order", default="arc", choices=["arc", "tempo", "playlist"])
    ap.add_argument("--peak", type=float, default=0.7)
    ap.add_argument("--w-tempo", type=float, default=W_TEMPO)
    ap.add_argument("--w-key", type=float, default=W_KEY)
    ap.add_argument("--w-trope", type=float, default=W_TROPE)
    ap.add_argument("--within", type=int, default=3, help="collision reporting window")
    ap.add_argument("--plan", action="store_true")
    args = ap.parse_args()

    if not STEMS.exists():
        sys.exit("no audio/stems.json — run tools/stems.py first")
    cache = json.loads(STEMS.read_text())

    src = AUDIO / "playlists" / args.band
    if not src.is_dir():
        sys.exit(f"no such source: {src.relative_to(REPO)}")

    tracks = []
    for w in sorted(src.glob("*.wav")):
        cid = w.stem.rsplit("--", 1)[-1]
        a = cache.get(cid)
        if not a:
            continue
        tracks.append({
            "clip": cid, "slug": w.stem.split("--")[0], "path": w,
            "bpm": a["bpm"], "camelot": camelot(a["key"], a["scale"]),
            "key": f"{a['key']} {a['scale']}", "density": a["vocal_density"],
            "duration": a["duration"], "contrast": a["grid_contrast"],
        })
    if not tracks:
        sys.exit("no analysed tracks — run tools/stems.py")

    tropes, unmatched, pats = trope_sets(tracks, args.band)
    if unmatched:
        print(f"! no lyric file for {len(unmatched)}: {', '.join(unmatched)}\n", file=sys.stderr)

    order = order_tracks(tracks, tropes, args)

    if args.plan:
        total = sum(t["duration"] for t in order)
        print(f"{args.band} — {len(order)} tracks, {int(total//60)}:{int(total%60):02d} "
              f"before transitions   (order={args.order}"
              + (f", peak={args.peak}" if args.order == "arc" else "") + ")\n")
        print(f"{'#':>3} {'bpm':>6} {'key':>5} {'vox':>5} {'ctr':>5}  track")
        for i, t in enumerate(order, 1):
            print(f"{i:3} {t['bpm']:6.1f} {t['camelot']:>5} {t['density']*100:4.0f}% "
                  f"{t['contrast']:5.2f}  {t['slug']}")

        print()
        for label, o in (("playlist", tracks), (args.order, order)):
            c = collisions(o, tropes, args.within)
            adj = [x for x in c if x[3] == 1]
            print(f"{label:9} trope collisions within {args.within}: {len(c):3}"
                  f"   adjacent: {len(adj):2}")
        c = collisions(order, tropes, args.within)
        if c:
            print(f"\nclosest surviving collisions in the {args.order} order:")
            for a, b, n, gap in sorted(c, key=lambda x: x[3])[:6]:
                print(f"  {order[a-1]['slug']}  <-{gap}->  {order[b-1]['slug']}"
                      f"   ({n} shared)")


if __name__ == "__main__":
    main()
