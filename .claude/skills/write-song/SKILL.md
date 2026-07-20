---
name: write-song
description: Use when writing a new song lyric for any of the six bands (Guessed, Laundry, Lucy Might, Purple Dog, The Bell Knows My Name, Coase Guard). Triggered by requests like "song for Guessed", "another laundry track", "make new song for purple-dog", "another gypsy-emo song", "write me a lucy-might song", "a Coase Guard track", or a bare theme with no style named (in which case ask which band). This is the only entry point for song requests — the six style specs are reference files it reads, not separate skills.
---

# write-song

Writes a new song for one of the six bands, checks it against the shared trope library so
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
   right category (Constructions / Phrases / Imagery / Motifs) with a one-line description, one
   example, and the source song — following the exact entry format already in the file. This is
   what makes the *next* song's check in step 5 catch a second use.

## Trope library discipline

The library is cumulative and cross-band by design — a device logged from a Purple Dog song
blocks reuse in a Bell Knows My Name song just as much as in another Purple Dog song. Never
skip step 5 or step 7. Never edit or remove an existing library entry to make a draft pass —
if a draft collides, the draft changes, not the library.
