# Coase Guard Band Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a sixth band, Coase Guard (industrial hip-hop), to the catalog in the existing `<band>/template.md` + `<band>/styles.md` format, and wire it into `write-song`'s band lookup table.

**Architecture:** This is a content-authoring project, not software — there is no code or test suite. "Verification" for each task means reading the file back and checking it against the design spec and the shared trope library (`.claude/tropes/library.md`), the same discipline `write-song` itself uses. Each task produces one complete file (or one table edit), committed on its own.

**Tech Stack:** Markdown files only. No build step, no dependencies.

## Global Constraints

- Enemy figures in lyrics/devices are always institutional/abstract (inspectors, licensors, the algorithm, absentee owners, the committee) — never an ethnic, religious, or national group, and no real-world hate-group iconography. (Design spec, Architecture > Recurring devices.)
- Any violence or conflict imagery stays stylized/legendary (a strike, a refusal, a standoff) — never a literal instruction toward real-world violence. (Design spec, same section.)
- No overtly partisan/programmatic content — no slogans, policy claims, or real-world political figures/parties. (Design spec, Non-goals.)
- Every new notable device/phrase/construction/motif must be checked against `.claude/tropes/library.md` before being finalized in `template.md`, per the same discipline `write-song` uses for real catalog songs. (Design spec + existing `write-song` workflow.)
- Folder name: `coase-guard`. Band display name: "Coase Guard". Personas: "The Foreman", "The Quartermaster". (Design spec, Architecture.)

---

### Task 1: Write `coase-guard/template.md`

**Files:**
- Create: `coase-guard/template.md`

