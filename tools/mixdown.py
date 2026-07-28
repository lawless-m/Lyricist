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
  tools/mixdown.py --plan --pin part-it-out:first    # fix a track's position

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
import math
import re
import shutil
import sys
import tempfile
from difflib import get_close_matches
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
AUDIO = REPO / "audio"
STEMS = AUDIO / "stems.json"
FILLERS = AUDIO / "fillers"
MIXES = AUDIO / "mixes"
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


def resolve_pins(tracks, specs):
    """--pin part-it-out:1 / :first / :last -> {position index: track}.

    Ordering is blind to what a track means. Part It Out is the song the band is
    named after and states its whole premise, and the arc buried it at position 20
    because it is 98.7bpm and F minor like a dozen others. Chronology had it first
    for a reason the cost function cannot see, so it gets told.
    """
    n = len(tracks)
    pins = {}
    for spec in specs or []:
        name, _, where = spec.rpartition(":")
        if not name:
            name, where = spec, "first"
        hits = [t for t in tracks if name in t["slug"]]
        if not hits:
            sys.exit(f"--pin {spec}: no track matching '{name}'")
        if len(hits) > 1:
            sys.exit(f"--pin {spec}: '{name}' matches {[h['slug'] for h in hits]}")
        pos = {"first": 1, "last": n}.get(where)
        if pos is None:
            try:
                pos = int(where)
            except ValueError:
                sys.exit(f"--pin {spec}: position must be a number, 'first' or 'last'")
        if not 1 <= pos <= n:
            sys.exit(f"--pin {spec}: position {pos} outside 1..{n}")
        pins[pos - 1] = hits[0]
    return pins


