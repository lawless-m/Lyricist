# Guessed — Suno Style Prompts

## Suno prompt notes
 
**Notation rules — these are hard, and getting them wrong audibly wrecks the take.**
 
Suno treats the two bracket types completely differently, and the difference is whether the words come out of the speakers:
 
- **`[Square brackets], on their own line` = direction.** Not sung. This is where *every* performance instruction goes — dynamics, arrangement, who's singing, what the production does, how a section ends. Be as verbose as you like in here; it costs nothing.
- **`(Parentheses)` = backing vocal. The contents get SUNG.** So parentheses may contain **only words you actually want to hear**. Never a description, never a stage direction, never a label.
Which means:
 
- **Never prefix a lyric with an inline direction.** `(doubled, half a beat behind) I answer to it` sings the phrase "doubled, half a beat behind" in a backing voice. Put "second voice half a beat behind" in the section tag, and leave the parentheses holding `(I answer to it)` and nothing else.
- **Never label the voice inside the parens.** `(gang: HE'S NOT FINE)` sings the word "gang". `(doubled, smeared) part it out` sings "doubled, smeared". The *who* belongs in the tag; the parens get the words alone.
- **Never use em-dash-wrapped prose as a direction.** `— (the loop returns, unchanged, indifferent) —` is not a tag and is not reliably skipped — it can be read aloud. Convert every one of these into a bracketed tag on its own line: `[The loop returns unchanged, indifferent]`.
- **Nothing between the brackets and the lyrics.** Every line in the body is either a `[tag]` on its own line or words to be sung. There is no third category.
Test before you paste: **read only the un-bracketed text and ask whether you'd be happy hearing all of it.** If any of it is you talking to the producer, it's in the wrong bracket.
 
- Paste the **bracketed section tags** (`[Verse 1 — dry slowed breakbeat, Rhodes, vinyl crackle, voice close and thin]`, `[The drop-out — everything cuts, voice alone, one line]`, etc.). The whole style depends on the loop staying indifferent and the drop-out actually dropping out, and the tags are the only way to get that.
- **State "no backing vocals, no gang vocals, solo female voice" explicitly in the style prompt**, and again in the final tags. Suno's instinct on anything with a repeated hook is to stack a crowd behind it, which destroys this style specifically.
- The **drop-out is the least predictable part** — regenerate several times to find a take where the production genuinely strips to nothing and the voice is dry and unaccompanied. A take that keeps the pad running underneath kills it. (Same job as chasing the crack in gypsy-emo's shout-back, the *turn* in hardcore's monologue, the swallow in dissoc's dissolve.)
- Ask for the vocal **close, thin, dry and forward** while everything else is drenched. That mismatch is the Portishead signature — she's in your ear, the band is down a corridor.
- **Theremin was getting overused** — it was sitting in the default block below, so it got
  copy-pasted into most songs' prompts regardless of fit. It's one texture in the palette, not
  a fixed ingredient: use it when a song specifically wants that wavering, spectral edge, and
  reach for tremolo guitar, spy-film strings, Rhodes, synth drone, or **Trautonium** (confirmed
  working in Suno — same eerie spectral-glide territory as theremin, e.g. the *The Birds*
  sound, and a good alternate pick when a song wants that texture without reaching for theremin
  again) the rest of the time so the catalogue's texture actually varies.
- Style prompt for the **dusty Dummy-era core** (recommended default):
  ```
  trip hop, slow dusty breakbeat behind the beat, vinyl crackle, Rhodes piano, tremolo guitar, spy-film strings, melancholic minor key, thin close-miked fragile female vocal, dry vocal against heavy reverb, sparse, unresolved, no backing vocals, no gang vocals
  ```
- **Frozen Third-era variant** (colder, crueller, no comfort — use for humiliation and for anything she's angry about but won't say):
  ```
  cold mechanical trip hop, krautrock motorik pulse, analogue synth drone, no reverb, brittle drum machine, dissonant strings, unsettling, relentless loop, flat detached solo female vocal, claustrophobic, no release, no backing vocals
  ```
- **Sparse acoustic variant** (Beth Gibbons solo / *Out of Season* — for regret, the childlessness material, the warmest and most exposed):
  ```
  sparse acoustic melancholy, nylon guitar, upright bass, brushed drums, distant strings, folk-jazz, intimate cracked female voice recorded close, room tone, no percussion in places, minor key, unresolved, solo vocal only
  ```
Core instrument/texture palette: slowed hip-hop breakbeat, Rhodes/Wurlitzer, vinyl crackle and surface noise as an instrument, tremolo/surf guitar, upright bass, muted strings, analogue synth drone, theremin or Trautonium (occasional, rotate between the two, not every song). **No guitar solos, no big drums, no key change, no crowd.** The **loop is the solo** — the way the violin carries gypsy-emo, the spoken monologue *is* the solo in institutional hardcore, and the sampler *is* the solo in dissociative hardcore.
 
---
 
