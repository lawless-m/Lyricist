# Trope Library & write-song Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the five standalone song-style skills with band-folder reference files (`template.md` + `styles.md`) plus one shared `write-song` skill that drafts songs, checks every draft against a cross-band trope library, saves output in the existing naming convention, and logs new devices so no device is ever reused a second time anywhere in the catalog.

**Architecture:** Content restructure, no application code. Five `.claude/skills/<style>/SKILL.md` files get split by section into `<band>/template.md` (everything except the Suno prompt notes) and `<band>/styles.md` (just the Suno prompt notes section). A new `.claude/skills/write-song/SKILL.md` becomes the sole trigger for song requests and reads those files plus `.claude/tropes/library.md` at write time. The library is seeded once from a real scan of the 73 existing songs; those songs are read-only and never modified.

**Tech Stack:** Markdown files only. Git for version control (`git@github.com:lawless-m/Lyricist.git`, branch `main`, already pushed).

## Global Constraints

- The 73 existing song files (`*/[!.]*.txt` under `guessed/`, `laundry/`, `lucy-might/`, `purple-dog/`, `the-bell-knows-my-name/`, excluding `*.style.txt`/`*.stand.txt`) must not be modified by this plan.
- Ban rule for the trope library: **any device already logged (1 use) is retired — a second use anywhere in the catalog, in any band, is not allowed.** There is no "used once, still available" state.
- Trope library has exactly three categories: Constructions, Phrases, Imagery/Motifs.
- Output naming convention (already established by the existing 73 songs, must be preserved): `<band>/<slug>.txt` for the lyric, `<band>/<slug>.style.txt` for the Suno style prompt — flat single-paragraph text, no markdown.
- After this plan, `.claude/skills/` contains only `write-song/`. The other five skill folders are deleted (not archived, not kept as redirects).

---

## File Structure

```
guessed/template.md                       (new — from .claude/skills/lurker/SKILL.md)
guessed/styles.md                         (new — from .claude/skills/lurker/SKILL.md)
laundry/template.md                       (new — from .claude/skills/dissociative-hardcore/SKILL.md)
laundry/styles.md                         (new — from .claude/skills/dissociative-hardcore/SKILL.md)
the-bell-knows-my-name/template.md        (new — from .claude/skills/gypsy-emo/SKILL.md)
the-bell-knows-my-name/styles.md          (new — from .claude/skills/gypsy-emo/SKILL.md)
purple-dog/template.md                    (new — from .claude/skills/institutional-hardcore/SKILL.md)
purple-dog/styles.md                      (new — from .claude/skills/institutional-hardcore/SKILL.md)
lucy-might/template.md                    (new — from .claude/skills/lucy-might/SKILL.md)
lucy-might/styles.md                      (new — from .claude/skills/lucy-might/SKILL.md)
.claude/skills/lurker/                    (deleted)
.claude/skills/dissociative-hardcore/     (deleted)
.claude/skills/gypsy-emo/                 (deleted)
.claude/skills/institutional-hardcore/    (deleted)
.claude/skills/lucy-might/                (deleted)
.claude/tropes/library.md                 (new — seeded trope library)
.claude/skills/write-song/SKILL.md        (new — the only remaining skill)
```

---

### Task 1: Migrate lurker → guessed/template.md + guessed/styles.md

**Files:**
- Create: `guessed/template.md`
- Create: `guessed/styles.md`
- Delete: `.claude/skills/lurker/SKILL.md` and the now-empty `.claude/skills/lurker/` directory

**Interfaces:**
- Consumes: `.claude/skills/lurker/SKILL.md` (existing file, do not modify until the delete step)
- Produces: `guessed/template.md`, `guessed/styles.md` — read by `write-song` in Task 7

- [ ] **Step 1: Extract the Suno prompt notes section into styles.md**

Run:
```bash
cd /home/matt/Git/Lyricist
{
  echo "# Guessed — Suno Style Prompts"
  echo
  awk '/^## Suno prompt notes$/{flag=1} flag{if(/^## Reference example/){exit} print}' .claude/skills/lurker/SKILL.md
} > guessed/styles.md
```

- [ ] **Step 2: Verify styles.md contains the three style-prompt variants**

Run: `grep -c '^  trip hop\|^  cold mechanical\|^  sparse acoustic' guessed/styles.md`
Expected: `3`

- [ ] **Step 3: Extract everything else (minus frontmatter, minus the Suno section) into template.md**