def order_tracks(tracks, tropes, args):
    import math
    if args.order == "playlist":
        return list(tracks)
    if args.order == "tempo":
        return sorted(tracks, key=lambda t: t["bpm"])

    pins = resolve_pins(tracks, args.pin)
    n = len(tracks)
    free_pos = [i for i in range(n) if i not in pins]
    free = [t for t in tracks if t not in pins.values()]

    # Deal the arc across the free positions only, from the free tempos only, so a
    # pinned track neither claims a target nor distorts the shape around it.
    free_targets = arc_targets([t["bpm"] for t in free], args.peak) if free else []
    targets = [0.0] * n
    for pos, tgt in zip(free_pos, free_targets):
        targets[pos] = tgt
    for pos, t in pins.items():
        targets[pos] = t["bpm"]        # pinned track sits at zero tempo cost

    median = sorted(t for t in targets if t) or [1.0]
    median = median[len(median) // 2]

    # Fill the tempo extremes first, plateau last. Filling left-to-right strands them:
    # the fastest track has only a couple of slots that suit it, trope repulsion pulls
    # the others into those slots, and whatever is left lands wherever the last free
    # position happens to be — which put a 153bpm track at position 37, after the set
    # had already come down to 81. A plateau track fits almost anywhere, so it can
    # afford to wait; an extreme cannot.
    fill = sorted(free_pos, key=lambda i: -abs(math.log2(targets[i] / median)))

    slots = [None] * n
    for pos, t in pins.items():
        slots[pos] = t
    remaining = list(free)
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
    return improve(slots, targets, tropes, args, frozen=set(pins))


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


def improve(slots, targets, tropes, args, passes=40, frozen=frozenset()):
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
            if i in frozen:
                continue
            for j in range(i + 1, len(slots)):
                if j in frozen:
                    continue
                slots[i], slots[j] = slots[j], slots[i]
                c = total_cost(slots, targets, tropes, args)
                if c < best - 1e-9:
                    best, improved = c, True
                else:
                    slots[i], slots[j] = slots[j], slots[i]
        if not improved:
            break
    return slots


# ----------------------------------------------------------------- rendering

XOVER_HZ = 180          # where the bass swap splits the band
GAIN = 0.85             # per-participant headroom before the limiter
DRUM_FLOOR = 0.25       # bar counts as "drums playing" above this share of median
RECENT_PENALTY = 25.0   # bpm-equivalent cost of reusing a recent filler
RECENT_KEEP = 6         # how many past fillers stay penalised
NEAR = 2                # never bed a join on a filler from a track this close by
DROP_IN = 0.03          # click guard on a hard entry, NOT a musical fade (seconds)
BED_SILENCE = 0.01      # a loop this silent reads as the mix stopping, not as a bar
ENDS_ITSELF = 1.5       # sound after the last drum, past which the track has ended
TAIL_FADE = 1.0         # fade every body out: Suno leaves crowd noise on some endings.
                        # 2.0 was audible as a crossover; the cheer it exists to cover
                        # is only 0.4s of the body, so 1.0 is ample.

# Below this kick phase-lock the grid is not describing the music, so nothing may be
# beatmatched, looped or stretched against it — such a join falls back to a plain cut.
# Laundry runs 0.10 min, 0.39 median, so this passes all of it. It exists for the
# other bands: the-bell and the-forge are rubato accordion with no kick at all, where
# refine_grid finds nothing, returns the tempo unrefined and reports lock 0.0. Without
# a floor the tool would confidently beatmatch against a grid that means nothing —
# which is the failure analyse.py already warns about in its own docstring, "beat
# tracking on rubato accordion is confident nonsense".
LOCK_FLOOR = 0.15


def bar_seconds(a):
    return a["grid"]["period"] * 4


def music_end(an, floor=-45.0):
    """When the band stops, which is not when the file stops. 14 of 33 laundry tracks
    run 2-4s past their last drum — a held chord, a decay, or in back-monday's case a
    crowd cheering. Two things need this: such a track has ALREADY ended, so a bed has
    no seam to cover; and a spinback taken from the file's end would be pulling the
    crowd backwards off the platter rather than the band.
    """
    stems = an.get("stems") or {}
    d = REPO / stems.get("drums", "")
    if not d.exists():
        return an["duration"]
    dur = duration(d)
    for s, e in reversed(silent_spans(d, floor, 0.30)):
        if e == float("inf") or e >= dur - 0.05:
            return s
    return dur


def head_energy(track, bars=8):
    """How loudly a track opens, as a share of its own typical bar. Below ~0.4 it
    creeps in; near 1.0 it starts at full power. Read off the cached bar_energy, so
    it costs nothing — it agrees with a measured RMS ratio to within about 0.09.
    """
    import statistics
    be = track["an"].get("bar_energy") or []
    if len(be) < bars + 4:
        return 1.0
    med = statistics.median([b for b in be if b > 0] or [1]) or 1
    return statistics.mean(be[:bars]) / med


def mix_points(a, tail_bars, head_bars):
    """Where this track enters and leaves the mix, both on downbeats.

    Out: the first downbeat at least a bar after the last vocal ends, so the mix-out
    never talks over the closing sung line — which is exactly what a fixed offset
    from the end does, and why the old mix kept fading over the last words.

    In: skip a dead intro and enter where the drums do, unless the vocal is already
    going by then, in which case enter at the first downbeat so nothing is clipped.

    Returns `tail_clean`: whether we actually got a bar of instrumental after the last
    vocal. That flag, not anything about the incoming track, is what decides a bridge.

    Measured on laundry: the median instrumental outro is 1.1 bars and 17 of 37 tracks
    sing to the last beat; the median internal gap in the back half is 2.8 bars and
    only 11 of 37 reach four. At 84% median vocal density there is nowhere in this
    material to hide a join, which is why the filler bed is needed far more often than
    "for the odd vocal intro" — the tracks contain no instrumental space, so the mix
    has to supply it.

    The obvious rule — "bridge when the NEXT track has a vocal intro" — was written
    first and is wrong twice over. It fired on 33 of 37 tracks, because laundry starts
    singing immediately and `drum_bar` is 0 nearly everywhere, so "vocal before drums"
    can never discriminate. More importantly it solves a problem that no longer
    exists: the out-point above already lands after A's last vocal, so A's tail is
    instrumental and B's vocal arriving over it is an ordinary handover. The case that
    genuinely needs a bed is the reverse — A singing to the very last bar, leaving
    nothing instrumental to hand over from.
    """
    import statistics
    bar = bar_seconds(a)
    first = a["first_downbeat"]
    dur = a["duration"]
    bars = a.get("bar_energy") or []

    drum_bar = 0
    if bars:
        med = statistics.median([b for b in bars if b > 0] or [0]) or 0
        for i, b in enumerate(bars):
            if b > med * DRUM_FLOOR:
                drum_bar = i
                break
    drums_at = first + drum_bar * bar
    vox_at = a["vocal_spans"][0][0] if a["vocal_spans"] else drums_at

    in_point = first if vox_at < drums_at else drums_at
    # Where B's GROOVE starts — the downbeat the drums arrive on. That, not the first
    # downbeat, is what must land on the grid. Most of these tracks open with a vocal
    # intro (finna-retard's runs 4.5s), so aligning the first downbeat drops the beat
    # a bar or two late; aligning the drum entry puts the beat exactly on the bar and
    # lets the intro run in over whatever is still playing.
    groove_at = drums_at

    # Play the track OUT. Cutting after the last vocal plus a bar sounded like the
    # song being interrupted, because the join then consumes bars from before that
    # point and fades A across its own closing line — good-dog was cut mid-ending.
    # These songs have no outros to mix over (median 1.1 bars), so the honest move is
    # to let them finish and let the bed cover the seam.
    last_bar = len(bars) - 1
    while last_bar > 0 and bars[last_bar] <= 0:      # trim trailing silence only
        last_bar -= 1
    out_point = min(first + (last_bar + 1) * bar, dur)
    latest = first + math.floor((dur - first) / bar) * bar
    out_point = max(in_point + 4 * bar, min(out_point, latest))

    # How many whole bars of instrumental sit between the last sung note and the end.
    # This varies hugely (0 to 7 bars) because it depends on whether the lyric carried
    # a [loop left running, faded, no ending] tag and whether Suno honoured it, so the
    # blend length is taken per track rather than fixed.
    last_vox = a["vocal_spans"][-1][1] if a["vocal_spans"] else dur
    avail = int((out_point - last_vox) // bar)
    return in_point, out_point, max(0, avail), groove_at


def pick_filler(bank, bars, from_bpm, to_bpm, recent, exclude):
    """Closest to the midpoint of the two tempos, minus anything we just used.

    Two rules beyond tempo, both learned by listening to the first render:

    Never bed a track on a filler cut from a track adjacent to the join. The mix put
    good-dog's own drum loop under good-dog's outro, so the song appeared to get
    stuck rather than hand over.

    Penalise recently-used loops. With twenty-odd plateau tracks at 93-96bpm, closest
    to the midpoint returned the same loop three joins running, which is precisely the
    tic the fillers exist to avoid. The penalty is in bpm units so it trades against
    tempo distance rather than overriding it.
    """
    cands = [f for f in bank if f["bars"] == bars and f["clip"] not in exclude]
    if not cands:
        cands = [f for f in bank if f["bars"] == bars]
    if not cands:
        return None
    mid = (from_bpm + to_bpm) / 2

    def cost(f):
        try:
            penalty = RECENT_PENALTY / (recent.index(f["clip"]) + 1)
        except ValueError:
            penalty = 0.0
        return (abs(f["bpm"] - mid) + penalty, -f["score"])

    return min(cands, key=cost)


def silent_spans(stem, floor=-45.0, minlen=0.15):
    """Silent intervals in a stem, in one pass, as (start, end) seconds."""
    import subprocess
    p = subprocess.run(
        ["ffmpeg", "-nostdin", "-loglevel", "info", "-i", str(stem),
         "-af", f"silencedetect=noise={floor}dB:d={minlen}", "-f", "null", "-"],
        capture_output=True, text=True)
    txt = p.stdout + p.stderr
    starts = [float(m) for m in re.findall(r"silence_start:\s*(-?[\d.]+)", txt)]
    ends = [float(m) for m in re.findall(r"silence_end:\s*([\d.]+)", txt)]
    return list(zip(starts, ends + [float("inf")] * (len(starts) - len(ends))))


def silent_in(spans, start, end):
    """Seconds of silence inside [start, end)."""
    return sum(max(0.0, min(e, end) - max(s, start)) for s, e in spans)


def bed_window(track, bars, back=32):
    """Where to cut the loop from — the latest clean bars, not simply the last ones.

    Taking the final bars before the mix-out point is the obvious choice and it is
    wrong, because the mix-out point is the end of the song. Suno endings thin out:
    across laundry, 19 of 37 tracks are more than 15% silent in their last four bars
    and no-blockers is 98% silent. Looping that turns a ragged ending into a
    rhythmic hole, which is exactly the dead air heard at ten of twenty joins —
    the silence arrives once per loop, on the bar, so it reads as the mix stopping.

    Silence is the constraint; DENSITY is the choice. Taking the first quiet-enough
    window was still wrong: keep-it-warm's first one sits one bar back and is 34%
    gaps, half the kick density of the track body, and looping that under a
    deceleration read as dropping to about 40bpm — half-time, not 17% slower. Eleven
    bars back the same track has a window with 2% gaps. So gather every window that
    is continuous enough and take the BUSIEST, breaking ties toward later ones.

    Gaps are measured at -30dB where hard silence is measured at -45dB: a sparse loop
    is not silent, it just has holes where hits should be, and the -45dB pass cannot
    see them. This is the `busy` term from fillers.py, which was the only one of its
    three scores that ever discriminated, and which this function dropped.
    """
    an = track["an"]
    stem = REPO / an["stems"]["drums"]
    bar = bar_seconds(an)
    hard = silent_spans(stem, -45.0, 0.15)
    gaps = silent_spans(stem, -30.0, 0.05)
    width = bars * bar
    ok, fallback = [], None
    for k in range(back + 1):
        start = track["out"] - width - k * bar
        if start < an["first_downbeat"]:
            break
        h = silent_in(hard, start, start + width) / width
        g = silent_in(gaps, start, start + width) / width
        if h <= BED_SILENCE:
            ok.append((g, k, start, h))
        if fallback is None or (h, g) < fallback[:2]:
            fallback = (h, g, start)
    if ok:
        g, k, start, h = min(ok)
        return start, h
    if fallback:
        return fallback[2], fallback[0]
    return max(0.0, track["out"] - width), 1.0


_INSTRUMENTAL = {}


def instrumental(track, tmpdir):
    """The track minus its vocal — which is drums AND BASS, and that is the point.

    The bed used the drums stem alone, because tools/stems.py throws the bass away
    (WANT = drums, vocals, other) on the reasoning that a bed only needs drums. It
    does not. Stripped of bass, the strongest periodicity in these tracks is the BAR,
    not the beat: read-the-card measures 1.190s (50bpm) on drums alone against 0.592s
    (101bpm) in full. So every bed built so far has been playing at a quarter of the
    apparent tempo, which is what "it goes down to about 40bpm" was hearing.

    Subtracting the vocal recovers the bass without re-separating anything: the saved
    stems sum to only 53% of the mix and the missing 47% is mostly low end, but the
    full mix still has it. full - vocals restores the beat exactly.
    """
    cid = track["clip"]
    if cid in _INSTRUMENTAL:
        return _INSTRUMENTAL[cid]
    voc = REPO / track["an"]["stems"].get("vocals", "")
    if not voc.exists():
        return track["path"]
    out = Path(tmpdir) / f"instr-{cid}.wav"
    run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y",
         "-i", str(track["path"]), "-i", str(voc),
         "-filter_complex",
         "[1:a]volume=-1[v];[0:a][v]amix=inputs=2:normalize=0[o]",
         "-map", "[o]", "-c:a", "pcm_s16le", str(out)])
    _INSTRUMENTAL[cid] = out
    return out


