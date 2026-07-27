# DJ mixdown — design

**Date:** 2026-07-27
**Status:** approved design, not yet implemented
**Scope:** laundry only (`audio/playlists/laundry`, 37 tracks)

## Problem

`audio/mixes/playlists-laundry-beat-tempo.mp3` doesn't sound mixed. It sounds
crossfaded. The user's words: "just cross fading really."

## Diagnosis

Five separate causes, only one of which is the crossfade itself. All measured
against the existing 32-track render, then re-measured after the 2026-07-27 sync
took the playlist to 37.

**1. Tempo-match almost never fires.** `mixtape.py` keeps playlist order, so BPM
runs 129 → 103 → 103 → 152 → 129 → 123 → 96. Only 11 of 36 joins fall inside the
±12% stretch clamp; the rest print "left alone" and get a raw crossfade between
two tempos. Sorted by BPM, 36 of 36 joins are inside the clamp. **Ordering is the
bottleneck, not the stretcher.**

**2. "Beat-align" only trims the head.** It cuts the incoming track to its first
beat, but the crossfade *starts* at `duration − xf` on the outgoing track — an
arbitrary point in its bar. Two tracks genuinely at 123bpm still land out of
phase. That is worse than a hard cut.

**3. No bars, only beats.** `--beats 8` is eight beats from wherever, not two bars
from a downbeat. Joins land mid-phrase.

**4. `acrossfade` runs both tracks full-band.** Two kicks and two basslines
overlapping for four seconds. This is the mud.

**5. The mix happens over each song's outro and intro** — the least mixable part
of a Suno track. Ringing chords, fades, and a cappella vocal pickups.

### The sixth cause, and probably the largest

A continuous mix is a **repetition amplifier**. Scattered listening hides shared
hook lines; an unbroken hour puts them side by side.

The playlist is chronological — order of rendering, with no artistic intent — so
every song written before the trope library is clustered at the front. Running the
295 regexes in `.claude/tropes/banned-patterns.tsv` over the 37 lyric files:

```
 6x PERM  stock precision count              at [4, 7, 12, 19, 21, 29]
 6x PERM  stock effort count                 at [17, 19, 20, 22, 28, 36]
 5x PERM  fold/buckle collapse               at [3, 4, 7, 9, 11]
 5x WATCH arbitrary-day marker               at [4, 5, 20, 28, 30]
 4x WATCH large-count number                 at [3, 13, 19, 22]
 3x BAN   rejection-reason mantra            at [1, 2, 33]
 2x PERM  inventory-of-loss couplet          at [5, 6]
```

Only 8 of 37 tracks carry no banned-pattern hit. Five joins in the current order
are adjacent collisions, and the opening six tracks form an unbroken chain:
1&2 share a mantra, 3&4 the fold/buckle collapse, 4&5 an arbitrary-day marker,
5&6 the inventory-of-loss couplet.

No amount of beatmatching touches this. It needs an ordering term.

## What the separation pass actually found

Run over all 37 on 2026-07-27. Three results change decisions made above.

**tempo-cnn was wrong on 20 of 37.** Mostly doubled — 176-191 where the truth is
88-95 — plus `keep-it-warm` halved to 61 from 121 and `four-degrees` off by 4:3.
Building on it would have given over half the mix wrong bar lengths. Tempo now comes
from essentia's `PercivalBpmEstimator` at tunebat's exact parameters; see the comment
block in `stems.py`.

**Laundry is essentially one tempo and one key.** 29 of 37 tracks sit between 82 and
104bpm, with only `121, 136, 147, 147, 153, 153` above. And **21 of 37 are F minor**,
with nothing else above three.

Both of those reshape the ordering:

- The harmonic term is close to vestigial. With 57% of the catalogue in one key,
  `camelot_distance` is zero for most pairs and can't discriminate. Weight it low and
  let tempo and trope repulsion do the work; keep the term for the F#/Eb minority.
- The arc is not a smooth curve, it's a plateau with one excursion. 31 tracks in a
  22bpm band, then a short climb through 121 and 136 to a four-track peak at 147-153.
  Order the plateau on trope spacing (tempo can barely order it), then climb, peak,
  and drag back down.
- **The `drag` filler has an obvious home**: 153 → 96 off the back of the peak, a 37%
  deceleration into the plateau. That is exactly the "long stretch from fast to slow"
  this was asked for, and the material has precisely one place to put it.

**Vocal density spreads 0.68 to 0.97, median 0.84.** Enough range for intensity debt
to discriminate after all — the concern that it would degenerate into a fixed interval
was wrong. A 0.97 track banks nearly three times the debt of a 0.68 one.

