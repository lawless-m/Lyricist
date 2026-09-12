# Ultracoase — Suno Style Prompts

## Suno prompt notes

- Paste the **bracketed section tags** (`[Verse 1 — clipped, technical, controlled]`,
  `[Hook — chanted, stacked]`, `[The wink — spoken, flat, cold]`, etc.) into Suno — the contrast
  between the clipped verse, the chanted hook, and the flat spoken wink is the whole engine.
- The **wink is the least predictable part** — regenerate a few times to find a take where the
  delivery actually drops cold instead of just going quiet. Same rule as Coase Guard's
  wink/tally: no audible temperature drop, no effect.
- **Naming real artists in the prompt is off-limits** (inherited from Coase Guard's own rule) —
  this band's sound is 1980s synth-new-wave-adjacent by design, but push the description
  through instrumentation and delivery cues, never a band name.
- Default style prompt:
  ```
  driving synth new wave, pulsing sequenced arpeggiated bassline, punchy Roland drum machine,
  taut urgent clipped baritone vocal verses, stacked gang-chanted hook, one flat cold
  spoken-word breakdown, propulsive motorik rhythm, stabbing analog synth brass hits, sharp
  violin accents cutting through the mix, mid-tempo pep not ballad, tight pacy 1980s new wave
  production
  ```
- If a take drifts too "cinematic ballad" (swelling, lush, widescreen), pull back the crescendo
  language and lean harder on "propulsive," "clipped," "taut," and "pep, not ballad" — that
  correction is what took the first take from a "Vienna"-style swell to the reference example's
  actual sound.
- The reference recording used a custom Suno voice persona (not a generic default AI voice) for
  the vocal — apply the saved **Ultracoase** voice (`tools/suno-voice.py Ultracoase`); a generic
  voice preset alone won't reproduce the "even better, not because it sounds like me" result.
  Clear it again for any other band (`tools/suno-voice.py --off`) — the form keeps the last
  voice across generations, so it will otherwise carry over silently. After generating, the
  clip's `metadata.persona_id` is the only proof it actually applied
  (Ultracoase = `dca2e5ed-5fa5-45fb-8311-e8991c599ae7`).

Core instrument/texture palette to draw from: analog synth pads and arpeggiators, Roland-style
drum machine, synth bass, stabbing synth brass, violin as a sharp accent (not a swelling lead) —
distinct from Coase Guard's distorted-808/industrial palette and from The Bell Knows My Name's
accordion-and-cimbalom palette.

---

## The custom voice wipes out the gang hook (2026-09-12)

**The owner's read, and it resolves a contradiction that has been sitting in these files.** All 19
style prompts ask for a `stacked gang-chanted hook`, `template.md` lists escalating to *"full
gang-vocal weight in the final hook"* as a device, and **the records do not have gang chants.**

The cause is the custom Voice. A persona is a single voice, so it cannot stack into a crowd, and
applying one appears to suppress the request entirely rather than blend with it. The clause has
therefore never fired on any Ultracoase track.

Two consequences:

- **The clause is inert in normal use** and the prompts can keep it or lose it without changing the
  sound. Worth leaving until someone tests removing it, since it has never been the active
  ingredient either way.
- **It is not inert without the persona.** Anything rendered in this style with the Voice off — a
  cross-style experiment, say — will get the gang hook for the first time and will not sound like
  Ultracoase. Drop the clause in that case. Found while rendering Guessed lyrics in this style with
  the persona deliberately off.