Run:
```bash
cd /home/matt/Git/Lyricist
awk 'NR==1 && /^---$/{fm=1; next} fm && /^---$/{fm=0; afterfm=1; next} fm{next} afterfm{afterfm=0; if(/^$/) next} /^## Suno prompt notes$/{skip=1} /^## Reference example/{skip=0} !skip' .claude/skills/lurker/SKILL.md > guessed/template.md
```

- [ ] **Step 4: Verify template.md has the expected sections and no frontmatter/Suno section**

Run: `grep -n '^## ' guessed/template.md`
Expected:
```
## The core idea
## No crowd — the inverted device
## Writing the words — sparse, oblique, repeated
## Song structure (the template)
## The recurring devices (checklist)
## Handling the subject matter
## Reference example (a finished song in this style)
## Don't let it calcify (rotate the surfaces, keep the bones)
## When writing a new one
```
Run: `head -1 guessed/template.md`
Expected: `# Lurker Trip-Hop — Song Style Spec` (no `---` frontmatter line)

- [ ] **Step 5: Delete the old skill**

Run: `rm -rf /home/matt/Git/Lyricist/.claude/skills/lurker`

- [ ] **Step 6: Commit**

```bash
cd /home/matt/Git/Lyricist
git add guessed/template.md guessed/styles.md .claude/skills/lurker
git commit -m "Migrate lurker skill into guessed/template.md + guessed/styles.md"
```

---

### Task 2: Migrate dissociative-hardcore → laundry/template.md + laundry/styles.md

**Files:**
- Create: `laundry/template.md`
- Create: `laundry/styles.md`
- Delete: `.claude/skills/dissociative-hardcore/SKILL.md` and the directory

**Interfaces:**
- Consumes: `.claude/skills/dissociative-hardcore/SKILL.md`
- Produces: `laundry/template.md`, `laundry/styles.md`

- [ ] **Step 1: Extract styles.md**

```bash
cd /home/matt/Git/Lyricist
{
  echo "# Laundry — Suno Style Prompts"
  echo
  awk '/^## Suno prompt notes$/{flag=1} flag{if(/^## Reference example/){exit} print}' .claude/skills/dissociative-hardcore/SKILL.md
} > laundry/styles.md
```

- [ ] **Step 2: Verify**

Run: `grep -c '^\s*```' laundry/styles.md`
Expected: `6` (three style-prompt variants, each a fenced code block with an open and close fence)

- [ ] **Step 3: Extract template.md**

```bash
cd /home/matt/Git/Lyricist
awk 'NR==1 && /^---$/{fm=1; next} fm && /^---$/{fm=0; afterfm=1; next} fm{next} afterfm{afterfm=0; if(/^$/) next} /^## Suno prompt notes$/{skip=1} /^## Reference example/{skip=0} !skip' .claude/skills/dissociative-hardcore/SKILL.md > laundry/template.md
```

- [ ] **Step 4: Verify**

Run: `grep -n '^## ' laundry/template.md`
Expected:
```
## The core idea
## Writing the words — the collage method
## Song structure (the template)
## The recurring devices (checklist)
## Reference example (a finished song in this style)
## Don't let it calcify (rotate the surfaces, keep the bones)
## When writing a new one
```

- [ ] **Step 5: Delete the old skill**

Run: `rm -rf /home/matt/Git/Lyricist/.claude/skills/dissociative-hardcore`

- [ ] **Step 6: Commit**

```bash
cd /home/matt/Git/Lyricist
git add laundry/template.md laundry/styles.md .claude/skills/dissociative-hardcore
git commit -m "Migrate dissociative-hardcore skill into laundry/template.md + laundry/styles.md"
```

---

### Task 3: Migrate gypsy-emo → the-bell-knows-my-name/template.md + the-bell-knows-my-name/styles.md

**Files:**
- Create: `the-bell-knows-my-name/template.md`
- Create: `the-bell-knows-my-name/styles.md`
- Delete: `.claude/skills/gypsy-emo/SKILL.md` and the directory

**Interfaces:**
- Consumes: `.claude/skills/gypsy-emo/SKILL.md`
- Produces: `the-bell-knows-my-name/template.md`, `the-bell-knows-my-name/styles.md`

- [ ] **Step 1: Extract styles.md**

```bash
cd /home/matt/Git/Lyricist
{
  echo "# The Bell Knows My Name — Suno Style Prompts"
  echo
  awk '/^## Suno prompt notes$/{flag=1} flag{if(/^## Reference example/){exit} print}' .claude/skills/gypsy-emo/SKILL.md
} > the-bell-knows-my-name/styles.md
```