**Grid phase must be fitted to the kick, not the onset envelope.** On this material
the onset envelope carries energy on every 8th and 16th, so the fit barely peaks:
contrast sat below 1.3 on 28 of 37. Fitting to the isolated kick moved that to 11 of
37 and lifted the median from ~1.13 to 1.46. It also moved phases materially —
`the-app-says-im-resting` by 390ms, two thirds of a beat — so the earlier grids were
not merely uncertain, they were wrong. All 37 fit on kick; the onset fallback never
fired.

## Non-goals

- Other bands. Laundry only until the engine is proven. `the-bell` and `the-forge`
  are rubato and will not survive beatmatching regardless.
- Changing `tools/mixtape.py`. It stays as the album-flow renderer.
- Full stem remixing / vocal ducking through joins (approach "C" in discussion).
  Deferred, not rejected — keeping the vocals stem on disk leaves the door open.
- Sample-accurate phase-locked beatmatching. Bar-aligned is the target.

## Architecture

Three new tools, each independently runnable, each cached so the expensive step
never repeats:

```
tools/stems.py     Demucks HTTP -> stems + analysis      (GPU, minutes, once)
tools/fillers.py   drums stems  -> 8-bar break bank      (CPU, seconds, re-runnable)
tools/mixdown.py   everything   -> the mix               (CPU, minutes, re-runnable)
```

`tools/mixtape.py` is untouched.

The split exists so the two heuristics most likely to need tuning by ear — the
grid/downbeat fit and the filler loop-picking — can be re-run without another
separation pass.

## 1. `tools/stems.py`

Talks HTTP to the Demucks server at `localhost:8766` (`/home/matt/Git/Demucks`).
No new dependencies in this repo. If the server isn't up, exit with the literal
start command, not a connection traceback:

```
.venv/bin/python run_server.py   # from /home/matt/Git/Demucks
```

Per track: `POST /separate {path}` → keep `drums.wav` and `vocals.wav` under
`audio/stems/<clipid>/`, discard `bass` and `other` (`--keep` to override).
`POST /request-unload` at the end so ComfyUI gets its VRAM back.

Writes `audio/stems.json`, keyed by clip id like the existing caches, kept
**separate from `analysis.json`** so current tooling isn't invalidated:

| field | meaning |
|---|---|
| `bpm_cnn` | tempo-cnn BPM from the `/separate` response |
| `grid` | `{t0, period}` — beat *n* lands at `t0 + n·period` |
| `grid_score` | fraction of drum onset energy landing on-grid |
| `downbeat_phase` | which beat index mod 4 is bar 1 |
| `vocal_spans` | `[[8.2, 31.5], ...]` seconds |
| `bar_energy` | per-bar RMS of the drums stem |

**The grid is fitted, not tracked.** `analyse.py` stores librosa's per-frame beat
list, which drifts over two minutes and contains inserted and dropped beats — bar
arithmetic on it is unreliable. Instead: take tempo-cnn's BPM as the period, then
search the single beat-period of phase that maximises drum-stem onset energy. One
1-D search, no dependence on librosa's beat list, and it extrapolates exactly to
any bar. `grid_score` falls out of it and is a better confidence signal than the
current `beat_salience`.

**Downbeats come from the isolated drums.** For each phase 0–3, sum low-band (kick)
energy on beats where `n mod 4 == phase`; argmax wins. Hopeless on a full mix,
easy on a clean drum stem — and its absence is why every join currently lands
mid-phrase.

**tempo-cnn also fixes octave errors.** librosa reports a lone 172bpm in a set
otherwise topping out at 162; that is the classic doubling artefact. Octave errors
don't merely misreport tempo, they actively poison ordering by sorting a slow
track to the fast end and creating a cliff at both ends of it.

Assumes 4/4. Correct for laundry; revisit for other bands.

## 2. `tools/fillers.py`

