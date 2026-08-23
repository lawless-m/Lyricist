# Disassembler — Suno Style Prompts

## Suno prompt notes

- Paste the **bracketed section tags** — the whole style depends on the breakdown genuinely
  emptying out so one quiet sentence can sit in the hole, and the tags are the only way to get
  that. The spike proved Suno will honour "kick fully removed" if you ask plainly.
- **State the no-crowd rule in the prompt as well as the tags.** Suno's instinct on a repeated
  shouted anchor is to stack a gang behind it, which is precisely the fence against `laundry`.
  Say "no gang vocals, no crowd, single voice" every time.
- **Say the vocal is percussive, not sung.** "Shouted vocal stabs used as percussion not melody,
  no singing anywhere" held on the spike and is worth keeping verbatim.
- **Fence the voice against `guessed`.** The first female take collided with her immediately, and
  the reason is that *close, dry, flat, unadorned female vocal* is a verbatim description of the
  lurker — a thin voice recorded against its will, in your ear, band down a corridor. Never write
  **close**, **intimate**, **fragile**, **breathy** or **confessional** into a Disassembler prompt.
  Reach for **MC** instead: drum & bass has that delivery natively, and it is projected, rhythmic
  and public. The distinction to hold is intent — Guessed's flatness is exhaustion and withholding;
  this one's is concentration. She is reading a list aloud to a room, briskly, not confiding in you.
- **The voice is a live choice, not a fixture.** The variants below currently say *female* because
  that is what is being tried, and an earlier version said *male* only because it was typed without
  being decided. State it explicitly in every prompt either way, and change it deliberately.
- **Warm echo on the vocal is the finding, not compression.** The take that worked came back with a
  warm echo delay on the voice, and that is what makes it sit right — the classic MC dub-delay
  throw, native to this music. It is now written into the variants so it recurs. Two honest
  caveats: Suno supplied that echo unasked (the prompt had said `heavily compressed`), so the
  compression term is kept alongside rather than removed, because it is not known which one earned
  it; and `sidechained` / `pumping` remain untried.
- **This is also the third fence against `guessed`, and the cleanest one.** She is a *dry voice in a
  reverberant room* — close and unprocessed, the band drenched behind her. Disassembler is the
  inverse: a voice carrying its own warm echo, thrown out over a dry precise mix. Do not write
  `dry vocal` into a Disassembler prompt.
- **Homographs are where takes actually differ.** Matt's finding on listening back: the technical
  strings render fine because they get spelled out phonetically in the lyric, and the thing that
  decides between two takes is Suno mispronouncing an *ordinary* word. The risk is words whose
  stress or vowel changes their meaning — **read** (reed/red) is the worst, then **minute**
  (MIN-it / my-NOOT), **record**, **object**, **subject**, **content**, **contract**, **present**,
  **invalid**, **live**, **lead**, **produce**, **refuse**, **permit**, **separate**.
- **Second and worse class: near-miss spellings.** Observed 2026-08-23 — `not-a-bus`'s "a tiered
  star with hubs" came back as **tired**. This is not a homograph (one spelling, two sounds) but two
  different words that look almost identical, where the model reads the wrong token outright:
  *tiered/tired*, *casual/causal*, *trial/trail*, *quiet/quite*, *form/from*, *manger/manager*,
  *unclear/nuclear*, *dairy/diary*. Worse than a homograph, because a homograph at least yields a
  real word in the right grammatical slot; this yields nonsense.
- **And this class appears to be deterministic, so rewrite it rather than re-rolling.** *tiered*
  came back as *tired* on **both** takes of `not-a-bus` — the model is not guessing, it is reading
  the token wrong every time. That splits the remedy: a homograph is a coin toss and worth another
  spin, a near-miss spelling is a fixed misreading and another spin wastes a render. The line was
  changed to "a tree of hubs", which says the same thing about the topology with no near-miss
  anywhere in it.
- **Compound failures are the worst and they hide.** Observed 2026-08-23 —
  `admired-not-used`'s "the read eval print loop" came back as **"red evil"**: *read* mis-stressed
  (class one) and *eval* misread as *evil* (class two), in adjacent words. Neither alone would have
  destroyed the line; together they produce a phrase that means nothing. Fixed by defusing both —
  "the **reed evaluate** print loop" — which spells the vowel and expands the abbreviation. When a
  phrase contains two risky tokens in a row, treat it as deterministic and rewrite without waiting
  for a second take.
