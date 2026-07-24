# Lyricist — Intention: refactoring the trope system

**Status:** intention document. Describes *what* and *why*, not *how*. Design latitude on
implementation is deliberate; the invariants below are not.

**Repo:** `lawless-m/Lyricist` — 7 bands, 112 songs, `.claude/skills/write-song/SKILL.md` as
sole entry point, `.claude/tropes/library.md` at 163 entries.

---

## Context

The system grew additively rather than combinatorially. Each band was specced when it was
written, against whatever existed at the time. The trope library was bolted on later
(seeded 2026-07-19 from a scan of the then-73 songs) to stop devices calcifying across the
catalogue.

The library works, and the core instinct behind it is right. But it was designed against a
smaller catalogue and it has begun to strain in ways that are now visible in the artefacts.

**The audience constraint that governs everything here:** the author is the primary
listener. The seven bands are a fiction; the ear is not. This is why the library bans
globally across bands, and that decision is correct and stays. Repetition is tiring
regardless of which band it arrives under.

---

## The core problem

**The library cannot distinguish deliberate repetition from drift.**

A band-signature device and an accidental cross-band leak are indistinguishable to it: one
use, logged, retired. But intentional recurrence is what makes a band a band, and
unintentional recurrence is what tires the listener out. Collapsing them into one rule
means the ratchet eats the signatures along with the leaks.

This is not hypothetical. It has already happened, and it is the root cause of every
finding below.

---

## Findings (evidence — do not re-derive)

1. **`the-bell-knows-my-name/template.md` mandates a device the library retires.**
   The spec lists `"I've got ___ where ___ should ___"` as a required recurring device and
   calls it "the emotional thesis." Library entry #1 retires exactly that construction and
   lists eight Bell songs as offenders. The reference example embedded in the same
   `template.md` uses it twice in its chorus. So a Bell draft is instructed to produce the
   device, shown a canonical example of it, then required to strip it — every time.

2. **`ultracoase/template.md` breaks its own central rule in its own reference example.**
   The spec is emphatic that the wink is *evidence, not analysis* — state the fact, never
   narrate the feeling underneath. The reference wink in
   `the-forge-doesnt-wait-for-me.txt` reads *"Truth is I left because staying meant
   becoming him. Doesn't make the leaving right. Just makes it mine to carry."* That is the
   feeling underneath, narrated, with the moral accounting supplied. By the spec's own
   definition it is a Coase Guard move.

3. **There is a live, unlogged cross-band leak, and it lives in the templates.**
   - `the-bell-knows-my-name/wheels-where-i-should-kneel.txt:30` —
     *"and the wandering didn't fix me, but the wandering feels real"*
   - `ultracoase/the-forge-doesnt-wait-for-me.txt:31` —
     *"and the leaving didn't save me, but the leaving wears my name."*

   Same formula, two bands, nothing in the library. Both songs are the reference examples
   embedded in their respective `template.md` files.

4. **The templates were never scanned.** The library was seeded from a scan of songs. The
   seven `template.md` files — the highest-propagation surface in the system, since a
   device there is imitated deliberately in every future song of that band — have never
   been checked against it. Findings 1–3 are all instances of this single gap.

5. **Style-prompt adaptation is being skipped.** 13 `*.style.txt` files are byte-identical
   to each other; another 11 likewise; another 9. `the-birds-have-stopped-singing.style.txt`
   is a verbatim copy of the cinematic default in `styles.md`. SKILL.md step 6 says to adapt
   the variant to the song's dial position. It is being selected wholesale instead. *(This
   may be intended — see open decisions.)*

6. **`guessed/best_lines.md` is the only positive signal in the repo.** Four lines, one
   band, stale. The negative record is automated, cumulative and enforced; the positive
   record is manual, partial and abandoned.

---

## Design principles

**Over-banning is silent; under-banning is audible.** A repeat gets heard and noted. A good
line revised away to satisfy the library is never heard and leaves no trace. The feedback
loop therefore only pushes one direction, and the library will tighten indefinitely with
nothing pulling back. Any change here should be biased toward permissiveness, because the
author cannot perceive the cost of the alternative.

**Fatigue decays; the library does not.** Permanent retirement on first use is the right
model for a published catalogue where any listener might hear any two songs adjacently. It
is the wrong model for one listener with a normal memory. A device that grated in March is
plausibly fresh by the following spring. Some entries genuinely warrant permanence — the
ones that calcified into house style — but those are a minority.

**The unit is the line in its position, not the line.** The library already half-knows this:
its entries are indexed by the job a line does ("band-instruction chorus opener",
"flash-of-legibility line"), not by its words. Preserve that. A saved line lifted out of its
setup loses what made it land — the reversal needs the thing it reverses.