- [ ] **Step 2: Verify**

Run: `grep -c '^\s*```' the-bell-knows-my-name/styles.md`
Expected: `6` (three style-prompt variants — darker/cinematic, softer/Midwest-emo, punkier/Gogol-Bordello — each a fenced code block with an open and close fence)

- [ ] **Step 3: Extract template.md**

```bash
cd /home/matt/Git/Lyricist
awk 'NR==1 && /^---$/{fm=1; next} fm && /^---$/{fm=0; afterfm=1; next} fm{next} afterfm{afterfm=0; if(/^$/) next} /^## Suno prompt notes$/{skip=1} /^## Reference example/{skip=0} !skip' .claude/skills/gypsy-emo/SKILL.md > the-bell-knows-my-name/template.md
```

- [ ] **Step 4: Verify**

Run: `grep -n '^## ' the-bell-knows-my-name/template.md`
Expected:
```
## The core idea
## Song structure (the template)
## The recurring devices (checklist)
## Reference example (a finished song in this style)
## When writing a new one
```

- [ ] **Step 5: Delete the old skill**

Run: `rm -rf /home/matt/Git/Lyricist/.claude/skills/gypsy-emo`

- [ ] **Step 6: Commit**

```bash
cd /home/matt/Git/Lyricist
git add the-bell-knows-my-name/template.md the-bell-knows-my-name/styles.md .claude/skills/gypsy-emo
git commit -m "Migrate gypsy-emo skill into the-bell-knows-my-name/template.md + styles.md"
```

---

### Task 4: Migrate institutional-hardcore → purple-dog/template.md + purple-dog/styles.md

**Files:**
- Create: `purple-dog/template.md`
- Create: `purple-dog/styles.md`
- Delete: `.claude/skills/institutional-hardcore/SKILL.md` and the directory

**Interfaces:**
- Consumes: `.claude/skills/institutional-hardcore/SKILL.md`
- Produces: `purple-dog/template.md`, `purple-dog/styles.md`

- [ ] **Step 1: Extract styles.md**

```bash
cd /home/matt/Git/Lyricist
{
  echo "# Purple Dog — Suno Style Prompts"
  echo
  awk '/^## Suno prompt notes$/{flag=1} flag{if(/^## Reference example/){exit} print}' .claude/skills/institutional-hardcore/SKILL.md
} > purple-dog/styles.md
```

- [ ] **Step 2: Verify**

Run: `grep -c '^\s*```' purple-dog/styles.md`
Expected: `6` (three style-prompt variants, each a fenced code block with an open and close fence)

- [ ] **Step 3: Extract template.md**

```bash
cd /home/matt/Git/Lyricist
awk 'NR==1 && /^---$/{fm=1; next} fm && /^---$/{fm=0; afterfm=1; next} fm{next} afterfm{afterfm=0; if(/^$/) next} /^## Suno prompt notes$/{skip=1} /^## Reference example/{skip=0} !skip' .claude/skills/institutional-hardcore/SKILL.md > purple-dog/template.md
```

- [ ] **Step 4: Verify**

Run: `grep -n '^## ' purple-dog/template.md`
Expected:
```
## The core idea
## Song structure (the template)
## The recurring devices (checklist)
## Reference example (a finished song in this style)
## When writing a new one
```

- [ ] **Step 5: Delete the old skill**

Run: `rm -rf /home/matt/Git/Lyricist/.claude/skills/institutional-hardcore`

- [ ] **Step 6: Commit**

```bash
cd /home/matt/Git/Lyricist
git add purple-dog/template.md purple-dog/styles.md .claude/skills/institutional-hardcore
git commit -m "Migrate institutional-hardcore skill into purple-dog/template.md + styles.md"
```

---

### Task 5: Migrate lucy-might → lucy-might/template.md + lucy-might/styles.md

**Files:**
- Create: `lucy-might/template.md`
- Create: `lucy-might/styles.md`
- Delete: `.claude/skills/lucy-might/SKILL.md` and the directory

**Interfaces:**
- Consumes: `.claude/skills/lucy-might/SKILL.md`
- Produces: `lucy-might/template.md`, `lucy-might/styles.md`

- [ ] **Step 1: Extract styles.md**

