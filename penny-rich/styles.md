# Penny Rich — Suno Style Prompts

## Suno prompt notes

**Notation rules — these are hard, and getting them wrong audibly wrecks the take.** Same rules as the lurker and Lucy specs; they're generic to Suno.

- **`[Square brackets], on their own line` = direction.** Not sung. Every performance instruction goes here — dynamics, arrangement, who's singing, what the band does, how a section ends. Be as verbose as you like; it costs nothing.
- **`(Parentheses)` = backing vocal, and the contents get SUNG.** Parentheses hold **only words you want to hear**. Never a description, never a stage direction, never a label. `(harmony) call it luck` sings the word "harmony".
- **Never use em-dash-wrapped prose as a direction.** Convert every one into a bracketed tag on its own line.
- **Nothing between the brackets and the lyrics.** Every line is either a `[tag]` on its own line or words to be sung.

Test before you paste: **read only the un-bracketed text and ask whether you'd be happy hearing all of it.**

- **This is the one spec where you *want* the harmony stack**, so say so — "close three-part harmony backing vocals" in the style prompt. Suno's reflex to put a crowd behind a repeated hook, which wrecks lurker and Lucy, is exactly right here. Let it.
- **The break is the least predictable part** — regenerate several times to find a take where the band genuinely stops for the plain line and then comes back *up to tempo* rather than swelling sentimentally underneath it. A take that goes gentle there kills the song. (Same job as chasing the crack in gypsy-emo's shout-back, the *turn* in hardcore's monologue, the swallow in dissoc's dissolve, the silence in lurker's drop-out, the strip-back in Lucy's near-yes.)
- Ask for the vocal **bright, warm, forward, slightly nasal, on the beat** — country phrasing, not jazz phrasing. Explicitly ask it *not* to be breathy or torchy; that's Lucy's voice and it's the wrong woman.
- Style prompt for the **fast porch core** (recommended default):
  ```
  fast traditional bluegrass, banjo rolls, fiddle, mandolin chop, upright bass, boom-chuck acoustic guitar, dobro, instrumental breaks trading solos, bright warm female lead vocal, high lonesome close three-part harmony, live room, no drums
  ```
- **Banjo-vaudeville variant** (the original seed — older, sillier, closer to the tent show):
  ```
  banjo vaudeville, old-time ragtime string band, tenor banjo, jug band bass, washboard, stride piano, honky-tonk upright, cheerful female lead vocal, barbershop-tinged harmony, novelty song energy, live and rowdy
  ```
- **Parlour variant** (slow, close, exposed — for wins where the wound is near the surface):
  ```
  slow mountain ballad, waltz time, dobro and fingerpicked guitar, no banjo roll, upright bass, distant fiddle, close family harmony, plain warm female voice recorded close, sparse, front-porch, no drums
  ```
- **Countrypolitan variant** (the Nashville end — bigger, glossier, for the brags):
  ```
  1970s countrypolitan, pedal steel, sweetened strings, tick-tack bass, telecaster, bright confident female lead vocal, polished Nashville production, big harmony chorus, upbeat
  ```
Core instrument palette: five-string banjo, fiddle, mandolin, dobro, flat-top guitar, upright bass, optional pedal steel or piano at the countrypolitan end. **The banjo is the solo — and for the first time in this house, it's an actual solo.** Every other spec bans them and nominates a substitute (the violin, the monologue, the sampler, the loop, the trumpet that never finishes). This one has real instrumental breaks, taken in turn, finished properly, and the fact that they finish is the point.

---
