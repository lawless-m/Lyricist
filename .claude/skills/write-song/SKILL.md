---
name: write-song
description: Use when writing a new song lyric for any of the seven bands (Guessed, Laundry, Lucy Might, Purple Dog, The Bell Knows My Name, Coase Guard, Ultracoase). Triggered by requests like "song for Guessed", "another laundry track", "make new song for purple-dog", "another gypsy-emo song", "write me a lucy-might song", "a Coase Guard track", "an Ultracoase song", or a bare theme with no style named (in which case ask which band). This is the only entry point for song requests — the seven style specs are reference files it reads, not separate skills.
---

# write-song

Writes a new song for one of the seven bands, checks it against the shared trope library so
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
| `coase-guard`               | Coase Guard, industrial hip-hop, the Foreman, the Quartermaster |
| `ultracoase`                | Ultracoase, synth new wave, Ultravox-adjacent                |

If the request names a theme but no band and it isn't clear from context, ask which band before
doing anything else.

## Workflow

1. Resolve the band (see table above).
2. Read `<band>/template.md` (persona, structure, devices, band-local rotation rules) and
   `<band>/styles.md` (Suno style-prompt variants for this band).
3. Read `.claude/tropes/library.md`.
4. Draft the song per `template.md`, picking a fresh theme/dial/arrangement per its own
   "don't let it calcify" guidance.
5. Two-layer trope check, both mandatory:
   - **Mechanical (deterministic):** run `.claude/tropes/check.sh <draft-file>` on the draft.
     A **BAN** hit means the draft changes — revise and re-run until it exits clean. A
     **WATCH** hit (stock words like frost/Tuesday/forty-one) is allowed only with a stated,
     song-specific justification in the conversation — never as an unexamined reflex.
   - **Fuzzy (judgement):** check the draft's constructions-with-slots and imagery motifs
     against the **Constructions** and **Imagery / Motifs** sections of
     `.claude/tropes/library.md`. The mechanical pass only covers exact anchors — a fresh
     sentence in a retired grammatical shape or a re-instantiated motif will pass the script
     and still must be caught here. **Any match, in any category, means revise the draft to
     avoid it, then re-check.** A device only needs to appear once in the library to be
     off-limits; there is no "safe to use twice" tier.
6. Build the style prompt from `styles.md` and the song's dial position, and **state the
   adaptation decision out loud before saving**: name the dial position, then either (a) what
   you changed from the base variant and why, or (b) why the base variant already fits this
   specific song exactly. The `.style.txt` is always saved per song — it's the paste-target
   Suno actually uses, so an unchanged default still gets its own copy, and identical files
   across songs are fine *when considered*. What's not fine is skipping the consideration:
   a variant pasted wholesale with no stated justification is a skipped step, not a default.

   Adaptation is graduated — reach for the lightest rung that fits:
   - **Reorder** (the usual move): Suno appears to weight terms by position — front-loaded
     terms dominate, and very long prompts risk losing the tail — so moving this song's lead
     texture to the front of the *same* term list changes the emphasis without changing the
     band's vocabulary. A wink-heavy song leads with the spoken-breakdown term; a
     chant-forward song leads with the gang-hook term; the default order is itself a
     statement that the song sits dead-centre.
   - **Swap or add a term** when the dial position needs a texture the base list lacks (or
     needs one removed) — per that band's own styles.md rotation guidance.
   - **Rewrite** only when a song genuinely departs from the band's core sound.

   Then save both output files:
   - `<band>/<slug>.txt` — the lyric, where `<slug>` is a short kebab-case phrase drawn from
     the song (matching the existing convention already used across all other band folders).
   - `<band>/<slug>.style.txt` — the flat, single-paragraph Suno style prompt. No markdown,
     no headers — just the prompt text itself, exactly as it will be pasted into Suno.
7. Log the new song's notable devices into `.claude/tropes/library.md`: add each one under the
   right category (Constructions / Phrases / Imagery / Motifs) with a one-line description, one
   example, and the source song — following the exact entry format already in the file. **Then
   mirror every entry that has a greppable anchor into `.claude/tropes/banned-patterns.tsv`**
   (severity `BAN`, or `WATCH` only for stock-word-style flags): a distinctive substring for
   exact phrases, a regex skeleton for mechanically-expressible constructions. An entry logged
   in the library but not mirrored into the TSV is invisible to the next song's deterministic
   check — the two files update together, in the same commit. This is what makes the *next*
   song's check in step 5 catch a second use.

## Trope library discipline

The library is cumulative and cross-band by design — a device logged from a Purple Dog song
blocks reuse in a Bell Knows My Name song just as much as in another Purple Dog song. Never
skip step 5 or step 7. Never edit or remove an existing library entry to make a draft pass —
if a draft collides, the draft changes, not the library.
