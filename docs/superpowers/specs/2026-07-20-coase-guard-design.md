# Coase Guard — New Band Design

## Problem

The catalog has five bands, each built around a distinct emotional engine and persona
(`guessed`, `laundry`, `lucy-might`, `purple-dog`, `the-bell-knows-my-name`). None of them
occupy the aesthetic explored in conversation: songs built around ideas from Hayek, Schmitt,
Coase, and Sorel — spontaneous order, friend/enemy clarity, the firm as a self-organizing unit,
myth as a tool that moves people whether or not it's literally true. A new band is needed to
carry that engine, following the existing `<band>/template.md` + `<band>/styles.md` pattern that
`write-song` already reads.

## Goals

- Add one new band, **Coase Guard**, in the established two-file format.
- Give it a genre distinct from the existing five: industrial hip-hop ("industrial white guy
  hip hop").
- Translate the four thinkers into a concrete songwriting engine — persona, structure, and a
  recurring-devices checklist — not an explicit political argument set to music.
- Keep the "enemy" institutional/abstract and any violence stylized/legendary, so the songs read
  as art about the ideas (the way Purple Dog is art about institutional dread) rather than
  literal endorsement or real-world targeting.
- Wire it into `write-song`'s band lookup table exactly like the other five.

## Non-goals

- Not writing actual song lyrics as part of this design — that's `write-song`'s job, per its
  existing workflow (draft → check against `.claude/tropes/library.md` → save → log).
- Not restructuring any of the other five bands or the trope library.
- Not producing overtly partisan/programmatic lyrics (slogans, policy claims, real-world
  political figures or parties).

## Architecture

### Folder

`coase-guard/` at the repo root, containing `template.md` and `styles.md`, matching the other
five bands' layout exactly.

### Personas

Two, sharing the band the way a two-vocalist act would — never duetting in the same song;
each has her/his own mode(s), same shared world and devices.

- **The Foreman** — runs a small, unlicensed, self-organizing crew (deliberately unspecific
  trade — could read as a work crew, a family outfit, a corner operation). Delivery: rapid,
  technical, cold-controlled flow — the "white guy rap" precision lane, not comedic. Two modes:
  - *What We Have* — present-tense pride in the crew's spontaneous order: things that work
    because nobody designed them, contempt for whoever shows up to inspect/license/plan.
  - *Where We Came From* — origin myth: the founding struggle retold as legend, decisive
    moments treated as sacred rather than examined.
- **The Quartermaster** — runs the household/family end of the same world. Trad-wife surface
  imagery (hearth, table, garden, kids) immediately undercut by blunt logistics — no
  sentimentality. One mode:
  - *Who Eats* — present-tense domestic reckoning: who's fed, who's let in, what's actually
    owed. She is the reality-check on the Foreman's myth-making, not a second mythmaker.

### Recurring devices (checklist for `template.md`)

- **The wink** (Foreman only) — one flat, clinical line per song where he half-admits the
  crew's story is more legend than fact, then keeps telling it anyway because it holds the crew
  together. Dramatizes the Sorel move rather than stating it.
- **The tally** (Quartermaster only) — her equivalent of the wink: not a myth-check but a
  resource-check — one cold, concrete number or fact that cuts through whatever warmth the verse
  just built.
- **Competent inventory** — a rattled-off list of things that run without a manual/permit/
  committee, concrete and blue-collar-textured.
- **The friend/enemy line** — one unhedged "us and them" moment per song. Enemy is always
  institutional/abstract (inspectors, licensors, the algorithm, absentee owners, the committee)
  — **never** an ethnic, religious, or national group, and no real-world hate-group iconography.
- **The founding flash** — a compressed, already-legendary retelling of a decisive past moment
  (a strike, a refusal, a standoff). Stylized/symbolic — never a literal instruction toward
  real-world violence.
- **The chant hook** — repeated, stacked, or call-and-response; the crew/household's shared
  claim, present from the start of the song (unlike Purple Dog's earned shout-back).

### Song structure

Cold industrial intro → rapped verse (scene/context) → chanted hook → rapped verse (escalation/
specific detail) → the wink or the tally (spoken/half-spoken, flat) → final hook, now carrying
that weight.

### Sound / `styles.md`

Industrial hip-hop: mechanized loops, distorted samples, factory-floor textures under rapid
technical rapped verses; chanted (not sung) hooks. Foreman's takes run harder/more metallic;
Quartermaster's run colder and sparser, more space between hits, so the domestic imagery has
room before it gets cut down. Following the existing `styles.md` convention, this file will
offer a small number of named Suno prompt variants (e.g. a harder/metallic Foreman variant and a
sparser Quartermaster variant) rather than one fixed prompt.

### `write-song` integration

Add a row to the band lookup table in `.claude/skills/write-song/SKILL.md`:

| Band folder    | Persona / genre aliases                              |
|-----------------|--------------------------------------------------------|
| `coase-guard`  | Coase Guard, industrial hip-hop, the Foreman, the Quartermaster |

No other change to `write-song`'s workflow — it already treats band folders as interchangeable
reference content.

## Open questions / accepted gaps

- `template.md` needs at least one full reference example song (the pattern every other band's
  template follows) — likely a Foreman "What We Have" track, per the existing per-band
  convention of one worked example. Left for the implementation plan to produce via the normal
  `write-song` drafting + trope-check flow, not authored as part of this design doc.
- Whether Quartermaster gets her own reference example in the initial `template.md` or picks one
  up on her first `write-song` invocation is left to the implementation plan.
