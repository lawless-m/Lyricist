# The Bell Knows My Name — Suno Style Prompts

## Suno prompt notes
 
- Paste the **bracketed section tags** (`[Verse 1 — slow, intimate, solo violin]`, `[Bridge — half-time, sparse, then huge]`, etc.) into Suno — it uses them to shape dynamics, and the slow-verse / fast-or-swelling-chorus contrast is what sells the lurch.
- **State the singer's gender in every prompt, and choose it per song.** Flagged 2026-08-24 by the
  owner: the band had been male for a long stretch, largely by default. The cinematic variant below
  leaves the voice unstated, so Suno picks — and it picks male — while the softer variant said
  *male vocals* outright, which was typed once and never revisited. Neither is a decision.

  **Use both the interface control and the prompt text, and expect neither to be binding.**
  Suno's create page has `Instrumental | Male | Female` buttons; the active one carries
  `variant-standard-legacy` in its class while the others are `variant-tertiary-legacy`, so a
  script can set it and confirm the click registered. Confirming the click is not confirming the
  outcome — the owner's experience is that **it does not always work**, so treat the control as a
  strong hint rather than a switch. Set the button, write *female vocal* in the style prompt too,
  and plan on judging the take by ear and re-rolling when it comes back wrong. This puts vocal
  gender in the same class as the chorus delivery noted below: something you regenerate for, not
  something you specify. One datapoint for keeping the prompt text: `an-hour-on-the-train`
  came back female on both takes from the style prompt alone — it was submitted before the button
  was clicked.
  **Current preference: female**, for a while, to correct the drift. The narrator's gender is free — the songs are aimed at one person
  and almost never depend on who is singing.
- **Name the gang vocal's placement, never its character.** Flagged 2026-08-25: `sanda-came-up`
  came back with crowd chanting all the way through and the owner's verdict was that it spoils it.
  Its prompt asked for *"gang vocals like a schoolyard skipping chant on the final line"* — and a
  chant is a **character**, so Suno applied it to the whole song rather than to the line. Every
  other song in the band says plainly *"gang vocals on the final line"* and renders correctly.
  The spec allows a crowd on the last line and nowhere else, so say that, and say it as a negative
  too: *solo voice throughout, no crowd and no chanting anywhere until the very end, one gang shout
  on the final line only*. Adjectives describing how the crowd should sound are the hazard.
- The vocal delivery on the chorus is the least predictable part — regenerate a few times to find a take where the singer actually cracks on the shout-back line.
- Style prompt for the **darker / cinematic** flavour (recommended default):
  ```
  cinematic gypsy emo ballad, sorrowful solo violin, cimbalom, swelling accordion, harmonic minor, cracked emotional vocals, rubato intro, dramatic crescendo, live room reverb
  ```
- Softer / Midwest-emo-adjacent variant:
  ```
  melancholic gypsy folk emo, twinkly nylon guitar, mournful violin, accordion, minor key, intimate confessional vocals, state female or male explicitly, dynamic build to cathartic chorus, reverb
  ```
- Punkier / Gogol-Bordello-with-feelings variant:
  ```
  gypsy punk emo, driving upright bass, frantic fiddle, accordion, Balkan brass, anthemic gang vocals, aching lead vocal, minor key, tempo shifts from slow to frantic
  ```
Core instrument palette to draw from: lead violin/fiddle, accordion, cimbalom (hammered dulcimer), upright bass, nylon-string guitar, optional Balkan brass.
 
---
 