```bash
cd /home/matt/Git/Lyricist
{
  echo "# Lucy Might — Suno Style Prompts"
  echo
  awk '/^## Suno prompt notes$/{flag=1} flag{if(/^## Reference example/){exit} print}' .claude/skills/lucy-might/SKILL.md
} > lucy-might/styles.md
```

- [ ] **Step 2: Verify**

Run: `grep -c '^\s*```' lucy-might/styles.md`
Expected: `6` (three style-prompt variants, each a fenced code block with an open and close fence)

- [ ] **Step 3: Extract template.md**

```bash
cd /home/matt/Git/Lyricist
awk 'NR==1 && /^---$/{fm=1; next} fm && /^---$/{fm=0; afterfm=1; next} fm{next} afterfm{afterfm=0; if(/^$/) next} /^## Suno prompt notes$/{skip=1} /^## Reference example/{skip=0} !skip' .claude/skills/lucy-might/SKILL.md > lucy-might/template.md
```

- [ ] **Step 4: Verify**

Run: `grep -n '^## ' lucy-might/template.md`
Expected:
```
## The core idea
## No crowd — the silent duet
## Refuse the pronoun
## Writing the words — the deniable line
## Song structure (the template)
## The recurring devices (checklist)
## Handling the subject matter
## Reference example (a finished song in this style)
## Don't let it calcify (rotate the surfaces, keep the bones)
## When writing a new one
```

- [ ] **Step 5: Delete the old skill**

Run: `rm -rf /home/matt/Git/Lyricist/.claude/skills/lucy-might`

- [ ] **Step 6: Commit**

```bash
cd /home/matt/Git/Lyricist
git add lucy-might/template.md lucy-might/styles.md .claude/skills/lucy-might
git commit -m "Migrate lucy-might skill into lucy-might/template.md + styles.md"
```

---

### Task 6: Create the seeded trope library

**Files:**
- Create: `.claude/tropes/library.md`

**Interfaces:**
- Consumes: nothing (content below is final, verified against the 73-song corpus during planning)
- Produces: `.claude/tropes/library.md` — read and appended to by `write-song` (Task 7)

This step seeds six entries found by a real scan of all 73 existing songs (not just the three
examples that motivated this project). The scan looked for lines, sentence-level constructions,
and imagery motifs recurring across 2+ distinct song files, excluding structural section tags
(`[...]` and em-dash-wrapped production directions, which are expected to recur because the
template prescribes them). None of the source songs are modified by this step.

- [ ] **Step 1: Write the library file**

Create `.claude/tropes/library.md` with this exact content:

```markdown
# Trope Library

Shared across every band. Consult before finalizing any song; log after.

**Rule: any device below has already been used once. A second use of it — in any band,
in any song — is not allowed.** There is no "used once, still fine" state: being in this
file at all means it's retired. Check every notable construction, distinctive phrase, and
imagery motif in a draft against this file before saving.

Seeded 2026-07-19 from a scan of the 73 pre-existing songs across all five bands. That scan
was targeted at things already repeating 2+ times in the existing catalog, not an exhaustive
catalog of every line ever written — devices used only once in the pre-existing catalog are
not listed here. Everything logged from this point forward (new songs written via
`write-song`) is added on its *first* use, so it's caught on any second use anywhere.

## Constructions

### "I've got [X] where [Y] should be" / "I've got [X] where [Y] was" — inventory-of-loss couplet
- Originally banned only in the lurker spec (`"___ where ___ should ___"`). It escaped into
  three other bands and became a load-bearing hook line there instead of staying banned.
- Example: "I've got a menu where a mouth should be, and you call this a courtesy" — purple-dog/robocaller
- Also seen: guessed/handle-where-a-name-should-be, laundry/finna-retard, laundry/same-red,
  purple-dog/i-dont-want-your-damn-boots, purple-dog/purple-dog, purple-dog/secure-the-scene,
  purple-dog/suspicious-activity, the-bell-knows-my-name/does-the-building-dream-us-too,
  the-bell-knows-my-name/do-you-hear-the-ground-you-keep, the-bell-knows-my-name/i-was-here-before-your-fathers,
  the-bell-knows-my-name/sing-the-valley-back-to-us, the-bell-knows-my-name/the-bell-knows-my-name,
  the-bell-knows-my-name/the-graves-i-didnt-dig, the-bell-knows-my-name/the-plum-trees-secret,
  the-bell-knows-my-name/wheels-where-i-should-kneel

### "and the [drums/churn] [fold/buckle] in (on themselves)(, doesn't lift)" — mechanical-collapse hook line
- Example: "— and the drums fold in on themselves —" — laundry/breeder
- Also seen: laundry/addicted-to-declining, laundry/turn-it-down (fold variant);
  laundry/turn-it-on, laundry/same-red, laundry/permanence-is-temporary, laundry/finna-retard
  (buckle variant); laundry/keep-it-warm, laundry/scroll-up ("the churn folds in on itself,
  doesn't lift" variant)

## Phrases

### "closer than that"
- A response/refrain line that has become a stock line in nearly every lucy-might song,
  traced back to the reference example embedded in the old lucy-might spec — it was never
  asked for as a recurring device, it just got copy-pasted from the example every time.
- Example: lucy-might/ask-me-again
- Also seen: lucy-might/keep-still, lucy-might/never, lucy-might/nobodys-licked-me-yet,
  lucy-might/sit-on-my-knee, lucy-might/stay-in-the-room-with-me, lucy-might/take-your-time,
  lucy-might/the-easiest-evening, lucy-might/the-view, lucy-might/youd-have-stood-up-for-me

### "and the fiddle starts confessing"
- Example: the-bell-knows-my-name/the-bell-knows-my-name
- Also seen: the-bell-knows-my-name/do-you-hear-the-ground-you-keep,
  the-bell-knows-my-name/does-the-building-dream-us-too, the-bell-knows-my-name/old-dogs-choose-to-go,
  the-bell-knows-my-name/sing-the-valley-back-to-us, the-bell-knows-my-name/wheels-where-i-should-kneel

## Imagery / Motifs

### Grandmother's-grandmother ancestral lineage (naming an ancestor two generations back doing something to the land)
- Example: "My grandmother's grandmother put her hands into this ground" — the-bell-knows-my-name/i-was-here-before-your-fathers
- Also seen: the-bell-knows-my-name/wheels-where-i-should-kneel,
  the-bell-knows-my-name/do-you-hear-the-ground-you-keep ("grandmothers' grandmothers"),
  the-bell-knows-my-name/sing-the-valley-back-to-us ("our grandmothers' grandmothers")

### The folder as physical proof of institutional process/effort
- Crosses bands: shows up as the same small prop (a folder holding letters/certificates/paperwork)
  standing in for bureaucratic effort or evidence, in two different styles.
- Example: "Eleven months. Every letter, in order, in a folder." — guessed/upheld-in-full
- Also seen: guessed/what-was-the-hurry-for ("a woman with a folder"),
  laundry/mind-the-man ("a certificate somewhere in a folder")
```

- [ ] **Step 2: Verify the file was written correctly**

Run: `grep -c '^### ' /home/matt/Git/Lyricist/.claude/tropes/library.md`
Expected: `6`

Run: `grep -n '^## ' /home/matt/Git/Lyricist/.claude/tropes/library.md`
Expected:
```
## Constructions
## Phrases
## Imagery / Motifs
```

- [ ] **Step 3: Commit**

```bash
cd /home/matt/Git/Lyricist
git add .claude/tropes/library.md
git commit -m "Seed shared trope library from a scan of the 73 existing songs"
```

---

### Task 7: Create the write-song skill

**Files:**
- Create: `.claude/skills/write-song/SKILL.md`

**Interfaces:**
- Consumes: `<band>/template.md`, `<band>/styles.md` (Tasks 1-5), `.claude/tropes/library.md` (Task 6)
- Produces: `<band>/<slug>.txt`, `<band>/<slug>.style.txt` when actually run (not part of this plan —
  this task only creates the skill definition)

- [ ] **Step 1: Write the skill file**

Create `.claude/skills/write-song/SKILL.md` with this exact content:

```markdown
---
name: write-song
description: Use when writing a new song lyric for any of the five bands (Guessed, Laundry, Lucy Might, Purple Dog, The Bell Knows My Name). Triggered by requests like "song for Guessed", "another laundry track", "make new song for purple-dog", "another gypsy-emo song", "write me a lucy-might song", or a bare theme with no style named (in which case ask which band). This is the only entry point for song requests — the five style specs are reference files it reads, not separate skills.
---

# write-song

Writes a new song for one of the five bands, checks it against the shared trope library so
nothing gets reused across the catalog, and saves it using the existing file convention.

## Band lookup

Resolve the request to a band folder using this table (persona/genre names are historical
aliases — users may say either):

| Band folder               | Persona / genre aliases                                  |
|----------------------------|------------------------------------------------------------|
| `guessed`                  | Guessed, lurker, lurker trip-hop                            |
| `laundry`                  | Laundry, dissociative-hardcore, dissociative hardcore        |
| `lucy-might`               | Lucy Might                                                   |
| `purple-dog`                | Purple Dog, institutional-hardcore, institutional hardcore    |
| `the-bell-knows-my-name`   | The Bell Knows My Name, gypsy-emo, gypsy emo                 |

If the request names a theme but no band and it isn't clear from context, ask which band before
doing anything else.

## Workflow

1. Resolve the band (see table above).
2. Read `<band>/template.md` (persona, structure, devices, band-local rotation rules) and
   `<band>/styles.md` (Suno style-prompt variants for this band).
3. Read `.claude/tropes/library.md`.
4. Draft the song per `template.md`, picking a fresh theme/dial/arrangement per its own
   "don't let it calcify" guidance.
5. Check every notable device in the draft — constructions, distinctive phrases, imagery
   motifs — against every entry in `.claude/tropes/library.md`. **Any match, in any category,
   means revise the draft to avoid it, then re-check.** A device only needs to appear once in
   the library to be off-limits; there is no "safe to use twice" tier.
6. Pick the appropriate style-prompt variant from `styles.md` (or adapt it to the song's dial
   position, following that file's own guidance), and save both output files:
   - `<band>/<slug>.txt` — the lyric, where `<slug>` is a short kebab-case phrase drawn from
     the song (matching the existing convention already used across all five band folders).
   - `<band>/<slug>.style.txt` — the flat, single-paragraph Suno style prompt. No markdown,
     no headers — just the prompt text itself, exactly as it will be pasted into Suno.
7. Log the new song's notable devices into `.claude/tropes/library.md`: add each one under the
   right category (Constructions / Phrases / Imagery-Motifs) with a one-line description, one
   example, and the source song — following the exact entry format already in the file. This is
   what makes the *next* song's check in step 5 catch a second use.

## Trope library discipline

The library is cumulative and cross-band by design — a device logged from a Purple Dog song
blocks reuse in a Bell Knows My Name song just as much as in another Purple Dog song. Never
skip step 5 or step 7. Never edit or remove an existing library entry to make a draft pass —
if a draft collides, the draft changes, not the library.
```

- [ ] **Step 2: Verify frontmatter and structure**

Run: `head -3 /home/matt/Git/Lyricist/.claude/skills/write-song/SKILL.md`
Expected:
```
---
name: write-song
description: Use when writing a new song lyric for any of the five bands (Guessed, Laundry, Lucy Might, Purple Dog, The Bell Knows My Name). Triggered by requests like "song for Guessed", "another laundry track", "make new song for purple-dog", "another gypsy-emo song", "write me a lucy-might song", or a bare theme with no style named (in which case ask which band). This is the only entry point for song requests — the five style specs are reference files it reads, not separate skills.
```

Run: `grep -c '^| \`' /home/matt/Git/Lyricist/.claude/skills/write-song/SKILL.md`
Expected: `5` (one row per band in the lookup table)

- [ ] **Step 3: Commit**

```bash
cd /home/matt/Git/Lyricist
git add .claude/skills/write-song/SKILL.md
git commit -m "Add write-song skill as the sole entry point for song requests"
```

---

### Task 8: Final verification

**Files:** none created or modified — read-only check across the whole restructure.

- [ ] **Step 1: Confirm .claude/skills/ contains only write-song**

Run: `ls /home/matt/Git/Lyricist/.claude/skills/`
Expected: `write-song`

- [ ] **Step 2: Confirm every band folder has both reference files alongside its songs**

Run:
```bash
for b in guessed laundry lucy-might purple-dog the-bell-knows-my-name; do
  test -f "/home/matt/Git/Lyricist/$b/template.md" && test -f "/home/matt/Git/Lyricist/$b/styles.md" && echo "$b: OK"
done
```
Expected: all five bands print `OK`

- [ ] **Step 3: Confirm the 73 pre-existing songs are unmodified**

Run: `cd /home/matt/Git/Lyricist && git log --diff-filter=M --name-only main -- '*.txt' | grep -v '\.style\.txt\|\.stand\.txt\|template\.md\|styles\.md'`
Expected: empty output (no `.txt` lyric file other than the newly created template/styles ones
has ever been modified)

- [ ] **Step 4: Confirm working tree is clean**

Run: `git status --short`
Expected: empty output — everything from Tasks 1-7 has already been committed

No commit needed for this task — it's verification only.