def self_bed(track, bars, tmpdir, tag):
    """Loop a track's OWN final bars into the outro Suno didn't render.

    Bedding a join on another song's loop does not work — it stands out, however
    well aligned, because it is a different kit in a different room arriving for
    sixteen seconds and leaving. The drag gets away with it only because a 153->96
    deceleration is audibly a device rather than glue.

    A track's own drums have none of that problem: same kit, same production, same
    mix. It reads as the ending continuing rather than as something else starting.
    This is exactly the [loop left running, faded, no ending] instruction the lyrics
    ask for and Suno honours about half the time — done in post, for the 30 tracks
    that didn't get it.

    Taken from the latest CLEAN bars before the mix-out point — see bed_window, and
    do not "simplify" this back to the final bars, which is where the dead air came
    from.

    The window is CHOSEN on the drums stem, because rhythmic density is what makes a
    loop worth looping, but the audio is CUT from the instrumental, because a bed
    without bass has no beat. Every join is a hard cut, so the melodic content the
    instrumental carries never overlaps B and cannot clash with it.
    """
    stem = REPO / track["an"]["stems"]["drums"]
    if not stem.exists():
        return None
    bar = bar_seconds(track["an"])
    start, frac = bed_window(track, bars)
    out = Path(tmpdir) / f"bed-{tag}.wav"
    run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y",
         "-ss", f"{start:.5f}", "-t", f"{bars * bar:.5f}",
         "-i", str(instrumental(track, tmpdir)),
         "-af", "afade=t=in:st=0:d=0.01", "-c:a", "pcm_s16le", str(out)])
    return {"file": out.name, "path": out, "clip": track["clip"],
            "bpm": track["bpm"], "bars": bars, "score": 1.0,
            "source": track["slug"], "self": True, "silence": round(frac, 3)}


def ramp_schedule(out_bars, hold_a, ramp_bars, from_bpm, to_bpm):
    """Per-bar target tempo: flat under A, ramp through the solo, flat under B.

    Ramping across the whole transition — which is what this did first — starts the
    filler drifting away from A the moment it enters, so two kits play at diverging
    tempos under the outgoing track. The filler may only move while it is alone.
    """
    out = []
    for k in range(out_bars):
        if k < hold_a:
            out.append(from_bpm)
        elif k < hold_a + ramp_bars:
            f = (k - hold_a + 1) / max(1, ramp_bars)
            out.append(from_bpm + (to_bpm - from_bpm) * f)
        else:
            out.append(to_bpm)
    return out


def render_ramp(filler, schedule, tmpdir, tag):
    """Render the loop for len(schedule) bars, one bar per entry at its own tempo.

    Bar-by-bar because atempo is constant per invocation. At 4- or 8-bar granularity
    a 96->123 ramp steps by 3-7bpm, which is audible as a lurch; per bar it is under
    1bpm and inaudible. This is also what lets the drag exceed the +/-12% stretch
    clamp on purpose — a drum loop is the one thing that survives 153->96.
    """
    src = filler.get("path") or (FILLERS / filler["file"])
    src_bar = 60.0 * 4 / filler["bpm"]
    parts = []
    for k, target in enumerate(schedule):
        ratio = target / filler["bpm"]
        ratio = min(max(ratio, 0.5), 2.0)
        off = (k % filler["bars"]) * src_bar
        p = Path(tmpdir) / f"ramp-{tag}-{k:03d}.wav"
        run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y",
             "-ss", f"{off:.5f}", "-t", f"{src_bar:.5f}", "-i", str(src),
             "-filter:a", f"atempo={ratio:.6f}", "-c:a", "pcm_s16le", str(p)])
        parts.append(p)

    lst = Path(tmpdir) / f"ramp-{tag}.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in parts))
    out = Path(tmpdir) / f"ramp-{tag}.wav"
    run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-f", "concat",
         "-safe", "0", "-i", str(lst), "-c:a", "pcm_s16le", str(out)])
    return out, duration(out)


def spinback_rates(steps, ratio=2.0):
    """Rates rising 1.0 -> R, where R makes the whole gesture `ratio` times shorter
    than its source. Solved rather than guessed: playing 2 bars back in 1 bar means
    the MEAN rate is 2, so the top rate has to be well above it (~3.5 at 12 steps).
    Picking a round-looking top rate instead leaves the spinback the wrong length and
    B lands off the bar.
    """
    want = steps / ratio                      # sum of 1/r must equal this
    lo, hi = 1.0, 64.0
    for _ in range(60):
        R = (lo + hi) / 2
        tot = sum(1.0 / (1 + (R - 1) * k / max(1, steps - 1)) for k in range(steps))
        lo, hi = (R, hi) if tot > want else (lo, R)
    R = (lo + hi) / 2
    return [1 + (R - 1) * k / max(1, steps - 1) for k in range(steps)]