Scores every bar-aligned 8-bar window of each drums stem on energy × consistency
(low variance across the eight bars, and first-four similar to last-four so the
loop doesn't jar). Best one or two per track → `audio/fillers/<bpm>-<clipid>-<bar>.wav`
plus an index. Roughly 30–70 breaks across the laundry tempo range. 20ms micro-fade
across the loop seam to kill the click.

**Drums only — no bass stem.** Bass is pitched, so a bass-carrying filler has a
key and can clash with whatever it's bridging. Keyless fillers bridge any harmonic
jump, which is the entire point. They will sound leaner than a full production;
that is correct for a break.

Re-runnable against the stem cache, which is what makes tuning the scoring
practical.

## 3. `tools/mixdown.py`

### Ordering

Greedy nearest-neighbour, as `harmonic_order` already does, but with three terms:

```
cost(c | placed) = w_tempo · |log2(bpm_c / bpm_prev)|
                 + w_key   · camelot_distance(prev, c)
                 + w_trope · Σ over last K placed: shared_tropes(c, placed[-i]) / i
```

`log2` on the tempo ratio makes it octave-symmetric and scale-free. The trope term
is a decaying repulsion over a window (K=6), because trope collision is a *spacing*
problem, not an adjacency one — tempo and key decide the joins, tropes decide the
spacing.

Trope sets come from running the `banned-patterns.tsv` regexes over each track's
lyric file. Weights exposed as `--w-tempo` / `--w-key` / `--w-trope`; they will
need tuning by ear.

`--order arc|tempo|harmonic|trope|playlist`, default `arc`. Playlist order is
retained only for comparison — the user confirms it carries no artistic intent, and
is in fact chronological, which is *why* the pre-trope-library songs cluster at the
front.

**`arc` rather than monotonic tempo.** A pure BPM sort climbs from 96 to 172 and
stops, which gives the set nowhere to go and no room for a `drag` — you cannot
descend from a peak you never leave. `arc` places the peak around 60–70% through
(`--peak`), climbing to it and descending after, so the shape is a set rather than a
ramp. The `drag` filler sits on the turn.

The tempo term is evaluated against the arc's *target* tempo at each position
instead of the previous track's, so the descent is as constrained as the climb.

**Known limits.** The TSV is a deliberate mechanical subset of `library.md`: it
catches 5 of the 9 fold/buckle tracks the library lists by hand. Spacing will be
good, not perfect.

All 37 audio slugs currently match a lyric filename exactly. Matching still keeps
a close-match fallback, because audio slugs derive from Suno titles while lyric
filenames are hand-made, and `suno-download.py` already documents that the two
drift (titles are often the hook line, not the filename). A track that silently
fails to match is scored as trope-free and can land next to something it echoes,
so the failure mode is invisible — the fallback is cheaper than the bug.

### Transition model

**Fillers are conditional** (`--fillers auto|always|never`, default `auto`). A
filler goes in only when it earns its place. A 24-bar filler is ~46s; on all 36
joins that would be nearly half the running time and would become a tic in its own
right.

There are **three roles**, with three different triggers, lengths and treatments.
They are not interchangeable.

| role | trigger | bars | ramp |
|---|---|---|---|
| `bridge` | B has a vocal intro, or the tempo gap can't be stretched | 24 | A's BPM → B's BPM |
| `rest` | intensity debt crossed the threshold | 16 | none |
| `drag` | the arc turns from ascent to descent | 32 | large, deliberate |

**bridge** is the original case. Its tempo justification is weaker than it first
appeared — with 37 tracks a BPM sort already puts 36/36 joins inside the clamp — so
it is now justified almost entirely by vocal intros, which was the user's original
reason for wanting fillers.

**rest** exists because the lyrics get intense and a continuous hour gives the
listener nowhere to stand. The trigger is not a property of a join but of a *run*,
so it accumulates: each track adds `vocal_density − baseline` to a running debt, and
when the debt crosses a threshold the next join gets a rest and the debt resets.
That places rests after the densest runs rather than at fixed intervals, and
self-spaces without a rule about minimum separation.

`vocal_density` — the fraction of a track where the vocal stem is actually sounding
— comes free from the separation pass. It measures the thing that matters (how
relentlessly someone is singing at you) with no lyric analysis at all. Measured 85%
on `part-it-out`.

A rest must be **treated**, not just a bare loop: low-passed, longer reverb, lower
level. Sixteen bars of dry breakbeat is not restful, it's a drum solo. This is the
one role where the `other` stem may beat drums as the bed, which is why it is now
kept.

**drag** is a long fast-to-slow deceleration — the hinge of the arc, not a join. It
deliberately exceeds the ±12% clamp, because a drum loop is the one thing that
survives being taken 152 → 96, and doing so *is* the musical move. Long on purpose:
a fast deceleration sounds like a tape stopping, a slow one sounds like a comedown.
Pitch-preserved via `atempo` (`asetrate` would drop pitch with it, which is a
vinyl-brake effect — a different, more dramatic device, not what a 32-bar comedown
wants). One or two per mix at most.

**Direct join** (8 bars): B enters high-passed at bar 0, bass swaps at bar 4, A is
out by bar 8.

**Filler join** (24 bars default, `--filler-bars out,ramp,in`):

| bars | what happens |
|---|---|
| 0–4 | A continues; filler enters at A's BPM, in phase with A's downbeats, high-passed |
| 4 | bass swap — A's lows out, filler's lows in; A begins fading |
| 4–8 | A fades out; filler alone by bar 8 |
| 8–8+R | filler alone, ramping A's BPM → B's BPM |
| 8+R | B enters on a downbeat, high-passed |
| +4 | bass swaps to B; filler fades out over four bars |

**Where A leaves:** first downbeat at least one bar after A's last vocal span ends,
so the mix-out never talks over the final sung line — which is exactly what a fixed
offset from the end does now. Falls back to eight bars from the end if that lands
too late.

**Where B enters**, decided from the vocal spans:
- B's vocal starts *before* B's drums (the a cappella pickup) → enter at B's first
  downbeat, over the filler bed. The pickup is preserved and lands on a groove
  instead of colliding with A's outro. This is the case fillers exist for.
- Otherwise → enter at B's first drum-active downbeat, skipping any dead intro.

### The bass swap

The single biggest audible change, and it applies to both join types. Split each
contribution at ~180Hz into low and high bands and volume-automate each band on its
own schedule, so the incoming track arrives high-passed while the outgoing keeps
the low end, then the lows trade at a defined bar. This is what makes a join read
as a mix rather than a dissolve.

### The tempo ramp

`atempo` is constant per invocation, so a filler ramping 96 → 123 is rendered
**bar by bar**, each bar at its own ratio, concatenated. Per-bar granularity puts
the steps under 1bpm — inaudible. Ramping in 4- or 8-bar chunks gives 3–7bpm steps,
which are clearly audible.

### Rendering

**Segment-wise, then concat** — not one giant filtergraph. `mixtape.py` builds a
single chained `acrossfade` graph; with 37 tracks and three-way overlaps that
becomes unmanageable and undebuggable. Each track body and each transition renders
to its own temp file, then one `concat`. This also makes `--only-join N` possible,
so a bad join can be re-rendered and auditioned in seconds instead of re-rendering
76 minutes.

## Output

Unchanged format: 320k mp3 plus a `.txt` with YouTube chapters above the marker and
technical detail below it. Chapter timings account for filler durations. Fillers
appear in the notes block only — nobody wants "Break 4" in their chapter list.

## Verification

Success criteria that don't require ears:

1. **No two vocal spans overlap anywhere in the output timeline.** This is the
   direct, objective encoding of "it doesn't sound like a smear", computable from
   `vocal_spans` plus the mix plan. Emitted by `--check`.
2. **Every track and every filler starts on a downbeat.** Pure grid arithmetic,
   unit-testable without rendering audio.
3. **No seam where tempo jumps more than 2%.**
4. **No two tracks sharing a live trope entry within 3 positions**, and a report of
   the closest surviving collision.
5. Total rendered duration matches the planned duration.

Then: render a 3-join test mix and listen before committing to 76 minutes.

## Build order

Each step ends in something audible or checkable.

1. `stems.py` → verify: `stems.json` populated for 37 tracks; `grid_score` high for
   programmed material; spot-check three downbeat phases by ear against the audio.
2. `fillers.py` → verify: listen to six fillers on loop; no click at the seam, no
   drift over four repeats.
3. `mixdown.py` ordering only → verify: `--check` reports zero adjacent trope
   collisions and 36/36 joins inside the clamp.
4. `mixdown.py` direct joins + bass swap → verify: render three joins, listen. This
   step alone should already beat the current mix.
5. `mixdown.py` fillers + tempo ramp → verify: render the three joins with the
   worst vocal intros.
6. Full render → verify: all five `--check` criteria, then listen.

Step 4 is a natural stopping point if the bass swap and ordering turn out to be
enough on their own.

## Risks and open items

- **4/4 assumed** throughout. Fine for laundry.
- **tempo-cnn can still octave-error.** Escape hatch: a BPM override keyed by clip
  id.
- **Demucks must be running**, and ComfyUI currently holds ~17.9GB of the 24GB
  card. The separation pass may need ComfyUI stopped; Demucks' `oom_retry_count`
  config suggests this contention is known.
- **Disk**: 31GB free. Stems for laundry are ~1.6GB, fillers ~100MB. Comfortable.
- **`audio/` is gitignored**, so stems, fillers and caches aren't reproducible from
  a clone — consistent with how `analysis.json` already works.
- `Four Degrees` was resolved to `ultracoase` by the band matcher but is in the
  laundry playlist and now has `laundry/four-degrees.txt`. Treated as laundry.
- **The trope regexes are a subset** of the hand-maintained library, so spacing is
  approximate. Worth revisiting if the mix still echoes.