**Interfaces:**
- Consumes: `.claude/tropes/library.md` (existing entries, read in Step 1 below, to confirm the reference song doesn't collide).
- Produces: `coase-guard/template.md` — read by `write-song` (Task 3 wires the lookup table to it) exactly the way it reads the other five bands' `template.md` files (persona, structure, devices checklist, reference example).

- [ ] **Step 1: Confirm the planned reference song doesn't collide with the trope library**

  Read `.claude/tropes/library.md`. Confirm none of the following (used in the reference song
  below) appear in it: the phrase "no blueprint", the construction "who's steady on the beam,
  who's slow, who never shows", the phrase "nobody built it", the "Foreman doesn't ask" line, or
  any close variant of the "X where Y should be" construction (already retired — the reference
  song must not use it). As of this plan's writing the library contains only: the "X where Y
  should be" construction, "drums/churn fold/buckle in", "you trust X, not Y", "closer than
  that", "and the fiddle starts confessing", the grandmother's-grandmother motif, the folder-as-
  proof motif, and the video-call-waiting-room motif — none of which appear in the content
  below, so this step is a confirmation read, not an editing step.

- [ ] **Step 2: Write the file**

  Create `coase-guard/template.md` with this exact content:

  ```markdown
  # Coase Guard — Song Style Spec

  A reusable brief for writing songs in the "Coase Guard" style — industrial hip-hop built
  around two personas who share one world: a self-organizing crew and the household that
  runs alongside it. Hand this to Claude with an instruction like *"another song in the style
  of this document"* and it should produce a new, standalone lyric set that shares the voice,
  structure, and signature moves below — not a rewrite of the reference example.

  ---

  ## The core idea

  This style translates four ideas into songwriting engines, not into an argument:

  - **Spontaneous order** (Hayek) — things run because the people doing them know their jobs,
    not because anyone planned it from above. The pride in these songs is pride in *unplanned*
    competence.
  - **The firm as a self-organizing unit** (Coase) — the crew and the household are both
    treated as informal enterprises with their own internal accounting, boundaries, and rules
    about who's in.
  - **Friend/enemy clarity** (Schmitt) — every song draws one unhedged line between "us" and
    whoever's trying to inspect, license, plan, or absorb "us." No hedging, no both-sides.
  - **Myth as a tool, used knowingly** (Sorel) — the Foreman is consciously telling a story that
    holds the crew together, and periodically admits it, then keeps telling it anyway.

  **Guardrail (load-bearing, not optional):** the "enemy" in every song stays institutional and
  abstract — an inspector, a licensor, an absentee owner, the algorithm, the committee. Never
  an ethnic, religious, or national group, and no real-world hate-group iconography. Any
  violence or conflict stays stylized and legendary — a strike, a refusal, a standoff — never a
  literal instruction toward real-world violence. This is art about the ideas, the way
  Purple Dog is art about institutional dread — not a policy tract and not an endorsement of
  harming anyone.

  ---

  ## The two personas

  Songs are always sung/rapped by one persona, never both at once — same shared world and
  devices, never a duet in the same song.

  ### The Foreman

  Runs a small, unlicensed, self-organizing crew. Keep the trade itself unspecific (it can read
  as a work crew, a family outfit, a corner operation) — the song is about the *shape* of
  competence without a manual, not about a specific industry. Delivery: rapid, technical,
  cold-controlled flow — precise multisyllabic rhyme, not chaotic, not comedic.

  Two modes:

  - **What We Have** — present-tense pride in the crew's spontaneous order: a rattled-off
    inventory of things that work because nobody designed them, contempt for whoever shows up
    to inspect/license/plan it.
  - **Where We Came From** — origin myth. The founding struggle retold as legend, in a voice
    that's already hardened the story into something closer to scripture than memory. Decisive
    or violent moments are treated as sacred, not examined — but stay stylized/symbolic (a
    strike, a refusal, a standoff), never a literal instruction. The wink (below) tends to land
    right before the final hook, admitting the retelling has been sanded smooth by however many
    times it's been told.

  ### The Quartermaster

  Runs the household/family end of the same world. Trad-wife surface imagery — hearth, table,
  garden, kids — immediately undercut by blunt logistics. She is the reality-check on the
  Foreman's myth-making, not a second mythmaker: no sentimentality, no legend-building, just the
  actual numbers.

  One mode:

  - **Who Eats** — present-tense domestic reckoning: who's fed, who's let in, what's actually
    owed. Every warm image gets cut down by a cold fact inside the same verse.

  ---

  ## Song structure (the template)

  1. **Intro** — cold industrial texture, mechanized loop under a low, half-spoken line
     establishing the scene.
  2. **Verse 1** — rapped, technical, controlled. Establishes the scene: the crew's present
     state (What We Have), the household's present state (Who Eats), or the opening beat of the
     origin story (Where We Came From).
  3. **Hook** — chanted, stacked or call-and-response. The shared claim, present from the start
     of the song (unlike Purple Dog's earned shout-back — here the crew/household is already
     unified going in).
  4. **Verse 2** — rapped, escalation. A concrete, specific detail: the inspector who showed up,
     the exact math of who eats, the specific moment the origin story turns.
  5. **The wink / the tally** — spoken or half-spoken, flat, cold, deliberately at odds with the
     energy around it. For the Foreman, this is **the wink**: he half-admits the story he's
     telling is more legend than fact, then keeps telling it anyway because it's what holds the
     crew together. For the Quartermaster, this is **the tally**: not a myth-check but a
     resource-check — one concrete number or fact that cuts through whatever warmth the verse
     just built.
  6. **Final hook** — chanted, now carrying the weight of what the wink/tally just admitted.

  ---

  ## The recurring devices (checklist)

  A new song should hit most of these:

  - **Competent inventory** — a rattled-off list of things that run without a manual, permit, or
    committee. Concrete and blue-collar-textured, never abstract ("nobody taught us how to read
    a spreadsheet" is weak; "nobody taught us who's steady on the beam" is the right register).
  - **The friend/enemy line** — one unhedged "us and them" moment per song. The enemy is always
    institutional/abstract per the guardrail above.
  - **The founding flash** (Where We Came From songs) — a compressed, already-legendary
    retelling of a decisive past moment. Stylized, never a literal instruction.
  - **The chant hook** — repeated, stacked, or call-and-response, the crew/household's shared
    claim, present from the start rather than earned through the song's arc.
  - **The wink** (Foreman) / **the tally** (Quartermaster) — see Song structure, step 5. Exactly
    one per song, and it must land as a genuine tonal break from the verse around it — flat and
    cold where the rest of the song is propulsive.
  - Delivery stays **rapid and technical**, never sloppy or comedic — the "white guy rap"
    register here is precision, not novelty.

  ---

  ## Reference example (a finished song in this style)

  **"No Blueprint"** — The Foreman, *What We Have* mode.

  ```
  [Intro — cold industrial, mechanized loop, spoken low]
  Nobody drew this. Nobody signed off on this. It just works.

  [Verse 1 — rapped, controlled, technical]
  Six men, no manual, we open before the sun,
  nobody's clocking hours, nobody's counting who's the one
  who taught the kid to weld, who taught the kid to drive —
  it just moves down the line, it just stays alive.
  No org chart on the wall, no consultant with a plan,
  just a nod at 5 a.m. and everybody understands.
  You send a man with a clipboard, try to tell us how it's done —
  we built this out of nothing, and it ran before he come.

  [Hook — chanted, stacked, full crew]
  Nobody built it — it just runs
  Nobody taught us — we're the sons
  No blueprint, no permit, no plan up above
  Just the line and the load and the ones that we love

  [Verse 2 — rapped, escalation]
  The Foreman doesn't ask, the Foreman already knows
  who's steady on the beam, who's slow, who never shows.
  No handbook for that. No test you can take.
  It's in the hands, it's in the years, it's in the choices that we make.
  Inspector came in March, said we're unlicensed and untrained —
  funny how the roof he stood under never leaked once in the rain.
  He wrote us up for paperwork. We wrote him off for good.
  Two different kinds of order — only one of us understood.

  [The wink — spoken, flat, cold]
  ...and yeah — maybe it wasn't always this clean.
  Maybe the story's better than the mornings ever were.
  Maybe I tell it smooth because a crew needs a reason to show up before the sun does.
  Doesn't make it less true. Just makes it mine to tell.

  [Final hook — chanted, weightier, full crew]
  Nobody built it — it just runs
  WE didn't ask — we ARE the ones
  No blueprint, no permit, no plan up above
  Just the line and the load and the ones that we love
  NOBODY TAUGHT US — WE'RE THE SONS
  ```

  Illustrative fragment in the Quartermaster's voice (*Who Eats* mode) — not a full song, shown
  here to establish her distinct register:

  ```
  [Verse — Quartermaster, cold-warm, sparse, more space between hits]
  Table's set for eight, I counted six that earned it.
  Two more show up hungry — fine, there's always a way,
  but don't mistake the seat at my table for a right,
  mistake it for a debt, 'cause that's what it is by Tuesday.
  Ask me if I love them — I'll set another plate.
  Ask me if I'll starve for it — get out of my way.

  [Hook — chanted, sparser, colder]
  Who eats first, who eats last, who doesn't eat at all —
  I decide it, not the calendar, not the county, not the hall.
  Warm hands, hard math, that's the only creed I keep —
  love is the kitchen. The ledger's what we eat.

  [The tally — spoken, flat]
  Six mouths, four hands, one bag of flour left — that's not a feeling, that's Thursday.
  ```

  ---

  ## When writing a new one

  Pick the persona and mode first (Foreman/What We Have, Foreman/Where We Came From, or
  Quartermaster/Who Eats). Pick a fresh **competent inventory** and a fresh institutional
  **enemy** — never reuse the clipboard inspector or the six-mouths-four-hands tally verbatim.
  Keep the wink/tally to exactly one per song, and make sure it actually lands as a tonal break,
  not just a quieter verse. Keep the enemy institutional and the violence stylized, per the
  guardrail at the top of this document — that constraint doesn't loosen as the catalog grows.
  ```

- [ ] **Step 3: Verify the file reads back correctly**

  Read `coase-guard/template.md` back in full. Confirm: the guardrail paragraph is present near
  the top, both personas and all three modes are documented, the structure section lists all
  six steps (intro/verse/hook/verse/wink-tally/final hook), the devices checklist is present,
  and both the full reference song and the Quartermaster fragment are present with their
  bracketed section tags intact.

- [ ] **Step 4: Commit**

```bash
git add coase-guard/template.md
git commit -m "Add Coase Guard template (Foreman + Quartermaster personas)"
```

---

### Task 2: Write `coase-guard/styles.md`

**Files:**
- Create: `coase-guard/styles.md`

**Interfaces:**
- Consumes: nothing (standalone Suno prompt reference).
- Produces: `coase-guard/styles.md` — read by `write-song` alongside `template.md` (Task 3 wires
  the lookup table).

- [ ] **Step 1: Write the file**

  Create `coase-guard/styles.md` with this exact content:

  ```markdown
  # Coase Guard — Suno Style Prompts

  ## Suno prompt notes

  - Paste the **bracketed section tags** (`[Verse 1 — rapped, controlled, technical]`,
    `[Hook — chanted, stacked, full crew]`, `[The wink — spoken, flat, cold]`, etc.) into Suno —
    the contrast between rapped verse and chanted hook is the whole engine, and the tags are how
    Suno knows to switch delivery mid-song.
  - The **wink/tally section is the least predictable part** — regenerate several times to find
    a take where the delivery actually goes flat and cold against the rest of the track. A take
    that keeps the same energy through the wink kills the effect; the whole device depends on
    the audible drop in temperature.
  - The Foreman and Quartermaster need **different core prompts**, not just different lyrics —
    same instrumentation family, different density and space.
  - Style prompt for **the Foreman, "What We Have" / "Where We Came From"** (recommended
    default):
    ```
    industrial hip-hop, distorted 808s, metallic factory-floor percussion, rapid technical
    rapped verses, cold aggressive delivery, chanted gang-vocal hooks, mechanized loops, minor
    key, tight compressed production
    ```
  - **Heavier variant** for Where We Came From (origin-myth songs, tribal layer under the
    machine):
    ```
    industrial hip-hop, tribal war-drum layer under mechanized percussion, distorted bass,
    rapid rapped verses building to a shouted chanted hook, minor key, heavier low-end,
    cavernous reverberant production
    ```
  - Style prompt for **the Quartermaster, "Who Eats"**:
    ```
    industrial hip-hop, sparse skeletal beat, wide space between hits, cold controlled rapped
    verses, low warm-toned female vocal turning clinical and flat, chanted hook with cold
    echo, minor key, stripped-back production
    ```
  Core instrument/texture palette to draw from: distorted 808s and sub-bass, metallic/factory
  percussion samples, mechanized loop textures, minimal melodic material — the chant *is* the
  hook, there's no sung melody to fall back on. No ad-libs or hype-man chatter — the cold
  control is the point.

  ---
  ```

- [ ] **Step 2: Verify the file reads back correctly**

  Read `coase-guard/styles.md` back in full. Confirm all three named style-prompt blocks
  (Foreman default, Foreman heavier/origin-myth variant, Quartermaster) are present and
  distinct from each other, and that the file matches the structure of the other five bands'
  `styles.md` files (prompt notes, then named blocks, then a shared instrument-palette
  paragraph).

- [ ] **Step 3: Commit**

```bash
git add coase-guard/styles.md
git commit -m "Add Coase Guard Suno style prompts"
```

---

### Task 3: Wire Coase Guard into `write-song`'s band lookup table

**Files:**
- Modify: `.claude/skills/write-song/SKILL.md` (the "Band lookup" table)

**Interfaces:**
- Consumes: `coase-guard/template.md` and `coase-guard/styles.md` from Tasks 1–2 (referenced by
  folder name only — this task doesn't read their contents).
- Produces: an updated band lookup table that `write-song` uses to resolve requests naming
  "Coase Guard", "industrial hip-hop", "the Foreman", or "the Quartermaster" to the
  `coase-guard` folder.

- [ ] **Step 1: Read the current table**

  Read `.claude/skills/write-song/SKILL.md`. Confirm the "Band lookup" table currently lists
  exactly five rows (`guessed`, `laundry`, `lucy-might`, `purple-dog`,
  `the-bell-knows-my-name`).

- [ ] **Step 2: Add the new row**

  In `.claude/skills/write-song/SKILL.md`, change:

  ```markdown
  | Band folder               | Persona / genre aliases                                  |
  |----------------------------|------------------------------------------------------------|
  | `guessed`                  | Guessed, lurker, lurker trip-hop                            |
  | `laundry`                  | Laundry, dissociative-hardcore, dissociative hardcore        |
  | `lucy-might`               | Lucy Might                                                   |
  | `purple-dog`                | Purple Dog, institutional-hardcore, institutional hardcore    |
  | `the-bell-knows-my-name`   | The Bell Knows My Name, gypsy-emo, gypsy emo                 |
  ```

  to:

  ```markdown
  | Band folder               | Persona / genre aliases                                  |
  |----------------------------|------------------------------------------------------------|
  | `guessed`                  | Guessed, lurker, lurker trip-hop                            |
  | `laundry`                  | Laundry, dissociative-hardcore, dissociative hardcore        |
  | `lucy-might`               | Lucy Might                                                   |
  | `purple-dog`                | Purple Dog, institutional-hardcore, institutional hardcore    |
  | `the-bell-knows-my-name`   | The Bell Knows My Name, gypsy-emo, gypsy emo                 |
  | `coase-guard`               | Coase Guard, industrial hip-hop, the Foreman, the Quartermaster |
  ```

  Also update the skill's frontmatter `description` field (currently reads "...for any of the
  five bands (Guessed, Laundry, Lucy Might, Purple Dog, The Bell Knows My Name)...") to say "six
  bands" and list Coase Guard, so the trigger description stays accurate:

  Change:
  ```
  description: Use when writing a new song lyric for any of the five bands (Guessed, Laundry, Lucy Might, Purple Dog, The Bell Knows My Name). Triggered by requests like "song for Guessed", "another laundry track", "make new song for purple-dog", "another gypsy-emo song", "write me a lucy-might song", or a bare theme with no style named (in which case ask which band). This is the only entry point for song requests — the five style specs are reference files it reads, not separate skills.
  ```

  to:
  ```
  description: Use when writing a new song lyric for any of the six bands (Guessed, Laundry, Lucy Might, Purple Dog, The Bell Knows My Name, Coase Guard). Triggered by requests like "song for Guessed", "another laundry track", "make new song for purple-dog", "another gypsy-emo song", "write me a lucy-might song", "a Coase Guard track", or a bare theme with no style named (in which case ask which band). This is the only entry point for song requests — the six style specs are reference files it reads, not separate skills.
  ```

- [ ] **Step 3: Verify**

  Read `.claude/skills/write-song/SKILL.md` back in full. Confirm the table has six rows, the
  new row's folder name matches `coase-guard` exactly (matching Tasks 1–2's folder), and the
  frontmatter `description` says "six bands" and lists Coase Guard.

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/write-song/SKILL.md
git commit -m "Wire Coase Guard into write-song band lookup"
```

---

### Task 4: Log the reference song's new devices into the trope library

**Files:**
- Modify: `.claude/tropes/library.md`

**Interfaces:**
- Consumes: the reference song "No Blueprint" and the Quartermaster fragment from Task 1.
- Produces: updated `.claude/tropes/library.md` with new entries, so a future song (in any
  band) that reuses "no blueprint," the clipboard-inspector beat, or the six-mouths-four-hands
  tally gets caught, matching the library's own "logged on first use" discipline.

**Rationale:** the design spec's reference example isn't a "real" catalog song (it has no
`.txt`/`.style.txt` files — same convention as Purple Dog's "I'm Fine" example, which also
isn't a saved file and also isn't in the library). But its devices are novel enough, and
visible enough (embedded in a spec other future songs will be written against), that logging
them now avoids the *template's own example* being copied verbatim in a future Coase Guard
song. This is a small deliberate deviation from the "I'm Fine" precedent, done because "I'm
Fine" predates the trope library's existence — nothing was being caught either way at the time
it was written.

- [ ] **Step 1: Add three new entries**

  In `.claude/tropes/library.md`, add to the **Constructions** section (after the existing
  "you trust [the record], not [the reality]" entry):

  ```markdown
  ### "Nobody [verb]ed it — it just [verb]s" — spontaneous-order chant hook
  - A chanted claim that a system runs without anyone having designed or authorized it.
  - Example: "Nobody built it — it just runs" — coase-guard/no-blueprint (template.md reference example)
  ```

  Add to the **Imagery / Motifs** section (after the existing video-call-waiting-room entry):

  ```markdown
  ### The clipboard inspector vs. the untested competence he's citing
  - An outside official (inspector/licensor/planner) criticizes the crew on paperwork/procedure
    grounds while standing on/using/benefiting from the exact competence he's dismissing (e.g.
    the roof that never leaked, under a citation for being "unlicensed").
  - Example: "Inspector came in March, said we're unlicensed and untrained — funny how the roof
    he stood under never leaked once in the rain." — coase-guard/no-blueprint (template.md
    reference example)

  ### The exact-headcount food tally as a stand-in for love
  - A domestic-scene song states a specific, small count (mouths/hands/portions) as the real
    measure of care, immediately after or instead of a sentimental declaration.
  - Example: "Six mouths, four hands, one bag of flour left — that's not a feeling, that's
    Thursday." — coase-guard/who-eats-fragment (template.md illustrative fragment)
  ```

- [ ] **Step 2: Verify**

  Read `.claude/tropes/library.md` back in full. Confirm it now has 3 new entries (one
  Construction, two Imagery/Motifs), each with the exact wording used in Task 1's file, and that
  no existing entry was edited or removed.

- [ ] **Step 3: Commit**

```bash
git add .claude/tropes/library.md
git commit -m "Log Coase Guard reference-example devices in trope library"
```