def spinback_steps(a_bpm, b_bpm, override=None):
    """Coarser stepping for bigger jumps — the gesture should be as blatant as the
    problem it is covering. At 4 steps each chunk holds one pitch long enough to hear
    it as a discrete tone, so a 40% jump reads as a stepped siren rather than glue.
    """
    if override:
        return override
    jump = abs(a_bpm / b_bpm - 1)
    return 4 if jump >= 0.25 else 8 if jump >= 0.10 else 12


def render_spinback(a, b, plan, tmpdir, idx, steps=None):
    """A's last two bars pulled backwards off the platter, then a hard cut to B.

    asetrate, not atempo: a record dragged backwards rises in pitch AND speed
    together, and holding the pitch would make it a time-stretch, which is the one
    thing this is not. The source is A's own audio, so the gesture starts at exactly
    the sample A ended on and at exactly A's speed — no seam at the top of it.

    Length is solved to exactly one bar of A so B still cuts in on a downbeat. Chunk
    edges get the same click guard as any other hard entry; at four steps those edges
    are 0.6s apart and would otherwise tick.
    """
    n = spinback_steps(a["bpm"], b["bpm"], steps)
    bar = bar_seconds(a["an"])
    end = min(a["out"], a.get("music_end", a["out"]))
    src_len = 2 * bar
    start = max(0.0, end - src_len)

    rev = Path(tmpdir) / f"spin-{idx:03d}-rev.wav"
    run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y",
         "-ss", f"{start:.5f}", "-t", f"{src_len:.5f}", "-i", str(a["path"]),
         "-af", "areverse", "-ar", "44100", "-c:a", "pcm_s16le", str(rev)])

    chunk = src_len / n
    parts = []
    for k, r in enumerate(spinback_rates(n)):
        p = Path(tmpdir) / f"spin-{idx:03d}-{k:02d}.wav"
        held = chunk / r                      # this chunk's length after speeding up
        edge = min(DROP_IN / 2, held / 4)
        run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y",
             "-ss", f"{k * chunk:.5f}", "-t", f"{chunk:.5f}", "-i", str(rev),
             "-af", f"asetrate=44100*{r:.6f},aresample=44100,"
                    f"afade=t=in:st=0:d={edge:.4f},"
                    f"afade=t=out:st={max(0.0, held - edge):.4f}:d={edge:.4f}",
             "-c:a", "pcm_s16le", str(p)])
        parts.append(p)

    lst = Path(tmpdir) / f"spin-{idx:03d}.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in parts))
    out = Path(tmpdir) / f"trans-{idx:03d}.wav"
    run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-f", "concat",
         "-safe", "0", "-i", str(lst), "-af", f"volume={GAIN}",
         "-c:a", "pcm_s16le", str(out)])
    return out, duration(out), 0.0, 0.0


def run(cmd):
    import subprocess
    subprocess.run(cmd, check=True, capture_output=True)


def duration(path):
    import subprocess
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(path)],
        capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def split_bands(idx, tag):
    """Linkwitz-Riley split so the two bands sum back to the original signal.

    NOT lowpass=f=180 plus highpass=f=180. Complementary Butterworth filters do not
    reconstruct: summing them measured -35.0dB at 180Hz, -5.9dB at 120 and -6.5dB at
    260. That notch sat on every one of the 36 joins and on the whole filler bed,
    scooping out exactly where kick body, bass fundamentals and vocal chest live.
    acrossover is a Linkwitz-Riley bank and nulls to 0.0dB at every frequency tested.
    """
    return f"[{idx}]acrossover=split={XOVER_HZ}:order=4th[{tag}lo_][{tag}hi_]"


def band_chain(tag, band, fades, delay_s, gain=GAIN):
    """Shape one band of an already-split participant: fade, attenuate, position."""
    chain = []
    for kind, st, d in fades:
        chain.append(f"afade=t={kind}:st={max(0.0, st):.4f}:d={max(0.01, d):.4f}:curve=tri")
    chain.append(f"volume={gain}")
    if delay_s > 0:
        ms = int(round(delay_s * 1000))
        chain.append(f"adelay={ms}|{ms}")
    return f"[{tag}{band}_]" + ",".join(chain)


def render_loopcut(a, b, plan, tmpdir, idx):
    """A plays out, its own outro loops N bars ramping to B's tempo, then a hard cut.

    No overlap at any point: A ends, the loop runs, B starts. Every blended bed tried
    before this stood out — a foreign loop, A's own loop under A, A's own loop after
    A — while the two joins that always worked were the hard-ish ones. So nothing
    crossfades here. The loop is A's own final bars, so the kit and the room do not
    change, and it accelerates to B's tempo so the cut lands on B's beat rather than
    merely near it.
    """
    src = plan["ramp"]
    out = Path(tmpdir) / f"trans-{idx:03d}.wav"
    run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-i", str(src),
         "-af", f"afade=t=in:st=0:d={DROP_IN},"
                f"afade=t=out:st={max(0.0, duration(src) - DROP_IN):.4f}:d={DROP_IN},"
                f"volume={GAIN}",
         "-c:a", "pcm_s16le", str(out)])
    return out, duration(out), 0.0, 0.0