**Specs are creative writing, not configuration.** The prose in the `template.md` files is
doing real work. Do not factor them into parameters or sliders. Anything built here is a
checking and scoping layer *alongside* hand-written specs.

---

## Sequence

Ordered by dependency and by information gained, not by size.

### 1. Scan the seven templates against the library
Cheapest, highest value, and it generates the schema for step 2 rather than requiring one to
be designed up front. Each collision forces a concrete signature-versus-drift call.

Every collision resolves exactly one of two ways, and both ways produce an edit:
- **Drift** → device retired; the spec must be updated to name what replaces it. A spec may
  not be left mandating a retired device.
- **Signature** → device scoped to that band; library entry flagged accordingly.

Expect findings 1–3 to fall out here, plus others.

### 2. Split the library by enforcement kind
The 163 entries are three different things sharing one format: exact phrases, constructions
with slots, and imagery motifs. Only the first is mechanically checkable.

Pull the mechanical subset into a deterministic pre-save check. This is the fix for the
silent-recall problem — 163 fuzzy judgements at write time degrade invisibly as the file
grows, and a miss is indistinguishable from a pass. Shrinking the fuzzy remainder to
something that can actually be held in view is the point.

### 3. Add decay
Entries gain a first-used marker and a class: **permanent** for the calcified, **cooling**
for everything else. No new judgement is required at write time — the existing logging step
records more fields. The cooling threshold is a tunable knob; start generous.

### 4. Positive loop, as a separate trigger
Fires on **listen**, not on write. Records the event *in position*: the line, what it turns
against, and where in the song it lands. It does not feed the ban list — it feeds the specs.
A positive event recurring is a candidate for promotion into a band's mandated devices,
which is the signature flag from step 1 pointing the other way. This is the piece that
closes the one-directional feedback described above.

### 5. Axes — last, and only if still wanted
Narrator scope (one body / crew / institution) and legibility discipline (evidence vs.
analysis) are already latent in the Ultracoase spec, which defines its band almost entirely
by subtraction from two others. Naming them would let bans be scoped more finely than
per-band. Not required by anything above. Scoping and checking layer only.

---

## Non-goals

- **Do not retro-fix the 112 existing songs.** They are the record of how the system got
  here, and the library was seeded from them — rewriting them invalidates its provenance.
- **Do not automate the positional judgement.** Whether a line earns its position needs the
  whole song and a listen. Pretending otherwise produces a positive library as brittle as
  the negative one is rigid.
- **Do not replace the prose specs.** See design principles.
- **Do not remove or weaken library entries to make a draft pass.** Existing SKILL.md
  discipline stands: the draft changes, not the library. Step 1 is the *only* sanctioned
  route by which an entry changes status, and it changes status by explicit decision, not
  by convenience.

---

## Open decisions — RESOLVED 2026-07-24

1. **Is Coase Guard live or frozen?** → **Live**, with an additional directive: decouple
   coase-guard and ultracoase so they are not parent–child. Applied: ultracoase/template.md's
   core-idea section rewritten to define the band in its own terms (four pillars stated
   positively, machinery named as its own, origin kept as a provenance-only footnote);
   Coase Guard treated like any live band (reference material annotated, chant added to the
   never-reuse list).

2. **Cooling threshold.** → **Songs-written-since only** (catalogue-wide count, not elapsed
   time). Exact threshold still tunable at step 3; bias generous.

3. **Is the style-file duplication (finding 5) intended?** → **Adaptation is wanted.** The
   step was being skipped. Applied: SKILL.md step 6 now requires stating the dial position
   and either what changed from the base variant or why the base fits exactly, before saving.

## Step 1 — COMPLETED 2026-07-24

All seven templates scanned against the library. Finding 3's closing-line formula turned out
to be a **three**-band leak (purple-dog's "and the quiet never saved me" makes three), now
logged as a retired construction. Every collision resolved as drift (nothing was scoped as a
band signature — in each case the *slot* was the signature and the *filling* was spent):
bell and purple-dog's mandated where/should construction converted to rotating slots; bell's
fiddle-confessing pre-chorus, so-tell-me scaffold, grandmother's-grandmother example, and
"but God" shout-back pivot (new watch entry) all handled; laundry's "occasional family nod"
contradiction removed; guessed's spent suggested-filling removed and logged; lucy-might's
"closer than that" and "twice" annotated in the reference; all seven reference examples now
carry historical-not-model annotation notes in the house style established by the ultracoase
wink note. Next in sequence: step 2 (split the library by enforcement kind).
