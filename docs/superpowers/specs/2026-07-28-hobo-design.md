# hobo — New Band Design

## Problem

The catalog has seven wired bands plus `girlboss`, and none of them occupy the 90s hip-hop /
guitar crossover lane — the Whale "Hobo Humpin Slobo Babe" sound: a fuzz riff over a live
breakbeat, cheap sampled junk on top, a motormouth female vocal and a shouted gang hook. A new
band, **hobo**, carries that sound, following the established `<band>/template.md` +
`<band>/styles.md` pattern `write-song` already reads.

The design problem is not the sound — it's the words. The requested method is collage, and
`laundry` already owns collage. hobo needs a collage engine that cannot be mistaken for
Laundry's.

## Goals

- Add one new band, **hobo**, in the established two-file format.
- Give it an engine distinct from all eight existing bands, and a lyric method that shares
  Laundry's mechanics without sharing its temperature.
- Fence it explicitly against `laundry` (collage) and `girlboss` (female-led hip-hop) — the two
  nearest neighbours — at the level of register, palette and instrumentation.
- Wire it into `write-song`'s band lookup table.
- Ship a reference example song in `template.md`, as every other band's template has.

## Non-goals

- Not drum'n'bass, and not the dry no-guitar indie hip-hop of `girlboss/styles.md`.
- Not a thesis band. The engine is an appetite, not an argument; nothing here is *about* poverty,
  homelessness or the economy, and no song should read as commentary on any of them.
- Not restructuring `laundry`, `girlboss`, or the trope library.
- Not wiring `girlboss` into `write-song` — its exclusion is out of scope here either way.

## Architecture

### Folder

`hobo/` at the repo root, containing `template.md` and `styles.md`, matching the seven wired
bands' layout exactly (`styles.md` plural — the `write-song` workflow reads that filename).

### Engine — junk swagger

Collage as **appetite**. Every image is something she found, and she wants it.

This is Laundry's method run at the opposite temperature, and that inversion is the whole design.
Laundry's images drift past a narrator who has stopped being able to feel them; hobo's pile up in
front of a narrator who wants all of them. Same mechanic — concrete nouns, missing joins, sound
picking the word — opposite charge. Laundry's collage is a symptom. hobo's is a boast.

Consequences that follow from the inversion, and must hold:

- **No comedown.** No rue, no numbness, no dawning awareness that the pile is worthless. The
  moment she suspects it, the song has become a different band's.
- **The joins are missing because she's moving too fast**, not because they dissolved. The
  drift has a cause and the cause is greed.
- **The song lands.** Against Laundry's no-landing rule: hobo ends hard, on the riff. She wins.

### Persona — the scavenger

Female lead: motormouth, sing-song, taunting, close-mic'd and in front of the beat. She owns a
mountain of worthless things and is genuinely thrilled about it.

**Girl-gang chorus** on the hooks — shouted, sloppy, playground/terrace unison, deliberately
untight. This is the second fence against `girlboss`, which also gang-chants but cold and
dead-on; hobo's gang is a mess on purpose.

### Device pool (checklist for `template.md`)

Four moves, **rotated, not mandatory**. Each song hits at least two, and never the same two as
the previous song — a fixed per-song device calcifies, which is what this pool exists to avoid.

- **The haul** — an inventory of found junk that accelerates until the list itself becomes the
  hook, the riff locking to it.
- **The drop-out taunt** — guitar cuts dead mid-hook, breakbeat left naked, she taunts into the
  hole a cappella, riff slams back in.
- **The appraisal** — a whole verse spent pricing one broken object, wrongly, at length, and
  with total confidence.
- **The trade** — one line: something genuinely valuable swapped for something worthless, and
  she came out ahead.

### The bones (never rotate)

The swagger register; collage assembled by appetite rather than drift; the fuzz riff as backbone;
the girl-gang chorus; the hard landing.

### Palette fence

hobo takes roadside, skip, car-boot and gutter junk. `laundry` keeps retail, shipping and
body-parts. Object for object, this is the main thing keeping the two collages from converging —
if a hobo draft reaches for a conveyor belt or a good kidney, it's drifting into Laundry.

### Song structure

Riff intro → motormouth verse → gang hook → verse → rotating device slot → final hook with the
riff doubled → hard stop on the riff.

### Sound / `styles.md`

Fuzz guitar riff as the backbone over a live-sounding 90s breakbeat, cheap sampled junk on top
(vinyl crackle, horn stabs, a wrong-speed sample), female motormouth vocal, shouted girl-gang
hook. Reference points: Whale, *Mellow Gold*-era Beck, Luscious Jackson, the *Judgment Night*
soundtrack. Following the existing convention, the file offers a small number of named Suno
variants rather than one fixed prompt — e.g. a riff-forward/heavier variant and a
sample-forward/looser variant — with rotation guidance.

### `write-song` integration

Add a row to the band lookup table in `.claude/skills/write-song/SKILL.md`:

| Band folder | Persona / genre aliases                                              |
|-------------|----------------------------------------------------------------------|
| `hobo`      | hobo, junk swagger, the scavenger, 90s hip-hop guitar crossover      |

The skill's description line also names the bands it triggers on; it needs updating from seven to
eight so a bare "write me a hobo song" resolves. No other change to the workflow — it already
treats band folders as interchangeable reference content.

## What hobo is not

- **Not `laundry`.** Its exact inverse; read them against each other. Laundry's narrator can't
  feel the objects, hobo's wants them; Laundry withholds catharsis and refuses to land, hobo
  lands hard.
- **Not `girlboss`.** girlboss's narrator is knowing, covert and competent, and the engine is
  trust-transgression. hobo's is loud, transparent and working nobody. Nothing is being got over
  on anyone; she's just delighted with a broken lamp.
- **Not `coase-guard`.** No politics, no friend/enemy line, no crew. She is outside the thing,
  not against it.

## Open questions / accepted gaps

- `template.md` needs a full reference example song, per the pattern every other band follows.
  It is produced through the normal `write-song` flow (draft → `check.sh` → fuzzy trope check →
  style prompt → log devices into `library.md` and `banned-patterns.tsv`), not authored inside
  this design doc.
- Whether the reference example leads with the haul or the appraisal is left to the
  implementation plan; it should demonstrate the two-device rotation rule rather than a fixed
  spine.
