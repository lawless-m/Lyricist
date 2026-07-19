# Trope Library & write-song Skill — Design

## Problem

Five song-style skills (`.claude/skills/{lurker,laundry,lucy-might,purple-dog,the-bell-knows-my-name}`)
each carry their own "don't let it calcify" section banning devices that got overused *within that
style*. In practice, overused devices leak **across** styles, and nothing catches it:

- Lurker's spec explicitly bans the construction `"___ where ___ should ___"`. That ban only ever
  applied to lurker. The construction has since become the load-bearing hook line in nearly every
  purple-dog and the-bell-knows-my-name song (`"I've got a menu where a mouth should be"`,
  `"I've got a checkbox where a choice should be"`, `"I've got a form where a hand should be"`, etc.
  — a dozen+ near-identical instances across two other styles).
- The exact phrase `"and the drums fold in on themselves —"` appears verbatim in at least four
  laundry (dissociative-hardcore) songs.
- The imagery motif `"my grandmother's grandmother [did X]"` recurs near-verbatim four+ times
  within the-bell-knows-my-name.

There is no shared record of what's already been used, so nothing stops it recurring, and each
style's local ban-list has to be hand-maintained after the fact.

## Goals

- Track overused devices **across all five styles**, not per-style.
- Catch three different kinds of repetition: exact/near-exact **phrases**, abstract **constructions**
  (same sentence template, different words), and **imagery/content motifs**.
- Make reuse detection part of the normal song-writing flow, not a separate manual step someone
  has to remember to run.
- Seed the library from the 73 existing songs (bands: `guessed`, `laundry`, `lucy-might`,
  `purple-dog`, `the-bell-knows-my-name`) without editing any of those existing files.

## Non-goals

- Not rewriting or "fixing" any of the 73 existing songs — they stay exactly as they are.
- Not an exhaustive catalog of every device ever used — only devices already proven to repeat
  2+ times across the existing corpus get seeded. Devices used only once in the existing 73 are
  not pre-logged (accepted gap; see Open Questions).
- Not building standalone tooling/scripts outside the Claude Code skill system — this is a
  skill-and-markdown design, not a software project.

## Architecture

### 1. Folder restructure

Each style's spec currently lives entirely in `.claude/skills/<style-name>/SKILL.md`. It moves
into the corresponding band folder at the repo root, split into two files:

- `<band>/template.md` — persona/voice, song structure, devices checklist, dial/theme guidance,
  and **band-local** rotation rules (e.g. "never reuse Talon's drain-body," "never reuse the
  Pepsi") — i.e. everything about writing the words. This is the existing SKILL.md content minus
  the Suno style-prompt blocks.
- `<band>/styles.md` — the reusable Suno style-prompt variants for that band (e.g. lurker's
  dusty-torch / frozen-mechanical / sparse-acoustic blocks).

Band ↔ old-skill-name mapping (also the alias table `write-song` uses to resolve a request):

| Band folder             | Old skill name         | Persona / genre label     |
|--------------------------|--------------------------|----------------------------|
| `guessed`                | `lurker`                 | Guessed (trip-hop)         |
| `laundry`                | `dissociative-hardcore`  | Laundry                    |
| `lucy-might`             | `lucy-might`              | Lucy Might                 |
| `purple-dog`             | `institutional-hardcore` | Purple Dog                 |
| `the-bell-knows-my-name` | `gypsy-emo`               | The Bell Knows My Name     |

`.claude/skills/<old-style-name>/` is deleted once its content has been migrated. After the
restructure, `.claude/skills/` contains only `write-song/`.

### 2. `write-song` skill — sole entry point

Lives at `.claude/skills/write-song/SKILL.md`. Its description/triggers cover all existing
request phrasing so nothing that currently works stops working: `"song for Guessed"`,
`"another purple-dog song"`, `"make new song for laundry"`, `"another gypsy-emo song"`, and a bare
theme with no style named (in which case it asks which band). It contains the band-alias table
above so both the band-folder name and the historical persona/genre name resolve correctly.

The five band folders no longer contain a triggerable skill — `template.md` / `styles.md` are
reference content that `write-song` reads, not skills Claude matches requests against directly.

### 3. write-song workflow

1. Resolve the band from the request (using the alias table; ask if ambiguous/unspecified).
2. Read `<band>/template.md` and `<band>/styles.md`.
3. Read `.claude/tropes/library.md`.
4. Draft the song per `template.md`.
5. Check every notable device in the draft (construction, distinctive phrase, imagery motif)
   against the library. Any collision → revise the draft, re-check.
6. Save `<band>/<slug>.txt` (lyric) and `<band>/<slug>.style.txt` (Suno style prompt), matching
   the existing naming convention exactly.
7. Log the new song's notable devices into the library as new entries. They are not yet
   "retired" — but per the 2-strikes rule below, the *next* use of any of them, in any band,
   is what gets blocked.

### 4. Trope library — `.claude/tropes/library.md`

One shared file, three sections: **Constructions**, **Phrases**, **Imagery / Motifs**.

Ban rule: **2 uses anywhere in the catalog → retired.** Because the first use already puts a
device in the library, this collapses to a single check: *does the draft collide with anything
already logged, at all?* If yes, it's a reuse and must be revised — there is no "used once, still
available" state to track separately, so entries don't need a running count, just provenance.

Entry format (illustrative):

```markdown
### "[X] where [Y] should be"
- Type: Construction
- Status: retired
- Example: "I've got a menu where a mouth should be" — purple-dog/robocaller
- Also seen: purple-dog (8×), the-bell-knows-my-name (5×), guessed (1×, origin)

### "and the drums fold in on themselves"
- Type: Phrase
- Status: retired
- Example: laundry/breeder
- Also seen: laundry/addicted-to-declining, laundry/turn-it-down, laundry/scroll-up

### Grandmother's-grandmother ancestral lineage
- Type: Motif
- Status: retired
- Example: "My grandmother's grandmother put her hands into this ground" — the-bell-knows-my-name/i-was-here-before-your-fathers
- Also seen: wheels-where-i-should-kneel, do-you-hear-the-ground-you-keep, sing-the-valley-back-to-us
```

### 5. Seeding

A one-time **targeted scan** of all 73 existing songs across all 5 band folders, looking for
phrases/constructions/motifs that already recur 2+ times anywhere in the corpus (not limited to
the 3 examples already found above — those three are confirmed hits, but the scan covers the
whole set). Each hit becomes a seeded, already-retired entry with source songs noted for
provenance. This is a read-only pass — none of the 73 song files are modified. Runs once, during
implementation, before `write-song` goes live.

## Open questions / accepted gaps

- Devices used only once in the existing 73 songs are not pre-logged (only 2+-time repeats get
  seeded), so a first future reuse of one of those won't be caught by the library — it would take
  a second future use (or manual review) to surface. Accepted tradeoff for keeping the seeding
  pass targeted rather than exhaustive.
- No automated/scripted enforcement — the check in step 5 of the workflow relies on `write-song`
  (i.e. Claude) actually reading and comparing against the library each time, not a linter.