def render_transition(a, b, plan, tmpdir, idx):
    """Render one join. Returns (path, seconds, a_tail_secs, b_head_secs).

    Both join shapes run the SAME bass swap, which is the single biggest audible
    change here: acrossfade ran both tracks full-band, so every join stacked two kicks
    and two basslines and turned to mud. Splitting at 180Hz and handing the low end
    over at a defined bar is what makes a join read as a mix rather than a dissolve.
    """
    tb = plan["b_head_bars"] * bar_seconds(b["an"])
    ramp, solo = plan.get("ramp"), plan.get("solo_secs", 0.0)

    # BEATMATCH the overlap by stretching A's tail to B's tempo. Without it a direct
    # join runs two records at slightly different speeds — 86.7 against 88.1 is 1.6%,
    # which drifts ~90ms across the join and flams. A's tail is stretched rather than
    # B's head because A is ending: nobody hears 1.6% over its final bars, whereas
    # stretching B would alter the whole song or leave a speed step where its body
    # begins. Both sides start on a downbeat, so matching tempo holds them locked.
    #
    # THE ARITHMETIC MATTERS AND WAS WRONG ONCE. atempo=r turns an input of length L
    # into an output of L/r. We want A's final N bars — exactly a_src_dur seconds of
    # source, untouched — to come out lasting N of B's bars. So the input length is
    # a_src_dur and the OUTPUT length is a_src_dur/stretch, which equals tb when the
    # bar counts match. Taking a_src_dur/stretch of input instead (and timing the
    # fades against a_src_dur*stretch, as an earlier version did) makes the tail ~5.6%
    # too long with its fades misplaced, which breaks bar alignment by construction —
    # the tempo is matched and the bars still collide.
    # B plays from its FIRST SAMPLE, not from its first downbeat. These tracks open
    # with a pickup before the downbeat — 1.4 to 2.3 seconds of it — and starting at
    # the downbeat threw that away on every track in the set. Instead B is placed so
    # its downbeat lands on the grid and the pickup runs in ahead of it, over whatever
    # is still playing, which is what a DJ does with an intro.
    lead = b["groove"]
    a_src_dur = plan["a_tail_bars"] * bar_seconds(a["an"])
    stretch = b["bpm"] / a["bpm"] if not ramp else 1.0
    if not (0.94 <= stretch <= 1.06):
        stretch = 1.0
    ta = a_src_dur / stretch          # length of A's tail in the OUTPUT timeline
    b_start = (ta + solo) if ramp else 0.0
    total = b_start + tb

    cmd = ["ffmpeg", "-nostdin", "-loglevel", "error", "-y",
           "-ss", f"{plan['a_from']:.5f}", "-t", f"{a_src_dur:.5f}", "-i", str(a["path"])]
    if ramp:
        cmd += ["-t", f"{max(0.1, total - plan.get('bed_delay', 0.0)):.5f}", "-i", str(ramp)]
    # B's downbeat target: the bed's bar line where there is a bed, otherwise one bar
    # into the join so the pickup has somewhere to live.
    # The target must leave room for the whole intro, rounded up to a whole bar of A
    # so the drop still lands on a bar line.
    bar_a = bar_seconds(a["an"])
    b_target = b_start if ramp else bar_a * max(1, math.ceil(lead / bar_a))
    if b_target < lead:
        b_target = bar_a * math.ceil(lead / bar_a)
    b_delay = max(0.0, b_target - lead)
    b_take = lead + tb
    b_start = b_delay + lead                     # where B's downbeat actually lands
    total = max(total, b_delay + b_take)
    cmd += ["-ss", "0", "-t", f"{b_take:.5f}", "-i", str(b["path"])]

    bi = 2 if ramp else 1
    parts, labels = [], []

    if stretch != 1.0:
        parts_pre = [f"[0]atempo={stretch:.6f}[a0]"]
        a_src = "a0"
    else:
        parts_pre, a_src = [], "0"

    if ramp:
        # A is NOT faded out. It plays its ending in full and simply stops on a
        # downbeat; the bed carries the seam from there. Fading A across its own last
        # line is what made good-dog sound cut off.
        #
        # A SELF-BED STARTS WHERE A ENDS — it must not overlap A at all. Fading it in
        # underneath meant A's real drums played against a copy of A's drums lifted
        # from four bars earlier: the same kit at two offsets, which flanges the song
        # against itself. That is what "slightly clashy" and "doesn't line up" were.
        # [loop left running, faded, no ending] means the drums carry on AFTER the
        # song stops, not alongside it. A foreign bed (the drag) still enters early,
        # because there it is a device and there is no copy to collide with.
        bed_at = plan.get("bed_delay", 0.0)
        f_in = DROP_IN if bed_at else ta * 0.5
        parts += parts_pre + [split_bands(a_src, "a"), split_bands(1, "f"), split_bands(bi, "b")]
        a_lo_out = (ta - DROP_IN, DROP_IN) if bed_at else (ta * 0.6, ta * 0.4)
        parts.append(band_chain("a", "lo", [("out", *a_lo_out)], 0) + "[alo]")
        parts.append(band_chain("a", "hi", [("out", ta - DROP_IN, DROP_IN)], 0) + "[ahi]")
        parts.append(band_chain("f", "lo",
                                [("in", 0 if bed_at else ta * 0.6, f_in),
                                 ("out", b_start - bed_at + tb * 0.4, tb * 0.4)],
                                bed_at) + "[flo]")
        parts.append(band_chain("f", "hi",
                                [("in", 0, f_in),
                                 ("out", b_start - bed_at + tb * 0.4, tb * 0.4)],
                                bed_at) + "[fhi]")
        parts.append(band_chain("b", "lo", [("in", 0, DROP_IN)], b_delay) + "[blo]")
        parts.append(band_chain("b", "hi", [("in", 0, DROP_IN)], b_delay) + "[bhi]")
        labels = ["alo", "ahi", "flo", "fhi", "blo", "bhi"]
    else:
        # Straight overlap: highs cross the whole join, lows trade at the midpoint.
        parts += parts_pre + [split_bands(a_src, "a"), split_bands(bi, "b")]
        parts.append(band_chain("a", "lo", [("out", ta * 0.5, ta * 0.25)], 0) + "[alo]")
        parts.append(band_chain("a", "hi", [("out", ta - DROP_IN, DROP_IN)], 0) + "[ahi]")
        parts.append(band_chain("b", "lo", [("in", tb * 0.5, tb * 0.25)], b_delay) + "[blo]")
        parts.append(band_chain("b", "hi", [("in", 0, DROP_IN)], b_delay) + "[bhi]")
        labels = ["alo", "ahi", "blo", "bhi"]

    mix = "".join(f"[{l}]" for l in labels)
    parts.append(f"{mix}amix=inputs={len(labels)}:normalize=0,alimiter=limit=0.97[out]")

    out = Path(tmpdir) / f"trans-{idx:03d}.wav"
    cmd += ["-filter_complex", ";".join(parts), "-map", "[out]",
            "-c:a", "pcm_s16le", str(out)]
    run(cmd)
    # a_src_dur, not ta: the body is cut from A's file at A's own speed, so what the
    # transition consumes from A is the SOURCE length, not the stretched output.
    return out, duration(out), a_src_dur, b_take


