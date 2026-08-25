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
- **Compound tokens fail even when they are ordinary English.** Observed 2026-08-24 —
  `not-a-login`'s repeated anchor came back as *lojin*, the `gi` softened as though the word were
  Italian. This is the `noquery` class and not a homograph: the fix is to split the compound, so
  the drop now reads **LOG IN**, which removes the offending letter pair altogether. Worth assuming
  for any run-together word, not only config tokens — `login`, `logout`, `signin`, `changelog`,
  `pagefile` all present the same hazard.
- **The two-take test is the diagnostic, and it now has a clean case both ways.** Observed
  2026-08-24 — `ten-years-is-plenty` rendered "the archive" as *arch hive* in one take and
  correctly in the other. Differing across takes of the same lyric is the signature of the
  stochastic class, so the correct response is to keep the good take and change nothing; the word
  is not at fault. The contrast is `not-a-bus`, where *tiered* came back as *tired* in **both**
  takes, which is what identified it as deterministic and worth rewriting. Before reaching for a
  rewrite, check the other take: it tells you which class you are in, and rewriting a stochastic
  miss throws away a correct word for no reason.
- **A line ending in a function word gets re-parsed across the break.** Observed 2026-08-24 and
  the subtlest failure so far — `series-is-and` had the couplet "series is and / parallel is or",
  and Suno sang it as *"series is ... and parallel is or"*, hearing the **and** as a conjunction
  reaching for the next line rather than as the operator being named. Nothing is mispronounced;
  the phrasing is simply wrong, which makes it harder to catch than a mangled word. Line breaks are
  not read as punctuation. Where a lyric uses a function word — *and, or, but, not, if* — as a
  **noun**, give it a frame that cannot be misread: the fix here was "two switches in series make an
  **and gate**", with the drop anchors becoming "AND GATE" / "OR GATE". Capitals did not help; the
  drop was already shouting them.
  The same song had a subtler instance the owner caught next: "a contact that opens when the coil
  pulls **is not**" — the ear waits for a sentence that never arrives. Now "is a **not gate**".
  A sweep of the whole catalogue for lines ending in a function word found no other cases: ordinary
  English endings like "so who was I keeping quiet for" or "that one does not" are stranded
  prepositions and elliptical negations, and they read correctly. The fault is not a line ending in
  a function word, it is a function word being used as a **noun** — which in practice means only
  where logic operators are being named.
- **Write years in full or they are just numbers.** Observed 2026-08-24 — `series-is-and` had
  "master's thesis, MIT, thirty-seven / Transactions of the ..., thirty-eight", which Suno reads
  correctly and which nobody hears as 1937 and 1938. A bare two-digit year survives on the page
  because the eye supplies the century; the ear does not. Say **nineteen thirty-seven**. Same fix
  applied to `show-it-dogs`, whose lineage opened on a bare "eighty-four". Note that "nineteen"
  does not trip the PERM ban on the word *nine* — the pattern is word-anchored.
- **Suno defaults to American pronunciation.** Observed 2026-08-25 — `series-is-and` said
  *rə-LAY* where the owner wanted the British *REE-lay*. This is not a homograph and re-rolling
  will not fix it: there is one word, two national readings, and the model has a default. Respell
  it — **ree-lay** — the same treatment as *cha root* and *loll*, and accept that the written lyric
  now carries an odd-looking word. Applied to all three occurrences including the paper's title.
  **Do not pre-emptively respell the rest.** A sweep of the catalogue for words with a known split
  found *data* (17), *process* (9), *status* (5), *schedule* (5), *garage* (4), *router* (2) and
  *privacy* (2). The audible ones are **schedule** (SHED-yool / SKED-jool), **garage**, **router**
  (ROOT-er / ROW-ter) and **privacy** — worth listening for specifically, but every class in this
  file earned its place by being heard rather than predicted, and mangling forty lines on a guess
  would break that.
- **Initialisms get read as words.** Observed 2026-08-24 — `series-is-and` rendered `AIEE` as a
  yelp rather than four letters. Suno has no way to know an initialism is not a word, and spacing
  the letters is unreliable. **Expand it instead**: the line now says *Transactions of the American
  Institute of Electrical Engineers*, which is what AIEE stands for, so the fix costs nothing and
  gains accuracy. Only skip the expansion where the initialism is itself the well-known name and
  the expansion would be the surprising form — nobody says International Business Machines. Note
  what did work in the same batch: `MIT`, `ISO`, `TCP`, `BSD`, `PDP`, `VAX`.
- **Coined tokens with no agreed pronunciation need writing out phonetically.** Observed
  2026-08-24 — `ten-years-is-plenty` could not say `chroot`, and the owner's response is the useful
  part: *"but then again who can!?"* Where a term has no settled spoken form among the people who
  use it daily, there is nothing for Suno to fall back on, so spell it the way it is actually said
  — **cha root**, which was re-rendered and confirmed correct by ear. Second instance, and it is not a
  Disassembler song: `guessed/emerald-three` has the line *I typed "lol"*, which came back as three
  letters. Spelled **loll** it renders as the word people actually say. Note the cost — the written
  lyric now carries a misspelling of the token, and the song's point is that she typed rather than
  spoke, which the letters arguably conveyed. The owner's ear wins; these files exist to be pasted
  into Suno, not read.

  **These classes are catalogue-wide.** They live in this file because the Disassembler material
  surfaced most of them, but every one applies to every band. Distinct from the compound-splitting fix above, which repairs a word that does
  have a correct reading. Same song: `serverless` became **server less**.
- **`lead` is the homograph most worth rewriting rather than re-rolling.** Observed 2026-08-24 —
  "the lead author" came back as *led author*. Homographs are normally stochastic and worth a
  re-roll first, but this one has an unusually strong wrong attractor and there is almost always a
  precise substitute that removes the ambiguity for free. Here it became **"the editor"**, which is
  what Eran Hammer actually was when he took his name off OAuth 2.0 — so the fix improved the
  accuracy as well. Apply the Slough test every time: check the replacement is still true.
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