- **Fourth class: run-together config tokens.** Observed 2026-08-23 — `ask-it-the-time`'s
  `noquery`, a real `ntp.conf` directive, was unsayable. Split them into the words a person would
  actually speak (`no query`), the same way `9P`, `p ninety-five` and `slash inet slash tcp` are
  written out. The `.txt` is a paste-target for a renderer, not a config file, so phonetic spacing is
  correct practice rather than a compromise — but keep the *spoken* form true to the real directive.
- **Third class: British place names.** Observed 2026-08-23 — `carbon-copy`'s "a building outside
  **Slough**" defeated it. Slough is a three-way homograph (*sluff* to shed, *sloo* a swamp, *slau*
  the town) and the town is the rarest reading, so it will lose every time. The same trap is
  everywhere in English place names: Loughborough, Leominster, Bicester, Frome, Gloucester,
  Worcester, Belvoir, Beaulieu, Happisburgh, Reading (town vs the act). Treat these as deterministic
  and pick an unambiguous town — the joke in a mundane-place line survives the substitution, the
  pronunciation does not — **but check the substitute is still true.** Slough was swapped for Swindon
  here and that broke the fact, since Slough is the actual data centre corridor and Swindon is not.
  The final line is "off the M4", which keeps the corridor, the mundanity and the accuracy. A
  pronunciation fix that introduces a factual error is a worse bug than the one it solves in this
  band.
- **But it is stochastic, so re-roll before you rewrite.** Matt's follow-up, and it changes the
  remedy: Suno is generally good at technical vocabulary and gets a word wrong *sometimes*, not
  reliably — the same line can come out right on the next take. So a mispronunciation is a re-roll,
  not a rewrite. Only change the words when a term fails repeatedly across takes, because rewriting
  on the first failure trades a good line away for a problem that may not recur. Knowing which words
  are *capable* of going wrong is still worth having: it tells you what to listen for and which take
  to keep.
- The **breakdown is the least predictable part** — regenerate to find a take where the beat
  genuinely stops and the voice is dry, close and unaccompanied. A take that keeps a pad running
  under it kills the signature move. (Same job as chasing the crack in gypsy-emo's shout-back or
  the strip-to-nothing in Guessed's drop-out.)
- Style prompt for the **neurofunk core** (recommended default):
  ```
  neurofunk drum and bass, 174 BPM, tightly edited amen-derived breaks, half-time reese bass, clean deep sub with headroom, cold precise dark production, metallic sound design, female MC, fast double-time spoken flow riding the break, projected and unemotional, clipped consonants, warm echo delay thrown on the vocal, heavily compressed, not intimate, not breathy, not fragile, shouted vocal stabs used as percussion not melody, no singing anywhere, single voice, no gang vocals, no crowd, breakdown with the beat fully removed, one spoken line in the silence at the same projected level, not whispered, not intimate
  ```
- **Rollers variant** (steadier, less surgical, for the fond and funny topics):
  ```
  rolling drum and bass, 174 BPM, deep rolling break, warm sub bass, minimal dark atmosphere, female MC, brisk spoken flow read aloud at speed over the break, projected and level, warm echo delay thrown on the vocal, heavily compressed, not intimate, not confessional, no singing, single voice, no gang vocals, no crowd, breakdown with the beat fully removed, one spoken line in the silence at the same projected level, not whispered
  ```
- **Techstep variant** (harsher and older, for dread — the certificate, the box nobody reboots):
  ```
  techstep drum and bass, 172 BPM, mechanical distorted breaks, industrial percussion, ominous sub, sparse and menacing, female MC, flat clipped spoken delivery, projected, warm echo delay thrown on the vocal, heavily compressed, not intimate, no singing, single voice, no gang vocals, no crowd, long instrumental stretches, breakdown with the beat fully removed
  ```
Core palette to draw from: edited breaks, reese and half-time bass, sub, metallic and mechanical
percussion, atmos pads, no melodic lead, no chorus in any sung sense. **The break is the solo** —
the way the violin carries gypsy-emo, the sampler carries laundry and the loop carries Guessed.

---