def plan_joins(order, bank, args):
    """Decide each join's shape. Fillers only where they earn their place."""
    joins = []
    # A drag needs somewhere worth winding down TO, which tempo alone cannot tell it.
    # Picking the largest tempo drop put it on keep-it-warm -> read-the-card: the
    # biggest drop in the mix at 21%, and the worst possible landing, because
    # read-the-card opens at 0.95 of its own body energy — it starts at full power.
    # Decelerating into that was heard as the drag "winding right down" while the next
    # track came in fast and energetic. So score the arrival too, and take the join
    # that both falls and lands quietly.
    # Only on the descent. Scoring the whole set put the drag on join 1, part-it-out
    # -> wash, which scores well (19% drop into a soft opening) and is musically
    # absurd: a long deceleration two minutes in, immediately after the track the
    # band is named for. The arc peaks at args.peak; a device that winds down belongs
    # after that, not before the mix has got going.
    after = int(len(order) * args.peak)
    fits = [(( order[i]["bpm"] / order[i + 1]["bpm"] - 1) * (1 - head_energy(order[i + 1])), i)
            for i in range(after, len(order) - 1)
            if order[i]["bpm"] > order[i + 1]["bpm"]]
    drag_at = max(fits)[1] if fits and max(fits)[0] > 0.02 else -1

    # Scratch the joins with the largest tempo discontinuity — the ones where no
    # amount of beatmatching helps, so the honest move is to make the jump audible
    # on purpose. Never where the drag already is, and never on a grid we cannot
    # read, since the source is two bars measured off that grid.
    jumps = sorted(
        (abs(order[i]["bpm"] / order[i + 1]["bpm"] - 1), i)
        for i in range(len(order) - 1)
        if i != drag_at
        and order[i]["lock"] >= args.lock_floor
        and order[i + 1]["lock"] >= args.lock_floor)
    scratch_at = {i for _, i in jumps[-args.scratch:]} if args.scratch else set()

    debt = 0.0
    for i in range(len(order) - 1):
        a, b = order[i], order[i + 1]
        debt += max(0.0, a["density"] - args.rest_baseline)
        kind, long_rest = "bridge", False
        if args.album:
            joins.append({"kind": "gap", "a_tail_bars": 0, "b_head_bars": 0})
            continue
        readable = (a["lock"] >= args.lock_floor and b["lock"] >= args.lock_floor)
        if not readable:
            joins.append({"kind": "cut", "a_tail_bars": 1, "b_head_bars": 1})
            continue
        if i in scratch_at:
            # Ahead of hardcut: a tempo jump is the more urgent problem, and
            # render_spinback takes its two bars from where the band stops, so a
            # track ending on crowd noise still spins back on the band.
            joins.append({"kind": "scratch", "a_tail_bars": 0, "b_head_bars": 0})
            continue
        if i == drag_at and not args.no_drag:
            # Ahead of hardcut too. The drag's bed comes from bed_window, which hunts
            # for a busy section, not from the ending — so a track that finishes on a
            # held chord can still carry one.
            kind = "drag"
        elif a["duration"] - a["music_end"] >= ENDS_ITSELF:
            # A track that ends on something which is not the band has already
            # finished: 14 of 33 laundry tracks run 2-4s past their last drum, on
            # crowd noise or a held chord. There is no seam there for a bed to cover,
            # so cut. The tempo still has to line up — see hardcut in render(), which
            # trims A so B's groove lands where A's next downbeat would have.
            joins.append({"kind": "hardcut", "a_tail_bars": 0, "b_head_bars": 0})
            continue
        elif debt >= args.rest_debt:
            # A rest is a longer loopcut, not a blended bed. "Apart from the drag"
            # applies here too: it is still A's own outro looping and then cutting,
            # just with more room before the cut.
            kind, debt = "rest", 0.0
        elif args.blends and a["tail_avail"] >= args.join_bars:
            kind = "direct"
        else:
            # Default. A beatmatched blend was the original shape and it lost: six of
            # its thirteen joins were heard as clashing or crunchy, against a loopcut
            # failure rate of four in twenty that turned out to be one bug in the bed
            # window. It also needs an instrumental tail that only 15 of 37 tracks
            # have. --blends restores it for material that can carry one.
            kind = "bridge"

        # Blend for as long as A's own outro allows, between join_bars and max_blend.
        # A fixed length was wrong both ways: too short for the tracks that do fade out
        # instrumentally, and impossible for the ones that sing to the last beat.
        blend = max(args.join_bars, min(args.max_blend, a["tail_avail"]))
        if kind in ("bridge", "rest"):
            long_rest = kind == "rest"
            kind = "cut" if args.no_bed else "loopcut"
        p = {"kind": kind, "a_tail_bars": blend if kind == "direct" else args.join_bars,
             "b_head_bars": blend if kind == "direct" else args.join_bars}
        if kind == "cut":
            p.update(a_tail_bars=1, b_head_bars=1)
        if kind == "loopcut":
            # Nothing of either track is consumed: A plays to its end, the loop runs
            # between them, B starts from its first sample.
            n = args.rest_loop_bars if long_rest else args.loop_bars
            p.update(a_tail_bars=0, b_head_bars=0, loop=4, out_bars=n, solo_bars=n)
        if kind == "drag":
            # Also a loopcut now, just with a much longer ramp. It used a foreign loop
            # under an exemption granted while it was the one transition that worked;
            # once the intro-trim bug was fixed that verdict no longer held, and it
            # was heard as too long and dropping in level — the level being B's own
            # quiet intro, which the trim had been hiding. Same kit, hard cut, and
            # short enough to read as a device rather than an interlude.
            p.update(a_tail_bars=0, b_head_bars=0, loop=8,
                     out_bars=args.drag_solo, solo_bars=args.drag_solo)
        elif kind == "rest":
            p.update(loop=8, out_bars=8, solo_bars=args.rest_solo)
        elif kind == "bridge":
            p.update(loop=4, out_bars=8, solo_bars=args.bridge_solo)
        joins.append(p)
    return joins


def hms(s, hours=False):
    s = int(s)
    if s >= 3600 or hours:
        return f"{s // 3600}:{(s % 3600) // 60:02d}:{s % 60:02d}"
    return f"{s // 60}:{s % 60:02d}"


def render(order, joins, args):
    bank = json.loads((FILLERS / "index.json").read_text()) \
        if (FILLERS / "index.json").exists() else []
    if not bank and any(j["kind"] != "direct" for j in joins):
        sys.exit("no filler bank — run tools/fillers.py --bars 4 and --bars 8")

    tmpdir = tempfile.mkdtemp(prefix="mixdown-")
    MIXES.mkdir(parents=True, exist_ok=True)
    style = "album" if args.album else "dj"
    out = MIXES / f"{args.band}-{style}{args.suffix}.{'wav' if args.wav else 'mp3'}"

    try:
        # Build the transitions first: each one tells us how much of the tracks
        # either side it consumes, which is what bounds the solo bodies.
        trans, recent = [], []
        for i, j in enumerate(joins):
            a, b = order[i], order[i + 1]
            plan = dict(j)
            plan["a_from"] = a["out"] - j["a_tail_bars"] * bar_seconds(a["an"])
            plan["b_from"] = 0.0
            if j["kind"] not in ("direct", "cut", "gap", "scratch", "hardcut"):
                f = self_bed(a, j["loop"], tmpdir, f"{i:03d}") \
                    or pick_filler(bank, j["loop"], a["bpm"], b["bpm"], recent,
                                   {t["clip"] for t in order[max(0, i - NEAR): i + NEAR + 2]})
                if f:
                    ta = j["a_tail_bars"] * bar_seconds(a["an"])
                    tb = j["b_head_bars"] * bar_seconds(b["an"])
                    solo = j["solo_bars"] * bar_seconds(a["an"])
                    need = ta + solo + tb
                    nbars = max(2, math.ceil(need / (60.0 * 4 / a["bpm"])))
                    # A self-bed starts after A, so it holds no bars under A and can
                    # begin ramping immediately; a foreign bed enters under A and must
                    # stay at A's tempo until A is gone.
                    self_bed_used = bool(f.get("self"))
                    hold = 0 if self_bed_used else max(1, round(ta / (60.0 * 4 / a["bpm"])))
                    sched = ramp_schedule(nbars, hold, max(1, j["solo_bars"]),
                                          a["bpm"], b["bpm"])
                    ramp, rdur = render_ramp(f, sched, tmpdir, i)

                    # B enters on a bar line OF THE BED, computed from the bed's own
                    # ramped timeline. Using solo_bars * A's bar length is wrong: the
                    # bed is accelerating through those bars, so its bars are not A's
                    # bars any more and B drops in between beats. The bed can be
                    # perfectly BPM-matched and B still lands off it.
                    bar_secs = [60.0 * 4 / t for t in sched]
                    n_hold = hold if not self_bed_used else 0
                    solo = sum(bar_secs[n_hold:n_hold + max(1, j["solo_bars"])])
                    plan["ramp"], plan["solo_secs"], plan["filler"] = ramp, solo, f
                    plan["bed_delay"] = ta if self_bed_used else 0.0
                    recent.insert(0, f["clip"])
                    del recent[RECENT_KEEP:]
                else:
                    plan["kind"] = "direct"
            if plan["kind"] == "hardcut":
                # No insert at all. A is trimmed by however far B's groove sits from
                # B's start, so B's first drum lands exactly where A's next downbeat
                # would have — the pulse carries across a join with nothing in it.
                bar_a = bar_seconds(a["an"])
                p_, dur, ta, tb = None, 0.0, b["groove"] % bar_a, 0.0
            elif plan["kind"] == "gap":
                g = Path(tmpdir) / f"trans-{i:03d}.wav"
                run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-f", "lavfi",
                     "-i", f"anullsrc=r=44100:cl=stereo", "-t", f"{args.gap:.3f}",
                     "-c:a", "pcm_s16le", str(g)])
                p_, dur, ta, tb = g, args.gap, 0.0, 0.0
            elif plan["kind"] == "scratch":
                p_, dur, ta, tb = render_spinback(a, b, plan, tmpdir, i,
                                                  args.scratch_steps)
            elif plan["kind"] in ("loopcut", "drag") and plan.get("ramp"):
                p_, dur, ta, tb = render_loopcut(a, b, plan, tmpdir, i)
            else:
                p_, dur, ta, tb = render_transition(a, b, plan, tmpdir, i)
            p = p_
            trans.append({"path": p, "dur": dur, "ta": ta, "tb": tb,
                          "kind": plan["kind"], "filler": plan.get("filler")})
            print(f"  join {i+1:2}/{len(joins)}  {plan['kind']:6} "
                  f"{a['bpm']:5.1f}->{b['bpm']:5.1f}  {dur:5.1f}s", flush=True)

        pieces, rows, clock = [], [], 0.0
        for i, t in enumerate(order):
            head = trans[i - 1]["tb"] if i > 0 else 0.0
            tail = trans[i]["ta"] if i < len(trans) else 0.0
            start = head if i > 0 else t["in"]
            stop = t["out"] - tail
            if stop <= start:
                stop = start + bar_seconds(t["an"])
            # Fade the last couple of seconds of every body. Suno tacks things onto
            # the ends of these tracks that are not the song — back-monday ends with
            # a crowd cheering, which starts at 168.0s against a mix-out at 168.4s,
            # so the mix played four tenths of a cheer and then hard-cut. A fade
            # covers that whole class of artefact without having to detect any of it.
            # This is A alone, before its own hard cut, not a crossfade between songs.
            body = Path(tmpdir) / f"body-{i:03d}.wav"
            blen = stop - start
            fade = min(args.tail_fade, blen / 4)
            run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y",
                 "-ss", f"{start:.5f}", "-t", f"{blen:.5f}",
                 "-i", str(t["path"]),
                 "-af", f"afade=t=out:st={max(0.0, blen - fade):.4f}:d={fade:.4f}",
                 "-c:a", "pcm_s16le", str(body)])

            # The listener hears the track from where its body starts, but the
            # transition before it already brought the vocal in, so the chapter
            # mark belongs at the start of that transition, not the body.
            rows.append((clock - (trans[i - 1]["tb"] if i > 0 else 0.0), t, i))
            pieces.append(body)
            clock += duration(body)
            if i < len(trans) and trans[i]["path"] is not None:
                pieces.append(trans[i]["path"])
                clock += trans[i]["dur"]

        lst = Path(tmpdir) / "concat.txt"
        lst.write_text("".join(f"file '{p}'\n" for p in pieces))
        # Limit the whole thing, not just each segment: per-segment limiting leaves
        # the concatenated result free to touch 0dBFS, which it did (-0.0 peak).
        enc = ["-c:a", "pcm_s16le"] if args.wav else ["-c:a", "libmp3lame", "-b:a", "320k"]
        run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-f", "concat",
             "-safe", "0", "-i", str(lst), "-af", "alimiter=limit=0.89:level=disabled"]
            + enc + [str(out)])

        total = duration(out)
        chapters = [f"{hms(max(0.0, t0))} {t['slug'].partition('-')[2].replace('-',' ').title()}"
                    for t0, t, _ in rows]
        notes = []
        for (t0, t, i), j in zip(rows, list(joins) + [None]):
            n = (f"{hms(max(0.0, t0))} {t['slug']}  [{t['bpm']:.1f}bpm {t['camelot']} "
                 f"vox {t['density']*100:.0f}% ctr {t['contrast']:.2f}]")
            if i < len(trans):
                tr = trans[i]
                n += f"  -> {tr['kind']}"
                if tr["filler"]:
                    n += f" on {tr['filler']['source']}"
            notes.append(n)

        shape = (f"album, {args.gap:.1f}s between tracks" if args.album
                 else f"arc order, peak {args.peak}")
        head = (f"{args.band} — {len(order)} tracks, {hms(total, hours=True)}   "
                f"{args.order} order" + ("" if args.album else f", peak {args.peak}")
                + (f", {args.gap:.1f}s gaps" if args.album else ""))
        kinds = {}
        for tr in trans:
            kinds[tr["kind"]] = kinds.get(tr["kind"], 0) + 1
        out.with_suffix(".txt").write_text(
            head + "\n\n" + "\n".join(chapters)
            + "\n\n--- notes (not for the description) ---\n"
            + f"joins: {kinds}\n" + "\n".join(notes) + "\n")
        print(f"\n{hms(total, hours=True)} -> {out.relative_to(REPO)}")
        print(f"joins: {kinds}")
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


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
    ap.add_argument("--render", action="store_true")
    ap.add_argument("--join-bars", type=int, default=2,
                    help="bars of each track consumed by a join (default 2 -> ~10s)")
    ap.add_argument("--rest-baseline", type=float, default=0.80,
                    help="vocal density above which a track banks rest debt")
    ap.add_argument("--rest-debt", type=float, default=0.55,
                    help="debt at which a rest is spent")
    ap.add_argument("--no-drag", action="store_true")
    ap.add_argument("--tail-fade", type=float, default=TAIL_FADE, metavar="SECS",
                    help="fade at the end of each body (0 to disable)")
    ap.add_argument("--blends", action="store_true",
                    help="restore beatmatched blends where A has an instrumental tail")
    ap.add_argument("--scratch", type=int, default=3, metavar="N",
                    help="spinback the N biggest tempo jumps (0 to disable)")
    ap.add_argument("--scratch-steps", type=int, metavar="N",
                    help="force the spinback's step count (default: 4/8/12 by jump)")
    # Every bed variant tried so far has been heard as standing out: a foreign loop,
    # the track's own loop under it, and the track's own loop after it. Blends and the
    # drag are both liked. --no-bed replaces bridges with a bar-aligned cut: A plays
    # out, B drops in on the next downbeat, nothing between them.
    ap.add_argument("--no-bed", action="store_true",
                    help="bar-aligned cut with no loop at all")
    ap.add_argument("--lock-floor", type=float, default=LOCK_FLOOR,
                    help="minimum kick phase-lock before a join may be beatmatched")
    # Album style: whole tracks, a breath between them, nothing beatmatched. For
    # material with no usable pulse — the-bell-knows-my-name and the-forge are rubato
    # accordion — where every device in this tool is the wrong device. Needs no stems,
    # so it runs on any band without a separation pass.
    ap.add_argument("--album", action="store_true",
                    help="whole tracks with a short pause; no grid, no stems needed")
    ap.add_argument("--gap", type=float, default=1.2,
                    help="seconds of silence between tracks in album mode")
    ap.add_argument("--rest-loop-bars", type=int, default=8,
                    help="loop bars for a rest (a longer breather)")
    ap.add_argument("--loop-bars", type=int, default=4,
                    help="bars of A's own outro looped between tracks (default 4)")
    # Bars the bed plays ALONE. Total join = 2 (A's tail) + solo + 2 (B's head), so a
    # bridge at solo=2 is 6 bars, about 16s at 88bpm. It was 4, i.e. 8 bars and 23s,
    # which read as too long: a bare drum loop needs less room than a musical break
    # would. The rest and the drag are meant to be events and stay longer.
    ap.add_argument("--max-blend", type=int, default=6,
                    help="longest direct blend when a track's outro allows it")
    ap.add_argument("--bridge-solo", type=int, default=2)
    ap.add_argument("--rest-solo", type=int, default=6)
    ap.add_argument("--drag-solo", type=int, default=6,
                    help="bars of deceleration in the drag (was 10; heard as too long)")
    ap.add_argument("--pin", action="append", metavar="SLUG:POS",
                    help="fix a track to a position: --pin part-it-out:first, "
                         "--pin oats:last, --pin breeder:12 (repeatable)")
    ap.add_argument("--limit", type=int, help="render only the first N tracks")
    ap.add_argument("--wav", action="store_true")
    ap.add_argument("--suffix", default="")
    args = ap.parse_args()

    cache = json.loads(STEMS.read_text()) if STEMS.exists() else {}
    if not cache and not args.album:
        sys.exit("no audio/stems.json — run tools/stems.py first, or use --album")

    src = AUDIO / "playlists" / args.band
    if not src.is_dir():
        sys.exit(f"no such source: {src.relative_to(REPO)}")

    # Album mode falls back to the librosa cache, which covers every band, so a band
    # that has never been through stems.py can still be sequenced.
    fallback = {}
    old_cache = AUDIO / "analysis.json"
    if args.album and old_cache.exists():
        fallback = json.loads(old_cache.read_text())

    tracks = []
    for w in sorted(src.glob("*.wav")):
        cid = w.stem.rsplit("--", 1)[-1]
        a = cache.get(cid)
        if not a and args.album and cid in fallback:
            f = fallback[cid]
            a = {"bpm": f.get("bpm", 100.0), "key": "C", "scale": "major",
                 "vocal_density": 0.0, "duration": f.get("duration", 0.0),
                 "grid_contrast": 0.0, "grid_lock": 0.0, "vocal_spans": [],
                 "grid": {"t0": 0.0, "period": 0.6}, "first_downbeat": 0.0,
                 "bar_energy": [], "stems": {}}
        if not a:
            continue
        if args.album:
            in_p, out_p, avail, groove = 0.0, a["duration"], 0, 0.0
        else:
            in_p, out_p, avail, groove = mix_points(a, args.join_bars, args.join_bars)
        tracks.append({
            "clip": cid, "slug": w.stem.split("--")[0], "path": w, "an": a,
            "bpm": a["bpm"], "camelot": camelot(a["key"], a["scale"]),
            "key": f"{a['key']} {a['scale']}", "density": a["vocal_density"],
            "duration": a["duration"], "contrast": a["grid_contrast"],
            "in": in_p, "out": out_p, "tail_avail": avail, "groove": groove,
            "lock": a.get("grid_lock", 0.0),
            "music_end": a["duration"] if args.album else music_end(a),
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
        pj = plan_joins(order, [], args)
        print(f"{'#':>3} {'bpm':>6} {'key':>5} {'vox':>5} {'ctr':>5}  track")
        for i, t in enumerate(order, 1):
            j = pj[i - 1]["kind"] if i - 1 < len(pj) else ""
            print(f"{i:3} {t['bpm']:6.1f} {t['camelot']:>5} {t['density']*100:4.0f}% "
                  f"{t['contrast']:5.2f}  {t['slug']:30} -> {j}")
        kinds = {}
        for j in pj:
            kinds[j["kind"]] = kinds.get(j["kind"], 0) + 1
        print(f"\njoins: {kinds}")

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

    if args.render:
        if args.limit:
            order = order[:args.limit]
        joins = plan_joins(order, None, args)
        print(f"rendering {len(order)} tracks, {len(joins)} joins")
        render(order, joins, args)


if __name__ == "__main__":
    main()
