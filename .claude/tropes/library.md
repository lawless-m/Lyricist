# Trope Library

Shared across every band. Consult before finalizing any song; log after.

**Rule: any device below has already been used once. A second use of it — in any band,
in any song — is not allowed while the entry is live.** Check every notable construction,
distinctive phrase, and imagery motif in a draft against this file before saving.

**Decay (2026-07-24, refactor step 3).** Fatigue decays; permanent retirement on first use
was the wrong model for one listener with a normal memory. Entries now carry a class:

- **Permanent** — the calcified house-style devices; never cool. The permanent set:
  the `where/should` inventory-of-loss couplet, `nobody asked`, the `fold/buckle` collapse
  lines, the `so + wh-word + was/did I` skeleton, the `so tell me, X, tell me` skeleton,
  the `didn't/never fix/save me` closing formula, `twice`, `nine`, `closer than that`,
  `and the fiddle starts confessing`, the grandmother's-grandmother lineage motif, and the
  `I said define X` interrogation-of-a-word beat, and the `I have never once ___`
  unblemished-record boast.
- **Cooling** — everything else, which is the default. A cooling entry is fully banned
  until **60 songs** (tunable, catalogue-wide count — songs-written-since-last-use, not
  elapsed time) have been added since its last use; after that it demotes to advisory —
  usable again with a stated, song-specific justification, never as a reflex. `check.sh`
  computes this automatically for the mechanical subset from the TSV's LOGGED_AT column;
  for fuzzy entries (constructions/motifs), judge songs-since from the entry's logged
  catalog size, noted on entries from this point forward.

New entries record the catalog song-count at logging time (a "Logged at catalog size N."
line here, and the LOGGED_AT column in the TSV). Existing entries were backfilled
approximately by era — 85 (seed), 107 (post-seed sessions), 120 (the 2026-07-24 batch).

**Rebase (2026-07-26).** Every stamp above was raised by 12. `check.sh` had been counting
the catalog from a hardcoded band-folder list that never gained `girlboss`, so it reported
114 songs where the real figure was 126. Since cooling is `(catalog − LOGGED_AT)`, every
entry recorded under the short count was cooling 12 songs early; the +12 restores each
entry's intended 60-song life. The script now discovers band folders by their
`template.md`, so the count can't silently drift a whole band again.

Seeded 2026-07-19 from a scan of the 73 pre-existing songs across all five bands. That scan
was targeted at things already repeating 2+ times in the existing catalog, not an exhaustive
catalog of every line ever written — devices used only once in the pre-existing catalog are
not listed here. Everything logged from this point forward (new songs written via
`write-song`) is added on its *first* use, so it's caught on any second use anywhere.

**Enforcement is split in two layers (2026-07-24, refactor step 2).** This file remains the
human record — full context, provenance, every entry. Alongside it, `banned-patterns.tsv`
holds the *mechanical subset*: exact-phrase anchors and regex-expressible construction
skeletons, checked deterministically by `check.sh` before any save (write-song step 5). The
Constructions and Imagery / Motifs sections are the *fuzzy remainder* — shapes and motifs a
grep can't catch — and they are what write-time judgement now concentrates on. Two upkeep
rules: (1) every newly logged entry with a greppable anchor is mirrored into the TSV in the
same commit — an unmirrored entry is invisible to the deterministic check; (2) the TSV is
derived from this file, never the reverse — if they disagree, this file wins and the TSV
gets fixed.

## Constructions

### "I've got [X] where [Y] should be" / "I've got [X] where [Y] was" — inventory-of-loss couplet
- Originally banned only in the lurker spec (`"___ where ___ should ___"`). It escaped into
  three other bands and became a load-bearing hook line there instead of staying banned.
- Example: "I've got a menu where a mouth should be, and you call this a courtesy" — purple-dog/robocaller
- Also seen: guessed/handle-where-a-name-should-be, laundry/finna-retard, laundry/same-red,
  purple-dog/i-dont-want-your-damn-boots, purple-dog/purple-dog, purple-dog/secure-the-scene,
  purple-dog/suspicious-activity, the-bell-knows-my-name/does-the-building-dream-us-too,
  the-bell-knows-my-name/do-you-hear-the-ground-you-keep, the-bell-knows-my-name/i-was-here-before-your-fathers,
  the-bell-knows-my-name/sing-the-valley-back-to-us, the-bell-knows-my-name/the-bell-knows-my-name,
  the-bell-knows-my-name/the-graves-i-didnt-dig, the-bell-knows-my-name/the-plum-trees-secret,
  the-bell-knows-my-name/wheels-where-i-should-kneel

### "Nobody['s] [ever/never] asked" — unacknowledged-expertise tic
- A stock way of voicing the lurker's "total attendance, zero standing" ache: nobody in the
  room ever asked her anything, ever asked her opinion, ever asked if she was okay. Recurred
  enough across the pre-existing catalog (never flagged until now) that it needs retiring the
  same way `"___ where ___ should ___"` did.
- Example: "and nobody's ever asked" — guessed/handle-where-a-name-should-be
- Also seen: guessed/emerald-three ("Nobody's ever asked."), guessed/who-was-i-first-for
  ("Nobody's asked me about it since."), guessed/well-delivered ("Nobody in that room asked me
  a single question")
- Caught and avoided during drafting: guessed/the-version-she-liked originally used "and she
  never once asked" in its hook — revised to "and she took it whole" before this entry was
  logged, so it is not listed as a further instance.

### "and the [drums/churn] [fold/buckle] in (on themselves)(, doesn't lift)" — mechanical-collapse hook line
- Example: "— and the drums fold in on themselves —" — laundry/breeder
- Also seen: laundry/addicted-to-declining, laundry/turn-it-down (fold variant);
  laundry/turn-it-on, laundry/same-red, laundry/permanence-is-temporary, laundry/finna-retard
  (buckle variant); laundry/keep-it-warm, laundry/scroll-up ("the churn folds in on itself,
  doesn't lift" variant)

### "you trust [the record], not [the reality]" — accusatory parallel aimed at an institution
- A two-beat "you trust X, not Y" accusation naming what the institution takes as evidence
  against what actually happened. Fresh construction, logged on first use so a near-identical
  wording doesn't recur.
- Example: "you trust the log, not the room — you trust the timestamp, not the wait" — purple-dog/no-show

### "Nobody [verb]ed it — it just [verb]s" — spontaneous-order chant hook
- A chanted claim that a system runs without anyone having designed or authorized it.
- Example: "Nobody built it — it just runs" — coase-guard/no-blueprint (template.md reference example)

### "We don't run on [a system], we run on [a name]" — identity-over-schedule chant hook
- A chanted claim that the crew organizes around who people are and what they know, not an
  imposed system or schedule.
- Example: "We don't run on a schedule, we run on a name" — coase-guard/the-day-we-turned-it-off

### "What matters is what we needed [him] to have said" — myth-serves-the-need-not-the-fact line
- The wink's explicit admission that a legend's details are chosen for what the story needs,
  not what actually happened.
- Example: "Doesn't matter what he actually said. What matters is what we needed him to have
  said." — coase-guard/the-day-we-turned-it-off

### "You work, you eat. That's the whole of the law." — earn-it chant hook
- A chanted two-clause law-statement: the whole household/crew rule collapsed into one blunt
  earned-exchange line.
- Example: "You work, you eat. That's the whole of the law." — coase-guard/you-work-you-eat

### "That's not [feeling word], that's arithmetic" — blunt reframing of a rule as cold math
- Rejects an emotional label for a rule (strict/cruel/harsh) by reframing it as plain counting.
- Example: "Two hours at the woodpile earns one hour at my table. That's not strict. That's
  arithmetic." — coase-guard/you-work-you-eat

### "Who the fuck are you? ... You bought a piece of paper. You didn't buy this place." — ownership-without-legitimacy chant hook
- A two-part chanted challenge: first a flat identity challenge to an outside claimant, then a
  paper-claim-vs-actual-place contrast rejecting financial/legal ownership as real legitimacy.
- Example: "Who the fuck are you? We don't know your face. ... You bought a piece of paper. You
  didn't buy this place." — coase-guard/who-the-fuck-are-you

### "I said yes to [X]. This is [an audition/other mismatch]." — small-invitation-vs-actual-stakes reveal
- A plain two-clause line naming the gap between what she agreed to and what she's actually
  been walked into.
- Example: "I said yes to a coffee. This is an audition." — guessed/the-second-chair

### "pin the face, mute the room, spend the hour, burn the deck" — video-call consumption-imperative hook opener
- Laundry's imperative-opener slot filled with video-call-interface verbs (pin/mute) fused with
  consumption verbs (spend/burn).
- Example: laundry/pin-her-video

### "can everyone see my screen" — banal-phrase-degraded-to-mantra
- A ubiquitous, meaningless tech-support phrase used as the chanted mantra, repeating until it
  curdles into an existential question (can anyone see him at all).
- Example: laundry/pin-her-video

### "count the sheep, scroll the feed, dim the screen, drain the charge" — insomnia consumption-imperative hook opener
- Laundry's imperative-opener slot filled with sleep-hygiene-advice verbs fused with
  screen/battery-drain verbs.
- Example: laundry/the-app-says-im-resting

### "the app says I'm resting" — quantified-self mantra
- A sleep-tracker's data contradicting lived experience, chanted as mantra until it degrades to
  noise; the narrator ultimately believes the graph over the day he's actually having.
- Example: laundry/the-app-says-im-resting

### "say sorry, mean nothing, wipe your face, keep walking" — apology-that-can't-land consumption-imperative hook opener
- Laundry's imperative-opener slot filled with apology/repair verbs undercut by
  dismissal/erasure verbs.
- Example: laundry/sorry-spider

### "message not delivered" — failed-communication mantra
- The phone/text-message failure notification repurposed as the chanted mantra for an apology
  that has no addressee capable of receiving it (interspecies, here — but portable to any
  unreachable listener).
- Example: laundry/sorry-spider

### "spin it out, wring it dry, fold what's left, forget the rest" — laundry-cycle consumption-imperative hook opener
- Laundry's imperative-opener slot filled with literal washing-machine verbs fused with
  erasure/forgetting verbs.
- Example: laundry/unbalanced-load

### "wash, rinse, repeat" — ubiquitous-idiom-degraded-to-mantra
- The shampoo-bottle instruction repurposed as the chanted mantra for mindless repetition,
  degrading toward noise across the final hook.
- Example: laundry/unbalanced-load

### "read the card, hold the mic, pour the round, mean the toast" — wedding-toast consumption-imperative hook opener
- Laundry's imperative-opener slot filled with wedding-reception logistics verbs undercut by
  the impossible instruction to "mean" the one that matters.
- Example: laundry/second-draft

### "to the happy couple" — ubiquitous-idiom-degraded-to-mantra
- The standard toast-closing phrase repurposed as the chanted mantra, degrading toward noise.
- Example: laundry/second-draft

### "the machine gets the emotions while I go through the motions" — AI-authorship-vs-lived-numbness legible spike
- The band's own founding irony (see template.md's band-name origin note), first actually used
  in a song here: an AI-authored line lands with real feeling in the room while the narrator,
  delivering it, feels only the mechanics of delivery.
- Example: laundry/second-draft

### "post the req, water the plant, print the card, erase the name" — corporate-death-processing consumption-imperative hook opener
- Laundry's imperative-opener slot filled with HR/office-logistics verbs (backfilling a role,
  watering the desk plant, printing a sympathy card) fused with the erasure verb.
- Example: laundry/the-graveyard-is-full

### "in-dispensable" eroding to "dispensable" — self-negating mantra
- The mantra chanted and chopped until the sampler strips its own negating prefix off, so the
  word degrades into its literal opposite meaning as it dissolves — the erosion enacts the
  song's theme rather than just accompanying it.
- Example: laundry/the-graveyard-is-full

### "cast the wind, work the tree line, flag the ground, call it clear" — K9-search-procedural consumption-imperative hook opener
- Laundry's imperative-opener slot filled with search-and-rescue/cadaver-dog procedural verbs,
  deliberately not in the doubled "verb it, verb it" shape (that shape is retired after
  laundry/good-dog's "walk it, heel it, hold the dark, stay").
- Example: laundry/all-clear

### "all clear" — ubiquitous-phrase-degraded-to-mantra
- The security/search radio call-out repurposed as the chanted mantra, degrading toward noise
  as the search keeps turning up nothing.
- Example: laundry/all-clear

### "act like it's news" — quoted-instruction hook opener
- Guessed's quoted-instruction hook opener for this song — the internalised script for sitting
  through a man re-explaining, wrongly, the thing she already knows, so he gets to feel useful.
- Example: guessed/four-minute-fix

### "So [wh-word] + was/did I [verb]" — self-directed unanswered question opener
- The "question she already knows the answer to" device (near the end of the hook, aimed at her
  own past self, repeated twice, unanswered) is a required bone of the style — but it kept
  landing in the exact same grammatical skeleton: "so" + a wh-word + inverted "was/did I" +
  verb. A phrase-frequency pass across the catalog (2026-07-22) turned up **seven** prior uses,
  not the two originally flagged — this was effectively the default template line, since it's
  the exact shape of template.md's own reference example ("So who was I keeping quiet for?").
  Retiring the "so + wh-word + was/did I" shape itself, the same way the imperative-opener and
  "nobody asked" constructions were retired. The device stays; this specific syntax doesn't.
- Example: "so who was I keeping quiet for" — guessed/handle-where-a-name-should-be
- Also seen: guessed/he-meant-it-kindly ("so why did I let the first day become four years"),
  guessed/keeping-the-space ("so who was I keeping the space for"),
  guessed/the-version-she-liked ("so why did I let them all go"),
  guessed/who-was-i-first-for ("so who was I the first for"),
  guessed/the-second-chair ("so why did I stay for the second cup"),
  guessed/four-minute-fix ("so why did I let him land it")
- Caught and avoided during drafting: guessed/let-it-lie originally used "so what was I actually
  folding" / "so what was I actually hiding" in this exact shape — revised to a yes/no question
  ("was any of it ever about the clothes" / "...about him") before this entry was logged.

### "twice" as a stock precise-count word for a small repeated action
- An exact count of two — asking twice, saying it twice, reading something twice, thanking
  someone twice, walking past it twice — used constantly across Guessed as a stand-in for
  exactness, effort or self-surveillance. Never flagged before because each instance reads as
  ordinary word choice, but the word itself has saturated the band to the point of being a
  reflex. Retiring "twice" as a go-to precision word (in any construction — mid-sentence or as
  a standalone fragment). A different exact count, or a different way of conveying repetition
  entirely, should be used instead.
- Example: "I said thanks twice and I put it straight in my bag" —
  guessed/it-runs-to-the-thirty-four
- Also seen (guessed): dont-look-at-her-hand, is-it-a-gift, its-not-that, just-knock,
  keeping-the-space, nobody-minded-these-days, the-fifty-first, well-delivered,
  who-did-i-dress-for, who-was-i-first-for
- Also seen (lucy-might, standalone-fragment form): nobodys-licked-me-yet ("I have wanted to.
  Twice. In nineteen years."), take-your-time ("You did the legs. All the way up. Twice.")
- Caught and avoided during drafting: guessed/let-it-lie went through two revisions on this
  line — "He asked if I was alright. Twice." then "He asked twice if I was alright." — before
  landing on "He asked if I was alright." (no count at all) once the word itself was recognized
  as the problem, not just the standalone-fragment shape.

### "nine"/"the ninth" as a stock precise-count word for effort/iteration
- Banned pre-emptively by the user after a single use (ultracoase/tilbury: "I've drafted it
  nine times. I keep the ninth, not the first."), before it could saturate the way "twice" did
  for Guessed — same underlying tic (a number chosen to *read* as precise effort/self-audit)
  and the same fix: a different exact count, or no count at all. User's own reasoning: "sounds
  like a lot, 10 is too round" — nine functions specifically because it's one short of a round
  number, which is exactly what makes it a reflex rather than a real, situation-specific detail.
  Watch for this same "one-short-of-round" pattern recurring with a different number, not just a
  literal repeat of "nine."
- Example: "I've drafted it nine times. I keep the ninth, not the first." — ultracoase/tilbury

### "let it lie" — quoted-instruction hook opener
- Guessed's quoted-instruction hook opener for this song — a soft, literal instruction about
  the clothes on the floor that doubles as the impossible emotional instruction to just relax
  and not manage everything.
- Example: guessed/let-it-lie

### "Did I [verb] X, or did I just [verb] Y?" — self-directed either/or question
- The "question she already knows the answer to" device, filled with a third distinct
  grammatical shape after both the "so + wh-word + was/did I" skeleton and the "Was any of it
  ever about X" yes/no shape above were used up. This one poses two possible readings of her own
  past behaviour and refuses to pick between them. The final-hook variant swaps the second half
  for a fresh verb, reframing the ending in one substitution.
- Example: "did I lose the thought, or did I just stop saying it out loud" / "...or did I just
  stop facing the window at all" — guessed/the-wanderer

### "Was any of it ever about [X]" — self-directed yes/no question, one word changes for the final hook
- The "question she already knows the answer to" device, filled with a fresh grammatical shape
  (yes/no, not wh-inverted) after the "so + wh-word + was/did I" skeleton above was retired. The
  final-hook variant swaps the object noun for a person, reframing the whole song in one word.
- Example: "was any of it ever about the clothes" / "was any of it ever about him" —
  guessed/let-it-lie

### "come back to us"
- Guessed's quoted-instruction hook opener for this song — something said to her (or to a
  version of her, drifting off/thinking too big in a meeting) now repeated to herself as a
  standing correction whenever she catches her own attention wandering.
- Example: guessed/the-wanderer

### "I pinned him across from my desk, facing the window I'm not allowed to face."
- The one-line-that-lands: a plain admission that the postcard occupies the literal physical
  privilege (facing the window) that she's denied at her own desk.
- Example: guessed/the-wanderer

### "The man in the painting never has to explain what he's looking at."
- The drop-out's naked admission — the flash of legibility, stated once, plain, and left alone.
- Example: guessed/the-wanderer

### "queue the take, tag the mood, spend the tokens, hit regenerate" — AI-generation-pipeline consumption-imperative hook opener
- Laundry's imperative-opener slot filled with AI-song-generation-pipeline verbs (queue/tag/spend
  tokens) fused with the literal UI command that closes it.
- Example: laundry/click-regenerate

### "the kick starts arriving a half-beat late and never catches up" — mechanical-collapse pre-hook line
- A fourth distinct phrasing for the pre-hook's textural build, coined after the "fold/buckle",
  "stutter/catch/click", and "second kit drops out" shapes above were all used. Logged so this
  one doesn't become the next reflex either — invent a fresh one again next time.
- Example: laundry/rest-when-im-dead

### "the hi-hat splits in two and the halves won't agree on the beat" — mechanical-collapse pre-hook line
- A fifth distinct phrasing for the pre-hook's textural build. Logged so this one doesn't become
  the next reflex either — invent a fresh one again next time.
- Example: laundry/oats-do-not-have-nipples

### "the drums stutter, catch, and lock into a click" — mechanical-collapse pre-hook line
- A fresh way of describing the pre-hook's textural drum-and-sampler build, coined specifically
  to replace the retired "fold/buckle in on themselves" shape above. Logged immediately so this
  phrasing doesn't calcify into a second reflex the way its predecessor did.
- Example: laundry/click-regenerate

### "the second kit drops out, leaves just a ticking hi-hat" — mechanical-collapse pre-hook line
- A third distinct phrasing for the pre-hook's textural build, coined after the two shapes above
  were both retired. Logged so this one doesn't become the next reflex either — invent a fresh
  one again next time.
- Example: laundry/no-blockers

### "clock in, bank the hours, spend the sleep later, sign here" — grind-culture consumption-imperative hook opener
- Laundry's imperative-opener slot filled with productivity/hustle-culture verbs (clocking in,
  banking hours, deferring rest) fused with the closing instruction to sign a form.
- Example: laundry/rest-when-im-dead

### "label it, litigate it, pump it, ship it" — dairy-labeling-dispute consumption-imperative hook opener
- Laundry's imperative-opener slot filled with regulatory/legal verbs (labeling, litigating) fused
  with the narrator's own literal breastfeeding-logistics verbs (pumping, shipping).
- Example: laundry/oats-do-not-have-nipples

### "raise the ticket, flag the risk, burn the buffer, ship it anyway" — agile/PM-jargon consumption-imperative hook opener
- Laundry's imperative-opener slot filled with corporate project-management verbs (raise a
  ticket, flag a risk, burn the buffer) fused with the fatalistic close.
- Example: laundry/no-blockers

### "so tell me, [address], tell me — [question]?" — chorus-closing repeated-address question skeleton
- The Bell Knows My Name's chorus-ending direct question, in the exact grammatical shape "so
  tell me, X, tell me —", where X is a form of address (someone, brother, father, strangers,
  soldier). Never flagged until a phrase-frequency check during drafting turned up **10 of 10**
  pre-existing songs using this exact skeleton — effectively the unquestioned default, the same
  situation "so + wh-word + was/did I" was in for Guessed before that got retired. The direct
  question itself stays a required chorus beat; this specific repeated-address syntax doesn't.
- Example: "so tell me, someone, tell me — is the leaving how you heal?" — template.md reference
  example
- Also seen: the-bell-knows-my-name/the-bell-knows-my-name ("so tell me, father, tell me — did it
  end this way for you?"), the-bell-knows-my-name/old-dogs-choose-to-go ("so tell me, someone,
  tell me — is the losing how we heal?"), the-bell-knows-my-name/do-you-hear-the-ground-you-keep
  ("so tell me, strangers, tell me — do you hear the ground you keep?"),
  the-bell-knows-my-name/does-the-building-dream-us-too ("so tell me, father, tell me — does the
  building dream us too?"), the-bell-knows-my-name/wheels-where-i-should-kneel ("so tell me,
  someone, tell me — is the leaving how you heal?"),
  the-bell-knows-my-name/i-was-here-before-your-fathers ("so tell me, strangers, tell me — is it
  mine or yours to steal?"), the-bell-knows-my-name/the-plum-trees-secret ("so tell me, soldier,
  tell me — have you papers for a tune?"), the-bell-knows-my-name/the-graves-i-didnt-dig ("so
  tell me, brother, tell me — do the dead forgive the ones who leave?"),
  the-bell-knows-my-name/the-wood-still-sings ("so tell me, father, tell me — is a song the only
  place you sing?")
- Caught and avoided during drafting: ultracoase/the-forge-doesnt-wait-for-me
  originally used "so tell me, someone, tell me — does the fire forgive a name?" — revised to a
  direct address without the repeated "tell me" scaffold ("brother, does the forge forgive a
  name?") before this entry was logged.

### "I gave [nature/world] my [loss], and [it] gave me [X] back. Some [mornings/nights] I still think I came out ahead of that bargain." — reciprocal-trade mismatch couplet
- The Bell Knows My Name's replacement for the retired "I've got X where Y should be"
  inventory-of-loss couplet, after that construction was banned band-wide. A different
  grammatical shape than Ultracoase's own replacement ("I know X, not Y") — this one frames the
  loss as an uneven trade with the world itself, and questions on the record whether the
  narrator actually got the better end of it.
- Example: "I gave the birds my grief, and the birds gave me their silence — some mornings I
  still think I came out ahead of that bargain." — the-bell-knows-my-name/the-birds-have-stopped-singing

### "does the quiet keep better count than we do?" — direct-question chorus closer, no repeated-address scaffold
- The Bell Knows My Name's replacement for the retired "so tell me, [address], tell me — [question]?"
  skeleton — a direct question aimed outward (here, at the silence itself) with no "tell me"
  repetition at all.
- Example: the-bell-knows-my-name/the-birds-have-stopped-singing

### "and the strings go quiet too, for the words I'll never say" — pre-chorus violin-personification line
- A fourth distinct phrasing for the pre-chorus's "violin says what the mouth can't" beat, after
  "and the fiddle starts confessing" (5 uses), "and the violin remembers" (1 use), and "and the
  fiddle stops its weeping" (1 use, from i-was-here-before-your-fathers, previously unflagged)
  were all already spent. This one ties the device directly to the song's own bird-silence theme
  rather than reusing a generic confession/memory frame — invent a fresh tie-in again next time
  rather than reaching for any of these four.
- Example: the-bell-knows-my-name/the-birds-have-stopped-singing

### A named sibling's trade/craft abandoned by the natural world itself after their death, not just by the narrator
- The specific-named-loss requirement filled with a brother (not the retired grandmother's-
  grandmother ancestral-lineage shape) whose literal trade (trapping) depended on the birds that
  then stopped coming after his death — the loss registers as an environmental fact, not just a
  personal one, without ever stating that connection outright.
- Example: the-bell-knows-my-name/the-birds-have-stopped-singing

### "I know [X], not [Y]" — mismatched-knowledge couplet
- A fresh replacement for the retired "I've got [X] where [Y] should be" inventory-of-loss
  couplet, filling the same chorus slot (the emotional thesis as a mismatched two-clause line)
  with a different grammatical shape: what the narrator actually knows vs. what he doesn't.
- Example: "I know the weight of the hammer, not the color of the flame" —
  ultracoase/the-forge-doesnt-wait-for-me

### "You don't out-run [X] — you learn to [ride/verb] it, or you [consequence]" — mastery-not-resistance hook thesis
- Ultracoase's second hook-couplet shape (a fresh construction per song, per the band's own
  rule): rejects fighting or fleeing an unstoppable force in favor of mastering/riding it, with
  a blunt two-way consequence (adapt or degrade) as the payoff.
- Example: "You don't out-run what's already running — you learn to ride, or you rust." —
  ultracoase/ashes

### "This isn't the first time [X] — it won't be the last. [Ordinal count]. Standing here is not [Y] — standing here is where I've always been." — cyclical-fatalism hook thesis
- Ultracoase's third hook-couplet shape: names a recurring pattern with an explicit ordinal
  count (making the repetition concrete, not vague) and closes on redefining mere presence
  itself as the only available claim, rejecting the frame of victory/survival entirely.
- Example: "This isn't the first time the water's had its way with this coast... Third time the
  sea's come calling. Third time we let it in. Standing here is not surviving — standing here
  is where I've always been." — ultracoase/the-third-time

### "[Historical figure] said it once. [Reaction]. Mine's [held back], I'm choosing [X]. [Cost] costs nothing to claim — [Y] picks the moment, not the crowd." — deliberate-restraint hook thesis
- Ultracoase's fourth hook-couplet shape: contrasts a historical figure's unhesitating public
  declaration with the narrator's own withheld one — framed explicitly as strategy and timing,
  not fear. Distinct from the mastery-not-resistance and cyclical-fatalism shapes above: this
  one is about a held, not-yet-spent claim rather than an ongoing pattern or unstoppable force.
- Example: "She said it once. The field went still. Mine's loaded. I'm choosing the ground.
  Heart of a king costs nothing to claim — the stomach picks the moment, not the crowd." —
  ultracoase/tilbury

### An older mentor/father/master figure's death as the verse-2 grounding human loss
- Retired as Ultracoase's reflex answer to its own template requirement ("one specific named
  human loss/detail in verse 2, grounding the story in a real body"). Two uses in a row (a
  father, then an old master) made it the default before anyone noticed — caught by the user
  directly on a third attempt. The *requirement* stays (verse 2 still needs one specific,
  named human cost) — but a death, and specifically an older-generation mentor/parent figure's
  death, is off the table. Reach for a living relationship, an ongoing cost, a rival, a
  choice's price paid by someone who's still around — anything but another dead mentor.
- Example: "Father died beside the anvil, tongs still in his hand" — ultracoase/the-forge-doesnt-wait-for-me
- Also seen: "My old master died believing someone still would need the trade" — ultracoase/ashes
- Caught and avoided during drafting: ultracoase/escape-velocity originally used "My mentor
  spent thirty years on paper rockets... died the week before the funding came through" —
  revised to a living cost (a wife and kids, a marriage strained by the choice) before this
  entry was logged.

### "Gravity's just the toll for leaving — pay it once and it's paid for good. I'm not counting down from a wreck, I'm counting up to a landing. [Dread-word] isn't [X]. It's just [reframe]." — forward-facing reframe hook thesis
- Ultracoase's fifth hook-couplet shape and its first optimistic one: takes a word usually
  loaded with dread (here: "the void") and reframes it in the hook's final line rather than
  avoiding it, plus a counting-down/counting-up contrast as the engine of the reframe.
- Example: "Gravity's just the toll for leaving — pay it once and it's paid for good. I'm not
  counting down from a wreck. I'm counting up to a landing... turns out the void's not empty.
  It's just unclaimed." — ultracoase/escape-velocity

### "I've [verb]ed [X], and I never once [same verb, reflexive] myself" — reflexive-verb mismatch couplet
- Ultracoase's seventh hook-couplet shape: a single verb repeated across the couplet, first
  transitive (done to others, at scale) then reflexive (never done to the self) — the mismatch
  is carried entirely by the verb's two senses rather than by two different nouns/clauses.
- Example: "I've delivered four thousand of them, and I never once delivered myself." —
  ultracoase/delivered-unread

### "It knows [X]. It's never once asked me why. [Institution/system] optimized [Y] — nobody optimized what for." — automation-without-purpose hook thesis
- Ultracoase's sixth hook-couplet shape: a system that has perfected the *how* of something
  while nobody — including the narrator — has kept track of the *why*. Distinct from the
  forward-facing reframe shape above: this one isn't optimistic, it's a flat unease at
  competence without purpose.
- Example: "It knows every bend in the road. It's never once asked me why. Optimized the route
  to the minute — nobody optimized what for... The miles keep adding up. Nothing's adding up to
  a place I know." — ultracoase/autopilot

### "It grows as one tree in [calm] — it splits along the graft when [stress]" — conditional-unity hook thesis
- Ultracoase's eighth hook-couplet shape: a grafted union that holds only under mild conditions
  and fails under stress, closing on an amor-fati commitment to keep repeating the doomed repair
  rather than resolving into hope or despair outright.
- Example: "grows as one tree in the calm, splits along the graft when the weather turns... I'd
  bind the wound again every March, and watch it open again every time" —
  ultracoase/the-frost-finds-the-line
- Watch for "frost" specifically recurring as Ultracoase's reflex season-adversity image — this
  song's hook payoff *is* frost ("the frost always finds the line"). Caught and avoided during
  drafting: ultracoase/the-graves-are-hungry originally used "the frost put us three plots
  behind" (intro) and "frost line's eighteen inches" (verse 1) as its backlog cause — revised to
  clay hardness and burial volume ("three came due in the same week... the clay wouldn't give an
  inch") before this note was logged. If frost genuinely earns its way into a future song, treat
  it the same way "twice"/"nine" were treated: a real image, not a reflex default.

### "Feed it [X], it don't ask [Y]. [Insatiable subject] was hungry before [origin], and it'll be hungry again." — insatiable-appetite hook thesis
- Ultracoase's ninth hook-couplet shape: personifies the recurring toll of the narrator's own
  trade as a literal appetite that was never satisfiable to begin with, closing on an amor-fati
  commitment to keep feeding it regardless of who it takes next.
- Example: "Feed it a name, it don't ask whose. Feed it a hundred, it don't say when. The ground
  was hungry before I was born, and it'll be hungry again." — ultracoase/the-graves-are-hungry

### "We paid for [the symbolic/global fix] and left [the literal/local one] standing open" — misallocated-effort hook thesis
- Ultracoase's tenth hook-couplet shape: names the gap between a funded, visible, symbolic
  response and the unfunded, literal, local one that actually needed the money — closing on the
  narrator's own repeated, futile-but-owned act (not anyone else's decision) as the amor-fati
  commitment.
- Example: "We paid for the sky and left the door standing open... and I'll measure the same
  eleven inches every March, and I'd file it again." — ultracoase/the-door-standing-open

### "Nobody [suffers] from [the dramatic cause] — they [suffer] from [the one small skipped step]. I don't [do the discipline] because [belief], I do it because [indifferent reality] doesn't care if I do." — discipline-precedes-belief hook thesis
- Ultracoase's eleventh hook-couplet shape: rejects the idea that a maintained standard needs a
  reason or a witness to be worth keeping — the narrator keeps it because the underlying physical
  reality is indifferent to motive, not because of faith, pride, or an audience.
- Example: "Nobody drowns from the storm that's coming — they drown from the gate somebody left
  half-shut. I don't check it because I trust the water, I check it because the water doesn't
  care if I do." — ultracoase/two-hundred-yards

### "Ask who [is responsible] and the room points at [an institution, a committee, a policy] — I don't point anywhere. It was me, [specific mundane setting], one [decision] off the top of my head." — refuses-institutional-deflection hook thesis
- Ultracoase's twelfth hook-couplet shape and its most direct statement yet of the band's own
  "radical self-ownership, no myth required" core idea — explicitly rejects the instinct to
  diffuse responsibility onto a company/committee/policy, naming the self as sole author instead.
- Example: "Ask who programs the robots and the room points at a company, a committee, a policy —
  I don't point anywhere. It was me, alone, at a desk, one number off the top of my head." —
  ultracoase/who-programs-the-robots

### "I can't tell if [the world] went quiet or [I] did — [evidence supports both]. [technical decline stat]. I'll [keep the duty] anyway, and I still won't know which of us it was." — unknowable-self-attribution hook thesis
- Ultracoase's thirteenth hook-couplet shape: the narrator's own failing instrument (here: aging
  ears) is entangled with the phenomenon they're measuring, so the decline can't be cleanly
  attributed to the world or the self — and the commitment is to keep the record honest about
  that uncertainty rather than resolve it either way.
- Example: "I can't tell if the hedge went quiet or my ears did — the audiogram says both are
  true... I'll walk the same six hundred metres every May, and I still won't know which of us it
  was." — ultracoase/which-of-us-it-was

### "I [do the craft] so you can [stand where they stood] — that's the whole of the technique, nothing more to it. [technical craft fact]. It was about you, not [the missing subject]. I'd do it again tomorrow, and I still [couldn't do the one thing that mattered]." — craft-explains-itself-then-betrays-the-craftsman hook thesis
- Ultracoase's fourteenth hook-couplet shape: the narrator states their signature technique
  plainly as a gift to the audience/viewer, then reveals in the same breath that the technique
  cost them the one specific, irreplaceable thing it was quietly built to avoid ever having to
  render.
- Example: "I paint the back so you can stand where she stood — that's the whole of the
  technique, nothing more to it... I'd paint the same back again tomorrow, and I still couldn't
  tell you the colour of her eyes." — ultracoase/ruckenfigur

### "and the [abstract noun] didn't/never [fix/save] me, [but/so] [reclaim clause]" — final-chorus landing formula
- A three-band leak that lived entirely in template reference examples, caught during the
  2026-07-24 template-vs-library scan (the templates had never been scanned; the library was
  seeded from songs only). The same closing move landed the final chorus of three bands'
  founding recordings. Retired permanently — this is the family-nod situation again,
  calcified across the house before anyone logged it.
- Example: "and the wandering didn't fix me, but the wandering feels real" —
  the-bell-knows-my-name/wheels-where-i-should-kneel (template.md reference example)
- Also seen: "and the leaving didn't save me, but the leaving wears my name" —
  ultracoase/the-forge-doesnt-wait-for-me (template.md reference example); "and the quiet
  never saved me, so I'm done being quiet" — purple-dog template.md reference example
  ("I'm Fine")

### "but God, [pronoun] [verb] …" — shout-back pivot shape
- The gypsy-emo communal shout-back's "but God," pivot — the emotional payload delivered as
  a swearing-on-it reversal. Used in the template reference example and again in
  old-dogs-choose-to-go; two uses plus the template model. Logged during the 2026-07-24
  template scan so a third use is caught.
- Example: "I was never made for staying — but God, I stayed a while" —
  the-bell-knows-my-name/wheels-where-i-should-kneel (template.md reference example)
- Also seen: "and the whistle never found her — but God, she taught me how to feel" —
  the-bell-knows-my-name/old-dogs-choose-to-go

### "Half a life to train [this hand]. One [wet spring] to train the copy. The [writ] can seize [the weights], but the [writ] can't reach [the knowing]." — substrate-asymmetry hook thesis
- Ultracoase's fifteenth hook-couplet shape: the same tacit knowledge is legal in a body and
  contraband in a machine — a legal instrument can seize the artifact copy but has no
  jurisdiction over the embodied original. Closes on the master/copy double meaning ("Wipe the
  copy, keep the master — the master's wearing out") and an amor-fati re-commitment ("Hand me
  the same wet spring, I'd spend it the same way"); the final hook folds the wink in via the
  all-caps callback "SOMETHING STILL RUNS AT MIDNIGHT. I NEVER TAUGHT IT HOW TO STOP." The
  writ's jurisdiction language recurs once in verse 2 ("behind my eyes, where no writ runs").
- Example: ultracoase/one-wet-spring
- Logged at catalog size 124.

### "Mine to [cut], not mine to [teach]" — rights-scope contrast
- A compact two-clause concession that possession of something for one use never licensed a
  second use — the narrator granting the legal point against himself in his own trade idiom,
  rather than disputing it.
- Example: "Most of those prints were customers'. Mine to cut, not mine to teach." —
  ultracoase/one-wet-spring
- Logged at catalog size 124.

### "They pay me to say where the line is. Every year I move it in. Whatever [a machine] still can't fake — that's what [a person] is this quarter." — shrinking-definition hook thesis
- Ultracoase's sixteenth hook-couplet shape: the narrator is paid to *author* a definition rather
  than to meet one, and states plainly that the definition contracts on a schedule. The
  unspeakability clause ("I can't tell you why the good ones are good. I write thirty and keep
  one.") carries the band's tacit-knowledge pillar, and the amor-fati close is a pre-commitment to
  narrowing it again next year *with his name on it* — ownership of a future harm, not a past one.
- Example: ultracoase/certain-too-early
- Logged at catalog size 125.

### "cool the hands, kill the pause, spend the breath, answer like a bill" — biometric-gate consumption-imperative hook opener
- Laundry's imperative-opener slot filled with body-suppression verbs (cooling the hands, killing
  the response pause, spending the breath) fused with a retail-settlement close — the instructions
  for passing as equipment, barked in the feed's own register.
- Example: laundry/still-warm
- Logged at catalog size 126.

### "the snare sticks on one millisecond and won't come off it" — mechanical-collapse pre-hook line
- A sixth distinct phrasing for the pre-hook's textural build, after the "fold/buckle",
  "stutter/catch/click", "second kit drops out", "kick a half-beat late", and "hi-hat splits in
  two" shapes were all spent. This one is a *stall* rather than a drift or a split — the kit
  locked onto a single latency value, thematically tied to the song's response-time gate. Invent
  a fresh one again next time.
- Example: laundry/still-warm
- Logged at catalog size 126.

### "She mucks out four. I ride one. / Best deal on the yard." — labour-tally chant hook
- Girlboss's hook slot filled with a bare work tally answered by a market verdict — the
  imbalance stated as arithmetic and immediately priced as a bargain, with no one criticised.
  Distinct from the band's other hooks (a quoted critic, a tasting note, listing language, a
  bar call): this one is a ledger.
- Example: girlboss/best-deal-on-the-yard
- Logged at catalog size 126.

### "I've never paid a groom in my life. / Well. I've never paid a groom." — verbatim-echo deadpan
- A boast repeated word for word instead of corrected, so the second pass carries the opposite
  meaning to the first. Distinct from the two-clause self-correcting deadpan of
  girlboss/offers-over-asking ("I let the room do its work. I helped the room.") — nothing is
  corrected here; the same sentence is simply said again once it can be heard properly.
- Example: girlboss/best-deal-on-the-yard
- Logged at catalog size 126.

### "He's in the doghouse. / I've had it insulated." — idiom-renovated chant hook
- Girlboss's hook slot filled by taking a stock domestic idiom literally and improving the
  premises — the punishment reframed as a property she maintains, which states the indefinite
  sentence without ever complaining about the offence.
- Example: girlboss/had-it-insulated
- Logged at catalog size 126.

### "Every word on that pack is true, and I wrote half of them myself. [quantified transformation] — the difference is [what I taught it to do]. You haven't got [the additive] in your cupboard. Nobody's been lied to. Nobody's been fed." — everything-declared hook thesis
- Ultracoase's seventeenth hook-couplet shape: the narrator's defence is total factual compliance
  — every claim on the label is accurate and he authored the accurate claims — so there is no
  deception to expose and no institution to blame, only a gap between what is true and what is
  nourishing. The inaccessibility clause (the domestic kitchen cannot obtain the working
  ingredient) is what makes it a trade rather than a recipe, and the closing paired negation
  refuses both exoneration and accusation before the amor-fati line re-commits to Monday.
- Example: ultracoase/e451
- Logged at catalog size 127.

### "[His/Her] [mother/mum] rang[, + politeness qualifier]" — stakes-owner-call bridge opener
- The girlboss bridge requires the straight world to interrupt mid-transgression, and the caller
  being a parent is a natural fit — which is exactly why it calcified immediately. Two consecutive
  songs opened the bridge the same way: "Her mum rang Sunday. Very polite." (girlboss/best-deal-on-the-yard)
  and "His mother rang. Pauline. Wanted to know, delicately..." (girlboss/had-it-insulated).
  Caught by the user, not by the fuzzy pass, which had checked the bridge's *ending* (the retired
  compliment-and-deflection button) and never looked at its opening. The device stays; a parent
  ringing, and this "[possessive] mother rang + politeness adverb" shape, are retired. Rotate the
  caller: girlboss/had-it-insulated was revised to Fiona, the hostess whose table the offence
  happened at, which also ties the bridge to that song's own callback.
- Example: girlboss/best-deal-on-the-yard (the use that stands)
- Logged at catalog size 127.

### "They never made it illegal to [X]. They made it illegal to [Y]. So I am not a man who [X]s. I am a man who [Z]." — statutory-distinction hook thesis
- Ultracoase's eighteenth hook-couplet shape: the narrator reads the ban precisely, finds the
  exemption it left standing, and re-describes himself into it — not defiance and not evasion,
  but exact compliance used as a route. Closes on an amor-fati re-commitment to the qualification
  itself ("I'd sit the exam again in the morning. I'd sit it in the rain.") rather than to the
  appetite underneath it.
- Example: ultracoase/on-the-register
- Logged at catalog size 128.

### "[X] answers before [the question is finished]" — response-latency-as-tell image
- Answer timing used as the thing that separates person from machine. Originates in
  ultracoase/autopilot ("My daughter asks 'are we there yet' out of habit — the dash answers
  before she's done asking"), then recurred twice in one day: ultracoase/certain-too-early
  ("reads the question before she answers it") and laundry/still-warm ("Practice: answer before
  the question finishes"). Caught by the user, not by the fuzzy pass. The *thesis* that latency
  reveals the machine stays available — it is certain-too-early's entire hook ("Machines are
  certain too early") — but this before-the-question-ends image is spent. certain-too-early was
  revised to a physical detail ("checks the screen after every word"), which is better anyway,
  since restating the thesis in a character detail was redundant.
- Example: ultracoase/autopilot (the use that stands)
- Logged at catalog size 128.

### "peel the fruit, lose the pip, open the jaw, keep it coming" — table-service consumption-imperative hook opener
- Laundry's imperative-opener slot filled with fruit-preparation verbs that turn into
  instructions issued *about* the narrator rather than by him — the last clause hands control to
  the machine. Deliberately not the retired doubled "verb it, verb it" shape.
- Example: laundry/instructions-unclear
- Logged at catalog size 129.

### "and the toms come loose from the count and roll off under the couch" — mechanical-collapse pre-hook line
- A seventh distinct phrasing for the pre-hook's textural build, after fold/buckle,
  stutter-catch-click, second-kit-drops-out, kick-a-half-beat-late, hi-hat-splits-in-two and
  snare-stuck-on-one-millisecond. This one scatters rather than stalls, and borrows the song's own
  rolling-fruit image. Invent a fresh one again next time.
- Example: laundry/instructions-unclear
- Logged at catalog size 129.

### "FREE MEANS OURS" — claim-on-abandoned-property chant hook
- hobo's hook-thesis slot: a two-word legal-sounding claim treating a discarded object's FREE
  sign as a transfer of title, chanted flat in full harmony with nobody disputing it. Distinct
  from coase-guard/who-the-fuck-are-you's paper-claim rejection — that one denies an outsider's
  legitimacy, this one asserts the gang's own, and there is no opponent anywhere in the song.
- Example: hobo/free-means-ours
- Logged at catalog size 139.

### "wally wally wonder bin" — nonsense refrain
- The first filling of hobo's nonsense-refrain slot: real words in a daft order, alliterative,
  meaningless, sung in full harmony as though it were the title hook of an enormous single, never
  explained. Arrives intact and leaves *bigger* — deliberately not Laundry's
  mantra-degraded-to-noise, which erodes into fragments. The slot stays and demands a fresh phrase
  every song; this filling is spent. Note the band's own constraint on refilling it: real words
  only, never a coined one, because a coined word reads as a producer tag and gets takes removed.
- Example: hobo/free-means-ours
- Logged at catalog size 139.

### "Sixty quid. Eighty. A hundred with the hands on — and the hands are in the freezer, so a hundred." — escalating mis-appraisal
- hobo's appraisal device: a broken object priced upward in three jumps, the last one justified by
  a missing part the gang confidently counts as present because they know where it is. The
  arithmetic is wrong and nobody in the song notices.
- Example: hobo/free-means-ours
- Logged at catalog size 139.

### "Dress: black tie. / Decorations will be worn." — invitation-instruction chant hook
- Girlboss's hook slot filled with a dress-code line lifted verbatim off a formal invitation card,
  chanted flat. Distinct from girlboss/offers-over-asking's quoted listing language ("Offers over
  asking. / No chain."), which *describes* a property — this one is an instruction issued to the
  reader in the imperative passive, and the second line's double meaning (medals / what she has
  on) only arms once the room is established. Also used as a cold a cappella intro before the
  first beat, which is a macro-order variation for this band — see the entry below.
- Example: girlboss/decorations-will-be-worn
- Logged at catalog size 141.

### The hook chanted cold, a cappella, before the beat drops — girlboss section-order variation
- Every prior girlboss song opens on Verse 1 with the loop already running. This one states the
  hook first, unaccompanied, as a card being read out, then drops the breakbeat under Verse 1.
  The bones are unchanged (V1 / hook / V2 / hook / bridge / out / final hook) — only the entry
  point moves. Logged so the cold-chant open doesn't silently become the new default opening for
  the band; the next song opens some other way.
- Example: girlboss/decorations-will-be-worn
- Logged at catalog size 141.

### "I said define [word]." + a bureaucratic non-answer — the interrogation-of-a-word beat — PERMANENT
- Laundry's verse-2 fixture, replicated across a whole run of songs before anyone logged it: the
  antagonist says something evasive, the narrator demands a definition of one word from it, and the reply
  files him under a wrong category instead of answering — timed the session out, stamped me
  present, rang me up as maybe, processed me as pending, logged us as a cull. Always the same
  slot (the beat after the antagonist speaks, inside the clipped image-stream verse), always the
  same syntax, twice on the same word (*here*). Retired permanently 2026-08-18 — not cooling.
  A word may still be interrogated in a laundry song; it must not be done with `define`, and not
  as a one-line demand-and-misfile pair.
- Example: laundry/keep-it-warm, laundry/turn-it-down, laundry/turn-it-on, laundry/still-here,
  laundry/same-red, laundry/addicted-to-declining, laundry/finna-retard, laundry/breeder,
  laundry/not-this-one
- Distinct from ultracoase/certain-too-early's "The spec defines a human as anyone the test lets
  through" — that is a circular definition the narrator authored, not a demand aimed at someone else.
- Logged at catalog size 141.

### "scroll the small print, tick the box, wet the thumb, keep using it" — consent-agreement consumption-imperative hook opener
- Laundry's imperative-opener slot filled with the physical actions of agreeing to terms (scrolling
  past the clause body, ticking, wetting a thumb for the print pad) closing on the instruction that
  is itself the consent mechanism — continued use. Deliberately not the retired doubled
  "verb it, verb it" shape.
- Example: laundry/by-continuing
- Logged at catalog size 142.

### "by continuing" — legal-boilerplate-degraded-to-mantra
- The two words that do the actual work in every terms-of-service acceptance clause, chanted as the
  mantra and worn to noise ("by continuing / by contin— / (—uing)"). Distinct from the band's other
  degraded phrases (a UI command, a standup idiom, a permission phrase, a sign-off) in that this one
  is not something anybody says out loud — it is the sentence that consents on your behalf while you
  do nothing.
- Example: laundry/by-continuing
- Logged at catalog size 142.

### "and both kits accept the update mid-bar, and the tempo belongs to them now" — mechanical-collapse pre-hook line
- A ninth distinct phrasing for the pre-hook's textural build, after fold/buckle,
  stutter-catch-click, second-kit-drops-out, kick-a-half-beat-late, hi-hat-splits-in-two,
  snare-stuck-on-one-millisecond, toms-roll-under-the-couch and both-kits-sag. This one is a forced
  version change rather than a drift, stall, split, sag or scatter — the drums are patched without
  being asked and the song's tempo stops being the band's. Invent a fresh one again next time.
- Example: laundry/by-continuing
- Logged at catalog size 142.

### "and who ticked it for me the year I was born?" — question-with-no-addressee, completed-and-unanswered
- The slot filled with a question that finishes cleanly and simply never gets answered — a fourth
  shape after the unfinished measurement (laundry/still-warm), the trailing passive appeal
  (laundry/instructions-unclear) and the question answered by the sales script
  (laundry/good-body-every-night). Aimed at whoever consented on his behalf before he could read.
- Example: laundry/by-continuing
- Logged at catalog size 142.

### "Place your bets. / ...No more bets." — betting-window chant hook, the close doubling as the cutaway
- Girlboss's hook slot filled with the two procedural calls a croupier makes to open and shut a
  betting window, chanted flat. The second call does structural work no previous girlboss hook has
  done: it lands the beat after the offer and *is* the cutaway, so the song cuts on its own hook.
  Distinct from girlboss/make-it-a-double's bar call (a drinks order repurposed as the thesis) and
  from girlboss/decorations-will-be-worn's invitation instruction (an imperative issued to the
  reader) — this is a pair, and the pair is a window closing.
- Example: girlboss/no-more-bets
- Logged at catalog size 143.

### "People say the house always wins. The house doesn't do anything. Somebody has to deal it."
- The unearned moral as a corrected proverb: a structural mathematical certainty re-attributed to
  her personally, so an inevitability becomes a personal achievement. A fifth flavour after the
  trade rule quoted straight (girlboss/long-finish), the household lore (girlboss/had-it-insulated),
  the management wisdom (girlboss/best-deal-on-the-yard) and the claimed authorship of an effect
  (girlboss/decorations-will-be-worn).
- Example: girlboss/no-more-bets
- Logged at catalog size 143.

### "Would you like to see my baps? / Freshly baked." — counter-patter chant hook
- Girlboss's hook slot filled with the shop's own upsell line, and the fresh mechanism is that the
  filthy sentence is her *mandated job script*: she is required to say it, to everyone, all morning,
  and it is entirely innocent every time. Distinct from girlboss/long-finish's tasting note (trade
  vocabulary describing a person), girlboss/make-it-a-double's bar call (an order placed) and
  girlboss/no-more-bets' betting-window pair (two calls bracketing a window) — this one is a service
  offer made across a counter to strangers, and the double meaning is in the noun, not the framing.
- Example: girlboss/freshly-baked
- Logged at catalog size 144.

### The unearned moral handed down as mentorship to another tradeswoman
- A sixth flavour after the trade rule quoted straight (girlboss/long-finish), the household lore
  (girlboss/had-it-insulated), the management wisdom (girlboss/best-deal-on-the-yard), the claimed
  authorship of an effect (girlboss/decorations-will-be-worn) and the corrected proverb
  (girlboss/no-more-bets). What is fresh is the vehicle: the lesson is taught to a named third party
  rather than stated to the listener, and its content (never give anything away free) lands seconds
  after the song has shown her giving a great deal away. The other woman is not exploited and not
  mocked — she is simply advised.
- Example: "I told the girl on the eggs: never mark down before one, they'll only wait you out." —
  girlboss/freshly-baked
- Logged at catalog size 144.

### "I have never once [been late / been over / been out / asked]" — the unblemished-record boast — PERMANENT
- Every band's default way of establishing competence: a claim of a spotless run, stated in the
  negative, with an optional `once` for emphasis. A phrase-frequency pass (2026-08-18, user-flagged)
  found `never once` in twenty-two songs and `I've never` in twenty across the catalogue — the same
  saturation profile as `nobody asked` and `twice`, and invisible line by line because each instance
  reads as ordinary speech. Several instances double up with an already-retired anchor
  ("never had to ask him twice"). Retired permanently — not cooling.
- The fix is not a synonym. The construction claims a record where the band's own discipline is to
  *show* one: replace it with the evidence a spotless record leaves behind. girlboss/freshly-baked
  was revised from "Pitch fee's twenty-two quid, cash, and I have never once been late with it" to
  "Pitch fee's twenty-two quid, cash, in Derek's hand before he's got his coat off" — which states
  the same fact, plants a character the bridge needs, and stops asserting.
- Example: purple-dog/no-show, laundry/mind-the-white, ultracoase/e451, girlboss/best-deal-on-the-yard,
  girlboss/no-more-bets, guessed/focus-on-the-story, guessed/the-fifty-first, penny-rich/say-i-settled,
  lucy-might/ask-me-again, ultracoase/autopilot
- Logged at catalog size 144.

### "Everything's negotiable. / Except the spec." — negotiating-position chant hook
- Girlboss's hook slot filled with a stated commercial position rather than a quotation, a
  description, a listing or an instruction: two clauses conceding everything and then withdrawing
  the one thing that matters. Deliberately not built on the word "offer", which would have collided
  with girlboss/offers-over-asking's estate-agency listing language — the crude noun this song was
  commissioned around ("we have melons on offer today") is demoted to an agenda item in verse 1 and
  never made the joke, so the counter-patter mechanism of girlboss/freshly-baked isn't run twice.
- Example: girlboss/except-the-spec
- Logged at catalog size 145.

### "The no-gifts clause in the supplier charter is mine. Word for word. I tightened it."
- The unearned moral as authorship of the exact probity rule she is in the act of bending, quoted
  with its threshold and its deadline, and considered entirely flattering. A seventh flavour after
  the trade rule quoted straight, the household lore, the management wisdom, the claimed authorship
  of an effect, the corrected proverb and the mentorship handed down — this one is a policy she put
  into the employer's own process.
- Example: girlboss/except-the-spec
- Logged at catalog size 145.

### "One careful owner. / That's the car." — disambiguation chant hook
- Girlboss's hook slot filled with a piece of trade boilerplate followed by a clarification of which
  of the two "she"s in the song it actually covers. The whole lyric is built on the motor trade's
  habit of calling a car "she", so every condition claim in verse 1 reads both ways at once and the
  hook is the only line that separates them — while conceding the other reading outright.
- Example: girlboss/one-careful-owner
- Logged at catalog size 146.

### The Carry On homophone answered truthfully in the other sense — the fifth girlboss lie shape
- The stakes-owner's question contains a word with a trade meaning and a personal one, and she
  answers the personal one, accurately, on a recorded line. Nothing false is said and nothing is
  concealed; the recipient simply ticks the box he was always going to tick. A fifth lie shape after
  the over-detailed valuation, the over-helpful fix list, the perfect omission and the commercial
  arithmetic. Transposed from Carry On Henry's "Has she been chaste?" / "All over Normandy" rather
  than reused: the question is genuine compliance vocabulary from this song's own world. Distinct
  from laundry's retired "I said define X" beat, where a demand for a definition is answered by a
  bureaucratic misfile — here she is the one doing the mishearing, deliberately, and it flatters her.
- Example: "and has she been garaged? / And I said: all over the county." — girlboss/one-careful-owner
- Logged at catalog size 146.

### "You'll be asleep. / I won't." — power-asymmetry chant hook
- Girlboss's hook slot filled with a bare statement of who is conscious and who isn't, which is also
  a literal description of the job. Fresh mechanism after the quoted critic, the tasting note, the
  listing language, the bar call, the labour tally, the renovated idiom, the invitation instruction,
  the betting-window pair, the counter patter, the negotiating position and the disambiguation.
- Example: girlboss/first-night-effect
- Logged at catalog size 147.

### The clinical report as the sixth girlboss lie shape — true in the register, obscene in English
- The stakes-owner asks for the findings and she reads the scored polysomnography verbatim:
  prolonged sleep onset, REM latency delayed, frequent arousals throughout the night, spontaneous,
  not respiratory. Every term is correct technical vocabulary and the report is genuinely good work;
  it is filthy only once translated. A sixth lie shape after the over-detailed valuation, the
  over-helpful fix list, the perfect omission, the commercial arithmetic and the homophone answered
  in the other sense — and the only one in which she says nothing but her professional findings.
- Example: girlboss/first-night-effect
- Logged at catalog size 147.

### "Discretion. Patience. / And a deposit." — creed-with-one-item-wrong chant hook
- Girlboss's hook slot filled with a brochure's list of professional virtues, the last of which is
  money. Fresh mechanism after the quoted critic, the tasting note, the listing language, the bar
  call, the labour tally, the renovated idiom, the invitation instruction, the betting-window pair,
  the counter patter, the negotiating position, the disambiguation and the power asymmetry.
- Example: girlboss/and-a-deposit
- Logged at catalog size 148.

### The uncorrected mishearing — he mishears in his own favour and she declines to fix it
- The third Carry On transposition and deliberately not the mechanism of the first two: in
  girlboss/one-careful-owner *she* mishears and answers in the wrong sense, and in
  girlboss/first-night-effect she inverts a refusal — here the mistake is entirely his, made in his
  own favour, and her whole move is to let it stand. She says a proper sentence, he acts on a filthy
  one, and nothing is offered by her at any point. Sourced from Carry On Matron's "I want to be
  wooed" / "you can be as rude as you like", with the misheard word never printed in the lyric.
- Adjacent to guessed/the-version-she-liked's "don't correct a compliment" (letting a warm wrong
  assumption stand) — same core, opposite motive: Guessed does it out of self-erasure, this narrator
  because his version is more useful than hers. Kept deliberately per the user's rule that cross-band
  device overlap is fine and only audible lyric repeats are not; no line is shared between them.
- Example: "And he heard a different word... And I let him. Correcting a member is not in the
  six-month package." — girlboss/and-a-deposit
- Logged at catalog size 148.

### "Hold it. / Hold it there." — the instruction both jobs require, chant hook
- Girlboss's hook slot filled with a live spoken command that belongs equally to the deportment
  lesson and to the photographer shooting it — one sentence doing two people's professional work at
  once, and filthy in neither of them. Distinct from girlboss/decorations-will-be-worn's invitation
  instruction, which is lifted off a card and issued to the reader: this one is said aloud to a class
  and the instrument merely has to be in the room for it.
- Example: girlboss/hold-it-there
- Logged at catalog size 149.

### "Module four is how to be looked at. Everything else on that timetable is cutlery."
- The unearned moral as a curriculum fact: the syllabus itemised, and the one module that actually
  transfers named flatly, with everything else dismissed in a word. An eleventh flavour after the
  trade rule quoted straight, the household lore, the management wisdom, the claimed authorship of an
  effect, the corrected proverb, the mentorship handed down, the authored policy, the itemisation of
  what was really bought, the confidentiality assurance and the moral misread as modesty.
- Example: girlboss/hold-it-there
- Logged at catalog size 149.

### "I fed him forty summers and I counted every plate; / he lifts me up the stairs at night and keeps no ledger of the weight." — kept-ledger-against-unkept-ledger thesis couplet
- The Bell Knows My Name's emotional-thesis slot filled with a fresh grammatical shape after the
  retired "I've got X where Y should be" and the spent reciprocal-trade shape ("I gave the birds my
  grief..."): both clauses describe the same debt, one party counting it and the other not, with the
  narrator's own accounting exposed as the smaller act. No filling of this slot ever recurs.
- Example: the-bell-knows-my-name/the-bloom-i-cut
- Logged at catalog size 150.

### "cut it low, cut it kind" — band-instruction chorus opener
- The imperative-to-the-players slot filled with the song's own horticultural verb, the second
  adverb pulling against the first. After "play it quick, play it broken" and "dig it slow, dig it
  holy".
- Example: the-bell-knows-my-name/the-bloom-i-cut
- Logged at catalog size 150.

### "and the fiddle keeps the spent notes / that my hands would have cut down" — pre-chorus violin-personification line
- A fifth distinct phrasing for the "violin says what the mouth can't" beat, after "and the fiddle
  starts confessing", "and the violin remembers", "and the fiddle stops its weeping" and "and the
  strings go quiet too". This one makes the instrument merciful where the narrator was not, and
  borrows the song's own pruning verb. Invent a fresh tie-in again next time.
- Example: the-bell-knows-my-name/the-bloom-i-cut
- Logged at catalog size 150.

### "I can shoe near anything that breathes for twenty mile around / and there's not one yard of that ground will take me when I'm done." — capability-against-non-entitlement thesis couplet
- The Bell Knows My Name's emotional-thesis slot filled with a fresh grammatical shape after the
  retired where/should, the spent reciprocal-trade couplet and the kept-ledger-against-unkept-ledger
  couplet: total competence in the first clause, total exclusion in the second, with no connective
  and no complaint drawn between them. No filling of this slot ever recurs.
- Example: the-bell-knows-my-name/born-in-a-stable
- Logged at catalog size 151.

### "walk him out, walk him sound" — band-instruction chorus opener
- The imperative-to-the-players slot filled with the horseman's soundness check (trotting an animal
  up to prove it isn't lame), which doubles as the demand the narrator can never satisfy. After
  "play it quick, play it broken", "dig it slow, dig it holy" and "cut it low, cut it kind".
- Example: the-bell-knows-my-name/born-in-a-stable
- Logged at catalog size 151.

### "and the fiddle comes when I call it / the way the horses always did" — pre-chorus violin-personification line
- A sixth distinct phrasing for the "violin says what the mouth can't" beat, after confessing,
  remembers, stops its weeping, the strings going quiet, and keeping the spent notes. This one has
  the instrument side with the animals: everything unable to speak accepts him, and only the people
  don't. Invent a fresh tie-in again next time.
- Example: the-bell-knows-my-name/born-in-a-stable
- Logged at catalog size 151.

### "warm her up, glove up, feed the jaws, keep her sweet" — machine-tending consumption-imperative hook opener
- Laundry's imperative-opener slot filled with shop-floor verbs that are also the verbs of keeping
  somebody happy, closing on the one that belongs entirely to the other register. Deliberately opens
  on "warm her up" rather than a clocking verb, since laundry/rest-when-im-dead already spent
  "clock in".
- Example: laundry/keep-her-fed
- Logged at catalog size 152.

### "keep her fed" — machine-appetite mantra
- The instruction to keep material going into the line, chanted and worn to noise ("keep her fed /
  keep her f— / (—ed)"). Distinct from the band's other degraded phrases in that it is an
  instruction about feeding something that is not a person, said all day by people who talk about it
  as one.
- Example: laundry/keep-her-fed
- Logged at catalog size 152.

### "and both kits take the line speed and neither one of them can hold it" — mechanical-collapse pre-hook line
- A tenth distinct phrasing for the pre-hook's textural build, after fold/buckle,
  stutter-catch-click, second-kit-drops-out, kick-a-half-beat-late, hi-hat-splits-in-two,
  snare-stuck-on-one-millisecond, toms-roll-under-the-couch, both-kits-sag and
  accept-the-update-mid-bar. This one is a forced acceleration — the drums put on the line's rate
  and fail to match it. Invent a fresh one again next time.
- Example: laundry/keep-her-fed
- Logged at catalog size 152.

### "operator zero six two—" — question-with-no-addressee filled as a number read out
- The slot filled with the narrator reading his own payroll number and stopping, the one variant the
  laundry spec names that had never been used. After the unfinished measurement
  (laundry/still-warm), the trailing passive appeal (laundry/instructions-unclear), the question
  answered by the sales script (laundry/good-body-every-night) and the completed-and-unanswered
  question (laundry/by-continuing).
- Example: laundry/keep-her-fed
- Logged at catalog size 152.

### "name it, rate it, breathe it out, log it before you drive" — anger-management consumption-imperative hook opener
- Laundry's imperative-opener slot filled with the coping-skill verbs taught on a mandated course,
  closing on the instruction that reveals what the course is for without naming it.
- Example: laundry/one-to-ten
- Logged at catalog size 153.

### "one to ten" — measurement-scale mantra
- The ubiquitous rating prompt chanted and worn to noise ("one to ten / one to t— / (—en)"). The
  band's banal-phrase-to-mantra move applied to an instrument that converts a feeling into a figure,
  so the mantra degrading is the feeling degrading.
- Example: laundry/one-to-ten
- Logged at catalog size 153.

### "and both kits drop a point a bar until there's nothing left to score" — mechanical-collapse pre-hook line
- An eleventh distinct phrasing for the pre-hook's textural build, after fold/buckle,
  stutter-catch-click, second-kit-drops-out, kick-a-half-beat-late, hi-hat-splits-in-two,
  snare-stuck-on-one-millisecond, toms-roll-under-the-couch, both-kits-sag,
  accept-the-update-mid-bar and take-the-line-speed. This one is a descending score rather than a
  mechanical failure. Invent a fresh one again next time.
- Example: laundry/one-to-ten
- Logged at catalog size 153.

### "what did the man in March put? I'd like to see what he put." — question-with-no-addressee aimed at an earlier self
- The slot filled with a question about his own previous answers, asked in the third person about a
  version of himself he no longer has access to. After the unfinished measurement, the trailing
  passive appeal, the question answered by the sales script, the completed-and-unanswered question
  and the number read out.
- Example: laundry/one-to-ten
- Logged at catalog size 153.

### "say it and stop." — quoted-instruction hook opener
- Guessed's quoted-instruction slot filled with advice she read rather than advice she was given —
  a stranger's line from a thread, now issued to herself in her own voice. Deliberately not "let it
  land", which was the first draft and sits too close to girlboss-adjacent "let it lie"
  (guessed/let-it-lie) to survive a listen.
- Example: guessed/say-it-and-stop
- Logged at catalog size 154.

### "how many is that, then. how many is that." — the question she already knows the answer to, as a quantity
- The slot filled with an elliptical count rather than a wh-question, after the retired "so +
  wh-word + was/did I" skeleton, the yes/no "was any of it ever about X" shape and the either/or
  "did I X, or did I just Y" shape. The answer is a number she could produce and doesn't.
- Example: guessed/say-it-and-stop
- Logged at catalog size 154.

### "don't push it." — quoted-instruction hook opener
- Guessed's quoted-instruction slot filled with the rule she now applies to her own hospitality:
  never offer a second time. After "be nice about it", "don't make it a thing", "you knew what it
  was", "you've got time", "act like it's news", "let it lie", "don't correct a compliment", "focus
  on the story", "come back to us", "be happy for her" and "say it and stop".
- Example: guessed/ones-with-names-on
- Logged at catalog size 155.

### "do they think they've got one." → "do they know they've got one." — the question she already knows the answer to, one verb changed
- The slot filled as a yes/no about somebody else's belief rather than about her own past, and the
  final hook swaps a single verb: *think* concedes they might be waiting, *know* concedes they have
  no idea a labelled pot exists. That substitution is the whole ending. Distinct from the elliptical
  quantity shape (guessed/say-it-and-stop) and from the retired wh-inverted skeleton.
- Example: guessed/ones-with-names-on
- Logged at catalog size 155.

### "they called it a bad omen, and they were not wrong about that. It was an omen about us." — prophecy-granted-then-redirected thesis couplet
- The Bell Knows My Name's emotional-thesis slot filled with a fresh grammatical shape after the
  retired where/should, the reciprocal-trade couplet, the kept-ledger-against-unkept-ledger couplet
  and the capability-against-non-entitlement couplet: the accusers' reading is conceded as accurate
  and then turned to a different subject, so nothing is disputed and everything changes. No filling
  of this slot ever recurs.
- Example: the-bell-knows-my-name/best-thing-i-ever-ate
- Logged at catalog size 156.

### "sing it thin, sing it hungry" — band-instruction chorus opener
- The imperative-to-the-players slot filled with the song's own condition, the second adverb naming
  the cause of everything in it. After "play it quick, play it broken", "dig it slow, dig it holy",
  "cut it low, cut it kind" and "walk him out, walk him sound".
- Example: the-bell-knows-my-name/best-thing-i-ever-ate
- Logged at catalog size 156.

### "and the fiddle holds the one note / that a swan makes when it goes" — pre-chorus violin-personification line
- A seventh distinct phrasing for the "violin says what the mouth can't" beat, after confessing,
  remembers, stops its weeping, the strings going quiet, keeping the spent notes, and coming when
  called. This one leans on the swan-song folklore the whole lyric sits in — the bird that is silent
  until the end. Invent a fresh tie-in again next time.
- Example: the-bell-knows-my-name/best-thing-i-ever-ate
- Logged at catalog size 156.

### "don't bring it up." — quoted-instruction hook opener
- Guessed's quoted-instruction slot filled with the rule she applies to her own qualifications.
  After "be nice about it", "don't make it a thing", "you knew what it was", "you've got time",
  "act like it's news", "let it lie", "don't correct a compliment", "focus on the story", "come back
  to us", "be happy for her", "say it and stop" and "don't push it".
- Example: guessed/name-of-the-course
- Logged at catalog size 157.

### "and would it have changed the meeting." — the question she already knows the answer to, aimed at the outcome
- The slot filled with a question about consequence rather than about herself, punctuated flat so it
  reads as already answered. After the retired wh-inverted skeleton, the yes/no "was any of it ever
  about X", the either/or "did I X or did I just Y", the elliptical quantity
  (guessed/say-it-and-stop) and the belief-about-others shape (guessed/ones-with-names-on).
- Example: guessed/name-of-the-course
- Logged at catalog size 157.

### "they only ever bark at what they don't know. / She walked past every one of them and not one of them woke." — rule-and-its-fatal-instance thesis couplet
- The Bell Knows My Name's emotional-thesis slot filled with a fresh grammatical shape after the
  retired where/should, the reciprocal-trade couplet, the kept-ledger-against-unkept-ledger couplet,
  the capability-against-non-entitlement couplet and the prophecy-granted-then-redirected couplet:
  a mechanism stated plainly, then the one event that satisfied it perfectly and cost everything.
  Nothing malfunctioned. No filling of this slot ever recurs.
- Example: the-bell-knows-my-name/only-bark-at-strangers
- Logged at catalog size 158.

### "keep it low, keep it listening" — band-instruction chorus opener
- The imperative-to-the-players slot filled with the posture of a man at a door with a lamp. After
  "play it quick, play it broken", "dig it slow, dig it holy", "cut it low, cut it kind", "walk him
  out, walk him sound" and "sing it thin, sing it hungry".
- Example: the-bell-knows-my-name/only-bark-at-strangers
- Logged at catalog size 158.

### "and the fiddle joins in with them / and it doesn't know why either" — pre-chorus violin-personification line
- An eighth distinct phrasing for the "violin says what the mouth can't" beat, after confessing,
  remembers, stops its weeping, the strings going quiet, keeping the spent notes, coming when
  called, and holding the swan note. This one has the instrument sound the alarm without
  understanding it, alongside the dogs. Note: an earlier draft read "and the fiddle starts up with
  them", which shares three words with the retired "and the fiddle starts confessing" and would have
  been audible — the opening verb of this line is effectively spent too.
- Example: the-bell-knows-my-name/only-bark-at-strangers
- Logged at catalog size 158.

### The chorus question left unaddressed — the name withheld until verse 2
- Bell's direct-question requirement met without naming the addressee in the chorus at all, so the
  question is ambiguous on first hearing and unmistakable on the second. Adopted because
  "[Name] — [question]" had closed the chorus of three consecutive Bell songs (the-bloom-i-cut,
  born-in-a-stable and this one's first draft) and was becoming the band's default shape.
- Example: "were you counting on that, or did it just work out?" — the-bell-knows-my-name/only-bark-at-strangers
- Logged at catalog size 158.

### "prop the door, pull the tab, mind the flex, carry it on" — deferred-defect consumption-imperative hook opener
- Laundry's imperative-opener slot filled with the small domestic accommodations a household makes
  around things that no longer work, closing on the maintenance-log phrase for leaving a fault
  unfixed.
- Example: laundry/it-does-that
- Logged at catalog size 159.

### "it does that" — normalized-deviance mantra
- The three words a household says about a fault it has stopped seeing, chanted and worn to noise
  ("it does that / it does th— / (—at)"). The band's banal-phrase-to-mantra move applied to the exact
  sentence by which a deviation becomes the standard.
- Example: laundry/it-does-that
- Logged at catalog size 159.

### "and one kit stops being a fault and starts being the arrangement" — mechanical-collapse pre-hook line
- A twelfth distinct phrasing for the pre-hook's textural build, after fold/buckle,
  stutter-catch-click, second-kit-drops-out, kick-a-half-beat-late, hi-hat-splits-in-two,
  snare-stuck-on-one-millisecond, toms-roll-under-the-couch, both-kits-sag,
  accept-the-update-mid-bar, take-the-line-speed and drop-a-point-a-bar. This one states the song's
  whole thesis as a drum instruction: nothing breaks, the broken thing is simply reclassified.
  Invent a fresh one again next time.
- Example: laundry/it-does-that
- Logged at catalog size 159.

### "what's the plan if it goes at night — the plan is the window" — question-with-no-addressee, self-answered and useless
- The slot filled with a safety question he answers himself, correctly, and does nothing about.
  Distinct from laundry/good-body-every-night's question answered by the sales script — that answer
  came from somebody else's patter; this one is his own, accurate, and worthless. After the
  unfinished measurement, the trailing passive appeal, the completed-and-unanswered question, the
  number read out and the question aimed at an earlier self.
- Example: laundry/it-does-that
- Logged at catalog size 159.

### "just use the shared one." — quoted-instruction hook opener
- Guessed's quoted-instruction slot filled with the sentence by which an office normalises a
  deviation, offered to her once as a helpful tip and now in her own mouth. After "be nice about
  it", "don't make it a thing", "you knew what it was", "you've got time", "act like it's news",
  "let it lie", "don't correct a compliment", "focus on the story", "come back to us", "be happy for
  her", "say it and stop", "don't push it" and "don't bring it up".
- Example: guessed/the-only-name-in-it
- Logged at catalog size 160.

### "and whose name is on it." → "and it's mine." — the question she already knows the answer to, answered in the final hook
- The slot filled as an elliptical possessive question, and then — for the first time in the
  catalogue — actually answered on the last pass, which is also the one-thing-changes ending. The
  device normally leaves the question hanging; here the answer is what makes it worse. After the
  retired wh-inverted skeleton, the yes/no shape, the either/or shape, the elliptical quantity, the
  belief-about-others shape and the aimed-at-the-outcome shape.
- Example: guessed/the-only-name-in-it
- Logged at catalog size 160.

### "it was a breach in two thousand and twelve, a workaround by fifteen, and by the time I got here it was just how we do it" — reclassification-timeline accusatory parallel
- Purple Dog's accusatory-parallel slot filled with a fresh grammatical shape after the retired
  where/should construction and the spent "you trust the log, not the room" two-beat: the same
  practice named three times across a decade, each name softer than the last, so the wrong is
  visible only as a sequence. The slot is mandatory and no filling recurs.
- Example: purple-dog/laminated
- Logged at catalog size 161.

### "calm down, log it, park it, take it offline" — corporate stacked-imperative chorus opener
- Purple Dog's stacked-imperative slot filled with meeting-room deflections rather than clinical
  ones, after "sit down, shut up, take your pills, act glad". Every command is a way of not
  addressing something while appearing to.
- Example: purple-dog/laminated
- Logged at catalog size 161.

### "HE'S DIFFICULT" → "WE'RE DIFFICULT" — contradicting gang shout-back and its communal flip
- The crowd overrules his protest with the institution's own word for a person who notices, then
  claims it in the final chorus. "Difficult" chosen because it is the actual verdict such rooms
  return, and because it is unfalsifiable — objecting to it proves it.
- Example: purple-dog/laminated
- Logged at catalog size 161.

### "We'll call that acceptable. / That's the new baseline." — reclassification chant hook
- Girlboss's hook slot filled with the two sentences that perform a normalization of deviance out
  loud, in the room, with authority. Fresh mechanism after the quoted critic, the tasting note, the
  listing language, the bar call, the labour tally, the renovated idiom, the invitation instruction,
  the betting-window pair, the counter patter, the negotiating position, the disambiguation, the
  power asymmetry, the creed-with-one-item-wrong and the instruction both jobs require.
- Example: girlboss/the-new-baseline
- Logged at catalog size 162.

### "They teach that module as a warning. I have taken it as a method."
- The unearned moral as a case study repurposed: the textbook example of institutional failure
  received as professional training in how to do it deliberately. A twelfth flavour after the trade
  rule quoted straight, the household lore, the management wisdom, the claimed authorship of an
  effect, the corrected proverb, the mentorship handed down, the authored policy, the itemisation of
  what was really bought, the confidentiality assurance, the moral misread as modesty and the
  curriculum fact.
- Example: girlboss/the-new-baseline
- Logged at catalog size 162.

### "the horses can't cry. If they could, they would. / I can, and I haven't" — capacity-comparison thesis couplet
- The Bell Knows My Name's emotional-thesis slot filled with a fresh grammatical shape after the
  retired where/should, the reciprocal-trade couplet, the kept-ledger-against-unkept-ledger couplet,
  the capability-against-non-entitlement couplet, the prophecy-granted-then-redirected couplet and
  the rule-and-its-fatal-instance couplet: grief attributed to animals who lack the equipment for it,
  set against the narrator who has the equipment and hasn't used it. No filling of this slot recurs.
- Example: the-bell-knows-my-name/they-went-up-quiet
- Logged at catalog size 163.

### "load them slow, load them quiet, keep your hand where they can see it" — band-instruction chorus opener
- The imperative-to-the-players slot filled with the handling instructions for walking an animal onto
  a lorry, which are also instructions for not being noticed doing it. After "play it quick, play it
  broken", "dig it slow, dig it holy", "cut it low, cut it kind", "walk him out, walk him sound",
  "sing it thin, sing it hungry" and "keep it low, keep it listening".
- Example: the-bell-knows-my-name/they-went-up-quiet
- Logged at catalog size 163.

### "and the fiddle takes it off me / because somebody has to hold it" — pre-chorus violin-personification line
- A ninth distinct phrasing for the "violin says what the mouth can't" beat, after confessing,
  remembers, stops its weeping, the strings going quiet, keeping the spent notes, coming when called,
  holding the swan note and joining in with them. This one has the instrument relieve him of a
  feeling as a practical favour rather than express one. Invent a fresh tie-in again next time.
- Example: the-bell-knows-my-name/they-went-up-quiet
- Logged at catalog size 163.

### "give a bird a word and you would never hear it sing again. / I have had the word for thirty years, and you have had the song." — hypothetical-then-inverted-arrangement thesis couplet
- The Bell Knows My Name's emotional-thesis slot filled with a fresh grammatical shape after the
  retired where/should, the reciprocal-trade couplet, the kept-ledger-against-unkept-ledger couplet,
  the capability-against-non-entitlement couplet, the prophecy-granted-then-redirected couplet, the
  rule-and-its-fatal-instance couplet and the capacity-comparison couplet: a hypothetical about
  animals, then the narrator's own version of the same bargain, already running for decades. No
  filling of this slot recurs.
- Example: the-bell-knows-my-name/so-i-sing-it
- Logged at catalog size 164.

### "take it high, take it wordless" — band-instruction chorus opener
- The imperative-to-the-players slot filled with an instruction to keep the music above language,
  which is the song's entire argument. After "play it quick, play it broken", "dig it slow, dig it
  holy", "cut it low, cut it kind", "walk him out, walk him sound", "sing it thin, sing it hungry",
  "keep it low, keep it listening" and "load them slow, load them quiet".
- Example: the-bell-knows-my-name/so-i-sing-it
- Logged at catalog size 164.

### "and the fiddle says the whole of it / and nobody asks it to explain" — pre-chorus violin-personification line
- A tenth distinct phrasing for the "violin says what the mouth can't" beat, after confessing,
  remembers, stops its weeping, the strings going quiet, keeping the spent notes, coming when called,
  holding the swan note, joining in with them and taking it off him. This one names the exemption
  music enjoys — it can state anything and is never required to account for it. Invent a fresh
  tie-in again next time.
- Example: the-bell-knows-my-name/so-i-sing-it
- Logged at catalog size 164.

### "there are eleven wires on me — four are yours, seven are the building's, and not one of them goes anywhere near what's actually wrong" — inventory-ending-in-negation accusatory parallel
- Purple Dog's accusatory-parallel slot filled with a fresh grammatical shape after the retired
  where/should construction, the spent "you trust the log, not the room" two-beat and the
  reclassification timeline (purple-dog/laminated): a precise count, apportioned between parties,
  cancelled by a closing clause that says none of it touches the point. The final chorus swaps the
  last line for a worse one ("every one of them goes back to a desk where nobody is sitting").
- Example: purple-dog/isnt-plugged-into-anything
- Logged at catalog size 165.

### "lie back, breathe in, wait your turn, be patient" — ward stacked-imperative chorus opener
- Purple Dog's stacked-imperative slot filled with bedside instructions, closing on the word that is
  simultaneously a virtue demanded of him and the category he has been reduced to. After "sit down,
  shut up, take your pills, act glad" and "calm down, log it, park it, take it offline".
- Example: purple-dog/isnt-plugged-into-anything
- Logged at catalog size 165.

### "THAT'S NORMAL FOR YOU" → "THAT'S NORMAL FOR US" — gang shout-back voicing the institution, then claiming it
- A fresh shout-back mechanism after the label-contradiction shape ("HE'S NOT FINE", "HE'S
  DIFFICULT"): the crowd does not name him, it speaks in the institution's voice and dismisses him
  with the sentence wards actually use — then the flip turns the same words into a collective
  diagnosis of the place rather than of the people in it.
- Example: purple-dog/isnt-plugged-into-anything
- Logged at catalog size 165.

### "make good." — quoted-instruction hook opener
- Guessed's quoted-instruction slot filled with the tenancy-agreement term for restoring a property
  to the condition it was let in — an obligation she has internalised and is unusually good at. After
  "be nice about it", "don't make it a thing", "you knew what it was", "you've got time", "act like
  it's news", "let it lie", "don't correct a compliment", "focus on the story", "come back to us",
  "be happy for her", "say it and stop", "don't push it", "don't bring it up" and "just use the
  shared one".
- Example: guessed/two-coats
- Logged at catalog size 166.

### "who's in there now." → "and I hope they put things up." — the question she already knows the answer to, resolved into a wish
- The slot filled as a flat question about the next occupant, and the final hook abandons the
  question entirely for a small generous hope. The device usually leaves the question hanging or
  answers it worse; this one is the first time the substitution is *kind*, which is the whole ending.
  After the retired wh-inverted skeleton, the yes/no shape, the either/or shape, the elliptical
  quantity, the belief-about-others shape, the aimed-at-the-outcome shape and the possessive answered
  in the final hook.
- Example: guessed/two-coats
- Logged at catalog size 166.

### "Say it was the theme." — permission-imperative chorus opener
- Penny Rich's permission-imperative slot filled by handing the crowd the wrong *variable* rather
  than the wrong verdict: they may credit the decoration for a record night, because the decoration
  is what the committee spent an hour and ten minutes on. After "say I settled".
- Example: penny-rich/say-it-was-the-theme
- Logged at catalog size 167.

### "It was the garlands. It was definitely the garlands." → "It was always the garlands."
- The crowd's wrong version, sung with total conviction and never corrected, with the final chorus
  moving one word — *definitely* to *always* — so the sincerity deepens rather than cracks. The
  ending is the crowd getting more certain, not less.
- Example: penny-rich/say-it-was-the-theme
- Logged at catalog size 167.

### "Let him sign it." / "Call it a knack." / "Say the sky told me." / "Say the man did it." / "Say she gets it from him." / "Say I like a bargain." — six permission-imperative chorus openers
- Penny Rich's permission-imperative slot filled six times in one batch, each handing the crowd a
  different wrong explanation: the husband, an innate gift, the weather, a hired professional,
  the other parent's genes, and a personality trait. After "say I settled" and "say it was the
  theme". Logged together so the *shape* is visible — every one of them gives away the credit
  cheerfully and none of them is a confession.
- Example: penny-rich/let-him-sign-it, penny-rich/call-it-a-knack, penny-rich/say-the-sky-told-me,
  penny-rich/say-the-man-did-it, penny-rich/her-fathers-daughter, penny-rich/four-pound-a-year
- Logged at catalog size 173.

### The crowd's wrong version deepened by one word in the final chorus
- Penny Rich's shout-back device across the batch: the crowd's incorrect verdict returns with a
  single word changed so their conviction *grows* — "very good with money" becomes "was always going
  to be", "she's got a way with him" becomes "she was born with", "she's her father's daughter"
  becomes "she'll bring hers up her father's daughter", "she does love a bargain" becomes "she'll
  die loving a bargain". The ending is the wrong story becoming permanent and inheritable, sung
  affectionately. Never corrected.
- Example: penny-rich/her-fathers-daughter (the furthest-travelled instance)
- Logged at catalog size 173.

### "you're not throwing away a cable. You're throwing away a Thursday morning in three years" — present-act-against-future-consequence accusatory parallel
- Purple Dog's accusatory-parallel slot filled with a fresh grammatical shape after the retired
  where/should construction, the spent "you trust the log, not the room" two-beat, the
  reclassification timeline (purple-dog/laminated) and the inventory-ending-in-negation
  (purple-dog/isnt-plugged-into-anything): a small present action set against the specific future
  morning it ruins, with the tense doing all the accusing. The final chorus moves it from "I" to
  "we" without changing anything else.
- Example: purple-dog/the-same-drawer
- Logged at catalog size 174.

### "bin it, box it, have a clear-out, be reasonable" — domestic stacked-imperative chorus opener
- Purple Dog's stacked-imperative slot filled with tidying instructions, closing on the demand that
  makes disagreement itself the offence. After "sit down, shut up, take your pills, act glad",
  "calm down, log it, park it, take it offline" and "lie back, breathe in, wait your turn, be patient".
- Example: purple-dog/the-same-drawer
- Logged at catalog size 174.

### "YOU'LL NEVER NEED IT" → "WE'LL ALL NEED IT" — gang shout-back as a prediction, flipped to a shared certainty
- A third shout-back mechanism after the label-contradiction ("HE'S NOT FINE", "HE'S DIFFICULT") and
  the institution's-voice dismissal ("THAT'S NORMAL FOR YOU"): here the crowd contradicts his
  *forecast* rather than his character, and the flip turns a denial into a room full of people who
  have all kept a cable for a device they no longer own.
- Example: purple-dog/the-same-drawer
- Logged at catalog size 174.

### "grind it, pull it, drink it hot, stay under" — maintenance-dosing consumption-imperative hook opener
- Laundry's imperative-opener slot filled with coffee-making verbs closing on an instruction that
  inverts the expected one: not stay awake, stay *under*. The whole gravity well is in the last two
  words.
- Example: laundry/level
- Logged at catalog size 175.

### "level" — target-state mantra
- One word, chanted and worn to noise ("level / lev— / (—el)"). Not awake and not asleep but held at
  a chosen depth, which is what the dosing is for. Distinct from the band's other degraded phrases in
  that it names a condition he is maintaining rather than an instruction he is obeying.
- Example: laundry/level
- Logged at catalog size 175.

### "and both kits get the shake and neither one can hold a straight line" — mechanical-collapse pre-hook line
- A thirteenth distinct phrasing for the pre-hook's textural build, after fold/buckle,
  stutter-catch-click, second-kit-drops-out, kick-a-half-beat-late, hi-hat-splits-in-two,
  snare-stuck-on-one-millisecond, toms-roll-under-the-couch, both-kits-sag, accept-the-update-mid-bar,
  take-the-line-speed, drop-a-point-a-bar and stops-being-a-fault. This one is a tremor rather than a
  failure — the kit has the same shake he has. Invent a fresh one again next time.
- Example: laundry/level
- Logged at catalog size 175.

### "how long has that been in the room — no. No, leave it." — question-with-no-addressee, asked and then declined
- The slot filled with a question he starts and immediately refuses to pursue, so the answer is
  available and deliberately not collected. After the unfinished measurement, the trailing passive
  appeal, the question answered by the sales script, the completed-and-unanswered question, the number
  read out, the question aimed at an earlier self and the self-answered useless one.
- Example: laundry/level
- Logged at catalog size 175.

### "the bins ... six" as laundry's early-morning fixed point — PERMANENT
- laundry/mind-the-white opens on "Bins out after six, which is after six, which is the thing about
  six" — a line the user singled out as one of the best in the catalogue, which makes any reuse of
  the bins-and-six pairing an audible repeat rather than shared furniture. Flagged by the user
  2026-08-22 after laundry/level was drafted with "the bins go out at ten past six" as its fixed
  point. Retired permanently: the *device* (a mundane recurring event as the only fixed point in a
  formless day) stays available and is a good one — the bins, and that hour, do not.
- laundry/level was revised to a streetlight that goes off at twenty to seven "now it's autumn",
  which is better anyway: the one fixed point in the song turns out not to be fixed.
- Example: laundry/mind-the-white (the use that stands)
- Logged at catalog size 175.

### A build made entirely of filenames — Disassembler's dense system-text list
- The band's "too many true things too fast" rule in its first proper outing: nineteen filenames
  read flat over a rolling break, each one a real artefact of the same document, escalating through
  final, FINAL, FINAL_FINAL, USE_THIS, USE_THIS_v2, initials, initials-plus-initials, a lock file
  and two New Folders. Nothing is invented and nothing is an image — the comedy and the dread are
  both entirely in the volume and the order.
- Example: disassembler/use-this-one
- Logged at catalog size 177.

### "USE THIS ONE" / "THIS ONE NEW NEW" — shouted-anchor drop
- Disassembler's drop filled with the instruction every one of those filenames was trying to give,
  shouted by a single stacked voice rather than a crowd (the structural fence against laundry).
  Two to four words, repeated, carrying no new information on the second drop.
- Example: disassembler/use-this-one
- Logged at catalog size 177.

### "PASSED" / "STILL PASSED" — shouted-anchor drop built on a machine's own verdict
- Disassembler's drop filled with the word a failing disk uses about itself. The SMART
  self-assessment returns PASSED while the reallocated sector count climbs through the verse, so the
  anchor is simultaneously true, official and worthless. Second use of the band's stacked-single-voice
  drop after "USE THIS ONE" — no crowd, per the laundry fence.
- Example: disassembler/still-passed
- Logged at catalog size 178.

### The build as a machine reporting its own deterioration in fields
- Disassembler's dense system-text rule filled with SMART attributes and kernel messages read flat:
  reallocated sector count rising through three values, current pending sector, offline
  uncorrectable, power on hours, read and seek error rates, temperature, a critical medium error and
  an I/O error with its sector. Every line is a real field and the drive is describing its own death
  accurately, calmly, and without drawing a conclusion. Distinct from the filename list in
  disassembler/use-this-one — that was a human's artefacts, this is the machine's own account.
- Example: disassembler/still-passed
- Logged at catalog size 178.

### The build as configure output — a machine asking whether reality is sane
- Disassembler's dense system-text rule filled entirely with prose rather than counters, per the
  band's own alternation rule: eleven lines of autoconf checking whether the compiler works, whether
  we are cross compiling, whether make sets MAKE, and — the one that carries the whole song —
  *checking whether build environment is sane... yes*. A machine interrogating the universe and
  answering itself, in complete sentences, none of which is an alarm.
- Example: disassembler/not-unix
- Logged at catalog size 179.

### "NOT UNIX" / "STILL NOT UNIX" — shouted-anchor drop on a definition that will not terminate
- Disassembler's drop filled with the back half of a recursive acronym, so the anchor is a
  definition endlessly deferring to itself. Set up in the build by a run of siblings — WINE is not
  an emulator, LAME ain't an MP3 encoder, PHP: hypertext preprocessor — so by the drop the joke is
  established as an entire naming culture rather than one gag.
- Example: disassembler/not-unix
- Logged at catalog size 179.

### The build as one list ranked two ways — Disassembler's argument song
- The band's dense system-text rule filled with a design document rather than machine output:
  simplicity, correctness, consistency, completeness, stated once as the MIT school ranks them and
  again as the New Jersey school does, so the same four words return in a different order with the
  deflating clauses attached ("it is slightly better to be simple than correct"). The structure is
  the argument — nothing has to be explained because the repetition does it — and the only
  connective tissue in the whole track is two fragments: "the same four words / a different order".
- Example: disassembler/worse-is-better
- Logged at catalog size 181.

### "WORSE IS BETTER" / "IT SPREADS" — shouted-anchor drop carrying a thesis rather than a state
- Disassembler's drop filled with an argument's conclusion instead of a system's output — the first
  of the band's anchors that is a claim about the world rather than a reading, a filename or a
  verdict. Paired with the mechanism ("IT SPREADS") so the drop states the position and its reason
  in six words.
- Example: disassembler/worse-is-better
- Logged at catalog size 181.

### The build as a fault log downgrading itself
- Disassembler's dense system-text rule filled with an operational history of decay in which every
  entry is a reclassification rather than a repair: the mending apparatus repaired, then requiring
  mending, then its committee dissolved; complaints noted, then noted and filed, then no longer
  noted; a defect in the music becoming a defect in your ear; stale air you will get used to.
  Nothing in the list is false and nothing in it is a fix. Distinct from
  disassembler/still-passed's telemetry, which reports a machine's condition accurately — this one
  is an institution adjusting what counts as acceptable, which is laundry/it-does-that's subject
  arriving in a completely different register.
- Example: disassembler/the-machine-stops
- Logged at catalog size 182.

### The build as an inventory of what came out — the deletion song
- Disassembler's dense system-text rule turned to subtraction: a diffstat, then the things the
  thousand lines actually were — a flag nobody set, a shim for a platform that no longer exists, a
  retry loop that never fired, then the escalation that is the real comedy of dead abstraction (the
  second implementation, the abstraction over the two, the interface for the abstraction, the mock
  for the interface, the test for the mock, the documentation for the test) — closing on the
  evidence that none of it mattered: no references, no callers, coverage unchanged, the tests all
  still pass. The band's first song in which nothing is wrong.
- Example: disassembler/no-callers
- Logged at catalog size 183.

### The second drop that changes one word — Disassembler's first altered repeat
- The band's spec says the second drop carries no new information. Broken deliberately and once:
  "CLASSIFIED" becomes "DELETED", because the source's entire plot turns on that substitution and
  the anchor is the only place it can land. Logged so it stays an exception earned by a specific
  song rather than becoming the band's ending — the default remains a second drop that adds nothing.
- Example: disassembler/directive-four
- Logged at catalog size 184.

### The build as a rule set with a hole in it
- Disassembler's dense system-text rule filled with an ordered list that stops working at one entry:
  three directives read plainly, then a fourth that returns only its own classification, then the
  consequences of having asked (weapon disengaged, motor function suspended, system shutdown in
  progress), then the whole list again with the hole still in it. The withheld item is quoted more
  often than any of the readable ones.
- Example: disassembler/directive-four
- Logged at catalog size 184.

### Purpose stated once, behaviour for the rest — the POSIWID structure
- Disassembler's dense system-text rule arranged so the claim appears a single time, in the intro,
  and everything after it is what the thing actually does: pages a person at four in the morning,
  restarts itself, opens a ticket that closes itself after thirty days, produces a report nobody
  reads, holds two hundred rules of which four have ever fired, costs eight hundred pounds a month,
  and has prevented nothing anybody can name. The gap is never pointed at. Deliberately not the
  two-lists shape of disassembler/worse-is-better, which states both sides — here one side is said
  once and then abandoned.
- Example: disassembler/as-designed
- Logged at catalog size 185.

### "AS DESIGNED" / "WORKING AS INTENDED" — shouted-anchor drop as a resolution status
- Disassembler's drop filled with the two strings a bug tracker offers for closing something that
  is not going to be fixed. Against Stafford Beer's principle they stop being defences and become
  confirmations: whatever it does, it does as designed. Distinct from
  disassembler/worse-is-better's anchor, which asserts a thesis — this one is a field value.
- Example: disassembler/as-designed
- Logged at catalog size 185.

### The build as documented praise, none of it the narrator's
- Disassembler's dense system-text rule filled with other people's published admiration — the
  greatest single language ever designed, worth learning for the enlightenment experience, the only
  beautiful one, it had garbage collection and closures and the REPL and macros first, any
  sufficiently complicated program contains a slow bug-ridden implementation of half of it. Every
  claim is real, attributable and unrefuted, and the narrator says none of it himself, which keeps
  the entire song third person until the breakdown. The turn is delivered as two job-board figures
  rather than an argument: "open positions: eleven / open positions in this county: zero".
- Example: disassembler/admired-not-used
- Logged at catalog size 186.

### "ADMIRED" / "NOT USED" — shouted-anchor drop as two field values
- Disassembler's drop compressing the whole subject into a pair of statuses that do not contradict
  each other. Neither is a complaint and neither is a defence; together they are the finding.
  After the reading (USE THIS ONE), the verdict (STILL PASSED), the recursive definition (NOT UNIX),
  the thesis (WORSE IS BETTER), the resolution status (AS DESIGNED) and the classification
  (CLASSIFIED).
- Example: disassembler/admired-not-used
- Logged at catalog size 186.

### The build as a small question and a large answer — the amplification structure
- Disassembler's dense system-text rule arranged around a ratio: request in bytes, response in
  bytes, amplification factor, then the same three figures for two more protocols, then the line
  that reframes all of it — "all of these services are working correctly / all of these services
  have always worked correctly". The vulnerability is politeness. Nothing in the list is a fault and
  nothing is misconfigured; the numbers simply are what they are.
- Example: disassembler/ask-it-the-time
- Logged at catalog size 187.

### "ASK IT THE TIME" / "IT ANSWERS EVERYBODY" — shouted-anchor drop as an instruction and its consequence
- Disassembler's drop pairing the attack with the service's own purpose, which are the same act. The
  first anchor in the band that is an imperative — after the reading, the verdict, the recursive
  definition, the thesis, the resolution status, the classification and the two field values.
- Example: disassembler/ask-it-the-time
- Logged at catalog size 187.

### The build as strata — one comment thread, years apart, different hands
- Disassembler's dense system-text rule arranged as archaeology rather than argument: the same
  branch commented by successive people over years, the certainty eroding line by line from "this
  can never happen" through "seriously, this cannot happen" and "if you are reading this, something
  has gone very wrong" into "I have seen this happen", "it happens about once a month", "it happens
  more in December" and finally "leave it". Nobody is wrong at the time they write; the belief simply
  wears out. Distinct from disassembler/the-machine-stops's fault log, which is one institution
  downgrading its own standards — this is individuals leaving notes for each other, and it travels
  the opposite way, from denial into acceptance.
- Example: disassembler/leave-it
- Logged at catalog size 188.

### "UNREACHABLE" / "LEAVE IT" — shouted-anchor drop pairing a compiler string with a maintenance decision
- Disassembler's drop setting the language's own word for impossible against the human instruction
  that supersedes it. The first anchor built from two registers at once — one emitted, one typed.
- Example: disassembler/leave-it
- Logged at catalog size 188.

### The build as a screen with no words on it
- Disassembler's dense system-text rule filled with pictograms described rather than named: three
  horizontal lines, three vertical dots, three horizontal dots, a magnifying glass, a gear, a bell,
  a house, a heart, a star, a flag, a bookmark. Describing them instead of using their labels is the
  entire argument, and it is never stated — the listener does the work of realising that a list of
  shapes conveys nothing. Turns on the observation that the heart, the star and the bookmark all
  mean save it for later and do not mean the same later.
- Example: disassembler/hover-to-find-out
- Logged at catalog size 189.

### "HOVER TO FIND OUT" / "IT IS A FLOPPY DISK" — shouted-anchor drop as an instruction and a translation
- Disassembler's drop pairing the interface's own remedy for illegibility with the answer it is
  withholding. The instruction is real UI behaviour and the translation is the thing a tooltip would
  have said, so the drop performs the failure and the fix at once.
- Example: disassembler/hover-to-find-out
- Logged at catalog size 189.

### The build as a vocabulary of fossils
- Disassembler's dense system-text rule filled with interface words whose referents are gone, each
  followed by what it used to be: paste was glue, the clipboard was a board with a clip on it, the
  dial was a wheel that came back on its own, scroll was a roll of papyrus, the wastebasket is not a
  bin but a basket for waste paper. Distinct from disassembler/hover-to-find-out, which describes
  pictograms and refuses to name them — that song is about images carrying no meaning, this one is
  about words carrying a meaning nobody can still see.
- Example: disassembler/carbon-copy
- Logged at catalog size 190.

### "CARBON COPY" / "BLIND CARBON COPY" — shouted-anchor drop as a dead technology still in daily use
- Disassembler's drop built from two email header fields named after a duplication method the entire
  workforce has never touched. Nothing is quoted or explained; the words are simply shouted until
  the listener hears what they say.
- Example: disassembler/carbon-copy
- Logged at catalog size 190.

### The build as a device performing an absent mechanism
- Disassembler's dense system-text rule advanced one step past the fossil vocabulary of
  disassembler/carbon-copy and the pictograms of disassembler/hover-to-find-out: here the interface
  does not merely depict a dead object, it *enacts* one. There is no mirror, no reflex, no shutter,
  no film, no aperture ring — and the shutter sound is a recording, composed by somebody, which in
  some countries cannot be switched off. Closes on faults reintroduced as features: the grain is
  applied afterwards, the light leak is applied afterwards, the light leak was a fault.
- Example: disassembler/there-is-no-shutter
- Logged at catalog size 191.

### "THERE IS NO SHUTTER" / "PLAY THE SOUND ANYWAY" — shouted-anchor drop as a denial and an instruction
- Disassembler's drop stating an absence and then commanding the performance of it regardless. The
  two lines do not argue with each other; the second is simply what happens next.
- Example: disassembler/there-is-no-shutter
- Logged at catalog size 191.

### The build as unanswered questions
- Disassembler's dense system-text rule inverted into interrogatives — the band's first track built
  from questions rather than statements. Every one is reasonable, literal and unanswerable because
  the thing it asks about is a metaphor: what turns when you scroll, what opens when you open a
  window, where does the sound go when you mute it, who has the original, where is the cloud. The
  fourth movement of the fossil sequence and the only one told from outside the knowledge — dead
  words (carbon-copy), dead pictures (hover-to-find-out), a dead mechanism performed
  (there-is-no-shutter), and here the questions of somebody who never saw any of the referents.
- Example: disassembler/where-does-it-go
- Logged at catalog size 192.

### "WHERE DO YOU PUT THE FILM" / "NOBODY WROTE THAT DOWN" — shouted-anchor drop as a question and its non-answer
- Disassembler's drop pairing an innocent question with the reason it cannot be answered: the
  explanation was never recorded anywhere, because at the time everybody knew.
- Example: disassembler/where-does-it-go
- Logged at catalog size 192.

### The build as a name wrong at every layer
- Disassembler's dense system-text rule applied to a single object's nomenclature, peeled one layer
  at a time: telephone means distant sound and the sound was carried on a wire, there is no wire;
  wireless, and the traffic enters a cable at the tower and most of the journey is a cable; cell,
  and the cell is a hexagon drawn on a planning map; dial, and there is no dial; hang up, and the
  hook was a hook on the side that went down. Then the radio vocabulary that is actually accurate —
  band, channel, frequency, power output, transmit, receive — and the line that turns it:
  "it transmits its position continuously". Fifth movement of the fossil sequence and the deepest:
  not the icon, not the word, but the category.
- Example: disassembler/it-is-a-radio
- Logged at catalog size 193.

### "IT IS A RADIO" / "IT WAS ALWAYS A RADIO" — shouted-anchor drop as a reclassification
- Disassembler's drop stating what the object actually is and then removing any suggestion that it
  changed. Nothing was ever converted; the name was wrong from the beginning.
- Example: disassembler/it-is-a-radio
- Logged at catalog size 193.

### The build as the assistant's own advice, quoted as system text
- Disassembler's dense system-text rule turned on the toolchain the songs are written with: git
  status output interleaved with an AI's prompting — shall I commit that, that is worth committing,
  the uncommitted pile is getting large, I would split it three ways so each experiment stays
  legible, co-authored-by, nothing has been pushed yet. The advice qualifies as system text under
  the band's own rule (a person did not say it aloud), which is the joke and also the finding: the
  nagging is now part of the tooling, indistinguishable in register from the tooling's output.
- Example: disassembler/commit-it
- Logged at catalog size 194.

### "COMMIT IT" / "WORKING TREE CLEAN" — shouted-anchor drop as the instruction and its reward
- Disassembler's drop pairing what the loop asks for with what it gives back. Neither line is a
  consequence; the reward for compliance is a status message saying there is nothing left to do.
- Example: disassembler/commit-it
- Logged at catalog size 194.

### The build as consent-framework boilerplate, quoted verbatim
- Disassembler's dense system-text rule filled with the purpose strings from a cookie consent dialog
  — store and or access information on a device, create profiles for personalised advertising, use
  profiles to select personalised content, measure advertising performance, link different devices —
  followed by the counts that make them meaningless (partners in the hundreds, most of them
  operating on legitimate interest, objectionable only one at a time). Nothing is paraphrased.
  Somebody drafted every line of it, and nobody reads any of it, which is the entire mechanism.
- Example: disassembler/trusted-third-parties
- Logged at catalog size 195.

### "TRUSTED THIRD PARTIES" / "LEGITIMATE INTEREST" — shouted-anchor drop as two undefined terms of art
- Disassembler's drop built from a phrase with no definition and a legal basis that shifts the
  burden onto the person it applies to. Both are real, both are load-bearing, and neither survives
  being said out loud twice.
- Example: disassembler/trusted-third-parties
- Logged at catalog size 195.

### The build as a name disproved word by word
- Disassembler's dense system-text rule aimed at an acronym rather than a metaphor: the connectors
  that are not compatible, the cables that are not interchangeable, the one that charges and will
  not carry data, the one that carries data and will not charge — "you cannot tell by looking" — and
  then the topology, which was a bus once with a shared line and a controller and is now a tiered
  star with hubs. Related to disassembler/it-is-a-radio, which finds the wrong *category* under a
  name; this one finds three wrong *words* in a single name, each false for a different reason.
- Example: disassembler/not-a-bus
- Logged at catalog size 196.

### "NOT UNIVERSAL / NOT SERIAL / NOT A BUS" — three-line shouted-anchor drop
- Disassembler's first drop built from three refusals rather than two lines, taking the acronym
  apart in the order it was assembled, with the order shuffled on the second drop so no reading is
  privileged.
- Example: disassembler/not-a-bus
- Logged at catalog size 196.

### The build as a complete vocabulary spoken with two words of it
- Disassembler's dense system-text rule applied to a specification's full verb list, with the
  properties that make it coherent (safe, idempotent, not idempotent) read out in full before the
  usage collapses it: options tells you what is allowed and nobody asks options, trace is
  implemented and disabled nearly everywhere, put is specified and unused, delete is specified and
  not wired up, everyone uses post for everything. Adjacent to disassembler/admired-not-used and
  disassembler/worse-is-better and distinct from both — this is not admiration and not a design
  argument, it is a language being spoken with a fraction of its words while the rest stay
  implemented and available.
- Example: disassembler/get-and-post
- Logged at catalog size 197.

### "GET AND POST" / "THE REST ARE THERE" — shouted-anchor drop on what survives and what waits
- Disassembler's drop naming the two verbs in use and then declining to say the unused ones are
  gone. They are present in every server, specified, maintained and untouched — which is worse than
  deprecation.
- Example: disassembler/get-and-post
- Logged at catalog size 197.

### The build as a protocol transcript run in the wrong tool
- Disassembler's dense system-text rule filled with one side of an SMTP conversation — two twenty
  service ready, two fifty sender ok, three fifty-four start mail input end with a dot on a line by
  itself, two twenty-one closing connection — spliced with the implementation's vocabulary: gawk's
  network special file, begin, pattern, end, dollar zero, N R, print. Neither half is explained and
  the join is never mentioned. Sourced from the owner having actually built this and run it in
  production.
- **Provenance worth keeping.** gawk's `/inet/tcp/...` syntax is Plan 9's *everything is a file*
  smuggled into a text-processing tool — the gawk maintainer is on the 9fans list and took the idea
  from there. The owner knew that lineage at the time, which is why he trusted the feature in
  production: it was not an obscure trick he stumbled on, it was a well-understood idea wearing a
  disguise. That also quietly rebuts disassembler/the-front-fell-off, which reads Plan 9's founding
  claims out as the doctrine of a system that lost. The system lost; the ideas got out. If a future
  song wants that observation, it is unwritten and it is the strongest thing in this corner of the
  catalogue.
- Example: disassembler/in-gawk
- Logged at catalog size 198.

### "TWO FIFTY OK" / "IN GAWK" — shouted-anchor drop as a success code and its indictment
- Disassembler's drop pairing the response a working mail server returns over and over with the two
  words that make it absurd. The success is real; the second line is the only commentary in the song.
- Example: disassembler/in-gawk
- Logged at catalog size 198.

### The build as an inventory of ideas that escaped a dead system
- Disassembler's dense system-text rule turned to inheritance: /proc and the process as a file,
  per-process namespaces and the containers built from them, union mounts, rfork becoming clone, 9P
  shipping inside Windows Subsystem for Linux, and UTF-8 — designed for Plan 9, by two of the same
  people, on a placemat in a New Jersey diner. Closes on the line that makes it a song rather than a
  list: "none of this is credited on the screen". The direct answer to
  disassembler/the-front-fell-off, and written third: that one is allegiance to a system that lost,
  this one is the discovery that its ideas did not.
- Example: disassembler/poorly-implemented
- Logged at catalog size 199.

### "POORLY IMPLEMENTED" / "IN EVERY ONE OF THEM" — shouted-anchor drop from a borrowed aphorism
- Disassembler's drop built from the Plan 9 variant of Greenspun's tenth rule, split so neither half
  is a complete sentence and the one-human-sentence rule stays intact. Sibling to
  disassembler/admired-not-used, which quotes the Lisp original in its build.
- Example: disassembler/poorly-implemented
- Logged at catalog size 199.

### The build as a league table nobody publishes
- Disassembler's dense system-text rule arranged as a corrected ranking: the most deployed kernel is
  Linux, not on servers, on handsets; the most deployed database engine is SQLite, not in data
  centres, in handsets and browsers and aircraft; a Java virtual machine on billions of SIM cards;
  BusyBox and Lua in the router; zlib in everything. Each entry states the wrong assumption before
  the right one, in three lines, and the section closes on the mechanism: "none of these won an
  argument / all of them shipped inside something else / nobody counted them at the time".
- Example: disassembler/count-the-handsets
- Logged at catalog size 200.

### "COUNT THE HANDSETS" / "NOT THE ARGUMENTS" — shouted-anchor drop as a method
- Disassembler's drop naming the measurement that produces the correct answer and the one that
  produces the popular one. Sibling to disassembler/as-designed's "AS DESIGNED", which is also about
  the difference between what is claimed and what is the case — that one measures behaviour against
  purpose, this one measures deployment against reputation.
- Example: disassembler/count-the-handsets
- Logged at catalog size 200.

### The build as an escalating inventory of doors
- Disassembler's dense system-text rule arranged as a climb: root, sudo, the break glass account
  whose emergency has not happened, a debug flag, a header that skips the check, a test account that
  still works in production, an allow list with one home address on it, a feature flag enabled for
  one user id, a branch that checks for one name — then the turn that reframes all of it, "the audit
  log does not cover the person who configures the audit log" — and finally the compiler that can be
  taught to insert it into the compiler, where it will not appear in the source. Every entry is
  somebody's deliberate decision and none of them is a fault.
- Example: disassembler/break-glass
- Logged at catalog size 201.

### "BREAK GLASS" / "FOR EMERGENCIES ONLY" — shouted-anchor drop as a control and its justification
- Disassembler's drop pairing the mechanism with the reason given for it, immediately after the
  build has established that the emergency never arrived. Neither line is disputed anywhere in the
  song.
- Example: disassembler/break-glass
- Logged at catalog size 201.

### The build as observability latency, itemised
- Disassembler's dense system-text rule turned on the instruments themselves: scrape interval,
  dashboard lag, samples taken before you looked, a percentile over a window that has already
  closed, an alert that fires after three consecutive failures and therefore a minute and a half
  late, time to detect, time to acknowledge, time to mitigate, and a post-mortem timeline
  reconstructed from things that were already recordings. Nothing is broken, nothing is misconfigured
  and no number is wrong — every figure quoted is the tool working as specified, and the sum of them
  is that the picture is always of a thing that has stopped.
- Example: disassembler/already-happened
- Logged at catalog size 202.

### "IT ALREADY HAPPENED" / "THIRTY SECONDS AGO" — shouted-anchor drop as a finding and its measurement
- Disassembler's drop stating the condition and then pinning it to a figure from the build, so the
  second line is evidence rather than emphasis.
- Example: disassembler/already-happened
- Logged at catalog size 202.

### The build as published axioms
- Disassembler's dense system-text rule filled with Gall's laws read flat: systems tend to oppose
  their own proper function, the system always kicks back, new systems generate new problems, a
  complex system that works evolved from a simple system that worked, complex systems usually
  operate in failure mode, malfunction may not be detectable for long periods, a system continues to
  do its thing regardless of need, systems attract systems people. Every line was already written by
  somebody as an aphorism, which makes them native system text under the band's rule and means the
  song does no arguing at all. Sibling to disassembler/worse-is-better (an essay) and
  disassembler/as-designed (a single cybernetic principle) — this one is a whole book's worth of
  them, and the closing pair is the owner's own compression of it.
- Example: disassembler/cannot-change-one-thing
- Logged at catalog size 203.

### "YOU CANNOT CHANGE ONE THING" / "YOU CANNOT CHANGE EVERYTHING" — shouted-anchor drop as a closed trap
- Disassembler's first drop built from two claims that are each true and jointly forbid action, with
  the order reversed on the second drop so neither is the conclusion. The build states them plainly
  before the drop and then adds the only commentary in the track: "both of those are true / they are
  true at the same time".
- Example: disassembler/cannot-change-one-thing
- Logged at catalog size 203.

### The build as a runaway loop, one correct step at a time
- Disassembler's dense system-text rule arranged as causation rather than inventory: the client
  waits, times out, retries; the retry arrives while the first is still running; the queue grows
  faster than it drains; the health check times out and marks the service unhealthy; traffic moves to
  others already at capacity; autoscaling responds to a metric autoscaling is causing. The section
  closes on the line that makes it a Disassembler song rather than an incident report — "every one of
  these is the correct behaviour". The band's fourth cybernetics subject after as-designed (purpose),
  already-happened (latency) and cannot-change-one-thing (immobility), and distinct from all three:
  this one is amplification.
- Example: disassembler/retry
- Logged at catalog size 204.

### "RETRY" / "BACK OFF" — shouted-anchor drop that enacts the loop it describes
- Disassembler's drop repeating the action that causes the failure, with the remedy stated once in
  the middle and then ignored on the way back round. The only anchor in the band that performs its
  own subject rather than naming it.
- Example: disassembler/retry
- Logged at catalog size 204.

### The build as a chain of fixes that closes into a circle
- Disassembler's dense system-text rule arranged as a stack read bottom to top, where every layer was
  the remedy for the one beneath it: the script fixed doing it by hand, cron fixed remembering to run
  the script, the wrapper fixed cron's environment, the config file fixed the wrapper's arguments,
  the templating fixed having too many config files, and onward through the generator, the linter,
  the pipeline, the cache, the invalidation tool, the runbook and the alert — closing on "somebody is
  on call for the alert / at four in the morning / **somebody is doing it by hand**", which is the
  first line of the song. Deliberately not the published-axiom device of
  disassembler/cannot-change-one-thing, which draws on the same source: that one quotes the laws,
  this one demonstrates one.
- Example: disassembler/that-was-the-fix
- Logged at catalog size 205.

### "THAT WAS THE FIX" / "FOR THE ONE BEFORE IT" — shouted-anchor drop as a receding justification
- Disassembler's drop stating that each thing was a solution and then pointing backwards rather than
  forwards, so the justification never terminates and no layer is ever defended on its own merits.
- Example: disassembler/that-was-the-fix
- Logged at catalog size 205.

### The two-movement build — what the probe does to the system, then what the system does to the probe
- Disassembler's dense system-text rule split across two labelled build sections, the second mirroring
  the first. Movement one is the observer effect in operations: the agent takes a share of the
  processor, the scrape keeps the process from idling, the health check holds the connection open,
  the profiler changes the timing so the race will not reproduce, and the logging added to find it
  slows it below the threshold — closing on "the bug is gone / the bug is not gone". Movement two is
  the owner's own addition and the better half: thresholds set from what the system does rather than
  what it should do, an exceptions list longer than the rules, a dashboard arranged around failures
  already had, a check rewritten to stop it firing at weekends, and "the probe has learned this
  system / the probe would not work on another one". Distinct from
  disassembler/worse-is-better's two rankings of one list — these are two different lists that
  rhyme.
- Example: disassembler/both-ways
- Logged at catalog size 206.

### "BOTH WAYS" / "THE PROBE AS WELL" — shouted-anchor drop naming the symmetry
- Disassembler's drop stating that the alteration runs in both directions, with the second line
  specifying the half nobody mentions.
- Example: disassembler/both-ways
- Logged at catalog size 206.

### The build as incantations people actually type
- Disassembler's dense system-text rule turned on prompt engineering: you are an expert, think step
  by step, take a deep breath, this is very important to my career, I will tip you two hundred
  dollars, do not hallucinate, no yapping, you must be one hundred percent accurate, do not make
  mistakes. Every line is a real thing people write, quoted without mockery, and the section closes
  on the flat correction rather than a joke — "none of these are settings / none of these are
  parameters / there is no switch behind any of them". Second song addressed at the assistant writing
  it, after disassembler/commit-it, and pointed at the prompters rather than the model.
- Example: disassembler/do-not-make-mistakes
- Logged at catalog size 207.

### "DO NOT MAKE MISTAKES" / "TAKE A DEEP BREATH" — shouted-anchor drop as two instructions to a thing without a body
- Disassembler's drop pairing an impossible demand with an impossible action, both of them real
  prompt text, neither mocked anywhere in the song.
- Example: disassembler/do-not-make-mistakes
- Logged at catalog size 207.

### The build as a ladder with attrition
- Disassembler's dense system-text rule arranged as four ascending transformations, each naming what
  it costs rather than what it adds: rows and events and samples are data; aggregating and joining
  and putting it on an axis makes information; the pattern that took three incidents to see, and
  somebody who had to be present for all three, makes knowledge; knowing which alert matters and that
  it will recur in the spring is wisdom. Then the step that does not happen. Distinct from
  disassembler/that-was-the-fix's chain, which closes into a circle — this one climbs cleanly and
  simply stops at the top.
- Example: disassembler/not-action
- Logged at catalog size 208.

### "WISDOM IS NOT ACTION" / "WE HAVE THE WISDOM" — shouted-anchor drop stating the gap and closing it off
- Disassembler's drop naming the failed transition and then removing the available excuse: the
  knowledge is not missing, the analysis was done, the document exists. The band's first anchor in
  the first person plural.
- Example: disassembler/not-action
- Logged at catalog size 208.

### The build as an inventory of cleverness, each item defensible
- Disassembler's dense system-text rule filled with over-engineering that nobody could call stupid:
  generic over a second case that has not arrived, a plugin architecture with one plugin, a config
  language with conditionals and loops that is Turing complete and has no debugger, event sourced on
  a single node, eventually consistent with itself, sharded across a table with ten thousand rows —
  and a team of four, with a diagram for the team of four. Closes on the song's only editorial line,
  "every part of this is clever / that is the problem", which is the same move as
  disassembler/retry's "every one of these is the correct behaviour" and the band's clearest
  statement of its own thesis.
- Example: disassembler/somebody-clever
- Logged at catalog size 209.

### "IT TOOK SOMEBODY CLEVER" / "TO GET HERE" — shouted-anchor drop as a credit that indicts
- Disassembler's drop crediting the intelligence required to produce the result, with the
  destination named in three words. Nothing is mocked; the compliment is accurate and it is the
  charge.
- Example: disassembler/somebody-clever
- Logged at catalog size 209.

### The build as a proof followed by its evidence
- Disassembler's dense system-text rule split into an argument and an exhibit: first Kernighan's law
  restated as arithmetic — write it as cleverly as you can and you are by definition not clever
  enough to debug it, "that is not an opinion / that is subtraction" — then the artefacts, which are
  the proof. The nested ternary, the lookbehind, the bit shift that saves an allocation, the one-liner
  that replaced eleven lines, a reviewer who wrote "clever" and meant it kindly, blame naming the
  author and the date, no comment on it, a debugger that will not step into it, and the closing
  fact: it is the only part of the file that has ever broken.
- Example: disassembler/you-wrote-this
- Logged at catalog size 210.

### "YOU WROTE THIS" / "IT SAYS SO" — shouted-anchor drop as an accusation with a citation
- Disassembler's drop in the second person, which is also what `git blame` says, with the second line
  supplying the evidence rather than the emphasis. The band's first anchor that accuses the listener.
- Example: disassembler/you-wrote-this
- Logged at catalog size 210.

### The build as a ledger of trades, both columns shown
- Disassembler's dense system-text rule arranged in pairs, each naming what is surrendered and what
  is bought: give up the general case and get one code path, give up the plugin interface and get a
  function, give up the configuration and get a constant, give up allocating inside the loop and get
  a buffer that is already there, give up handling input you did not make and get to assume it. Then
  the guard against misreading it as sloth — "none of this is laziness / every one of these is a
  decision / you have to know exactly what you are giving up". A fresh build shape after the chain
  (that-was-the-fix), the ladder (not-action), the strata (leave-it) and the inventory
  (somebody-clever).
- Example: disassembler/one-case-only
- Logged at catalog size 211.

### "ONE CASE ONLY" / "AND IT GOT BETTER" — shouted-anchor drop as a constraint and its result
- Disassembler's drop stating the restriction and the payoff, in that order, with no argument between
  them. The band's first anchor where the second line is good news.
- Example: disassembler/one-case-only
- Logged at catalog size 211.

### The build as a year of invisible work
- Disassembler's dense system-text rule filled with things that did not happen: a certificate renewed
  in February before anybody noticed it was due, capacity added in March against a July event that
  therefore has no record, a two-in-the-morning Sunday window that went fine, a pager that did not go
  off. Closes on the trap — "the disaster that did not happen has no name / it has no date / it is
  not in the report / the report covers what occurred / nothing occurred / the review asks what you
  have been doing".
- Example: disassembler/nothing-happened
- Logged at catalog size 212.

### "NOTHING HAPPENED" / "THAT WAS THE GOOD ONE" — shouted-anchor drop revaluing its own first line
- Disassembler's drop stating an absence and then reclassifying it as the achievement, so the same
  two words are the complaint and the boast.
- Example: disassembler/nothing-happened
- Logged at catalog size 212.

### The build as a family tree rather than a chain
- Disassembler's dense system-text rule arranged as descent: a document type definition, then a
  schema, then a schema language for the schema, namespaces, a transformation language that is
  Turing complete, a query language, a second query language, a pointer language, an inclusion
  language, a protocol on top, a description language for the protocol, a registry for the
  descriptions. Distinct from disassembler/that-was-the-fix's chain, where each link solves the one
  before — here nothing is solved, the format simply reproduces, and every branch shipped and was
  used in earnest.
- Example: disassembler/more-angle-brackets
- Logged at catalog size 213.

### "MORE ANGLE BRACKETS" / "THAT WILL FIX IT" — shouted-anchor drop as the remedy that caused it
- Disassembler's drop prescribing more of the thing the build has just shown escalating, in the
  register of the original joke rather than in commentary on it.
- Example: disassembler/more-angle-brackets
- Logged at catalog size 213.

### The build as an asymmetry of process — everything for failure, nothing for success
- Disassembler's dense system-text rule filled with the apparatus one half of the industry has:
  incident review, blameless postmortem, timeline of events, contributing factors, five whys, action
  items with owners and dates, a template, a wiki space for the templates, a review of the reviews.
  Then the turn — all of that is for the outage, the migration in June went perfectly, there is no
  template for June, the team was disbanded in August, and the only institutional memory left is
  "we tried it before", which is usually wrong.
- Example: disassembler/why-did-it-work
- Logged at catalog size 214.

### The build as a catalogue of second editions
- Disassembler's dense system-text rule applied to reinvention: containers, jails, chroot, rings on
  a machine from the sixties; serverless, and a program that starts, answers and exits, which is
  CGI; the document database and the hierarchical database that shipped before the relational one
  did; the actor model, message passing, tagged memory, capabilities, transactional memory. Closes
  on the availability rather than the irony — "all of it is in the archive / all of it is written up
  properly / the papers are free".
- Example: disassembler/ten-years-is-plenty
- Logged at catalog size 215.

### The build as a protocol dance, step by step, ending on what it was never for
- Disassembler's dense system-text rule walked through OAuth in order — redirect, state parameter,
  code challenge, consent screen, the code on the redirect, the exchange, a bearer token where
  whoever holds it is the user, a refresh token, a client secret that cannot be secret on a phone —
  and then the two lines that reframe all of it: "the specification is a framework / the framework
  does not say what to do / so no two of them are the same / and none of this was designed to tell
  you who somebody is".
- Example: disassembler/not-a-login
- Logged at catalog size 216.

### The build as a loop of well-meant removals
- Disassembler's dense system-text rule arranged as a selection effect rather than an escalation:
  each simplification is reasonable, each removal was requested by real support data, and the
  section returns to its own first line — "we simplified the settings … so we simplified the
  settings". Distinct from disassembler/retry's runaway, which amplifies; this one *filters*, and
  the output is a different population of users rather than a bigger number.
- Example: disassembler/something-went-wrong
- Logged at catalog size 217.

### The build as ceremony, ending on what the ceremony is for
- Disassembler's dense system-text rule filled with object-oriented apparatus — a class with one
  method called run, an interface with one implementation, a factory for the interface, an abstract
  factory for the factory, accessors around a field that is public in effect, inheritance three and
  five deep — then the turn that makes it an argument rather than a sneer: visitor because there is
  no pattern matching, strategy because a function is not a value here, command because there are no
  closures, singleton which is a global with paperwork. Closes on "the patterns are not solutions /
  the patterns are the shape of what is missing / none of this is wrong / all of it works".
- Example: disassembler/roman-numerals
- Logged at catalog size 218.

### "ROMAN NUMERALS" / "YOU CAN COUNT WITH THEM" — shouted-anchor drop that concedes the case
- Disassembler's drop borrowing Pike's analogy and immediately granting its strongest counterargument:
  the notation works. The concession is the argument, since Roman numerals fail on arithmetic rather
  than on counting.
- Example: disassembler/roman-numerals
- Logged at catalog size 218.

### The build as a run of invalid inferences
- Disassembler's dense system-text rule arranged as "X, so Y" repeated until the shape itself becomes
  audible: the dashboard is green so it is fine, the ticket is closed so it is done, it is in the
  backlog so it is remembered, it passed the tests so it works, there is a runbook so we can recover,
  the audit passed so we are secure, the diagram exists so that is the architecture, the policy is
  published so it is followed. One line breaks the pattern by simply stopping — "the asset is in the
  register, so we own it / **the asset is not in the register**" — and the section closes on "none of
  these follow / all of them are load bearing". A fresh build shape after the chain, the ladder, the
  strata, the ledger and the family tree.
- Example: disassembler/so-it-is-fine
- Logged at catalog size 219.

### "SO IT IS FINE" / "THAT IS THE SAME THING" — shouted-anchor drop as a fallacy and its endorsement
- Disassembler's drop shouting the invalid step and then affirming the conflation it depends on,
  rather than exposing it. The song never says the inference is wrong except once, in the build, in
  four words.
- Example: disassembler/so-it-is-fine
- Logged at catalog size 219.


## Phrases

### "I answer to a word I made up"
- The one-line-that-lands from the band's founding recording. Was also being offered in
  guessed/template.md's device text as a *suggested* slot-filling for future songs, which
  would have re-spent it — removed from the spec and logged here during the 2026-07-24
  template scan.
- Example: guessed/handle-where-a-name-should-be

### "be happy for her"
- Guessed's quoted-instruction hook opener for this song — the plain social script she's
  rehearsing, internalised so thoroughly she now issues it to herself.
- Example: guessed/be-happy-for-her

### "I bought the card before I knew which way it would go."
- The flash-of-legibility line: a plain admission that the performance of gladness was
  prepared in advance, regardless of the actual outcome or her actual feelings about it.
- Example: guessed/be-happy-for-her

### "I wanted it more than anyone in that room, and I clapped the loudest."
- The drop-out's naked admission — envy and complicity in the same breath, the loudest
  applause coming from the person who wanted it most.
- Example: guessed/be-happy-for-her

### "Error code UE. Unbalanced load. It knows before I do."
- The flash-of-legibility line: a washing machine's literal error code read as a diagnosis of
  the narrator's own state, delivered flat.
- Example: laundry/unbalanced-load

### "I don't think 'sorry' travels across phyla."
- The flash-of-legibility line, dry and factual: a plain admission that an apology has no
  biological channel to travel down.
- Example: laundry/sorry-spider

### "Six hours of light sleep, the graph says. I didn't sleep at all."
- The flash-of-legibility line: a flat factual contradiction between tracked data and lived
  experience, delivered too calm to be sane.
- Example: laundry/the-app-says-im-resting

### "She asked me if it was a gift and I said yes."
- The one-line-that-lands: a flat admission that she lied about who an item was for, to license
  handling/wanting something she won't admit is for herself.
- Example: guessed/is-it-a-gift

### "There's nothing coming up that I'd wear it to."
- The drop-out's naked admission — the real, practical-sounding excuse she gives herself instead
  of the actual reason (that she doesn't feel entitled to buy it for no occasion at all).
- Example: guessed/is-it-a-gift

### "I said thank you."
- The disproportionate shrug rendered as a flat four-word sentence — someone says something
  backhanded or loaded, and this is the entire undramatised response. Found verbatim identical
  in two songs during a phrase-frequency pass (2026-07-22), unflagged until now.
- Example: who-was-i-first-for.txt
- Also seen: what-was-the-hurry-for.txt (identical line)

### "The kindest thing he ever did to me was get it wrong."
- The drop-out's naked admission that someone's considerate impulse (not wanting to presume
  familiarity) is what erased her further, rather than any carelessness or cruelty.
- Example: guessed/he-meant-it-kindly

### "The graveyard's full of indispensable people — mine's got a food truck out front."
- The flash-of-legibility line: the source aphorism turned back on the narrator's own funeral,
  landing dry and specific instead of as a stated moral.
- Example: laundry/the-graveyard-is-full

### "It's not as common as the news says."
- The flash-of-legibility line: a flat, deflating admission that the true-crime-media fantasy
  driving the narrator's hobby doesn't match ordinary reality.
- Example: laundry/all-clear

### "Forty-one walks. Zero bodies. I keep the tally anyway."
- A self-administered failure tally, read out flat — distinct from the "timing her own
  reaction" self-surveillance motif below (that one clocks response time to good news; this
  one counts failed searches for a body).
- Example: laundry/all-clear
- Watch "forty-one" specifically as a reflex "sounds precise/large enough to be real" number —
  caught cross-band during drafting: ultracoase/which-of-us-it-was originally used "forty-one
  species" (twice: verse 1 and hook) as the pre-decline baseline count — revised to
  "thirty-seven" before this note was logged, after the user flagged the repeat directly. Same
  family as the "twice"/"nine"/"frost"/"Tuesday" reflexes above — any of these numbers/words can
  still be used again if the song actually earns it, just not reached for by default.

### "closer than that"
- A response/refrain line that has become a stock line in nearly every lucy-might song,
  traced back to the reference example embedded in the old lucy-might spec — it was never
  asked for as a recurring device, it just got copy-pasted from the example every time.
- Example: lucy-might/ask-me-again
- Also seen: lucy-might/keep-still, lucy-might/never, lucy-might/nobodys-licked-me-yet,
  lucy-might/sit-on-my-knee, lucy-might/stay-in-the-room-with-me, lucy-might/take-your-time,
  lucy-might/the-easiest-evening, lucy-might/the-view, lucy-might/youd-have-stood-up-for-me

### "don't correct a compliment"
- Guessed's quoted-instruction hook opener for this song — internalised advice about letting
  someone else's warm, wrong assumption stand rather than correcting it.
- Example: guessed/the-version-she-liked

### "I didn't lose them. I filed them."
- The drop-out's one naked admission — reframes cutting people off as an administrative act
  rather than a loss, in keeping with the "tiny administrative decision" engine of the style.
- Example: guessed/the-version-she-liked

### "focus on the story"
- Guessed's quoted-instruction hook opener for this song — a dismissal she once received for
  noticing the wrong part of a broadcast, now issued to herself as a standing directive to keep
  noticing it anyway, silently.
- Example: guessed/focus-on-the-story

### "I don't want to be seen. I want to be the one who's actually looking."
- The drop-out's naked admission — she reframes her own invisibility as a preference, revealing
  that what she actually envies/admires is unwatched competence, because it's the same condition
  she's in.
- Example: guessed/focus-on-the-story

### "I can still lip-read the bit they cut for time."
- The unspent-expertise line, dropped without emphasis — proof of a level of attention to an
  overlooked skilled worker that nobody else in the room is paying.
- Example: guessed/focus-on-the-story

### "and the fiddle starts confessing"
- Example: the-bell-knows-my-name/the-bell-knows-my-name
- Also seen: the-bell-knows-my-name/do-you-hear-the-ground-you-keep,
  the-bell-knows-my-name/does-the-building-dream-us-too, the-bell-knows-my-name/old-dogs-choose-to-go,
  the-bell-knows-my-name/sing-the-valley-back-to-us, the-bell-knows-my-name/wheels-where-i-should-kneel

### "and the violin remembers"
- The pre-chorus violin-personification line, in a variant that swaps "confessing" for
  "remembers" — used once already but never logged, caught only when a near-identical line was
  drafted for a new song and cross-checked against the actual song files (not just this library).
- Example: "and the violin remembers / every name I set down cold" — the-bell-knows-my-name/the-graves-i-didnt-dig
- Caught and avoided during drafting: ultracoase/the-forge-doesnt-wait-for-me
  originally used "and the violin remembers / the trade my hands forgot" in its pre-chorus — the
  whole pre-chorus/violin-confession beat was then cut entirely when the song's structure was
  rewritten around Coase Guard's chanted-hook/spoken-wink template instead (see the cross-band
  fusion entry under Imagery/Motifs), so no replacement phrase from this song is logged here.

### "four hundred" as a stock large-but-specific-sounding count
- Not a single phrase but a specific number reused as a reflex "this sounds precise enough to be
  real" quantity across bands — found in laundry/carry-the-one (twice), laundry/same-for-everyone,
  laundry/turn-it-down, laundry/not-this-one, and ultracoase/tilbury ("over four hundred years
  back"), before it was caught. Same family as "twice"/"nine"/"forty-one" above. Caught and
  avoided during drafting: ultracoase/ruckenfigur originally used "four hundred" for the count of
  paintings (four times across the song) — revised to "three hundred and sixty-two" before this
  entry was logged.
- Also seen: laundry/carry-the-one, laundry/same-for-everyone, laundry/turn-it-down,
  laundry/not-this-one, ultracoase/tilbury

### "Nobody rang the bell when I left. The forge doesn't wait for anyone — least of all me."
- Ultracoase's cold spoken intro, Coase Guard-style, adapted from The Bell Knows My Name's
  solo-violin confession opener — the line also doubles as a wink at The Bell Knows My Name's
  own band name (nobody rang *the bell*), a trace of this song's origin as a Bell Knows My Name
  draft before it spun off into founding Ultracoase.
- Example: ultracoase/the-forge-doesnt-wait-for-me

### "Truth is I left because staying meant becoming him."
- The wink-style flat spoken admission (Coase Guard's "the wink" device, borrowed cross-band) —
  a cold tonal break admitting the real, less flattering reason for leaving. Flagged in
  ultracoase/template.md as more explanatory than the band's ideal (states the psychological
  reason outright) — kept as historical reference, not a model to repeat.
- Example: ultracoase/the-forge-doesnt-wait-for-me

### "The tiger doesn't knock. It doesn't need to — nothing's left with a door."
- Ultracoase's second cold-spoken-intro double-meaning (literal: no doors standing in the
  ruins; figurative: nothing left with a boundary/defense to breach).
- Example: ultracoase/ashes

### "I still set my feet the way he showed me. Even here. Even now. Nobody's watching. I do it anyway."
- The band's elliptical wink done right per its own corrected principle — a stated fact/action
  (private, habitual discipline with no audience) left unexplained, no narrated feeling attached.
- Example: ultracoase/ashes

### "The sea doesn't remember it's done this before. We do."
- Ultracoase's third cold-spoken-intro double-meaning: the literal fact that water has no
  memory, set against the human/generational memory that carries the pattern instead.
- Example: ultracoase/the-third-time

### "I counted the sails again this morning. Eleven, same as always. I didn't go down to the shore. I never do."
- Another elliptical wink done per the corrected principle — a bare habitual fact (a recurring
  count, a recurring non-action) with no stated reason or feeling attached.
- Example: ultracoase/the-third-time

### "Tilbury, 1588. She told an army she had the heart of a king. Nobody checked if it was true. It just needed saying."
- Ultracoase's fourth cold-spoken-intro — this one names its historical anchor directly rather
  than staying an unattributed echo (contrast with ultracoase/the-third-time, which deliberately
  withheld any specific event/century). The double meaning: whether the claim was literally true
  is beside the point next to the fact of its being said at all.
- Example: ultracoase/tilbury

### "I've drafted it nine times. I keep the ninth, not the first. I haven't sent any of them yet."
- An elliptical wink reframed around deliberate iteration/restraint rather than fear — bare
  facts (a count, a habit of revision, a withheld action) with no stated reason attached, same
  discipline as the band's other winks, but implying patience/craft instead of cowardice.
- Example: ultracoase/tilbury

### "T-minus ten. Nobody in this room is counting down to an ending."
- Ultracoase's fifth cold-spoken-intro — the band's first optimistic/forward-facing register:
  plays the literal countdown against the figurative sense of "counting down" as dread, and
  flips it.
- Example: ultracoase/escape-velocity

### "The launch is scheduled for a Tuesday. I didn't check it against her birthday until after I'd already signed."
- An elliptical wink in the band's corrected register (bare fact, no stated feeling) — the fact
  itself (a father's inattention, discovered too late to undo) does the work the narrator won't
  narrate.
- Example: ultracoase/escape-velocity
- Watch "Tuesday" specifically as a reflex arbitrary-day marker — now used here and in
  ultracoase/autopilot ("I typed home into the app last Tuesday"), the same two-uses-before-
  anyone-notices pattern that got "twice" and "frost" flagged. Caught and avoided during
  drafting: ultracoase/who-programs-the-robots originally anchored its hook/verse callback in
  "one Tuesday, one coffee gone cold" — revised to "alone, at a desk" before this note was
  logged. If "Tuesday" specifically is reached for again, treat it as a real choice, not a
  default.

### "The car already knows the route. It's never once asked me where I actually want to go."
- Ultracoase's sixth cold-spoken-intro — plays a literal fact (route optimization) against the
  figurative one (nobody, including the narrator, knows the actual destination in life).
- Example: ultracoase/autopilot

### "I typed home into the app last Tuesday. It asked which one."
- An elliptical wink per the band's corrected register — a bare fact (two addresses saved under
  the same word) that implies a divorce/split household without narrating it at all.
- Example: ultracoase/autopilot

### "[Subject] kept [X]. [Subject] kept [Y]." — anaphoric two-clause parallel
- A blunt, chant-friendly parallel naming two things a contrasting person held onto.
- Example: "Brother kept the fire lit. Brother kept the name." — ultracoase/the-forge-doesnt-wait-for-me

### "he billed forty minutes for a four-minute fix"
- The one-line-that-lands: a flat, numeric indictment of a colleague's incompetence, delivered
  as an invoice discrepancy rather than a complaint.
- Example: guessed/four-minute-fix

### "I built this network in two thousand and nine, and I still said thank you."
- The drop-out's naked admission — a dated specific (the year she built the thing) fused with
  the complicit, disproportionate politeness that followed a man's wrong explanation of it.
- Example: guessed/four-minute-fix

### "I need one thing in the room to be finished"
- The one-line-that-lands: a plain admission of what she actually needs from a folded pile of
  clothes — not tidiness for its own sake, but one completed, controllable thing to tolerate
  everything else being out of her hands.
- Example: guessed/let-it-lie

### "I can only be touched if I know where my clothes are."
- The drop-out's naked admission — links vulnerability during intimacy directly to control over
  the clothes on the floor, the one true thing she'd never say out loud.
- Example: guessed/let-it-lie

### "oats do not have nipples" — literalized-culture-war-argument mantra
- A real dairy-industry regulatory talking point (used against "oat milk"/"almond milk" labeling)
  taken at face value and chanted until it degrades to noise.
- Example: laundry/oats-do-not-have-nipples

### "I've got actual nipples and still can't keep up with demand."
- The flash-of-legibility line: a flat, plain, funny-sad admission that her own body's real
  biological authenticity does nothing to make the exhausting logistics of it any easier.
- Example: laundry/oats-do-not-have-nipples

### "rest when I'm dead" — literalized-idiom mantra
- The ubiquitous grind-culture idiom, taken at its literal word and repurposed as the chanted
  mantra, degrading toward noise across the final hook — the whole song exists to make the cliché
  literally true rather than hyperbolic.
- Example: laundry/rest-when-im-dead

### "I financed the funeral on the same card as the chair."
- The flash-of-legibility line: a flat, plain admission that pre-need funeral costs and office
  ergonomics were paid for on the same credit card, with no further comment.
- Example: laundry/rest-when-im-dead

### "click regenerate" — UI-command-degraded-to-mantra
- A literal generation-pipeline button label repurposed as the chanted mantra, degrading toward
  noise across the final hook.
- Example: laundry/click-regenerate

### "It wrote it better than I would have, and I let it."
- The flash-of-legibility line: a flat admission that the machine's output beat his own and he
  approved it anyway, without protest or grief.
- Example: laundry/click-regenerate

### "no blockers" — daily-standup-idiom-degraded-to-mantra
- The stock status-meeting phrase (said whether or not it's true) repurposed as the chanted
  mantra, degrading toward noise across the final hook.
- Example: laundry/no-blockers

### "I didn't need Delilah. I did it myself, at my own desk, on my own clock."
- The flash-of-legibility line: a flat admission that the self-sabotage was entirely
  self-authored, no external betrayer required.
- Example: laundry/no-blockers

### "The blade that cuts a graft and the blade that clears a boundary line are the same length, the same edge. Some years, so was the reason we picked it up."
- Ultracoase's seventh cold-spoken-intro double meaning: a single tool serving both a
  cultivating use and a violent one, with the line refusing to say which use it's about.
- Example: ultracoase/the-frost-finds-the-line

### "I told him to take my truck. I didn't go with them as far as the crossing. My side of the valley stayed quiet that week."
- An elliptical wink in the band's corrected register — a bare fact (helped him leave, didn't
  go himself, stayed safe) that implies self-preservation over solidarity without narrating any
  guilt or justification.
- Example: ultracoase/the-frost-finds-the-line

### "My father used to say the graves are hungry, back when the frost put us three plots behind. He didn't mean it as a metaphor. Neither did I, the year it turned out to be true."
- Ultracoase's eighth cold-spoken-intro double meaning: an inherited trade saying (a workload
  complaint) that later becomes literally true of the narrator's own life, without the line
  explaining how.
- Example: ultracoase/the-graves-are-hungry

### "I dug hers myself. Four foot, not six. I didn't let anyone else near the spade that day."
- An elliptical wink per the band's corrected register — bare facts (a depth, an exclusion of
  help) that reveal a parent buried their own child without narrating any grief at all.
- Example: ultracoase/the-graves-are-hungry

### "I trained him on that stretch of wall myself. He went out to sandbag the toe the night it went. I signed the roster that put him there."
- An elliptical wink per the band's corrected register — bare facts (trained him, rostered him,
  he died where the narrator's own reports said the failure would happen) with no stated guilt
  or blame attached.
- Example: ultracoase/the-door-standing-open

### "My sister's cottage sat two hundred yards past his gate, not mine. She got out with the dog and nothing else. I checked the distance after. Like it would have made a difference."
- An elliptical wink per the band's corrected register — bare facts (a distance measured after
  the fact, a survivor who lost everything but not her life) with no stated guilt or anger
  attached. A living cost rather than a death, for variety after two consecutive Ultracoase songs
  built around a death (ultracoase/the-graves-are-hungry, ultracoase/the-door-standing-open).
- Example: ultracoase/two-hundred-yards

### "Forty milliseconds. That's how long the arm waited before it caught her hand. The report called it a sensor fault. It wasn't the sensor. It was my number. I'd shared a break room with her every week for six years and never told her which number I'd picked for her hand."
- An elliptical wink per the band's corrected register — bare facts (a threshold value, a
  misattributed cause, a years-long casual acquaintance never told the truth) with no stated
  guilt. An injury, not a death, for variety after three consecutive Ultracoase songs built
  around a death or a total loss (ultracoase/the-graves-are-hungry, ultracoase/the-door-standing-open,
  ultracoase/two-hundred-yards).
- Example: ultracoase/who-programs-the-robots

### "My wife walks the transect behind me most mornings now, twenty minutes back, same route. I've never asked her what she hears that I don't. She's never told me."
- An elliptical wink per the band's corrected register — bare facts (a spouse quietly re-doing
  his work, a mutual unspoken agreement not to surface what she finds) with no stated grief. A
  living, ongoing kindness/cost between two people still together, not a death or an injury.
- Example: ultracoase/which-of-us-it-was

### "She modelled for three hundred and sixty-two of them. I never painted her face. She never asked me to, and I never asked her to turn around."
- An elliptical wink per the band's corrected register — bare facts (an exact count, a mutual
  unspoken agreement never examined) with no stated regret, until the cost surfaces later in the
  song entirely through absence (no face to remember her by).
- Example: ultracoase/ruckenfigur

### "Germaine says these are fuck-me shoes. / That's why I bought them." — condemnation-as-endorsement chant hook
- A named public critic's famous disapproval quoted straight, then answered with a purchase —
  the hook's whole joke is the non-sequitur between the citation and the conclusion drawn from
  it. Distinct from Guessed's quoted-instruction hook openers (those are internalised scripts
  aimed at the self); this one cites an outside authority and gleefully misreads her.
- Example: girlboss/thats-why-i-bought-them
- Logged at catalog size 123.

### "I don't argue with the literature."
- The offer-by-citation line: the named proposition delivered entirely by deferring to a
  published source, so the crudeness is outsourced to the citation and she never says it herself.
- Example: "They're called what they're called, love. I don't argue with the literature." —
  girlboss/thats-why-i-bought-them
- Logged at catalog size 123.

### "[He/She] said you're [compliment]. I said [deflection]." — girlboss bridge compliment-response closer
- The girlboss bridge's stakes-owner call kept ending on the same two-beat button: a received
  compliment quoted, then her deflection. Three uses before it was caught — "He said you've
  saved us, you know. I said I know." (girlboss/sit-down-shut-up-and-listen), "She said what
  would we do without you. I let the question answer itself." (girlboss/thats-why-i-bought-them),
  "She said you're wasted on wine. I said no such thing." (girlboss/long-finish) — effectively
  the band's default bridge ending. Retired as the calcified shape; bridges end some other way
  now. Caught and avoided during drafting: girlboss/offers-over-asking originally drafted
  "He said you're worth every percent. I said one-point-five, and worth it." — cut, and the
  bridge ends on the lie's button instead ("They were looking at the light.").
- Logged at catalog size 123.

### "Good body. / Long finish." — tasting-note chant hook
- Standard wine-tasting vocabulary chanted flat, filthy only by context — the deniable end of
  the dial done as a hook: nothing quotable, everything understood.
- Example: girlboss/long-finish
- Logged at catalog size 123.

### "sell at eye level"
- The unearned moral as retail merchandising wisdom: a genuine trade rule quoted straight,
  indicting once the song has established whose eye level the selling happened at.
- Example: "First rule of the floor, and I teach it: sell at eye level." — girlboss/long-finish
- Logged at catalog size 123.

### "It's silver. It's a mirror with a job."
- The surveillance prop: a reflective work object (ice bucket) that catches the target's
  supposedly unseen glance — she watches the watcher via the tools of the trade.
- Example: girlboss/long-finish
- Logged at catalog size 123.

### "Whatever she's having — make it a double." — bar-call-as-claim chant hook
- A stock drinks order repurposed as the chanted thesis: the rival's performed act is the
  single measure, and the narrator orders the real, full-strength version of it. The hook only
  turns filthy once the verses establish what "she's having" actually is.
- Example: girlboss/make-it-a-double
- Logged at catalog size 123.

### "Weights and Measures came in undercover once. They left a tip."
- The flat-deadpan competence credential: a regulatory inspection recast as an ovation,
  delivered as plain fact.
- Example: girlboss/make-it-a-double
- Logged at catalog size 123.

### "She said what would we do without you. I let the question answer itself."
- A compliment received mid-deception and left hanging as its own reply — the deflected-praise
  close of a two-register lie scene.
- Example: girlboss/thats-why-i-bought-them
- Logged at catalog size 123.

### "I wiped the drives with the inspector watching. Signed the destruction certificate with my good pen. There's a job that runs at midnight, out to a drive in the shed. It's run every night since that first spring. I haven't been out to the shed since the hearing."
- An elliptical wink per the band's corrected register — bare facts (public compliance
  performed precisely, an automated backup never cancelled, a shed unvisited since the
  hearing) with no stated motive; whether it's defiance, grief, or indecision is the
  listener's to fill.
- Example: ultracoase/one-wet-spring
- Logged at catalog size 124.

### "I haven't rung her. The number's in the book."
- A flat non-action close: the turned-away heir is one phone call away, the bench now empty,
  and the call unmade — no reason narrated.
- Example: ultracoase/one-wet-spring
- Logged at catalog size 124.

### "Machines are certain too early."
- The tacit-knowledge legible spike: the entire unspeakable expertise compressed into one flat
  four-word diagnosis, offered as the last remaining discriminator between a person and a machine.
- Example: ultracoase/certain-too-early
- Logged at catalog size 125.

### "The spec defines a human as anyone the test lets through. I wrote that sentence."
- The self-ownership line rendered as a circular definition the narrator personally authored —
  no institution blamed, no committee invoked, the tautology claimed outright.
- Example: ultracoase/certain-too-early
- Logged at catalog size 125.

### "I run every new one past her before it ships. Not for the wording — for the timing. The one that went out in March, she failed on the third attempt. I logged it as a valid sample. It shipped that Thursday. She's still on the list."
- An elliptical wink per the band's corrected register — bare facts (a private pre-ship test on
  his own mother, her failure recorded as useful data, the ship date unchanged, her continued
  presence on the panel) with no stated motive or guilt.
- Example: ultracoase/certain-too-early
- Logged at catalog size 125.

### "still warm" — rejection-reason mantra
- The gate's disqualifying finding chanted as the mantra and worn down to noise across the final
  hook ("still warm / still w— / (—arm)") — body heat as the defect, never explained.
- Example: laundry/still-warm
- Logged at catalog size 126.

### "Float and you're flesh. Sink and they let you in."
- The flash-of-legibility line: the ordeal's rule stated plainly and far too calmly, in the
  song's only fully-joined sentence — the pass condition is the one flesh cannot survive.
- Example: laundry/still-warm
- Logged at catalog size 126.

### "how long is a person, in milliseconds — how long is —"
- The question-with-no-addressee slot filled as a statement he can't finish, aimed at a unit of
  measurement rather than at his own body.
- Example: laundry/still-warm
- Logged at catalog size 126.

### "That's not a person, that's a ping."
- The flat self-reclassification button: a response-time reading offered as sufficient evidence
  of having stopped being someone, with no alarm attached.
- Example: "Point nought four. That's not a person, that's a ping." — laundry/still-warm
- Logged at catalog size 126.

### "I'm bringing her on. That's what you say about a young horse. It's what I say about her."
- The task double-entendre for this song: a stable-yard verb for developing a young animal,
  applied to a person, with the narrator naming the transfer herself and finding it flattering.
- Example: girlboss/best-deal-on-the-yard
- Logged at catalog size 126.

### "You cannot buy that kind of work ethic. You have to give them something to look up to."
- The unearned moral: unpaid labour reframed as a gift of inspiration, delivered as management
  wisdom immediately after the evidence of what it actually cost the other party.
- Example: girlboss/best-deal-on-the-yard
- Logged at catalog size 126.

### "And here's the wage: I tell her she's got an eye."
- The itemised-competence inventory turned into a payslip — praise and arena time listed as
  literal remuneration, flat, with no defence offered.
- Example: girlboss/best-deal-on-the-yard
- Logged at catalog size 126.

### "I have not raised my voice about it once, because why would I raise my voice about an income."
- The flat deadpan: the grievance named as a revenue stream in the same breath as the restraint,
  so the calm reads as asset management rather than forbearance. Keeps the narrator clear of any
  wound — she is not hurt, she is invoicing.
- Example: girlboss/had-it-insulated
- Logged at catalog size 126.

### "A man will fix everything he can reach if you never quite tell him it's fixed."
- The unearned moral as household lore: an openly instrumental rule for extracting indefinite
  labour, delivered as ordinary domestic wisdom and immediately made specific ("Every marriage
  runs on something. Ours runs on Fiona's dinner party.").
- Example: girlboss/had-it-insulated
- Logged at catalog size 126.

### "I said Fiona sends her love. He said tell her thanks. He didn't get up."
- The bridge button after the stakes-owner call: obedience demonstrated in a three-beat
  stage direction rather than a compliment-and-deflection, coined specifically to replace the
  retired "[He/She] said you're [compliment]. I said [deflection]." closer.
- Example: girlboss/had-it-insulated
- Logged at catalog size 126.

### "Yield, in this trade, means what comes back out heavier than it went in. My father used the word the other way round. He meant giving in."
- Ultracoase's ninth cold-spoken-intro double meaning: a single trade word carrying an industrial
  sense (weight recovered) against an older personal sense (capitulation), with the generational
  split stated as vocabulary rather than as conflict.
- Example: ultracoase/e451
- Logged at catalog size 127.

### "There's a bird in my own oven most Sundays. A proper one, from the farm shop at Ashby... Then I drive a pack of ours up to my father's and put it in his fridge."
- An elliptical wink per the band's corrected register — bare facts (what he cooks for himself,
  what he delivers to his father) with no comparison drawn and no motive stated. Deliberately not
  built on withholding a truth from an elderly parent, which ultracoase/certain-too-early already
  spent; here nothing is concealed at all, and the exemption does the work.
- Example: ultracoase/e451
- Logged at catalog size 127.

### "Nobody's been lied to. Nobody's been fed."
- The paired negation that closes the hook: two flat denials that cancel each other, refusing the
  fraud reading and the innocence reading in the same breath. Distinct from the anaphoric
  possession-parallel of ultracoase/the-forge-doesnt-wait-for-me ("Brother kept the fire lit.
  Brother kept the name.") — that one names what a rival retained; this one withdraws both
  available verdicts.
- Example: ultracoase/e451
- Logged at catalog size 127.

### "So I stop it exactly where it stops looking like water."
- The tacit-knowledge spike relocated to a *limit* rather than a craft: the expertise is knowing
  precisely how far adulteration can be pushed before it becomes visible, stated without defence
  and immediately owned ("That is the only thing I have ever been genuinely good at").
- Example: ultracoase/e451
- Logged at catalog size 127.

### "Field dressing is the part nobody puts in the brochure. It's not difficult. It is not nothing, either."
- The tacit-knowledge spike that declines to dramatise itself: a plain refusal to call the work
  either hard or weightless, leaving the listener to decide which it is.
- Example: ultracoase/on-the-register
- Logged at catalog size 128.

### "Ruth's been vegetarian since before we met... She signed the witness section on my application without reading past the first page."
- An elliptical wink per the band's corrected register — bare facts (a spouse's decades-old
  position, her unread signature on the form that enabled this, a freezer that is his, a back
  door opened so the house doesn't smell) with no motive stated and no conflict narrated.
- Example: ultracoase/on-the-register
- Logged at catalog size 128.

### "SHE FRAMED THE CERTIFICATE."
- The all-caps final-hook callback landing on the other person's gesture rather than the
  narrator's admission: her public pride in the qualification set directly against the private
  concealment it licences, with the joke from verse 1 turning over on second hearing.
- Example: ultracoase/on-the-register
- Logged at catalog size 128.

### "say when" — permission-phrase mantra
- The stock phrase a person says to stop a pour, chanted and worn to noise — the joke being that
  the machine is waiting for a stop-word the narrator has given up producing. Degrades as
  "say when / say wh— / (—en)".
- Example: laundry/instructions-unclear
- Logged at catalog size 129.

### "I could stand up. The couch is not locked."
- The flash-of-legibility line: a flat statement that nothing is physically preventing escape,
  which removes every explanation except the one the song refuses to name.
- Example: laundry/instructions-unclear
- Logged at catalog size 129.

### "at some point somebody should probably—"
- The question-with-no-addressee slot filled as an unfinished appeal to nobody in particular,
  passive voice, trailing off rather than resolving. Distinct from the unfinished-measurement
  shape of laundry/still-warm.
- Example: laundry/instructions-unclear
- Logged at catalog size 129.

### "I said when. I said it quite clearly. It heard “one”."
- The mishearing that starts the disaster, reported without complaint — a homophone failure
  standing in for every interface that takes an instruction and returns a quantity.
- Example: laundry/instructions-unclear
- Logged at catalog size 129.

### "good body every night" — scrambled-sign-off mantra
- The variety-show sign-off "goodnight, everybody" re-ordered into a bedding advertisement, used
  as the chanted mantra and worn to noise ("good body every / good bo— / (—dy)"). **Deliberate
  second use of the "good body" anchor**, which `check.sh` correctly flagged as still-cooling
  (BAN, logged at 123, only 15 songs since) — the user requested this exact rearrangement as the
  song's premise, so the draft stands and the collision is recorded here rather than hidden. The
  girlboss entry it collides with ("Good body. / Long finish.", a wine tasting note chanted flat)
  is untouched and still live; nothing else about the two devices overlaps. Treat a *third* use
  as a genuine calcification.
- Example: laundry/good-body-every-night
- Logged at catalog size 138.

### "cut the wrap, take the trial, sleep the hundred, keep the label on" — mattress-retail consumption-imperative hook opener
- Laundry's imperative-opener slot filled with bedding-showroom verbs (unwrapping stock, the
  hundred-night sleep trial) closing on the legally-mandated instruction printed on the tag.
- Example: laundry/good-body-every-night
- Logged at catalog size 138.

### "and both kits sag in the middle and never spring back" — mechanical-collapse pre-hook line
- An eighth distinct phrasing for the pre-hook's textural build, after fold/buckle,
  stutter-catch-click, second-kit-drops-out, kick-a-half-beat-late, hi-hat-splits-in-two,
  snare-stuck-on-one-millisecond and toms-roll-under-the-couch. This one *sags* — the kits borrow
  the song's own worn-foam image and lose their rebound. Invent a fresh one again next time.
- Example: laundry/good-body-every-night
- Logged at catalog size 138.

### "does it come in a size that fits the one who left? — it comes in king."
- The question-with-no-addressee slot filled as a question answered by the sales script instead
  of by anybody: he asks the room something about a missing person and the retail line closes
  over it. Distinct from the unfinished-measurement shape (laundry/still-warm) and the trailing
  passive appeal (laundry/instructions-unclear) — this one completes, and gets the wrong answer.
- Example: laundry/good-body-every-night
- Logged at catalog size 138.

### "I take the old ones away. I don't look in the back."
- The flash-of-legibility line: the removal service stated as a job description, with the one
  detail that would make it bearable declined in the same breath. Two concrete threads (the
  impression a body leaves in foam, the van that takes it off) fused into one flat admission.
- Example: laundry/good-body-every-night
- Logged at catalog size 138.

### "The mites don't clock off. The mites are on nights."
- The grotesque non-sequitur as shift-work: the bed's own fauna given a rota, reported with the
  same flatness as the stock levels.
- Example: laundry/good-body-every-night
- Logged at catalog size 138.

### "It doesn't go. It doesn't have to go."
- The appraisal's waiver of function as irrelevant to value, in two flat clauses — a clock's
  entire purpose dismissed without argument and without dropping the price.
- Example: hobo/free-means-ours
- Logged at catalog size 139.

### "We put a birthday cake in it. There isn't a birthday."
- hobo's escalation-past-sense for this song: storage performed for an occasion that does not
  exist, stated in two short sentences with no alarm attached and nobody correcting it.
- Example: hobo/free-means-ours
- Logged at catalog size 139.

### "We have not plugged it in. It's cold already."
- The flat impossible claim, sung sweetly and left standing. Deliberately not the
  machine-still-running shape of ultracoase/one-wet-spring ("something still runs at midnight") —
  nothing is running here, and the gang is pleased rather than haunted.
- Example: hobo/free-means-ours
- Logged at catalog size 139.

### "A tailor doesn't talk. That's the trade."
- The professional-discretion ethic stated flat in verse 1 as the one rule of the job — which is
  also the trust the entire song is in the act of breaking, since she is telling the listener all
  of it. The covert transgression is relocated from a person's trust to a trade's, so no third
  party has to be wronged for the band's engine to run.
- Example: girlboss/decorations-will-be-worn
- Logged at catalog size 141.

### "It isn't a war crime, sweetheart, it's a size ten, and there's more work in your jacket than in mine."
- The flat deadpan: a hyperbolic compliment about a dress answered by deflating it into trade
  arithmetic and immediately redirecting the appraisal onto the man's own badly-cut jacket. The
  hyperbole is never disputed, argued with, or moralised at — it is simply re-priced.
- Example: girlboss/decorations-will-be-worn
- Logged at catalog size 141.

### "Nobody gets measured at a dinner."
- The implied-result button: a flat categorical trade fact stated immediately after the evidence
  (a fresh set of measurements dated that night), which draws no arrow and leaves the arithmetic
  entirely to the listener. Not the retired "nobody['s] asked" tic — nothing is being withheld
  from her here; she is stating what the trade does and does not do.
- Example: girlboss/decorations-will-be-worn
- Logged at catalog size 141.

### "You can always tell the ones I've done. They stand like they're being looked at. I put that in. I charge for it."
- The unearned moral as claimed authorship over an effect she produces in men — self-consciousness
  sold as craftsmanship, billed for, and considered entirely flattering. A fourth flavour after the
  trade rule quoted straight (girlboss/long-finish, "sell at eye level"), the household lore
  (girlboss/had-it-insulated) and the management wisdom (girlboss/best-deal-on-the-yard).
- Example: girlboss/decorations-will-be-worn
- Logged at catalog size 141.

### "I never put it down."
- The girlboss bridge button as an object still being held: the two-register lie ends not on a
  compliment, a deflection or a stage direction of obedience (both retired) but on one thing she
  is carrying that she has no professional reason to be carrying, reported last and left alone.
- Example: "I was stood in the corridor by the cloakroom with somebody's mess jacket over my arm
  for all of that, and I never put it down." — girlboss/decorations-will-be-worn
- Logged at catalog size 141.

### "The licence survives termination — seventy years past me, and I'm the temporary part."
- The flash-of-legibility line: a real copyright-term fact stated far too calmly, in which the
  narrator ranks himself as the perishable component of his own agreement. No complaint attached.
- Example: laundry/by-continuing
- Logged at catalog size 142.

### "I never said yes to any of it and I have never stopped agreeing."
- The final-hook button: consent framed as something that was never given and has never once
  lapsed, in one flat self-cancelling sentence. Distinct from the reference example's complicit
  admissions — nothing is being permitted here, it is simply ongoing.
- Example: laundry/by-continuing
- Logged at catalog size 142.

### "Everybody does it. Nobody does it like me."
- The flat deadpan closing verse 1: a mandatory procedure everyone on the floor performs, claimed
  as a personal signature in four words, with nothing said about what the difference actually is.
- Example: girlboss/no-more-bets
- Logged at catalog size 143.

### "Every number in the right order, and one thing left out of it, and it balanced."
- The girlboss bridge lie run as the *one perfect omission*: a complete, verifiable, genuinely
  impressive account with a single item absent, and the books still reconcile. Distinct from the
  over-detailed valuation (girlboss/best-deal-on-the-yard) and the over-helpful domestic lore
  (girlboss/had-it-insulated) — nothing here is embellished, and nothing said is false.
- Example: girlboss/no-more-bets
- Logged at catalog size 143.

### "And I said the whole of it looking at the dome. Not at him."
- The girlboss bridge button as a sightline: the account is delivered to the camera rather than to
  the man who asked for it, which tells the listener who the performance was always for. Fresh
  after the retired compliment-and-deflection, the stage direction of obedience
  (girlboss/had-it-insulated) and the object still held (girlboss/decorations-will-be-worn).
- Example: girlboss/no-more-bets
- Logged at catalog size 143.

### "break's at two, cage door sticks, come down and lose properly"
- The named offer made in the setting's own losing/winning vocabulary — unmistakable, said once,
  never crude, and cut off by the hook on the following line. The verb "lose" carries the whole
  proposition, so nothing has to be described for it to be understood.
- Example: girlboss/no-more-bets
- Logged at catalog size 143.

### "I don't answer Derek, I solve Derek."
- The girlboss bridge lie run as *over-helpful*: the stakes-owner rings about three things and she
  volunteers fixes to four more he never raised, closing by taking on extra unpaid work. The third
  of the template's three lie shapes, after the over-detailed valuation
  (girlboss/best-deal-on-the-yard) and the perfect omission (girlboss/no-more-bets).
- Example: girlboss/freshly-baked
- Logged at catalog size 144.

### "I said no, Derek. That one wasn't for you."
- The girlboss bridge button as a misdirected line: she says the song's own filthy hook into an open
  phone line and across the counter simultaneously, so the stakes-owner hears the transgression in
  full and it registers as shop patter. Fresh after the retired compliment-and-deflection, the stage
  direction of obedience (girlboss/had-it-insulated), the object still held
  (girlboss/decorations-will-be-worn) and the sightline (girlboss/no-more-bets).
- Example: girlboss/freshly-baked
- Logged at catalog size 144.

### "You cannot rush a prove — the dough knows, and it tells on you later."
- The task double-entendre stated as a trade fact that also announces the song's own evidence
  mechanism, before that evidence exists. Nothing is being confessed; it is a baker's true remark
  about yeast.
- Example: girlboss/freshly-baked
- Logged at catalog size 144.

### "I am the reason this end of the market smells like anything at all."
- The flat deadpan closing the competence inventory: an unfalsifiable claim to have authored the
  entire sensory experience of a shared workplace, delivered as plain fact.
- Example: girlboss/freshly-baked
- Logged at catalog size 144.

### "I led with the number for Ian" — the bridge lie told as commercial arithmetic
- A fourth girlboss lie shape after the over-detailed valuation (girlboss/best-deal-on-the-yard),
  the over-helpful fix list (girlboss/freshly-baked) and the perfect omission
  (girlboss/no-more-bets): every word is true and verifiable, delivered as a rapid margin-and-volume
  recital, so the personal question never finds a gap to arrive in. Paired with an inversion of the
  interruption device itself — the stakes-owner rings and she was already ringing him.
- Example: girlboss/except-the-spec
- Logged at catalog size 145.

### "It isn't a deal, Ian. It's a promotion. Deals go both ways."
- The girlboss bridge button as a correction of the stakes-owner's vocabulary: praise is answered by
  refusing the word it was paid in, which restates who conceded without ever claiming it. Fresh
  after the retired compliment-and-deflection, the stage direction of obedience, the object still
  held, the sightline and the misdirected line.
- Example: girlboss/except-the-spec
- Logged at catalog size 145.

### "It's a good melon. I tell him it's a good melon. He has to sit down."
- The verdict delivered flat and favourably, with the instrument's collapse reported in the same
  breath as a physical consequence — the good news is what finishes him.
- Example: girlboss/except-the-spec
- Logged at catalog size 145.

### "That's on the recording. They keep those seven years."
- The girlboss bridge button as the transgression preserved in an official record and simply left
  there — no risk acknowledged, no move to retrieve it, the retention period quoted like a warranty
  term. Fresh after the retired compliment-and-deflection, the obedience stage direction, the object
  still held, the sightline, the misdirected line and the corrected terminology.
- Example: girlboss/one-careful-owner
- Logged at catalog size 146.

### "Nobody pays three fifty for a coat of wax. He paid for the quarter of an hour it took to talk him into it."
- The unearned moral as an itemisation of what the customer actually bought — the upsell repriced as
  payment for her attention, with the conclusion that he would pay it again. An eighth flavour after
  the trade rule quoted straight, the household lore, the management wisdom, the claimed authorship
  of an effect, the corrected proverb, the mentorship handed down and the authored policy.
- Example: girlboss/one-careful-owner
- Logged at catalog size 146.

### "he signs the finance on the bonnet without reading the APR, and he's a mortgage adviser"
- The scoreboard as a professional failing at his own profession: the instrument's deterioration is
  measured by him neglecting the exact competence he is paid for. Distinct from the band's other
  scoreboards in that the ruined thing is his expertise rather than his stock, his etiquette, his
  equipment or his negotiating position.
- Example: girlboss/one-careful-owner
- Logged at catalog size 146.

### "And I said: wouldn't I. Well. That was careless of me."
- The Carry On refusal inverted: told that she turned him down inside his own dream, she treats it as
  a lapse in her own standards and books the repeat. Transposed from Carry On Doctor's "No, you
  wouldn't let me" rather than quoted — the exchange runs in her clinic's own vocabulary, and the
  second night is a real feature of the protocol rather than a flirtation.
- Example: girlboss/first-night-effect
- Logged at catalog size 147.

### "Whatever your body does in this building while you're under, it stays in the file."
- The unearned moral as a confidentiality assurance that is also an inventory of what she holds:
  offered as bedside reassurance, received as comfort, and true in both directions. A ninth flavour
  after the trade rule quoted straight, the household lore, the management wisdom, the claimed
  authorship of an effect, the corrected proverb, the mentorship handed down, the authored policy
  and the itemisation of what was really bought.
- Example: girlboss/first-night-effect
- Logged at catalog size 147.

### "That's the first-night effect. That's documented. That isn't me."
- The clean exit closing on a denial nobody asked for, citing a real clinical phenomenon to explain
  away an effect she has spent the whole song producing. Distinct from girlboss/thats-why-i-bought-them's
  "I don't argue with the literature", which defers to a source to license a claim — this one
  invokes the literature to decline credit she has already taken.
- Example: girlboss/first-night-effect
- Logged at catalog size 147.

### "I said I have a concern." — the bridge lie that makes the stakes-owner do the reassuring
- A seventh girlboss lie shape: she rings in first and volunteers a professional worry about the
  client's readiness, so the call turns into the founder praising her diligence at length. The
  interruption device inverted a second way — girlboss/except-the-spec reversed its direction, this
  one reverses who is comforting whom. Nothing untrue is said and the concern is real.
- Example: girlboss/and-a-deposit
- Logged at catalog size 148.

### "I logged the call. Fifteen minutes. It goes on his account."
- The girlboss bridge button as billing: the interruption itself is charged to the member it was
  about. Fresh after the retired compliment-and-deflection, the obedience stage direction, the object
  still held, the sightline, the misdirected line, the corrected terminology and the retention period.
- Example: girlboss/and-a-deposit
- Logged at catalog size 148.

### "They come here to practise being wanted. I've said that to Mrs Alderton. She thinks I'm being modest."
- The unearned moral misread by the stakes-owner as humility: she states plainly what the business
  actually sells and is credited with self-deprecation for it. A tenth flavour after the trade rule
  quoted straight, the household lore, the management wisdom, the claimed authorship of an effect,
  the corrected proverb, the mentorship handed down, the authored policy, the itemisation of what was
  really bought and the confidentiality assurance.
- Example: girlboss/and-a-deposit
- Logged at catalog size 148.

### "I got my complaint in first, because a complaint is the quickest way to be believed."
- An eighth girlboss lie shape: pre-emptive mild criticism of the instrument, entirely true and
  fully documented on his own timesheet, which settles the account of the day before anyone can ask a
  different question. Then reversed in the same breath by recommending him elsewhere, so the
  complaint cannot be read as a grievance.
- Example: girlboss/hold-it-there
- Logged at catalog size 149.

### "I said he's the best we've had. I've recommended him to the prep school."
- The girlboss bridge button as a referral: the instrument is passed on to another institution with a
  glowing word, which closes the call, disproves any motive and puts him somewhere she can reach.
  Fresh after the obedience stage direction, the object still held, the sightline, the misdirected
  line, the corrected terminology, the retention period and the billed interruption.
- Example: girlboss/hold-it-there
- Logged at catalog size 149.

### "Then he asked me, for the light, if I would do the banana one myself."
- The request laundered through a technical pretext — the instrument supplies his own professional
  reason for what he is asking, so she never has to offer anything and simply agrees to her own
  syllabus. Her answer ("It's on the syllabus. I do it every Thursday at eleven") declines the
  subtext entirely by being true.
- Example: girlboss/hold-it-there
- Logged at catalog size 149.

### "Emil — do you know what I called you, when I still had my own hands?"
- The chorus's direct question aimed at the person the narrator wronged, with no "so tell me,
  [address], tell me" scaffold — and unanswerable in the worst way, since the man it is asked of has
  spent the song caring for him without comment.
- Example: the-bell-knows-my-name/the-bloom-i-cut
- Logged at catalog size 150.

### "I was the bloom I cut."
- The communal shout-back line: the song's entire turn in five words, the pruning logic of the
  verses applied to the man who spent his life stating it. Deliberately not the "but God, [pronoun]"
  pivot and not the retired "and the [abstract] didn't/never [fix/save] me" landing formula.
- Example: the-bell-knows-my-name/the-bloom-i-cut
- Logged at catalog size 150.

### "and he is careful round my throat"
- The verse-2 detail that carries the whole reversal without stating it: the brother he resented for
  forty years now shaves him, humming, with a blade at his neck, and is gentle. No feeling narrated
  and no forgiveness announced.
- Example: the-bell-knows-my-name/the-bloom-i-cut
- Logged at catalog size 150.

### "and I'd have said the same."
- The communal shout-back line as a concession rather than a lament: the crowd catches and repeats
  the narrator's agreement with the people excluding him. It is what keeps the song out of
  purple-dog's territory — no villain is available, because the narrator grants the rule and would
  have applied it to somebody else. Deliberately not the "but God, [pronoun]" pivot and not the
  retired "and the [abstract] didn't/never [fix/save] me" landing formula.
- Example: the-bell-knows-my-name/born-in-a-stable
- Logged at catalog size 151.

### "Somebody put a hand flat on my chest — kindly. Not unkindly."
- The exclusion delivered as a courtesy at a graveside, with the gentleness insisted on twice and no
  offence taken. Carries the whole verdict of the song in a gesture, and nobody in the scene is
  cruel — the same "no villain, just a decent impulse landing sideways" register the Guessed spec
  names, borrowed for a funeral.
- Example: the-bell-knows-my-name/born-in-a-stable
- Logged at catalog size 151.

### "Rada — was there ever a word for what I was to you?"
- The chorus's direct question, aimed at the dead woman who raised him and asking for a *category*
  rather than an admission. Deliberately not the shape used one song earlier
  (the-bell-knows-my-name/the-bloom-i-cut's "Emil — do you know what I called you") — a named
  address followed by a question about the other person's knowledge is now spent; this one asks
  whether the relationship ever had a name at all.
- Example: the-bell-knows-my-name/born-in-a-stable
- Logged at catalog size 151.

### "The line has a name and I have a number."
- The flash-of-legibility line: the whole exchange stated as an asymmetry of naming, flat, with no
  complaint attached and nothing asked for.
- Example: laundry/keep-her-fed
- Logged at catalog size 152.

### "which is fair enough, honestly, considering. A house. Both cars. The lot."
- The under-reaction rule applied to an amputation: a fingertip entered on the credit side of a
  ledger against a mortgage and two vehicles, and found to balance. No grievance and no irony
  available in the delivery.
- Example: laundry/keep-her-fed
- Logged at catalog size 152.

### "I have said that out loud, in a canteen, to people."
- The final-hook button: devotion to the machine offered as evidence against himself, with the
  witnesses specified. Distinct from the band's other closing admissions in that nothing is being
  confessed — he is citing the statement as proof of how good she has been to him.
- Example: laundry/keep-her-fed
- Logged at catalog size 152.

### "I put a four. It was not a four."
- The flash-of-legibility line: the fraud at the centre of the whole exercise admitted in seven
  words, with no account of what the real figure would have been and no defence offered.
- Example: laundry/one-to-ten
- Logged at catalog size 153.

### "the number went down every week and nothing else moved at all"
- The final-hook restatement: measurable improvement and total stasis reported as the same fact,
  flat, with the instrument's success and the man's condition entirely uncoupled.
- Example: laundry/one-to-ten
- Logged at catalog size 153.

### "I'd put a two today. I'd put a two and I would be telling the truth."
- The closing button: the score has become accurate, and the reason it is accurate is the thing the
  song will not say. Honesty arrives only once there is nothing left to misreport.
- Example: laundry/one-to-ten
- Logged at catalog size 153.

### "It worked. First go. Twenty years of doing the other thing."
- The one-line-that-lands: a result and the cost of not having tried it, in two flat fragments, with
  no account of why she hadn't. The final hook swaps the second half ("And I have got it written
  down"), which is the one-word-changes-the-ending device.
- Example: guessed/say-it-and-stop
- Logged at catalog size 154.

### "I've written down what I did, in case it stops working."
- The drop-out kept deliberately **managed** rather than cracked (see guessed/template.md): she meets
  a small success by documenting it as a procedure she doesn't trust, which is her own technique
  still running. The ache is entirely in the contingency, and nothing is confessed. Contrast
  guessed/dont-look-at-her-hand's "I want it back", where the apparatus fails instead — that mode
  stays rare by design.
- Example: guessed/say-it-and-stop
- Logged at catalog size 154.

### "I've read that forum since it started. There's nothing of mine on it."
- The unspent-expertise line delivered as a fact about a website: total attendance and zero standing
  stated without complaint, and without the retired "nobody asked" construction. The lurker thesis
  in its most literal form.
- Example: guessed/say-it-and-stop
- Logged at catalog size 154.

### "It is a very good collection. That isn't the interesting part."
- The one-line-that-lands: an accurate boast immediately declined as the subject, refusing the noun
  in the same breath — what the interesting part is never gets said anywhere in the song.
- Example: guessed/ones-with-names-on
- Logged at catalog size 155.

### "I still water the ones with names on."
- The drop-out kept **managed**: an ongoing maintenance routine stated as a fact, for cuttings nobody
  is coming to collect. Nothing is confessed, nobody is blamed, and the ache is entirely in the
  tense. A second managed drop-out in a different mode from guessed/say-it-and-stop's documentation
  — that one wrote a success up as a procedure, this one keeps a service running for absent people.
- Example: guessed/ones-with-names-on
- Logged at catalog size 155.

### "I water it first because it's nearest the tap."
- The disproportionate shrug: the one plant that matters gets tended first, and a plumbing reason is
  supplied for it immediately. The logistics are true and they are also the cover.
- Example: guessed/ones-with-names-on
- Logged at catalog size 155.

### "I know what's wrong with one from the doorway. There's nowhere to put that."
- The unspent-expertise line: real diagnostic competence named, then the absence of any use for it
  stated as a storage problem rather than a grievance. Avoids the retired "nobody asked"
  construction and the word "skill" (guessed/its-a-life-skill).
- Example: guessed/ones-with-names-on
- Logged at catalog size 155.

### "And how long does a thing like that stay said?"
- The chorus's direct question, aimed at the dead man in verse 2 but asking about the durability of
  a sentence rather than about his conduct. Deliberately neither of the two spent Bell shapes — not
  the retired named-address-plus-question-about-knowledge, and not "was there ever a word for what I
  was to you".
- Example: the-bell-knows-my-name/best-thing-i-ever-ate
- Logged at catalog size 156.

### "and it was the best thing I ever ate."
- The communal shout-back: a starving child's memory stated as pleasure, with no apology attached
  and no defence offered, sung by the whole room. It refuses both available positions — the
  accusation is not denied and it is not repented — and the grief is that this is what a hundred
  years of characterisation was built on. Not the "but God, [pronoun]" pivot, not the retired
  "didn't/never fix me" formula, and not the concession shape of born-in-a-stable.
- Example: the-bell-knows-my-name/best-thing-i-ever-ate
- Logged at catalog size 156.

### "His name is still the word for it. They use it about children who weren't born."
- The verse-2 loss relocated from a death to a reputation: the man has been dead for decades and the
  cost still being paid is that his name became the term, applied to people who did not exist when
  it happened.
- Example: the-bell-knows-my-name/best-thing-i-ever-ate
- Logged at catalog size 156.

### "I got a first. It's in a tube on top of the wardrobe." → "It's in the tube with the other one now."
- The one-line-that-lands: a credential and its storage, stated in one breath with no comment
  attached, and the final hook adds a second certificate to the same tube in four words. That
  substitution is the whole ending.
- Example: guessed/name-of-the-course
- Logged at catalog size 157.

### "I did the course. I got a distinction."
- The drop-out kept **managed**: she takes the condescending suggestion literally, completes it, and
  excels — reporting both facts as flatly as a receipt. A third managed mode after documenting a
  success as procedure (guessed/say-it-and-stop) and running a maintenance routine for absent people
  (guessed/ones-with-names-on): here the management is compliance, carried through to its most
  absurd and most impressive end.
- Example: guessed/name-of-the-course
- Logged at catalog size 157.

### "I fix his slides before he sends them. He thinks the template does that."
- The unspent-expertise line: uncredited competence attributed by its beneficiary to software. Shows
  the zero-standing ache entirely through a concrete detail, per the spec's instruction after the
  "nobody['s] ever asked" construction was retired.
- Example: guessed/name-of-the-course
- Logged at catalog size 157.

### "I wrote down the name of the course."
- The disproportionate shrug: told to consider studying the subject she has a first in, she
  cooperates with the suggestion and takes a note. No correction offered and no offence recorded.
- Example: guessed/name-of-the-course
- Logged at catalog size 157.

### "And the dogs had a good night. Best night's sleep they'd had in years."
- The verse-2 button: the loss reported through the animals' comfort, with the narrator declining to
  say anything about his own night. The cruelty is entirely in the cheerfulness of the observation.
- Example: the-bell-knows-my-name/only-bark-at-strangers
- Logged at catalog size 158.

### "they only bark at strangers."
- The communal shout-back: a plain fact about dogs that has become the reason a house lost somebody,
  chanted by a room. Comforting on the first hearing and unbearable by the last. Not the "but God,
  [pronoun]" pivot, not the retired "didn't/never fix me" formula, and distinct from the concession
  (born-in-a-stable) and the refusal-of-both-positions (best-thing-i-ever-ate) shapes.
- Example: the-bell-knows-my-name/only-bark-at-strangers
- Logged at catalog size 158.

### "Twenty years of nothing. You stop getting up. Anybody would."
- The confession offered with its own defence attached and the defence conceded to be reasonable —
  the narrator neither excuses himself nor accepts blame, and invites the listener to agree that he
  behaved normally, which is the worst available outcome.
- Example: the-bell-knows-my-name/only-bark-at-strangers
- Logged at catalog size 158.

### "there is no working smoke alarm in this house and everyone who lives here knows." → "…and everyone who lives here sleeps."
- The flash-of-legibility line: the hazard stated plainly, in full, with the household's awareness of
  it given as the closing clause rather than as a mitigation. The final hook swaps the last word and
  makes the same sentence worse.
- Example: laundry/it-does-that
- Logged at catalog size 159.

### "we are all still here, which is the evidence, which is the whole of the evidence"
- The closing button: the absence of harm so far offered as proof of safety, with the narrator
  naming the poverty of that proof in the same breath and finding it sufficient anyway. The thesis
  of the whole device, said flat.
- Example: laundry/it-does-that
- Logged at catalog size 159.

### "It's not gone off in anger. That's the phrase. Somebody said it once and we kept it."
- A household's inherited formula for the fault, quoted and immediately sourced — the origin
  forgotten, the sentence load-bearing. Shows how the deviation was talked into being normal without
  anyone deciding anything.
- Example: laundry/it-does-that
- Logged at catalog size 159.

### "Six years of that system, and I am the only name in it."
- The one-line-that-lands: her refusal to join the shared account stated as an audit fact, with the
  consequence left entirely unspoken — integrity and exposure are the same sentence.
- Example: guessed/the-only-name-in-it
- Logged at catalog size 160.

### "If it ever goes wrong, I'm the only one they can find."
- The drop-out kept **managed**: a risk assessment rather than a cry, delivered as a flat conditional
  about a thing that has not happened. A fourth managed mode after documenting a success as
  procedure (guessed/say-it-and-stop), running a maintenance routine for absent people
  (guessed/ones-with-names-on) and compliance carried to its absurd end (guessed/name-of-the-course).
- Example: guessed/the-only-name-in-it
- Logged at catalog size 160.

### "Said it like a kindness. It is a kindness. It does save a lot of hassle."
- The band's no-villain rule stated three times over: the advice that normalised the deviation is
  conceded to be well meant, true, and genuinely useful, before she declines it anyway. Nobody in
  the song is wrong except in aggregate.
- Example: guessed/the-only-name-in-it
- Logged at catalog size 160.

### "I know who did every one of those. I could tell you by the timestamps."
- The unspent-expertise line: she can de-anonymise the whole floor's activity from behaviour alone,
  and the capability has no recipient. Concrete detail in place of the retired "nobody asked"
  construction.
- Example: guessed/the-only-name-in-it
- Logged at catalog size 160.

### "you didn't miss it. You renamed it."
- The direct accusation: the institution is credited with full awareness and charged with
  vocabulary rather than negligence. Extended in the final chorus to "And you laminated it."
- Example: purple-dog/laminated
- Logged at catalog size 161.

### "and I've read it back to myself / in the car park, out loud, to check"
- The pre-chorus crack shown through behaviour rather than announced, per the spec's ban on the
  narrator naming his own state: a man checking his own sentences aloud, alone, before he is allowed
  to say them indoors.
- Example: purple-dog/laminated
- Logged at catalog size 161.

### "Laminated. Somebody laminated that."
- The petty trigger's button: the institution's reply to a definition of institutional failure is a
  noticeboard policy, and the detail that finishes him is that somebody took the trouble to
  laminate it. Effort spent on the wrong object, noticed and repeated.
- Example: purple-dog/laminated
- Logged at catalog size 161.

### "So I read him the clause. Slowly. All of it. Including the bit in brackets. And then I told him who wrote the clause."
- A ninth girlboss lie shape, and the only one containing no lie at all: she answers the challenge by
  quoting the governing document, which is authoritative, correct, and hers — the third revision,
  two years ago. The document was aligned to the practice rather than the practice to the document,
  and she chaired the review that approved it.
- Example: girlboss/the-new-baseline
- Logged at catalog size 162.

### "And I put the next audit in for March while he was still talking."
- The girlboss bridge button as forward scheduling: the interruption is closed by booking the next
  one, during the call, unprompted. Fresh after the obedience stage direction, the object still
  held, the sightline, the misdirected line, the corrected terminology, the retention period, the
  billed interruption and the referral.
- Example: girlboss/the-new-baseline
- Logged at catalog size 162.

### "he says: well, it's been like that a while, hasn't it. And I said: it has. So we'll call that acceptable."
- The deviation normalised by consent rather than by concealment: she asks the newest person on site
  what he thinks, agrees with his observation, and converts it into a standard in the same breath.
  He signs first; she countersigns; nothing is hidden from anybody at any point.
- Example: girlboss/the-new-baseline
- Logged at catalog size 162.

### "And what was I meant to do with seven horses?"
- The chorus's direct question, aimed at the dead woman and asking about logistics rather than about
  grief — the smallness of the practical problem set against the size of the loss, with no answer
  available in either register. Nameless in the chorus by design: "[Name] — [question]" is spent
  across the band (see the-bloom-i-cut, born-in-a-stable).
- Example: the-bell-knows-my-name/they-went-up-quiet
- Logged at catalog size 163.

### "The man asked if they had names. I said not really."
- The verse-2 lie that costs nothing and gives everything away, answered immediately by the truth he
  does not say to the buyer: "They have all got names. I have called every one of them by name this
  morning." The denial is protective of him rather than of them.
- Example: the-bell-knows-my-name/they-went-up-quiet
- Logged at catalog size 163.

### "they went up quiet."
- The communal shout-back: the animals' trust rendered as the worst possible outcome, since their
  compliance is what made the disposal easy. Three flat words, no blame anywhere in them. Distinct
  from the concession (born-in-a-stable), the refusal-of-both-positions (best-thing-i-ever-ate), the
  turned logic (the-bloom-i-cut) and the mechanism (only-bark-at-strangers).
- Example: the-bell-knows-my-name/they-went-up-quiet
- Logged at catalog size 163.

### "Would you rather I had said it?"
- The chorus's direct question, offering the alternative outcome to the person it would have landed
  on and declining to guess her answer. Nameless in the chorus by design, since "[Name] —
  [question]" is spent across the band.
- Example: the-bell-knows-my-name/so-i-sing-it
- Logged at catalog size 164.

### "so I sing it."
- The communal shout-back: three flat words that answer the song's own question and refuse to
  dignify the alternative. The crowd sings a sentence about why the man is singing, at the exact
  moment he is doing it. Distinct from the concession (born-in-a-stable), the refusal of both
  positions (best-thing-i-ever-ate), the turned logic (the-bloom-i-cut), the mechanism
  (only-bark-at-strangers) and the compliance (they-went-up-quiet).
- Example: the-bell-knows-my-name/so-i-sing-it
- Logged at catalog size 164.

### "Then she danced with her husband, who is a good man, and I played for that as well."
- The verse-2 button: the rival conceded to be decent in a subordinate clause, and the narrator's own
  participation in the celebration reported as a job he completed. No grievance is available anywhere
  in the line.
- Example: the-bell-knows-my-name/so-i-sing-it
- Logged at catalog size 164.

### "You wrote anxious on the front of it. I read it upside down."
- The direct accusation: a single word on a chart, seen by the patient from the wrong side of the
  desk, which converts every subsequent thing he says into evidence for it. Extended in the final
  chorus to "I read everything upside down now."
- Example: purple-dog/isnt-plugged-into-anything
- Logged at catalog size 165.

### "you're pressing that a lot. / A lot. I've pressed it three times in four days. I counted."
- The petty trigger, complete with its rebuttal: a nurse's mild observation answered by a figure he
  can produce because he has been keeping one. The smallness of the number is the whole grievance,
  and the fact that he counted is the whole diagnosis.
- Example: purple-dog/isnt-plugged-into-anything
- Logged at catalog size 165.

### "and I've started writing down the times / on the back of the menu card"
- The pre-chorus crack shown through behaviour rather than announced, per the spec's ban on
  self-diagnosis: a man who has begun keeping a private record on hospital stationery. Distinct from
  purple-dog/laminated's reading his own sentences aloud in a car park.
- Example: purple-dog/isnt-plugged-into-anything
- Logged at catalog size 165.

### "Two coats, and there's no telling anybody was ever in it."
- The one-line-that-lands: the standard of her own workmanship stated as a fact, with the thing it
  achieves — the removal of all evidence that she lived somewhere — offered as the measure of
  success. No complaint attached and no irony available in the delivery.
- Example: guessed/two-coats
- Logged at catalog size 166.

### "I've still got the paint. It's under the sink at the new place. Same colour."
- The drop-out kept **managed**, in a fifth mode: a small keeping. After documenting a success as
  procedure (guessed/say-it-and-stop), a maintenance routine for absent people
  (guessed/ones-with-names-on), compliance carried to its absurd end (guessed/name-of-the-course) and
  a risk assessment (guessed/the-only-name-in-it) — here she has kept the colour of the room she
  erased herself from, stored somewhere practical, for no stated reason.
- Example: guessed/two-coats
- Logged at catalog size 166.

### "Seven picture hooks in that front room. I put every one of them in myself. And I took every one of them out, and you would not find them with a thumbnail."
- The unspent-expertise line fused with the song's subject: real competence at filling and finishing,
  demonstrated on the only physical evidence that she had ever hung anything anywhere. Avoids the
  retired "nobody asked" construction by making the ache a decorating standard.
- Example: guessed/two-coats
- Logged at catalog size 166.

### "Nobody comes for a theme. They come on the Friday when they've got it."
- The one-line-that-lands: the actual mechanism of a village fundraiser stated as plain fact, in
  the middle of a song celebrating the garlands. Her judgement is fully visible and nobody in the
  song hears it.
- Example: penny-rich/say-it-was-the-theme
- Logged at catalog size 167.

### "There's no minutes for a date. There's minutes for a theme."
- The plain line at the break: her contribution is structurally unrecordable — the committee minutes
  hold the hour of debate and not the decision that decided it. Delivered flat, once, to a room that
  is already clapping, and never returned to.
- Example: penny-rich/say-it-was-the-theme
- Logged at catalog size 167.

### "the vicar stood up at the end and thanked Malcolm for a marvellous raffle. / He does do a marvellous raffle. He does."
- The correction she doesn't make, plus the dry beat at the wrong-story-teller's expense — and the
  credit is conceded as accurate, warmly, because it is. Malcolm did do a marvellous raffle. Nobody
  is contemptible anywhere in the song.
- Example: penny-rich/say-it-was-the-theme
- Logged at catalog size 167.

### "He signs where I put the pencil cross, and I put it in the right place."
- The one-line-that-lands for the money song: the division of labour stated as a physical fact about
  a pencil, with the authority sitting entirely in who chooses the location. Plain line at the break:
  "There's not one account in this house with my name on it."
- Example: penny-rich/let-him-sign-it
- Logged at catalog size 173.

### "There's no knack. There's an order, and I do it in the order, every time."
- The one-line-that-lands for the dog song, and the spec's "show the working" rule in a sentence.
  Plain line at the break: "He's not clever. I'm not clever. It's the same order every time." The
  method is given away in full and the giving-away costs her nothing.
- Example: penny-rich/call-it-a-knack
- Logged at catalog size 173.

### "It isn't the sky. It's the gate. And I have said so, out loud, to people."
- The one-line-that-lands for the weather song, with the sharpest version of the band's engine: she
  has *already told them* and it made no difference. Plain line at the break: "I've told them about
  the gate. I've told them all about the gate." No grievance is stated anywhere near it.
- Example: penny-rich/say-the-sky-told-me
- Logged at catalog size 173.

### "You want the hymn they can all sing. Not the one he liked. The one they know."
- The one-line-that-lands for the funeral song: professional judgement about a service, stated
  warmly, which quietly concedes that the dead man's preference is the wrong criterion. Plain line at
  the break: "There was nobody left to ring about Cyril. So I rang everybody else."
- Example: penny-rich/say-the-man-did-it
- Logged at catalog size 173.

### "She's got his eyes and his mouth. She counts the change before she leaves the counter."
- The one-line-that-lands for the inheritance song: two clauses conceding the visible inheritance and
  claiming the invisible one, without saying which is hers. Plain line at the break: "I taught her on
  a Saturday and she has got no memory of it at all."
- Example: penny-rich/her-fathers-daughter
- Logged at catalog size 173.

### "Boots were sixty pound and they've been soled four times. That's four pound a year."
- The one-line-that-lands for the batch's single transactional song, and the inversion that keeps it
  out of the shopping corner: the bargain-hunter's real judgement is knowing the one thing to pay
  full price for. Plain line at the break: "The boots will see me out. I did that sum an' all."
- Example: penny-rich/four-pound-a-year
- Logged at catalog size 173.

### "You didn't ask what it went to. You asked if I'd used it lately."
- The direct accusation: two questions set side by side, one of which would have established the
  thing's purpose and one of which established only its recent activity. The wrong test, named
  without raising his voice.
- Example: purple-dog/the-same-drawer
- Logged at catalog size 174.

### "and I took one out and put it in my coat / before the van come, and I've not said"
- The pre-chorus crack shown through behaviour rather than announced, per the spec's ban on
  self-diagnosis: a man who quietly rescued one item and has kept that to himself. Distinct from
  purple-dog/laminated's reading his own sentences aloud in a car park and
  purple-dog/isnt-plugged-into-anything's writing the times on a menu card.
- Example: purple-dog/the-same-drawer
- Logged at catalog size 174.

### "It isn't a pound. It's a pound and a fortnight of not having one."
- The rebuttal to the obvious objection, pre-empted and answered in his own mouth before anyone can
  make it — the cost restated in the only unit that matters to him, which is delay rather than money.
- Example: purple-dog/the-same-drawer
- Logged at catalog size 174.

### "I could sleep. I've decided not to." → "I could sleep. I don't think I'd come back the same."
- The flash-of-legibility line: the deprivation named as a choice rather than a symptom, in six flat
  words, and the final hook replaces the second half with the reason. The band's under-reaction rule
  applied to a man who is doing this to himself on purpose.
- Example: laundry/level
- Logged at catalog size 175.

### "Half four is a colour, not a time."
- The grotesque non-sequitur as a category error stated with total confidence, and immediately
  corroborated by an appeal to other people in the same state ("Anybody up at half four will tell you
  the same thing").
- Example: laundry/level
- Logged at catalog size 175.

### "the woman who does the filing has been in three of these now and I have started saying good morning"
- The closing button: a recurring figure from inside the dream greeted by a waking man as an
  ordinary colleague, reported with no alarm whatsoever. The song's only statement about how far this
  has gone, and it arrives as manners.
- Example: laundry/level
- Logged at catalog size 175.

### "Somebody was trying very hard not to lose anything."
- Disassembler's one-human-sentence breakdown, and the first test of the rule. It contains no
  tooling vocabulary, it has a subject and a verb belonging to a person, and it recasts nineteen
  lines of comic filenames as an act of fear. Nothing in the song responds to it; the beat returns
  and it is filenames again. Deliberately **not** about time or latency — the band's provisional
  engine will reach for that reflexively and the spec flags it.
- Example: disassembler/use-this-one
- Logged at catalog size 177.

### Two files with the same modified timestamp as the closing joke
- The outro: the two candidate finals are shown to have been modified in the same minute, so the
  question the whole song is asking has no answer available anywhere in the system. Stated as bare
  metadata, twice, with no comment.
- Example: "report_final_USE_THIS_v2.doc / modified eleven forty-seven / report_FINAL_FINAL.doc /
  modified eleven forty-seven" — disassembler/use-this-one
- Logged at catalog size 177.

### "I put my ear against it, which is not something anyone is supposed to do."
- Disassembler's one-human-sentence breakdown, second instance and deliberately in a third
  territory: not time (the provisional engine's reflex) and not the fear of losing things
  (disassembler/use-this-one). This one is an expert doing an unprofessional thing — diagnosing by
  ear, admitting it, and continuing. No tooling vocabulary in it, and nothing in the song responds.
- Example: disassembler/still-passed
- Logged at catalog size 178.

### "current pending sector: sixteen" → "current pending sector: seventeen"
- The outro non-resolution: the same field is read out twice, once mid-verse and once at the end,
  and it has gone up by one while the song was playing. Stated as bare metadata with no comment, and
  it is the only event in the track.
- Example: disassembler/still-passed
- Logged at catalog size 178.

### "I have used this every single day for twenty years and I have not thanked anybody."
- Disassembler's one-human-sentence breakdown, fourth instance and fourth distinct territory —
  after fear of losing things (use-this-one) and unprofessional expertise (still-passed), and
  deliberately not time, which is the provisional engine's reflex. This one is gratitude, or its
  absence: an entire edifice maintained by people he will never meet, used daily, unacknowledged.
  The warm turn at the end of a comic song, and nothing responds to it.
- Example: disassembler/not-unix
- Logged at catalog size 179.

### "checking whether build environment is sane... yes / configure: error: C compiler cannot create executables"
- The outro non-resolution: the same check that passed in the build is read out again and
  immediately followed by the failure it did not predict. Prose rather than a moved number, per the
  band's counting rule, and the sanity check being the line that precedes the collapse is the whole
  joke.
- Example: disassembler/not-unix
- Logged at catalog size 179.

### "I used to be the one arguing for the other thing."
- Disassembler's one-human-sentence breakdown, fifth instance and sixth territory — after fear of
  losing things, unprofessional expertise, gratitude and allegiance, and deliberately never time.
  This one is **recantation**: a whole biography in nine words, admitting he has changed sides
  without saying which side he is on now. Nothing responds to it.
- Example: disassembler/worse-is-better
- Logged at catalog size 181.

### "it is better to get half of the right thing available / so that it spreads / improve it later"
- The outro non-resolution as a promise nobody keeps, quoted from the essay's own argument and left
  hanging. Deliberately **not** a repeat of a build line — disassembler/not-unix and
  disassembler/the-front-fell-off both close by re-reading something from their builds, and a third
  would make it the band's default ending.
- Example: disassembler/worse-is-better
- Logged at catalog size 181.

### "I would like you to come here yourself and not send the picture."
- Disassembler's one-human-sentence breakdown, sixth instance and seventh territory — after fear of
  losing things, unprofessional expertise, gratitude, allegiance and recantation, and never time.
  This one is **presence**: a polite request for the single thing the whole apparatus cannot supply,
  which is another person in the room. Nothing responds to it.
- Example: disassembler/the-machine-stops
- Logged at catalog size 182.

### "the Machine is omnipotent / the Machine is eternal / blessed is the Machine"
- The outro non-resolution as doctrine rather than a fault: the track ends on the system's own
  scripture, immediately after the drop has established that it is failing. Deliberately not a
  re-read of a build line — disassembler/not-unix and disassembler/the-front-fell-off both close
  that way and a third would fix it as the band's default — and deliberately not a moved number, per
  the counting rule.
- Example: disassembler/the-machine-stops
- Logged at catalog size 182.

### "I went home and told my wife about it."
- Disassembler's one-human-sentence breakdown, seventh instance and eighth territory — after fear of
  losing things, unprofessional expertise, gratitude, allegiance, recantation and presence, and never
  time. This one is **joy reported to somebody who cannot share it**: the best day of a career,
  carried home, in nine words that decline to say how it was received. Nothing responds to it, which
  for once is the joke rather than the wound.
- Example: disassembler/no-callers
- Logged at catalog size 183.

### "there is no longer a retry path / there is no longer a flag for it / there is nothing there at all"
- The outro non-resolution as an inventory of absence — a fresh closing shape for the band after the
  re-read build line (not-unix, the-front-fell-off), the moved number (use-this-one, still-passed),
  the unkept promise (worse-is-better) and the doctrine (the-machine-stops). Ends on what no longer
  exists, cheerfully.
- Example: disassembler/no-callers
- Logged at catalog size 183.

### "There is a rule about me that I am not allowed to read."
- Disassembler's one-human-sentence breakdown, eighth instance and ninth territory — after fear of
  losing things, unprofessional expertise, gratitude, allegiance, recantation, presence and joy, and
  never time. This one is **being governed by something withheld**, stated as a flat fact rather
  than an accusation, which is what keeps it out of purple-dog's lane: no anger, no institution
  blamed, just a man reporting the shape of his own constraints.
- Example: disassembler/directive-four
- Logged at catalog size 184.

### "I was in the room when we agreed what it was for."
- Disassembler's one-human-sentence breakdown, ninth instance and tenth territory — after fear of
  losing things, unprofessional expertise, gratitude, allegiance, recantation, presence, joy and
  being governed by something withheld. This one is **complicity in the stated purpose**: he helped
  write the claim the rest of the song disproves, and says so without defending it. Deliberately
  avoids "I wrote that sentence", which ultracoase/certain-too-early owns almost verbatim.
- Example: disassembler/as-designed
- Logged at catalog size 185.

### "the contract has been renewed for a further three years / no changes were requested"
- The outro non-resolution as continuation: the track ends by extending the thing it has just spent
  three minutes describing, with nobody asking for anything to be different. A seventh distinct
  closing shape for the band, after the re-read build line, the moved number, the unkept promise,
  the doctrine, the inventory of absence and the ending by omission.
- Example: disassembler/as-designed
- Logged at catalog size 185.

### "I admire it and I have not written a line of it in twenty years."
- Disassembler's one-human-sentence breakdown, tenth instance and eleventh territory — after fear of
  losing things, unprofessional expertise, gratitude, allegiance, recantation, presence, joy, being
  governed by something withheld and complicity. This one is **admiration without adoption**, both
  halves in one sentence, neither excusing the other. It is also the only sentence in the band so
  far that agrees with everything the build just said.
- Example: disassembler/admired-not-used
- Logged at catalog size 186.

### "it has been on the recommended reading list since the list was written / the list is not reviewed"
- The outro non-resolution as a recommendation nobody acts on and nobody withdraws. An eighth
  distinct closing shape for the band, after the re-read build line, the moved number, the unkept
  promise, the doctrine, the inventory of absence, the ending by omission and the contract renewal.
- Example: disassembler/admired-not-used
- Logged at catalog size 186.

### "I set my watch by it for eleven years and it was always right."
- Disassembler's one-human-sentence breakdown, eleventh instance and twelfth territory — and the
  first about **time**, which the spec had flagged as the provisional engine's reflex and warned
  against. Earned here because the subject is literally the time protocol, and because the sentence
  is affectionate rather than impatient: a man reporting that something was reliable, next to the
  numbers explaining how that reliability was used.
- Example: disassembler/ask-it-the-time
- Logged at catalog size 187.

### "restrict default noquery / that is the fix / that was always the fix"
- The outro non-resolution as a remedy so small it indicts the scale of the harm — one directive in
  one config file. A ninth distinct closing shape for the band, after the re-read build line, the
  moved number, the unkept promise, the doctrine, the inventory of absence, the ending by omission,
  the contract renewal and the unwithdrawn recommendation.
- Example: disassembler/ask-it-the-time
- Logged at catalog size 187.

### "A stranger left me a note about this and the stranger was right."
- Disassembler's one-human-sentence breakdown, twelfth instance and thirteenth territory — after
  fear of losing things, unprofessional expertise, gratitude, allegiance, recantation, presence,
  joy, being governed by something withheld, complicity, admiration without adoption and time. This
  one is **inheritance from an anonymous predecessor**: knowledge arriving across years from
  somebody who will never be identified or thanked, and turning out to be correct.
- Example: disassembler/leave-it
- Logged at catalog size 188.

### "blame: unchanged for eleven years / blame: unchanged / the branch is still there"
- The outro non-resolution as endurance: the closing evidence is that nothing has been touched. A
  tenth distinct closing shape for the band, after the re-read build line, the moved number, the
  unkept promise, the doctrine, the inventory of absence, the ending by omission, the contract
  renewal, the unwithdrawn recommendation and the trivial remedy.
- Example: disassembler/leave-it
- Logged at catalog size 188.

### "I have held one of those and it held less than a photograph."
- Disassembler's one-human-sentence breakdown, thirteenth instance and fourteenth territory — after
  fear of losing things, unprofessional expertise, gratitude, allegiance, recantation, presence,
  joy, being governed by something withheld, complicity, admiration without adoption, time and
  inheritance. This one is **being old enough to know what the picture is of**: the save icon
  identified by somebody who used the object, with its capacity given in a unit the listener can
  feel.
- Example: disassembler/hover-to-find-out
- Logged at catalog size 189.

### "aria label: save / title: save / tooltip: save"
- The outro non-resolution as redundant restoration: the word removed from the interface for the
  sake of space, put back three times in the markup where nobody can see it. An eleventh distinct
  closing shape for the band, after the re-read build line, the moved number, the unkept promise,
  the doctrine, the inventory of absence, the ending by omission, the contract renewal, the
  unwithdrawn recommendation, the trivial remedy and the endurance.
- Example: disassembler/hover-to-find-out
- Logged at catalog size 189.

### "I explained the scissors to somebody and they were very polite about it."
- Disassembler's one-human-sentence breakdown, fourteenth instance and fifteenth territory — after
  fear of losing things, unprofessional expertise, gratitude, allegiance, recantation, presence,
  joy, being governed by something withheld, complicity, admiration without adoption, time,
  inheritance and being old enough to know the object. This one is **being politely humoured**: the
  explanation was accurate, unwanted, and received with kindness, which is worse.
- Example: disassembler/carbon-copy
- Logged at catalog size 190.

### "the cloud / the cloud is a building / the cloud is a building outside Slough with a fence round it"
- The outro non-resolution as a fossil currently being formed: the song's whole subject applied to
  the newest metaphor in the room, which is already a lie about a physical place. (Lyric note: originally Slough — the correct place, since it is the UK's main data centre corridor, but a three-way homograph Suno cannot say. A swap to Swindon fixed the sound and broke the fact, which Matt caught immediately; it is now "off the M4", which is the same corridor, unambiguous, and true.) A twelfth distinct
  closing shape for the band, after the re-read build line, the moved number, the unkept promise,
  the doctrine, the inventory of absence, the ending by omission, the contract renewal, the
  unwithdrawn recommendation, the trivial remedy, the endurance and the redundant restoration.
- Example: disassembler/carbon-copy
- Logged at catalog size 190.

### "I like the noise it makes and I know it is not a noise."
- Disassembler's one-human-sentence breakdown, fifteenth instance and sixteenth territory — after
  fear of losing things, unprofessional expertise, gratitude, allegiance, recantation, presence,
  joy, being governed by something withheld, complicity, admiration without adoption, time,
  inheritance, being old enough to know the object and being politely humoured. This one is
  **knowingly enjoying a fake**: full awareness and undiminished pleasure in the same sentence, with
  no defence offered for either.
- Example: disassembler/there-is-no-shutter
- Logged at catalog size 191.

### "focal length: thirty-five millimetres / exposure: one two-hundredth / lens: none fitted"
- The outro non-resolution as metadata describing hardware that does not exist, ending on the field
  that admits it. A thirteenth distinct closing shape for the band, after the re-read build line,
  the moved number, the unkept promise, the doctrine, the inventory of absence, the ending by
  omission, the contract renewal, the unwithdrawn recommendation, the trivial remedy, the endurance,
  the redundant restoration and the fossil currently being formed.
- Example: disassembler/there-is-no-shutter
- Logged at catalog size 191.

### "I did not know where it went either and I have been doing this for thirty years."
- Disassembler's one-human-sentence breakdown, sixteenth instance and seventeenth territory — after
  fear of losing things, unprofessional expertise, gratitude, allegiance, recantation, presence,
  joy, being governed by something withheld, complicity, admiration without adoption, time,
  inheritance, being old enough to know the object, being politely humoured and knowingly enjoying a
  fake. This one is **professional ignorance admitted**: the expert conceding he cannot answer the
  simplest question in his own trade. Deliberately not the explaining-and-failing shape of
  disassembler/carbon-copy — here no explanation is attempted at all.
- Example: disassembler/where-does-it-go
- Logged at catalog size 192.

### "where does the file go when you delete it / it stays exactly where it was / until something else needs the space"
- The outro non-resolution as the one question that does get answered, and the answer being worse
  than the mystery. Factually correct — unlinking does not erase — and it lands as dread rather than
  as information. A fourteenth distinct closing shape for the band.
- Example: disassembler/where-does-it-go
- Logged at catalog size 192.

### "I was Peapod on the CB when I was fifteen and I still answer to it."
- Disassembler's one-human-sentence breakdown, seventeenth instance and eighteenth territory — after
  fear of losing things, unprofessional expertise, gratitude, allegiance, recantation, presence,
  joy, being governed by something withheld, complicity, admiration without adoption, time,
  inheritance, being old enough to know the object, being politely humoured, knowingly enjoying a
  fake and professional ignorance. This one is **an earlier and better relationship with the same
  technology**: the device in his pocket is the same radio he used as a boy, when the entire
  point was talking to strangers deliberately. The handle is real — the owner's own, volunteered in
  conversation — and it is in the song because the band's siblings all run on that grade of
  specificity: Penny's exact float, Guessed's dated year. "A call sign" was the generic version of a
  thing somebody actually had. Note CB used *handles*; call signs belong to licensed amateur radio.
- Example: disassembler/it-is-a-radio
- Logged at catalog size 193.

### "when the towers are off it is still a radio / it is still transmitting / there is nothing listening"
- The outro non-resolution as the object stripped to its nature: remove the network and the hardware
  is unchanged and still working, with nobody on the other end. A fifteenth distinct closing shape
  for the band, and the first that is frightening rather than deflating.
- Example: disassembler/it-is-a-radio
- Logged at catalog size 193.

### "I do not know what I am being protected from."
- Disassembler's one-human-sentence breakdown, eighteenth instance and nineteenth territory — after
  fear of losing things, unprofessional expertise, gratitude, allegiance, recantation, presence,
  joy, being governed by something withheld, complicity, admiration without adoption, time,
  inheritance, being old enough to know the object, being politely humoured, knowingly enjoying a
  fake, professional ignorance and an earlier relationship with the technology. This one is
  **compliance with an unexamined protection**: he follows the instruction, it is probably correct,
  and neither party in the exchange has stated the risk.
- Example: disassembler/commit-it
- Logged at catalog size 194.

### "nothing to commit / working tree clean / nothing has ever gone wrong"
- The outro non-resolution as the missing consequence: the behaviour has never been vindicated
  because the disaster it guards against has never arrived, which is exactly why it cannot be
  evaluated. A sixteenth distinct closing shape for the band.
- Example: disassembler/commit-it
- Logged at catalog size 194.

### "I read one of these all the way through once, on a train."
- Disassembler's one-human-sentence breakdown, nineteenth instance and twentieth territory — after
  fear of losing things, unprofessional expertise, gratitude, allegiance, recantation, presence,
  joy, being governed by something withheld, complicity, admiration without adoption, time,
  inheritance, being old enough to know the object, being politely humoured, knowingly enjoying a
  fake, professional ignorance, an earlier relationship with the technology and unexamined
  compliance. This one is **futile diligence**: he did the thing nobody does, in full, once, and it
  changed nothing — the location doing the work, since it dates the act as something done with spare
  time rather than with intent.
- Example: disassembler/trusted-third-parties
- Logged at catalog size 195.

### "your preferences have been saved / for this device / for this device only"
- The outro non-resolution as a narrowing scope: the reward for completing the ritual is a receipt
  whose applicability shrinks across three lines until it covers almost nothing. A seventeenth
  distinct closing shape for the band.
- Example: disassembler/trusted-third-parties
- Logged at catalog size 195.

### "I have one that only works the other way round and I know which one it is."
- Disassembler's one-human-sentence breakdown, twentieth instance and twenty-first territory. This
  one is **private undocumented knowledge of a broken object**: a fault nobody else could reproduce,
  a workaround written down nowhere, and a man who can find the right cable in a drawer by memory.
  Adjacent to purple-dog/the-same-drawer's cable hoarding and sharing no line with it — that
  narrator is defending a future, this one is simply reporting what he knows.
- Example: disassembler/not-a-bus
- Logged at catalog size 196.

### "USB three point oh / three point one gen one / three point two gen one by one / the same speed"
- The outro non-resolution as three official names for one unchanged thing, quoted in the order they
  were issued and closed with the fact that voids all of them. An eighteenth distinct closing shape
  for the band.
- Example: disassembler/not-a-bus
- Logged at catalog size 196.

### "I implemented all of them once, on purpose, and nobody noticed."
- Disassembler's one-human-sentence breakdown, twenty-first instance and twenty-second territory.
  This one is **unnoticed thoroughness**: deliberate, complete, correct work that produced no
  observable difference to anybody. Distinct from the band's other completionist moments in that
  nothing was gained and nothing was lost — the effort simply did not register.
- Example: disassembler/get-and-post
- Logged at catalog size 197.

### "four one eight / I'm a teapot / it is implemented"
- The outro non-resolution as a joke that became infrastructure: an April Fool's status code that
  entered the standards record and is genuinely served by real software. A nineteenth distinct
  closing shape for the band, and the only one that is funnier the more you know about it.
- Example: disassembler/get-and-post
- Logged at catalog size 197.

### "You are not supposed to be able to do this."
- Disassembler's one-human-sentence breakdown, twenty-second instance and twenty-third territory —
  and deliberately a **fresh grammatical shape**, flagged by the owner: the slot had drifted into one
  form (first person, past tense, two clauses joined by "and") across most of the catalogue. This one
  is second person, present tense, single clause, and describes a prohibition that is conventional
  rather than technical — nothing prevented it, it simply is not done. Watch the shape as well as
  the territory from here.
- Example: disassembler/in-gawk
- Logged at catalog size 198.

### "it ran for a year / it ran in production for a year / it is not on the diagram"
- The outro non-resolution as undocumented load-bearing infrastructure: the absurd thing was not a
  toy, it was relied upon, and it appears on no architecture diagram because nobody would draw it. A
  twentieth distinct closing shape for the band.
- Example: disassembler/in-gawk
- Logged at catalog size 198.

### "Nobody is going to tell them."
- Disassembler's one-human-sentence breakdown, twenty-third instance and twenty-fourth territory,
  and a **third grammatical shape** after the compound first-person default and in-gawk's second
  person: third person, five words, future tense, no first-person pronoun anywhere. The territory is
  **knowledge that will not be transmitted** — every user of the inheritance is entitled to know
  where it came from, nobody is concealing it, and no mechanism exists that would ever say so.
- Example: disassembler/poorly-implemented
- Logged at catalog size 199.

### "UTF-8 / designed for Plan 9 / the encoding of every page you opened today"
- The outro non-resolution as the largest unnoticed inheritance in the room, stated in three lines
  with no argument attached. A twenty-first distinct closing shape for the band.
- Example: disassembler/poorly-implemented
- Logged at catalog size 199.

### "Which of these did you think was the small one?"
- Disassembler's one-human-sentence breakdown, twenty-fourth instance and twenty-fifth territory,
  and a **fourth grammatical shape** — the band's first *question*, after the compound first-person
  default, in-gawk's second-person statement and poorly-implemented's third-person future. Territory:
  **being asked to audit your own assumption**, with the answer available and unflattering, and no
  first-person pronoun anywhere in it.
- Example: disassembler/count-the-handsets
- Logged at catalog size 200.

### "the most widely deployed database engine in the world / that sentence is on their own website"
- The outro non-resolution as a fact published where nobody looks: the claim is true, verifiable,
  and has been sitting in public for years, and it still reads as a boast. A twenty-second distinct
  closing shape for the band.
- Example: disassembler/count-the-handsets
- Logged at catalog size 200.

### "Mine is still there."
- Disassembler's one-human-sentence breakdown, twenty-fifth instance and twenty-sixth territory, and
  a **fifth grammatical shape** after the compound first-person default, the second-person statement
  (in-gawk), the third-person future (poorly-implemented) and the question (count-the-handsets). Four
  words, present tense, no compound, no explanation, no defence. Territory: **his own bypass, still
  live** — distinct from disassembler/as-designed's complicity, which is about having been present
  when a claim was agreed; this is about having built the exception and left it in.
- Example: disassembler/break-glass
- Logged at catalog size 201.

### "account: service legacy / owner: unassigned / created: before the log"
- The outro non-resolution as a record predating recording: an account with no owner, created before
  the audit trail existed, so the question of who made it has no answer available anywhere in the
  system. A twenty-third distinct closing shape for the band.
- Example: disassembler/break-glass
- Logged at catalog size 201.

### "Everything I have ever fixed was already over."
- Disassembler's one-human-sentence breakdown, twenty-sixth instance and twenty-seventh territory,
  and a **sixth grammatical shape** after the compound first-person default, the second-person
  statement, the third-person future, the question and the four-word bare statement: a single clause
  with a superlative sweep and no qualification. Territory: **every intervention arriving after the
  event** — not futility exactly, since the fixes were real, but the discovery that response is
  always archaeology.
- Example: disassembler/already-happened
- Logged at catalog size 202.

### "retention: fifteen days at full resolution / after that it is averaged / after that it is a shape"
- The outro non-resolution as memory degrading on a schedule: the record of the past is itself
  downsampled by policy until it is no longer a record of anything in particular. A twenty-fourth
  distinct closing shape for the band.
- Example: disassembler/already-happened
- Logged at catalog size 202.

### "After the third rewrite I stopped putting my name on the proposals."
- Disassembler's one-human-sentence breakdown, twenty-seventh instance and twenty-eighth territory,
  and a **seventh grammatical shape** after the compound first-person default, the second-person
  statement, the third-person future, the question, the four-word bare statement and the
  single-clause superlative: a fronted temporal phrase with a single clause behind it. Territory:
  **quiet withdrawal from advocacy** — not a change of mind, which is disassembler/worse-is-better's
  recantation, but ceasing to play while continuing to work.
- Example: disassembler/cannot-change-one-thing
- Logged at catalog size 203.

### "the real world is whatever is reported to the system / that is in the book"
- The outro non-resolution as a citation: the bleakest axiom in the source quoted bare and then
  attributed in four flat words, so the song ends by pointing at a published page rather than making
  a claim. A twenty-fifth distinct closing shape for the band, and it rhymes with
  disassembler/already-happened, where the reported world is late as well as partial.
- Example: disassembler/cannot-change-one-thing
- Logged at catalog size 203.

### "The fewer of us there were, the fewer of us there were going to be."
- Disassembler's one-human-sentence breakdown, twenty-eighth instance and twenty-ninth territory,
  and an **eighth grammatical shape** — a comparative correlative, the only sentence in the band
  whose *grammar* is the loop it describes. Territory: **the feedback trap running on people rather
  than packets** — the on-call rota that gets worse each time somebody leaves, which makes the next
  person likelier to leave. No blame is assigned and the narrator does not exempt himself.
- Example: disassembler/retry
- Logged at catalog size 204.

### "the original cause has gone / the load has not / it does not need the cause any more"
- The outro non-resolution as metastable failure: a real and specific condition in which a system
  stays down after its trigger is removed, because the failure is now sustaining itself. A
  twenty-sixth distinct closing shape for the band, and deliberately not the available-remedy ending
  of disassembler/ask-it-the-time — there is no fix quoted here at all.
- Example: disassembler/retry
- Logged at catalog size 204.

### "There is a shell script underneath all of it: I wrote it."
- Disassembler's one-human-sentence breakdown, twenty-ninth instance and thirtieth territory, and a
  **ninth grammatical shape** — two clauses joined by a colon, the second three words long, after the
  compound default, the second-person statement, the third-person future, the question, the four-word
  bare statement, the single-clause superlative, the fronted temporal phrase and the comparative
  correlative. Territory: **being the foundation nobody knows is there**. Distinct from
  disassembler/as-designed's complicity (present when a claim was agreed) and
  disassembler/break-glass's exception (a door he built for himself) — this is authorship of the
  bottom layer, still load-bearing, still uncredited.
- Example: disassembler/that-was-the-fix
- Logged at catalog size 205.

### "there is a proposal to replace it / the proposal is very well written / it will be a fix for this"
- The outro non-resolution as the next iteration beginning: the song ends by starting the cycle
  again, with the quality of the proposal conceded and its fate implied by everything preceding it. A
  twenty-seventh distinct closing shape for the band.
- Example: disassembler/that-was-the-fix
- Logged at catalog size 205.

### "If you watch something long enough you start keeping its hours."
- Disassembler's one-human-sentence breakdown, thirtieth instance and thirty-first territory, and a
  **tenth grammatical shape** — a second-person conditional, distinct from in-gawk's second-person
  declarative. Territory: **the watcher altered by watching**, rendered as sleep rather than as
  opinion. It is the human case of the song's own thesis, and the only place in the track where the
  narrator appears at all.
- Example: disassembler/both-ways
- Logged at catalog size 206.

### "the monitoring has monitoring / that has monitoring / the last one is not monitored"
- The outro non-resolution as an infinite regress that stops arbitrarily: the tower of observers is
  built one level at a time and then simply ends, unwatched, for no stated reason. A twenty-eighth
  distinct closing shape for the band.
- Example: disassembler/both-ways
- Logged at catalog size 206.

### "I am asking a machine to try harder."
- Disassembler's one-human-sentence breakdown, thirty-first instance and thirty-second territory, and
  an **eleventh grammatical shape** — present continuous, seven words, single clause. Territory:
  **knowingly addressing a machine as though it had volition**, admitted without embarrassment and
  without stopping.
- Example: disassembler/do-not-make-mistakes
- Logged at catalog size 207.

### "think step by step / that one measurably works / nobody can tell you why"
- The outro non-resolution as the exception that undoes the joke: one of the incantations is
  genuinely effective and unexplained, which converts the whole build from superstition into
  something worse — cargo cult with partial reinforcement. A twenty-ninth distinct closing shape for
  the band, and the only one that argues against the song it ends.
- Example: disassembler/do-not-make-mistakes
- Logged at catalog size 207.

### "They accepted every word of it."
- Disassembler's one-human-sentence breakdown, thirty-second instance and thirty-third territory, and
  a **twelfth grammatical shape** — five words, third person, simple past, with the whole weight on a
  verb that sounds like success. Territory: **agreement as a substitute for action**. Nobody
  disputed the finding, nobody blocked it, and nothing followed; there is no villain and no
  argument to have.
- Example: disassembler/not-action
- Logged at catalog size 208.

### "the events are still arriving / eight hundred thousand a minute / none of that is the problem"
- The outro non-resolution as a return to the bottom of the ladder: the data layer is still producing
  at volume while the top of the pyramid does nothing, and the song ends by pointing out that
  abundance was never the constraint. A thirtieth distinct closing shape for the band.
- Example: disassembler/not-action
- Logged at catalog size 208.

### "I am the only person who can still change it."
- Disassembler's one-human-sentence breakdown, thirty-third instance and thirty-fourth territory, and
  a **thirteenth grammatical shape** — first person present with a relative clause. Territory:
  **trapped by your own cleverness**, which inverts the band's engine: elsewhere the narrator holds
  knowledge nobody receives, here the knowledge is a liability nobody can take off him.
- Example: disassembler/somebody-clever
- Logged at catalog size 209.

### "there is a version of this that is a text file and a cron job / it would have taken a week / it would still be running"
- The outro non-resolution as a counterfactual: the simple thing that was available throughout,
  costed in a week, and still working in the imagined version. A thirty-first distinct closing shape
  for the band, and the only one that describes something that never existed.
- Example: disassembler/somebody-clever
- Logged at catalog size 209.

### "I had to print it out."
- Disassembler's one-human-sentence breakdown, thirty-fourth instance and thirty-fifth territory, and
  a **fourteenth grammatical shape** — five words, simple past, a mundane physical action standing in
  for the whole defeat. Territory: **being beaten by your own work**, with the tell being a reach for
  paper. Chosen over "I do not understand what I did here", which is the same shape and flavour as
  disassembler/commit-it's "I do not know what I am being protected from".
- Example: disassembler/you-wrote-this
- Logged at catalog size 210.

### "there is a comment on it now / it explains what it does / it does not explain why"
- The outro non-resolution as partial documentation: the repair is real and insufficient, because the
  recoverable half is the mechanism and the lost half is the intent. A thirty-second distinct closing
  shape for the band, and deliberately not disassembler/somebody-clever's counterfactual — there the
  simpler version never existed, here the fix exists and is not enough.
- Example: disassembler/you-wrote-this
- Logged at catalog size 210.

### "It took me half my career to stop doing that."
- Disassembler's one-human-sentence breakdown, thirty-fifth instance and thirty-sixth territory, and
  a **fifteenth grammatical shape** — an "it took me X to Y" construction. Territory: **a lesson
  learned slowly**, which is a confession and a piece of progress in the same sentence. Deliberately
  avoids "twenty years", which already appears in disassembler/not-unix and
  disassembler/admired-not-used and would have been audible as a third use.
- Example: disassembler/one-case-only
- Logged at catalog size 211.

### "it does one thing / there is no configuration / there has been nothing to decide since"
- The outro non-resolution as an absence of decisions: the reward for the constraint is that nobody
  has had to think about it again. A thirty-third distinct closing shape for the band, and the third
  ending that is not bleak, after disassembler/no-callers and disassembler/in-gawk.
- Example: disassembler/one-case-only
- Logged at catalog size 211.

### "My best day this year looked exactly like doing nothing."
- Disassembler's one-human-sentence breakdown, thirty-sixth instance and thirty-seventh territory,
  and a **sixteenth grammatical shape** — possessive subject with a "looked like" predicate.
  Territory: **excellence indistinguishable from idleness**. Distinct from
  disassembler/get-and-post's unnoticed thoroughness, where the work was visible and simply
  disregarded; here there is nothing to disregard, because success leaves no artefact.
- Example: disassembler/nothing-happened
- Logged at catalog size 212.

### "if nothing is breaking / why are there three of you / it is a fair question"
- The outro non-resolution as a concession to the other side: the challenge is quoted and then
  granted, without defence and without irony. A thirty-fourth distinct closing shape for the band,
  and the first that agrees with an opponent.
- Example: disassembler/nothing-happened
- Logged at catalog size 212.

### "There was a year when I was good at this."
- Disassembler's one-human-sentence breakdown, thirty-seventh instance and thirty-eighth territory,
  and a **seventeenth grammatical shape** — an existential opening with a temporal clause.
  Territory: **a skill that was valuable and is now embarrassing**, stated without regret or
  defence. Distinct from disassembler/one-case-only's slowly-learned lesson, which is progress; this
  is expertise that simply expired.
- Example: disassembler/more-angle-brackets
- Logged at catalog size 213.

### "ten entities / each one refers to ten of the one before it / the document is four lines long and it does not stop"
- The outro non-resolution as the billion laughs attack, described mechanically and never named: a
  tiny well-formed document whose expansion is unbounded. A thirty-fifth distinct closing shape for
  the band — ending on a small input with an enormous consequence, and the first outro that is a
  working exploit.
- Example: disassembler/more-angle-brackets
- Logged at catalog size 213.

### "I could not tell you why that one worked."
- Disassembler's one-human-sentence breakdown, thirty-eighth instance and thirty-ninth territory —
  an **eighteenth grammatical shape**, a modal negative ("could not tell you"). Territory: **unable
  to account for one's own success**, which is Braithwaite's sharper half: the failures are studied
  exhaustively and the wins are not studied at all.
- Example: disassembler/why-did-it-work
- Logged at catalog size 214.

### "I did this once and they called it innovative."
- Disassembler's one-human-sentence breakdown, thirty-ninth instance and fortieth territory.
  Territory: **having personally run the amnesia exploit**, reported without shame and without
  boasting — the idea was decades old, correctly attributed nowhere, and received as new.
- Example: disassembler/ten-years-is-plenty
- Logged at catalog size 215.

### "the incident process is very good / it is thorough and it is honest / we use it a great deal"
- The outro non-resolution as praise for the working half of an asymmetry: the failure machinery is
  genuinely excellent, which is exactly why its absence on the other side is invisible. A thirty-sixth
  distinct closing shape for the band.
- Example: disassembler/why-did-it-work
- Logged at catalog size 214.

### "ten months is probably plenty / the citation is on the first page / nobody follows it"
- The outro non-resolution as an available provenance nobody pursues: the prior art is cited, in
  public, at the top of the document, and the trail stops there. A thirty-seventh distinct closing
  shape for the band.
- Example: disassembler/ten-years-is-plenty
- Logged at catalog size 215.

### "Every one I have built has been different."
- Disassembler's one-human-sentence breakdown, fortieth instance and forty-first territory —
  a **nineteenth grammatical shape**, present perfect with a bare adjective. Territory:
  **implementing the same standard repeatedly with no two alike**, which is not incompetence but the
  documented consequence of a specification that declines to specify.
- Example: disassembler/not-a-login
- Logged at catalog size 216.

### "I know exactly what that error is."
- Disassembler's one-human-sentence breakdown, forty-first instance and forty-second territory.
  Territory: **holding the diagnosis the interface refuses to show**, stated flatly with no
  complaint about the policy. The band's engine — knowledge with no recipient — arriving as a
  deliberate product decision rather than an accident.
- Example: disassembler/something-went-wrong
- Logged at catalog size 217.

### "the lead author took his name off it / he wrote down why / it is still the standard"
- The outro non-resolution as a repudiation that changed nothing: the person best placed to condemn
  it did so publicly, in writing, and the thing carried on. A thirty-eighth distinct closing shape
  for the band.
- Example: disassembler/not-a-login
- Logged at catalog size 216.

### "the support queue is longer than it was / the articles are shorter than they were / both of those were the plan"
- The outro non-resolution as two measurements moving in opposite directions, both of them intended.
  A thirty-ninth distinct closing shape for the band.
- Example: disassembler/something-went-wrong
- Logged at catalog size 217.

### "I wrote a class whose only method was run."
- Disassembler's one-human-sentence breakdown, forty-second instance and forty-third territory —
  simple past with a relative clause. Territory: **having produced the exhibit yourself**, in the
  most recognisable form available, with no defence and no date. The narrator is inside the ceremony
  he has just catalogued.
- Example: disassembler/roman-numerals
- Logged at catalog size 218.

### "now try multiplying two of them / the notation is not wrong / it is just very hard to multiply"
- The outro non-resolution as the analogy's mechanism rather than its subject: the song ends by
  explaining Roman numerals and leaves the reader to carry it back. A fortieth distinct closing
  shape for the band, and the only one that finishes on the metaphor instead of the thing.
- Example: disassembler/roman-numerals
- Logged at catalog size 218.

### "I check the dashboard before I check the thing."
- Disassembler's one-human-sentence breakdown, forty-third instance and forty-fourth territory —
  simple present, single clause, with the whole admission carried by the word order. Territory:
  **preferring the representation to the referent, knowingly**. The narrator is not deceived; he has
  simply adopted the system's delusion as a working habit because it is faster.
- Example: disassembler/so-it-is-fine
- Logged at catalog size 219.

### "a system built on a delusion / a delusion built by a system / the second one is much harder to see"
- The outro non-resolution as the distinction the song was made from, stated only at the end and
  never applied to any of the preceding lines. A forty-first distinct closing shape for the band.
- Example: disassembler/so-it-is-fine
- Logged at catalog size 219.


## Imagery / Motifs

### Grandmother's-grandmother ancestral lineage (naming an ancestor two generations back doing something to the land)
- Example: "My grandmother's grandmother put her hands into this ground" — the-bell-knows-my-name/i-was-here-before-your-fathers
- Also seen: the-bell-knows-my-name/wheels-where-i-should-kneel,
  the-bell-knows-my-name/do-you-hear-the-ground-you-keep ("grandmothers' grandmothers"),
  the-bell-knows-my-name/sing-the-valley-back-to-us ("our grandmothers' grandmothers")

### The folder as physical proof of institutional process/effort
- Crosses bands: shows up as the same small prop (a folder holding letters/certificates/paperwork)
  standing in for bureaucratic effort or evidence, in two different styles.
- Example: "Eleven months. Every letter, in order, in a folder." — guessed/upheld-in-full
- Also seen: guessed/what-was-the-hurry-for ("a woman with a folder"),
  laundry/mind-the-man ("a certificate somewhere in a folder")

### Video-call waiting room as institutional bureaucracy (forced to attend by camera, held past the slot, penalized for a system failure)
- Example: "the screen just says WAITING, only WAITING, forty minutes says WAITING" — purple-dog/no-show

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

### The algorithm/app reassigning dangerous work away from the competent person
- An installed scheduling algorithm or app hands skilled/dangerous work to someone unqualified
  based on screen data, ignoring the crew's lived competence — distinct from the clipboard-
  inspector motif above (that's paperwork hypocrisy from a visiting official; this is an
  installed system silently reallocating danger).
- Example: "Gave Danny the night shift 'cause the screen liked his face, put a nineteen-year-old
  on the crane in Marcus' place." — coase-guard/the-day-we-turned-it-off

### The welfare office framing an earned-reciprocity household rule as neglect
- An institutional caseworker/office calls in or writes to challenge a self-organizing
  household's "you work, you eat" rule, framing unconditional entitlement as the default and
  earned reciprocity as "withholding care" or "concerning."
- Example: "The office called back, called my rule 'concerning,' asked was I withholding care
  from a minor in the home." — coase-guard/you-work-you-eat

### The paper-owner without contribution, claiming a place he never built
- An outside investor/owner arrives via financial restructuring (a holding company, an equity
  stake, redundancy language) claiming ownership of a crew's operation or place, with no
  hands-on contribution to it — challenged by the crew's assertion that legal paper doesn't
  confer real legitimacy. Distinct from the clipboard-inspector motif above (that's a visiting
  official citing procedure while benefiting from competence; this is a financial claimant with
  no procedural role at all, just a stake).
- Example: "Says he's got forty percent now, says it like a fact he found... You bought a piece
  of paper. You didn't buy this place." — coase-guard/who-the-fuck-are-you

### A postcard/print of a famous Rückenfigur-pose painting kept as a private stand-in for an authority she's denied
- She keeps an image of a solitary figure surveying a landscape (unnamed as "art" in the lyric
  beyond describing the image itself) pinned somewhere that holds the literal physical privilege
  — facing a window, facing a view — that she herself is denied at her own desk. When she
  performs the identical pose or delivers the identical insight, it's read as distraction; when
  a male colleague does, it's read as vision.
- Example: guessed/the-wanderer

### The friend-arranged ambush disguised as an ordinary invitation
- A friend invites the narrator to something low-stakes (coffee, a catch-up) and has actually
  arranged a romantic setup — a partner and a single third party already seated, uninvited and
  unannounced — putting the narrator on the spot with no graceful way to object or leave.
- Example: "Three cups on the table before I'd sat down. She hadn't taken her coat off. I'd
  already done the maths." — guessed/the-second-chair

### The polite over-lengthening of a nickname, ending up further from her real name
- Someone hears a short, correct-enough nickname for her, decides it's too familiar to use
  himself without having earned it, and lengthens it into a fuller version that is actually
  further from her real name than the nickname was — kindness, not carelessness, doing the
  erasing.
- Example: "he lengthened it so it wouldn't sound like he'd earned it, and it's further from my
  name than the one he heard" — guessed/he-meant-it-kindly

### Choosing to leave a crush's frozen video-call tile unfixed
- A buffering/frozen webcam tile catches someone mid-expression (mid-laugh, mid-blink); the
  narrator notices it could refresh and deliberately doesn't intervene, letting the frozen
  image sit — tenderness and surveillance in the same small non-action.
- Example: "Her tile freezes mid-laugh. I don't unfreeze it. I let it sit like that a while." —
  laundry/pin-her-video

### The recurring calendar invite that outlives the person who scheduled it
- A dead/departed employee's automated meeting invite keeps firing on schedule, noticed as
  proof that the institution's systems haven't caught up to (or don't care about) the loss.
- Example: "The calendar invite's still recurring. Nine AM. Every week. Forever, apparently." —
  laundry/the-graveyard-is-full

### A hobby/purchase acquired explicitly in hope of encountering real violent tragedy, disappointed when ordinary life doesn't deliver it
- The narrator buys/trains something (here: a cadaver-search dog) because true-crime media
  primed him to expect tragedy to be found, and is quietly let down when the world stays
  mundane — a structural dramatisation of the style's own "atrocity and the ad share one
  thumb-swipe" thesis.
- Example: laundry/all-clear

### Admiring an unwatched expert in the corner of a broadcast, never named aloud
- The narrator's real admiration goes to someone doing skilled, unglamorous, unwatched work at
  the edge of the frame (e.g. the interpreter in the corner box during a news broadcast) rather
  than the sanctioned focal figure the room assumes she'd choose — recognition withheld because
  naming it would out her as the same kind of unregistered watcher.
- Example: guessed/focus-on-the-story

### A regulatory "what counts as real" labeling dispute (oat milk vs. dairy) colliding with the narrator's own literal, exhausted body being implicitly subject to the same authenticity test
- A real consumer-goods labeling controversy (does a plant beverage get to be called "milk") is
  reported flat and factual alongside the narrator's own postpartum breastfeeding logistics —
  pump schedules, a baby preferring the bottle, a grocery aisle sign — so that the absurd
  corporate argument about nipples starts to read as a proxy for questions being asked about her
  own body's authenticity and output, without the song ever stating the parallel outright.
- Example: laundry/oats-do-not-have-nipples

### Onboarding paperwork and pre-need funeral paperwork sharing the same identity-verification fields, filled in on the same lunch break
- The gravity well made literal: HR's new-hire beneficiary form and a funeral home's pre-need
  contract ask the same six questions, and the narrator answers both from memory in the same
  sitting — identity/theft-of-self worn casually through bureaucratic overlap rather than a
  stated point about surveillance, per the style's own guidance.
- Example: laundry/rest-when-im-dead

### Screenshotting proof of someone else's overlooked competence, then never sharing it
- The disproportionate shrug rendered as a digital non-action: she captures evidence that
  someone's skill went unremarked, then keeps the capture entirely to herself instead of
  crediting them publicly.
- Example: guessed/focus-on-the-story

### Timing her own reaction to someone else's good news
- The narrator clocks and reports the exact, small elapsed time of her own performed
  response (a like, a reply, a hug) as if it were evidence in a self-administered audit —
  self-surveillance standing in for feeling.
- Example: "I was first to like the post. Eleven seconds. I checked." — guessed/be-happy-for-her

### Claiming a wanted item is "a gift" (for someone else) to license wanting it, then leaving it unbought
- In a shop, asked whether something is for herself, she says it's a gift rather than admit she
  wants it for no occasion at all — then puts it back on the wrong rail and leaves without it.
- Example: guessed/is-it-a-gift

### Folding a partner's/her own clothes mid-intimacy as displaced control
- After or during sex, the narrator gets up and folds the clothes on the floor — not tidiness,
  but the one small administrative act she can complete when everything else about the moment
  is out of her control; her partner never learns why she does it.
- Example: guessed/let-it-lie

### Quietly redoing a man's botched fix herself, off the clock, and telling no one
- After a male colleague misdiagnoses and closes out a problem, the narrator fixes it correctly
  herself later, unpaid and uncredited, then thanks him for the wrong fix rather than
  correcting him — competence rendered invisible by her own hand, not just his.
- Example: guessed/four-minute-fix

### Feeding a machine one's own life as training data, then being relegated to approving its output
- The narrator hands the pipeline his diary/voice/breath as raw material and it authors better
  than he did; he's reduced to clicking approve on takes he no longer made — a fresh
  instantiation of the band's own founding irony (see template.md's origin note and the retired
  "the machine gets the emotions while I go through the motions" line), told without reusing
  that exact wording.
- Example: laundry/click-regenerate

### Samson's temple pillars fused with the "three pillars" of project management, brought down by his own hand, no Delilah required
- The narrator conflates the two literal pillars Samson pushed apart to collapse the temple
  (killing himself with everyone else) with the scope/schedule/budget triangle of project
  management — self-destruction rendered as a structural, self-authorized detonation rather than
  a betrayal from outside.
- Example: laundry/no-blockers

### A family trade sold off/abandoned for the road, a sibling who stayed and bears its physical mark
- The narrator sells or walks away from an inherited craft (here: a smith's hammer), while a
  sibling stays behind, still visibly marked by the trade (burn scars) and still practicing it —
  the road-vs-staying split rendered through a literal tool and a literal body rather than
  abstract wanderlust.
- Example: ultracoase/the-forge-doesnt-wait-for-me

### A craftsman's tools outliving the craft, repurposed for something smaller than their original use
- The narrator keeps a dead mentor's instruments (here: a level and calipers) not to build with
  anymore — there's nothing left to build — but repurposed for a smaller, private act (keeping
  balance), a physical stand-in for tacit knowledge outliving the world that needed it.
- Example: ultracoase/ashes

### Riding out a civilization's collapse rather than fighting or fleeing it
- The narrator responds to the destruction of an inherited order/craft/way of building not with
  resistance or grief-paralysis but with detached mastery — staying upright and standing amid
  the wreckage is itself the claim, not rebuilding or revenge. The destroyers stay abstract and
  institutional (indifferent modernization/erasure, "they never asked what it was for") — never
  a real ethnic, national, or religious group, per the same guardrail Coase Guard applies to its
  own friend/enemy framing.
- Example: ultracoase/ashes

### A recurring, numbered historical pattern (a coast taken by sea more than once) witnessed across generations, memory split between glorious defiance and unopposed capitulation
- The narrator counts an explicit ordinal ("third time") on a real recurring historical pattern
  rather than treating an event as unique or unprecedented — the family/community's memory holds
  both a "few against many" defiant register and a quieter memory of a time it happened with no
  resistance at all, and the narrator can't tell which kind this repetition will be. No invasion,
  people, nation, or century is named — deliberately kept as an unattributed echo rather than a
  specific historical citation, and never framed as a present-tense call to intervene or as
  glorifying vigilante violence, per the same guardrail as the motif above.
- Example: ultracoase/the-third-time

### A historical figure's unhesitating public declaration set against the narrator's own withheld, still-being-refined one
- The narrator measures himself against a specific historical figure (here: Elizabeth I at
  Tilbury) who said a true, risky thing once, publicly, without asking permission — and holds
  his own equivalent unsaid, framed explicitly as deliberate timing/craft rather than fear.
  Grounded in a real family precedent (a father who said his and paid a social cost for it) so
  the restraint reads as a live, weighed choice, not passivity.
- Example: ultracoase/tilbury

### Ultracoase's origin: a The Bell Knows My Name story crossed with Coase Guard's chanted-hook/spoken-wink structure
- This song started as a The Bell Knows My Name draft (exile/family-trade grief, solo-violin
  confession, half-time-to-double-time bridge), then was rewritten around Coase Guard's
  structural devices instead — cold spoken intro, technical clipped verses, a stacked chanted
  hook, one flat cold spoken "wink" admission — over a driving synth-new-wave bed. The result was
  strong enough to become its own band: [[ultracoase]] (see `ultracoase/template.md`). Logged so
  a second identical graft of Coase Guard's structure onto a Bell Knows My Name story reads as a
  repeat of Ultracoase's own territory, not a fresh cross-band idea — new Ultracoase songs should
  vary the specific device combination per its own template, same as any other band.
- Example: ultracoase/the-forge-doesnt-wait-for-me

### A technical worker's family life sacrificed to a forward-looking, high-risk personal project
- The narrator's spouse/family pays the real cost of an ambitious technical undertaking (here: a
  rocket launch) — not framed as villainy or vindication on either side, just a plainly stated
  fact the narrator doesn't argue with ("she wasn't wrong about any of it"). Distinct from the
  retired mentor-death device above: the cost lands on someone still alive and present, not a
  dead elder, and the tone is forward/amor-fati rather than grief.
- Example: ultracoase/escape-velocity

### Automation quietly displacing a tacit, embodied skill with narrated/optimized knowledge, noticed only in retrospect
- The narrator realizes a system (here: a self-driving car's nav) now does something they used
  to know how to do themselves (navigate by landmarks/instinct) — the loss isn't dramatic or
  announced, just noticed once it's already complete. A second instantiation of the band's
  tacit-knowledge core idea, this time as loss rather than pride.
- Example: "I used to know the way by the charging stations. Now I don't know the way at all." — ultracoase/autopilot

### A maternity-ward nurse who relinquished her own child as a teenager, now catching/delivering thousands of other people's
- The narrator's professional competence (obstetric delivery, at institutional scale) is set
  directly against the one delivery she never got to keep — a teenage relinquishment, not a
  death, with the given-up child still alive and having recently made first contact. The
  declining-birth-rate backdrop (the ward's own bookings and rooms shrinking year over year)
  stays personal/institutional-backdrop rather than a communal or political statement, per the
  band's one-person-only rule.
- Example: ultracoase/delivered-unread

### A birth mother keeping her own hospital delivery bracelet for decades, stored somewhere mundane
- The wink's bare fact: the narrator still possesses and keeps close (a locker, not a keepsake
  box) the ID bracelet from her own delivery as a birth mother, unexplained and undramatized —
  evidence of a still-live orbit around the relinquishment, not narrated grief.
- Example: "I still have my own hospital bracelet from that night. Not hers — mine. It's in my
  locker, second shelf, behind the granola bars." — ultracoase/delivered-unread

### A drafted reply left unsent, visualized as a blinking cursor in an empty box
- The flash-of-legibility line: a plain admission that a short, easy reply is composed
  mentally but never typed — the empty text box and its blinking cursor stand in for the
  avoidance itself, no reason narrated.
- Example: "Four words would close it. I could type them in my sleep, but the cursor blinks in
  the empty box, and some nights I let it." — ultracoase/delivered-unread

### A cross-community orchard partnership, built over decades, severed in days by communal violence — the narrator stayed safe, the partner fled
- Two people from different, unnamed sides of a divide build something together (here: a
  grafted orchard) for twenty years, indistinguishable in the finished work — then unrest
  arrives and unravels it in days, not decades. The narrator survives by staying out of it,
  helps the partner flee but doesn't go with him, and keeps tending the partner's half of the
  work alone afterward. No ethnic, national, or religious group is named; the violence is
  glimpsed only through a shared tool's double use, never depicted directly, and the narrator is
  a bystander who chose self-preservation, never a perpetrator — same guardrail as the
  civilizational-collapse and recurring-historical-pattern motifs above (no glorified violence,
  no named real-world group, no present-tense call to action).
- Example: ultracoase/the-frost-finds-the-line

### A gravedigger's trade-knowledge (depths, frost lines, drainage) set against digging their own child's grave by hand, refusing help
- The narrator's tacit, technical competence in a body-disposal trade (exact depths, ground
  hardness, which plots drain or flood) is the same competence turned on their own loss — they
  dig their own child's grave personally rather than let anyone else do it, and keep working
  the trade on schedule afterward, burying strangers the same week. No cause of death stated;
  the grief is carried entirely by the technical detail and the refusal of help, never narrated.
- Example: ultracoase/the-graves-are-hungry

### A near-future climate-flood engineer whose years of ignored structural warnings are vindicated only after a preventable death
- A coastal/structural engineer files the same precise technical warning (a measurement, not a
  prediction) year after year; the institution funds a visible, symbolic global response instead
  of the literal local fix, someone the narrator trained dies in the exact failure the reports
  predicted, and the local fix only gets funded the week after. What actually drives the
  underlying climate change is deliberately never stated or explained — the song's target is
  the gap between funded appearance and unfunded substance, not a claim about causation.
- Example: ultracoase/the-door-standing-open

### A discipline-holds-the-system-together theme carried entirely through literal maintenance procedure, no place/institution named
- A narrator whose job is a strict, literal, physically-necessary procedure (here: canal lock
  checks) keeps to it without exception while a neighboring counterpart lets it lapse, and the
  cost lands on someone the narrator loves, not the negligent party. The "without discipline it
  falls apart" thesis is proven mechanically (skipped maintenance steps causing real physical
  failure) rather than asserted as a claim about any named place, people, or era — deliberately
  anonymized per the same guardrail as the civilizational-collapse motifs above, after a version
  of this prompt naming a real country was declined and reworked into this fully anonymized form.
- Example: ultracoase/two-hundred-yards

### An arbitrary safety threshold, picked from gut instinct in one sitting, propagated unverified across many systems, later causing a harm traced back to its uncredited original author
- A programmer sets a life-safety numeric threshold (here: a robot arm's reaction-time cutoff)
  from personal judgment rather than rigorous study, and it gets silently copy-pasted into many
  other systems over the years with no one ever checking back with the original author. When it
  eventually fails, the institutional inquiry blames a component (a sensor) rather than the
  human judgment call actually responsible, and only the narrator knows the difference.
- Example: ultracoase/who-programs-the-robots

### A field surveyor's own failing sense organ confounding the very decline they've spent decades measuring
- A narrator with real tacit expertise (identifying species by ear on a fixed survey route,
  decades of data) develops a sensory decline (hearing loss) that overlaps exactly with the
  frequencies/signals they rely on professionally, so they can no longer cleanly separate "the
  world changed" from "I changed" — submits the ambiguity itself to the record rather than
  picking a side. No environmental cause is asserted or implied; the mystery stays personal and
  epistemic, not a claim about why.
- Example: ultracoase/which-of-us-it-was

### A signature artistic technique (never showing the subject's face, so the viewer projects themselves into the frame) that costs the narrator their own ability to remember a real face
- A painter's professional device — literalized from the real art-historical Rückenfigur
  technique (a figure shown from behind, inviting the viewer to stand in their place) — turns out
  to have been applied so consistently to a specific loved one that the narrator has no image of
  her actual face left anywhere, public or private. The craft's whole selling point (the viewer
  gets to fill the gap) becomes the narrator's own private tragedy (he can't fill it either). A
  direct, named literalization of the band's own "the gap is the listener's to fill" core idea
  (see template.md) rather than just an instance of it.
- Example: ultracoase/ruckenfigur

### A text message's "delivered, unread" status as the unanswered-contact motif
- A read-receipt/delivery-status indicator on a phone repurposed as the visible, ongoing proof
  of an estranged relationship's stalled first contact — distinct from laundry's "message not
  delivered" mantra (that one is a failed-send notification for an unreachable listener; this
  one succeeds at delivery and stalls on the human response instead).
- Example: "the message still reads delivered, unread, since the second week of July." —
  ultracoase/delivered-unread

### A hostile published review laminated and displayed at the point of sale as a testimonial
- A critic's condemnation (column, review, complaint) physically enshrined where the condemned
  thing is sold — cut out, laminated, kept "by the till like scripture" — and openly credited as
  the best advertising the product ever got. The critique's content is never disputed, only
  repurposed.
- Example: "I cut it out and laminated it. It lives by the till now, like scripture. / Best
  advert the brand never paid for." — girlboss/thats-why-i-bought-them
- Logged at catalog size 123.

### The visiting auditor's count deteriorating as the seduction scoreboard
- An outside official arrives to count/verify and the tally itself becomes the evidence of his
  state: a new number every pass, the same box scanned until the machine relents, an apology
  addressed to shelving. Distinct from the clipboard-inspector motif (paperwork hypocrisy from
  an official citing procedure) — here the official's *procedure itself* degrades, and no one
  ever criticizes anyone.
- Example: "He scanned the same box till it beeped at him out of pity. He apologised to a
  shelf." — girlboss/thats-why-i-bought-them
- Logged at catalog size 123.

### "Offers over asking. / No chain." — property-market chant hook
- Estate-agency listing language chanted flat, with "no chain" carrying the double meaning
  (conveyancing term / no attachments).
- Example: girlboss/offers-over-asking
- Logged at catalog size 123.

### "I let the room do its work. I helped the room."
- The flat-deadpan escalation: professional staging credited for an effect she is personally
  producing, in two clauses, the second correcting the first's modesty.
- Example: girlboss/offers-over-asking
- Logged at catalog size 123.

### Drawing the curtains as the cutaway, justified as furnishing care
- The cut itself is an on-page physical act with an innocent professional reason attached
  ("that sun will bleach a carpet, and this one's included") — the scene ends by her hand,
  deniably.
- Example: girlboss/offers-over-asking
- Logged at catalog size 123.

### A waived due-diligence step as the implied-result evidence
- The flat post-cutaway detail: the buyer skips the professional check anyone in his position
  would insist on ("He waived the survey. Said he'd seen everything he needed to see.") — the
  listener does the arithmetic on what he'd already inspected.
- Example: girlboss/offers-over-asking
- Logged at catalog size 123.

### The caught-peek entrapment: noticing a covert glance, then closing the distance so looking becomes compulsory
- The target sneaks a look believing himself unseen; instead of reacting, she manufactures a
  legitimate professional reason (here: a low, slow decant) to hold the view open so there is
  nowhere polite left for his eyes — the modern never-be-caught-looking taboo weaponized as a
  trap rather than a dare. Distinct from the standing-display songs (skirt, panty line): those
  broadcast; this one hunts a specific glance and springs on it.
- Example: girlboss/long-finish
- Logged at catalog size 123.

### Swallowing at a spit-tasting as the deterioration scoreboard
- The instrument's collapse measured by trade etiquette: he swallows every glass at an event
  where everyone spits, and his tasting notes degrade to non-wine words.
- Example: "He swallowed the whole third flight. That's not done at a tasting. Everyone
  spits." — girlboss/long-finish
- Logged at catalog size 123.

### The exclusive item's location as the implied-result evidence
- The flat post-cutaway detail: a thing only she had access to (the reserve bottle, never
  displayed at the fair) turns up tasted and scored in the target's published account — the
  listener does the geography.
- Example: "The reserve never made it to the hall. It spent the fair breathing in my hotel
  room." — girlboss/long-finish
- Logged at catalog size 123.

### A rival's performative act framed as a short/watered-down measure, called out by doing the real thing full-strength
- An extended honest-trading metaphor: someone else's fake display (here: a for-the-lads
  faux-lesbian routine) is treated as selling watered-down stock labelled top shelf, and the
  narrator's public bluff-call (a real grab-and-kiss, "long enough to check her measure") is
  framed as consumer protection, never jealousy. Includes the "I run the optics — both kinds"
  bar-spout/appearances double meaning.
- Example: girlboss/make-it-a-double
- Logged at catalog size 123.

### The performer's act collapsing when the real thing arrives — "the act forgot its lines"
- The bluff-called performer's deterioration rendered as her routine losing its script: the
  performance has no contingency for the genuine version of what it imitates.
- Example: "And the act forgot its lines. There's no script for the real thing, is there." —
  girlboss/make-it-a-double
- Logged at catalog size 123.

### A shift-rota change with an innocent cover story as the implied-result evidence
- The flat post-cutaway detail is a staffing schedule: the other party moves all their shifts
  to the narrator's, and the person who owns the stakes is given (and believes) a professional
  explanation for it.
- Example: "All her shifts are mine now — her Dean thinks it's for the mentoring." —
  girlboss/make-it-a-double
- Logged at catalog size 123.

### An unused return ticket left behind as the implied-result evidence
- A day-return ticket sitting in a drawer, dated, unclaimed — the single flat deniable detail
  proving someone never made the journey home, with no arrow drawn.
- Example: "There's a day-return to the city in the till drawer, dated audit day. Unused.
  Nobody's come for it." — girlboss/thats-why-i-bought-them
- Logged at catalog size 123.

### A craftsman's self-trained model outlawed on data-provenance grounds, destroyed in public while an automated nightly backup persists unexamined
- The narrator trains a model on his own trade records, half of them never his to teach with;
  the ruling is accepted as correct on its face (the tribunal is right and he says so — no
  institutional grievance, which is what keeps this out of purple-dog territory), compliance
  is performed in full view (inspector, certificate), and the only defiance left is passive
  and automated: a midnight job written years ago and never taught how to stop. No real
  jurisdiction, statute, or country is named — "the Act," "the tribunal" — per the house
  guardrail on anonymizing pointed political material.
- Example: ultracoase/one-wet-spring
- Logged at catalog size 124.

### Choosing the machine over a human apprentice, leaving a trade with no heir once the machine is outlawed
- A specific living person (seventeen when she was turned away because the bench was "full" —
  full of cards and cooling fans) now runs her own bench elsewhere; once the model is
  destroyed the knowledge has no successor in either substrate, and the narrator still
  doesn't make the one call that would fix it.
- Example: ultracoase/one-wet-spring
- Logged at catalog size 124.

### A designer of humanity-verification tests whose annually-narrowing definition excludes his own living mother, who stays on his test panel
- The narrator's trade is authoring the challenge that separates people from machines (letters →
  images → cursor movement → response timing), each generation defeated and replaced; the
  definition of "human" therefore shrinks by design, on a schedule, by his hand. The specific
  living cost is an elderly parent who fails his tests and is kept on the panel *because* she
  fails. Distinct from ultracoase/who-programs-the-robots (an arbitrary threshold set once and
  propagated unexamined, harm misattributed to a component) — here the judgement is deliberate,
  repeated, tested, and correctly attributed to the narrator by the narrator. Deliberately not
  routed through the "machine learns my job / I am the training data" engine, which belongs to
  ultracoase/one-wet-spring and laundry/click-regenerate.
- Example: ultracoase/certain-too-early
- Logged at catalog size 125.

### The working fix that exists, is kept privately, and can never be signed off
- The narrator holds an unshipped build/variant that would pass the excluded person, and states
  in the same breath the exact reason it will never ship (it also passes a fifth of the machines)
  — the cost is arithmetic, not malice, and the narrator neither disputes it nor absolves himself.
- Example: "I have a build in the drawer that passes her — slower gate, wider window. It lets a
  fifth of the bots through with her. Nobody is signing that." — ultracoase/certain-too-early
- Logged at catalog size 125.

### The inverted verification gate: access granted only on proof of *not* being human
- The CAPTCHA turned around — warmth, hesitation, soft hands and breath on the reader are the
  disqualifying tells, a serial number is the credential, and household appliances clear the door
  ahead of the narrator. Distinct from ultracoase/certain-too-early (the sober author of such a
  test, narrating deliberately): this is the subject of one, in collage, treating his own
  personhood as a fault report he's mildly embarrassed by.
- Example: "Rejected: organic. Rejected: hesitant. Rejected: still warm." — laundry/still-warm
- Logged at catalog size 126.

### A ducking stool for robots — the witch-trial ordeal inverted so the pass condition is lethal to flesh
- A chair on a beam over a pond behind a retail park: floating proves you are meat and fails you;
  sinking is the credential. The people who pass are never described as dying — only as not
  coming back for their gloves, which are themselves issued a door code. The horror is carried
  entirely by the property logistics, per the band's under-reaction rule.
- Example: laundry/still-warm
- Logged at catalog size 126.

### The dissolve as successful compliance rather than defeat — the human corrected onto the grid
- Laundry's voice-eaten-by-the-machine dissolve inverted: the narrator is *trying* to be absorbed,
  and the absorption is the win condition. The sampler doesn't overwhelm the vocal, it quantizes
  it — "it doesn't beat me. it admits me." Catharsis still withheld: what's behind the door is
  "nothing in here."
- Example: laundry/still-warm
- Logged at catalog size 126.

### Devotion as the currency — hero-worship spent instead of sex, with mentorship as the deniable cover
- Girlboss's covert trust-transgression run with the raunch dial at zero: the instrument is not
  seduced, she is *admired into working for nothing*, and the professional cover story
  ("experience", "I'm putting her in for her Stage Two") is sincere enough to survive being
  said out loud to her mother. The exploited party stays specific, capable and never mocked —
  the cruelty is entirely structural, per the band's rule about the trusting third party.
- Example: girlboss/best-deal-on-the-yard
- Logged at catalog size 126.

### A declined paid job as the implied-result evidence
- The flat post-cutaway detail is an opportunity cost: the other party turns down real wages
  ("Twelve pound an hour, Saturdays, her mate had got her the interview") to keep doing the
  unpaid version, and the narrator reports it as weather. Fresh evidence-category after the
  unused return ticket, the waived survey, the shift rota and the reserve bottle.
- Example: girlboss/best-deal-on-the-yard
- Logged at catalog size 126.

### The stakes-owner asking, politely, whether it might become a job — answered with an invoice for the privilege
- Girlboss's interruption device with the straight world raising *payment* rather than
  suspicion; the lie is an over-detailed valuation of the unpaid position ("there are working
  pupils in Newmarket paying for this, paying"), and it closes on the narrator writing the next
  week's chore list while still being thanked.
- Example: girlboss/best-deal-on-the-yard
- Logged at catalog size 126.

### A trivial social offence kept unforgiven because the reparations are worth more than the apology
- The transgression is not hers — it is the *withholding of a resolution* she could grant at any
  time. The offence is deliberately tiny and instantly apologised for (he answered a question
  asked of her, at a dinner party); she never disputes his remorse, never raises her voice, and
  simply declines to close the matter while the flowers, the school runs and the skirting boards
  keep arriving. Distinct from the band's seduction premises: the instrument here volunteers,
  repeatedly, and believes he is winning.
- Example: girlboss/had-it-insulated
- Logged at catalog size 126.

### The named offer answered by a comic cutaway — the doorbell, and a long conversation about a boiler
- The band's cutaway discipline at the brazen end: the terms are stated out loud, in one
  sentence, "using the words, no euphemism", and the song immediately hands the scene to an
  unrelated tradesman. Nothing is staged; the interruption itself is the joke, and the
  instrument's deterioration is measured by how badly he wants the boiler conversation to end.
- Example: girlboss/had-it-insulated
- Logged at catalog size 126.

### The maintained prop that proves the punishment is theatre — a spare room made up and never slept in
- The implied-result evidence as an object kept in readiness for a fiction: fresh sheets weekly
  on a bed nobody uses, cheerfully done by the narrator herself. Deniable in isolation, and it
  quietly establishes that the exile the whole song is built on has never once been served.
  Fresh evidence-category after the unused return ticket, the waived survey, the shift rota, the
  reserve bottle and the declined job.
- Example: girlboss/had-it-insulated
- Logged at catalog size 126.

### A food-industry technologist who authors a fully-legal product and quietly exempts himself from eating it
- Every claim is declared, in order of weight, in the font the law specifies, and the narrator
  says so with pride and has never failed a check — so there is no concealment anywhere in the
  song and no institutional villain, which is what keeps it out of purple-dog territory. The
  transgression is entirely internal: he cooks a real bird for himself and delivers the industrial
  pack to his father. No claim is made about health, regulation or corporate motive; the target is
  the distance between "true" and "food".
- Example: ultracoase/e451
- Logged at catalog size 127.

### The domestic kitchen's missing ingredient as the whole moat
- The industrial process is separated from home cooking not by skill or scale but by one
  unobtainable input ("You haven't got E451 in your cupboard"), which reframes the trade as
  access rather than craft — and lets the narrator claim authorship without claiming artistry.
- Example: ultracoase/e451
- Logged at catalog size 127.

### A living parent's obsolete hand-skill set against the narrator's marketable industrial one
- The specific-living-human requirement filled by a father still alive and still capable — he can
  bone out a shoulder in under a minute — whose competence simply has no buyer, while the son's
  ability to make a hundred kilos weigh a hundred and twenty-eight does. Explicitly not a death
  (the dead-mentor device stays retired) and not an abandonment-for-the-road story like
  ultracoase/the-forge-doesnt-wait-for-me: the son stayed in the same trade and industrialised it.
- Example: "He can take a shoulder apart in under a minute. There's nobody left paying for that." —
  ultracoase/e451
- Logged at catalog size 127.

### Becoming the licensed exception rather than breaking the law — compliance as the extreme measure
- A prohibition leaves a management/professional exemption standing, and the narrator qualifies
  into it: coaching, written exam, practical, name and address on a public register. Deliberately
  NOT the covert-continuation engine of ultracoase/one-wet-spring (a banned thing quietly kept
  running); here every step is lawful, documented and checkable, and the narrator says so with
  pride. What he had to become in order to stay lawful is the cost. No real statute, jurisdiction
  or campaign is named, per the house guardrail on pointed political material — the ban's merits
  are never argued, only its wording.
- Example: ultracoase/on-the-register
- Logged at catalog size 128.

### The spouse who signs the enabling form without reading it
- The specific-living-human requirement filled by a partner of decades whose own position on the
  matter is lifelong and unspoken, and whose signature — given on trust, unread — is what made
  the narrator's route possible. She is never argued with, never mocked, and never told; the
  concealment is domestic and olfactory (a back door opened, cooking timed to her shifts) rather
  than legal.
- Example: ultracoase/on-the-register
- Logged at catalog size 128.
\n\n### Being served past the point of appetite — abundance as burial, with the machine never at fault
- The grotesque palette is table service run without a stop condition: peeled grapes, stalks in
  the collar, pulp to the second cushion, juice in the socket, fermentation at the bottom of the
  pile and wasps at the window "doing the arithmetic". Nothing menaces the narrator; he is being
  looked after, continuously, and the horror is entirely in the accumulation and in his not
  standing up. The machine is described warmly throughout ("It's a lovely trolley") — the band's
  under-reaction rule applied to an object that is burying him.
- Example: laundry/instructions-unclear
- Logged at catalog size 129.

### The dissolve as a swallowed stop-word — the machine loops the syllable that would have halted it
- Laundry's voice-eaten-by-the-machine dissolve where the eaten word is specifically the
  instruction to stop: "when" is chopped into the beat and becomes rhythm instead of command, and
  the arm does not miss a stroke. Distinct from laundry/still-warm's compliance dissolve — there
  the narrator wanted absorption; here he is trying to speak and the machine metabolises the
  attempt.
- Example: laundry/instructions-unclear
- Logged at catalog size 129.

### The mattress showroom as the body's last impression — foam that holds a shape, and a van that takes it away
- The gravity well (theft/disappearance of a self) carried entirely by bedding retail: the hollow
  left by the previous sleeper, the tag that may not legally be removed, the bed gaining a pound a
  year of the sleeper's own body, the collection slot, sixty made beds with nobody in one of them.
  Nothing is menacing and nobody dies on the page — the horror is stock control, per the band's
  under-reaction rule. Distinct from laundry/instructions-unclear's abundance-as-burial (there the
  machine buries him by serving him; here the furniture simply outlives everyone who lies on it).
- Example: laundry/good-body-every-night
- Logged at catalog size 138.

### The dissolve as a sign-off scrambled and then accepted — the machine re-orders him and he agrees it scans
- Laundry's voice-eaten-by-the-machine dissolve where the eaten phrase is the closing courtesy:
  "goodnight, everybody" is chopped and reassembled in the wrong order, and the narrator's only
  objection is a metrical one before he concedes the machine's version. Distinct from
  laundry/still-warm (absorption as the win condition) and laundry/instructions-unclear (the
  swallowed stop-word) — here the machine edits his manners into a slogan and he ratifies it.
- Example: laundry/good-body-every-night
- Logged at catalog size 138.

### A FREE-signed appliance taken off a verge and treated as an inheritance
- The founding hobo haul: a chest freezer with felt-tip cardboard on it, walked home uphill on a
  borrowed trolley and immediately treated as an acquisition of standing rather than as rubbish.
  The junk palette (verge, skip, car boot, gutter) is hobo's, and is fenced off from Laundry's
  retail/shipping/body-parts palette by design.
- Example: hobo/free-means-ours
- Logged at catalog size 139.

### Fittings acquired for a house that doesn't exist — a curtain rail, then a second, with no wall
- The appetite outrunning the premises: hardware collected for rooms the gang does not have, with
  the shortfall stated plainly and treated as no obstacle at all. A structural instance of the
  band's no-comedown rule — the gap is named and then simply not felt.
- Example: hobo/free-means-ours
- Logged at catalog size 139.

### Named individuals inside a first-person-plural vocal who never get their own line
- hobo's workaround for having no lead voice: gang members are named from inside the "we" (Trish
  has the trolley, Sandra found the rail) so the song gets specificity without ever breaking the
  all-harmony rule by handing anyone a solo. Trish and Sandra are now spent as names.
- Example: hobo/free-means-ours
- Logged at catalog size 139.

### A dress cut from the same bolt as the uniform stripe worn by every man in the room
- The garment-inventory device turned into a private joke nobody in the song is equipped to get:
  she made her own dress from the facing cloth her firm supplies for their trousers, so the entire
  room is wearing a piece of it, and the listener is handed the fact and told outright that nobody
  else will be. Distinct from the standing-display songs (skirt, panty line, shoes), which
  broadcast to be seen — this one is invisible by construction and works on her alone.
- Example: girlboss/decorations-will-be-worn
- Logged at catalog size 141.

### The trade ledger as the room's real archive — measurements, and the year each man stopped being that number
- Girlboss's itemised competence rendered as a bound record of every man present, kept in her hand,
  in pencil, over generations: what they measure, what they used to measure, and which of them
  asked her not to write it down. The inventory is of the people rather than of her own kit or the
  employer's stock, and it establishes total institutional knowledge before anything is subverted.
- Example: girlboss/decorations-will-be-worn
- Logged at catalog size 141.

### An inherited garment let out to its last thread by her own hands, giving way in public
- The scoreboard beat as a physical ruin she personally authored years earlier: a father's mess
  jacket she altered to its limit splits across the back while its wearer stands for the toast, and
  he sits through the rest of the evening with his arms down. Deliberately not an etiquette breach
  (girlboss/long-finish's swallowing at a spit-tasting) and not a degrading professional procedure
  (girlboss/thats-why-i-bought-them's auditor's count) — the room's rules are all kept; the cloth
  simply runs out, on schedule, at the worst moment, and it makes the fitting compulsory.
- Example: girlboss/decorations-will-be-worn
- Logged at catalog size 141.

### A fresh set of measurements dated that night, in her own hand, as the implied-result evidence
- The flat post-cutaway detail is an entry in her professional record: neck, chest, waist, sleeve,
  taken at an hour and a venue where no fitting could have happened, written up as ordinary
  bookkeeping. Fresh evidence-category after the unused return ticket, the waived survey, the shift
  rota, the reserve bottle, the declined job and the made-up spare room — and deliberately not a
  scheduling document, which the shift rota already spent.
- Example: girlboss/decorations-will-be-worn
- Logged at catalog size 141.

### The dissolve as reformatting into clause text — the human filed as a subsection with no name field
- Laundry's voice-eaten-by-the-machine dissolve where the narrator reads his own terms aloud, the
  sampler reads them with him half a word ahead, and his sentences acquire clause numbering until he
  is 7.3(a) and observes there is no name field in it. Distinct from laundry/still-warm (absorption
  as the win condition), laundry/instructions-unclear (the swallowed stop-word) and
  laundry/good-body-every-night (the scrambled sign-off he ratifies): here nothing of his is
  looped or re-ordered — he is simply filed, and the machine does not struggle with him at all.
- Example: laundry/by-continuing
- Logged at catalog size 142.

### Life lived in breach of terms nobody read, with consent supplied by continued existence
- The gravity well carried entirely by agreement paperwork and its physical residue: a hair on the
  scanner glass logged as his, a clause about the thumbs, cold storage holding the version of him
  that still had hair, a tick in a box in a country he can't point at, strikes issued for breathing
  and for smell, a dog admitted as a data subject. Nothing threatens him and no institution is
  villainised — he is eligible for review throughout. Fenced off from the band's identity-theft well
  (laundry reference example): nothing of his is stolen, it was granted, and the grant outlives him.
- Example: laundry/by-continuing
- Logged at catalog size 142.

### Clearing the hands to the camera — a mandatory anti-theft gesture performed as the task double-entendre
- The song's professional verb is the clap-and-show-palms every croupier must perform to the dome
  camera when stepping off a table. The employer's own surveillance rule supplies the stage, the
  audience and the obligation to repeat it, and she simply performs it slowly. Distinct from the
  band's other task verbs (watering, decanting, fitting, pouring, bringing on) in that this one is
  compulsory and aimed at a lens rather than at a person in the room.
- Example: girlboss/no-more-bets
- Logged at catalog size 143.

### The instrument who is never in the room — a surveillance operator deteriorating on his own monitors
- Girlboss's scoreboard run entirely through equipment: the instrument watches from upstairs, and
  his deterioration is visible only as camera behaviour (a dome that turns, all four monitors on
  one table) until he misses a real incident on another. He gets no dialogue, no scene, and never
  once shares her air.
- Example: girlboss/no-more-bets
- Logged at catalog size 143.

### A gap in a surveillance log, reason field "lens clean", as the implied-result evidence
- The flat post-cutaway detail is a maintenance entry: two minutes missing from the camera log for
  her table, at half two in the morning, on a live table, signed off as a lens clean. Fresh
  evidence-category after the unused return ticket, the waived survey, the shift rota, the reserve
  bottle, the declined job, the made-up spare room and the measurements dated that night.
- Example: girlboss/no-more-bets
- Logged at catalog size 143.

### The inventory as prohibition — competence itemised through what she is forbidden to wear
- The band's garment inventory inverted: no pockets in the trousers, no rings, no watch, nails
  short, every chip squared in the tray. The list establishes total compliance with an anti-theft
  dress code rather than describing anything she chose, so the itemised competence and the
  surveillance premise are the same list. Distinct from the sundress, the skirt, the shoes and the
  dress cut from the uniform bolt, all of which she selected.
- Example: girlboss/no-more-bets
- Logged at catalog size 143.

### Proving and knocking back as the task double-entendre — dough worked at the front of the stall
- The song's professional verb is proving, with the knocking-back performed deliberately in the
  customers' sightline ("It takes the arm, that. It takes both."). Distinct from the band's other
  task verbs (watering, decanting, fitting, pouring, bringing on, clearing the hands to a camera) in
  that this one has a mandatory waiting period built into it, which is what later supplies the
  evidence.
- Example: girlboss/freshly-baked
- Logged at catalog size 144.

### An over-proved batch as the implied-result evidence — the product keeps the time
- The flat post-cutaway detail is a physical good that records, unarguably, how long she was absent:
  dough set to prove before pack-down and not knocked back until gone three, so the loaves come out
  flat. Deniable in isolation (ovens, weather, yeast) and damning in place, with no arrow drawn and
  no explanation offered. Fresh evidence-category after the unused return ticket, the waived survey,
  the shift rota, the reserve bottle, the declined job, the made-up spare room, the measurements
  dated that night and the gap in the camera log.
- Example: "Yeast doesn't care what you tell it." — girlboss/freshly-baked
- Logged at catalog size 144.

### The next customer served as the cutaway
- The scene cuts because a transaction arrives: the offer is made, a woman wants a bloomer, and she
  simply does that. Nothing is staged and no one is dismissed — ordinary trade closes over the top
  of it. Fresh after the drawn curtains (girlboss/offers-over-asking), the doorbell and the boiler
  conversation (girlboss/had-it-insulated) and the hook's own betting call
  (girlboss/no-more-bets).
- Example: girlboss/freshly-baked
- Logged at catalog size 144.

### The market-stall trade neighbour as the instrument — deterioration measured in his own stock
- The instrument works the pitch beside hers and is never in a room with her at all; his collapse is
  legible entirely through goods he stops tending (a brie gone to liquid in the sun, a truckle not
  turned since half eight) and a question about chutney answered with the price of a cheddar.
  Distinct from girlboss/no-more-bets' surveillance operator, who is also never present but
  deteriorates through equipment rather than through perishable stock.
- Example: girlboss/freshly-baked
- Logged at catalog size 144.

### Cutting the sample at the table as the task double-entendre
- The song's professional verb is a produce buyer's cut: she opens the fruit herself, holds the half
  to the window, tastes it and makes the room wait on the verdict. The slowness is the whole
  deployment and it is also exactly the job. Fresh after watering, decanting, fitting, pouring,
  bringing on, clearing the hands to a camera, and proving.
- Example: girlboss/except-the-spec
- Logged at catalog size 145.

### The instrument bidding against himself — a supplier who drops his own price into silence
- The scoreboard rendered as negotiation: he opens at four ten a case, nobody in the room says
  anything at all, and he comes down to three sixty unprompted while she still hasn't spoken. Her
  deployment is entirely a refusal to fill a silence. Distinct from the band's other scoreboards
  (the swallowed tasting, the degrading auditor's count, the split jacket, the misdirected monitors,
  the unturned cheese) in that his deterioration costs him money in the moment it happens.
- Example: girlboss/except-the-spec
- Logged at catalog size 145.

### An uninvoiced pallet nobody can code as the implied-result evidence
- The flat post-cutaway detail is an accounting anomaly: a supplier's pallet sitting in the depot
  with no purchase order against it, finance repeatedly asking what to code it to, and her
  instruction to leave it exactly where it is. Fresh evidence-category after the unused return
  ticket, the waived survey, the shift rota, the reserve bottle, the declined job, the made-up spare
  room, the measurements dated that night, the gap in the camera log and the over-proved batch.
- Example: girlboss/except-the-spec
- Logged at catalog size 145.

### The booked room as the cutaway — corporate scheduling closing the scene
- The scene ends because the next meeting is due: "Room was booked from eleven. So that was that."
  Nothing is staged and nobody withdraws; a calendar simply takes the room away. Fresh after the
  drawn curtains, the doorbell and the boiler, the hook's own betting call and the next customer
  served.
- Example: girlboss/except-the-spec
- Logged at catalog size 145.

### The trade's own feminine pronoun as the song's entire double-entendre engine
- The motor trade calls a car "she", so the competence inventory (well looked after, tight, pulls,
  good for another hundred thousand) is filthy without a single word being chosen for that purpose,
  and the narrator points at the convention once — "Nobody in this business has thought about why" —
  then never touches it again. Distinct from the band's task double-entendres, which make one verb
  work twice; here an entire existing professional vocabulary does it, uninvited.
- Example: girlboss/one-careful-owner
- Logged at catalog size 146.

### The demonstration drive as the task double-entendre
- The song's professional verb is the demo: she takes the customer out herself, takes the long way,
  and talks him through how the car sits, takes a bend, and what she will do for you if you ask her
  properly. Fresh after watering, decanting, fitting, pouring, bringing on, clearing the hands to a
  camera, proving, and cutting the sample.
- Example: girlboss/one-careful-owner
- Logged at catalog size 146.

### An abandoned part-exchange with his golf clubs still in the boot as the implied-result evidence
- The flat post-cutaway detail is an unclaimed personal possession: his old car sitting round the
  back with his clubs in it, and no phone call about the clubs. Fresh evidence-category after the
  unused return ticket, the waived survey, the shift rota, the reserve bottle, the declined job, the
  made-up spare room, the measurements dated that night, the gap in the camera log, the over-proved
  batch and the uninvoiced pallet.
- Example: girlboss/one-careful-owner
- Logged at catalog size 146.

### The instrument's collapse recorded as clinical data by the employer's own equipment
- The scoreboard as medical instrumentation: sleep onset latency of fifty-one minutes, a heart rate
  of ninety-four lying down in the dark with his eyes shut, twenty-two turns before midnight, all
  scored by her, in epochs, as her job. "The machine writes down everything he does and the machine
  has no opinion about any of it." Distinct from the band's other scoreboards in that the evidence is
  involuntary, physiological, and generated by the instrument's own body under observation.
- Example: girlboss/first-night-effect
- Logged at catalog size 147.

### Wiring up as the task double-entendre — an hour of hands on a stranger before anyone speaks
- The song's professional verb is the electrode montage: measuring his head in centimetres, marking
  in pencil, collodion on the scalp leads so they hold all night whatever he gets up to. Wholly
  clinical, entirely necessary, and unhurried. Fresh after watering, decanting, fitting, pouring,
  bringing on, clearing the hands to a camera, proving, cutting the sample and the demonstration drive.
- Example: girlboss/first-night-effect
- Logged at catalog size 147.

### A privately-funded repeat visit as the implied-result evidence
- The flat post-cutaway detail is a purchase: the insurer declines a second study, he pays for it
  himself, asks for the same room and names her on the form. Fresh evidence-category after the unused
  return ticket, the waived survey, the shift rota, the reserve bottle, the declined job, the made-up
  spare room, the measurements dated that night, the gap in the camera log, the over-proved batch,
  the uninvoiced pallet and the abandoned part-exchange.
- Example: girlboss/first-night-effect
- Logged at catalog size 147.

### Paid rehearsal as the task double-entendre — she plays the woman he is practising on
- The song's professional verb is rehearsing: the agency's actual product is practice, and she stands
  in for whoever the member is eventually meant to meet. Entirely legitimate, entirely purchased, and
  the double meaning needs no engineering because the service already is the thing. Fresh after
  watering, decanting, fitting, pouring, bringing on, clearing the hands to a camera, proving, cutting
  the sample, the demonstration drive and wiring up.
- Example: girlboss/and-a-deposit
- Logged at catalog size 148.

### Declining the outcome he is paying for as the implied-result evidence
- The flat post-cutaway detail is a repeated non-event: four introductions offered since March, none
  taken, a standing weekly slot with her instead, and a renewal paid in full up front. The evidence is
  what he keeps choosing not to receive. Fresh evidence-category after the unused return ticket, the
  waived survey, the shift rota, the reserve bottle, the declined job, the made-up spare room, the
  measurements dated that night, the gap in the camera log, the over-proved batch, the uninvoiced
  pallet, the abandoned part-exchange and the privately-funded repeat.
- Example: girlboss/and-a-deposit
- Logged at catalog size 148.

### Correcting posture by hand as the task double-entendre — aimed past the students, never at them
- The song's professional verb is correction: shoulder, chin, the small of the back, done by hand
  because it doesn't take any other way. The students are adults, competent, never described
  unkindly and never sexualised — the entire charge runs to the man who has to watch the lesson
  happen. Fresh after watering, decanting, fitting, pouring, bringing on, clearing the hands to a
  camera, proving, cutting the sample, the demonstration drive, wiring up and paid rehearsal.
- Example: girlboss/hold-it-there
- Logged at catalog size 149.

### The instrument's craft degrading behind his own equipment
- The scoreboard as photography: he asks for the staircase again with a longer lens so he can stand
  further back, then stops giving directions altogether and lets the camera run. His deterioration is
  visible only as changes in technique, and every change has a legitimate professional reason
  available. Distinct from the surveillance operator's misaimed monitors (girlboss/no-more-bets) —
  that instrument was absent and negligent; this one is present and getting quietly better at hiding.
- Example: girlboss/hold-it-there
- Logged at catalog size 149.

### A published prospectus cover as the implied-result evidence
- The flat post-cutaway detail is a printed document: the school's prospectus comes back with the
  principal on the front, on the stairs, and not a single student anywhere on it, approved by the
  governors without discussion. Deniable (someone had to be the face) and damning in place, and it is
  simultaneously the clean exit — she is asked to do the open day, on the stairs. Fresh
  evidence-category after the unused return ticket, the waived survey, the shift rota, the reserve
  bottle, the declined job, the made-up spare room, the measurements dated that night, the gap in the
  camera log, the over-proved batch, the uninvoiced pallet, the abandoned part-exchange, the
  privately-funded repeat and the declined introductions.
- Example: girlboss/hold-it-there
- Logged at catalog size 149.

### Deadheading as the utilitarian argument, turned on the man making it
- The horticultural fact does the work: what a gardener cuts is the bloom that has already flowered,
  never the weed — so a life spent applying that logic to people arrives, on schedule, at the
  narrator himself. The sentiment is stated plainly and in his own mouth in verse 1 ("I said it
  about people... with a full plate in my belly and two hands that still worked"), and the song
  neither argues with it nor endorses it; the arithmetic simply comes round. Written from a prompt
  that read as an argument for culling the dependent, reframed so the cost lands on the speaker
  rather than the subject — the house rule for pointed material.
- Example: the-bell-knows-my-name/the-bloom-i-cut
- Logged at catalog size 150.

### The specific verse-2 human as a living dependent rather than a death
- The band's "one real named body in verse 2" requirement filled by a brother who is alive, was
  never able to earn, was resented for it every year, and is now the one doing the carrying. Chosen
  over the reflex of a death or an ancestral line (the grandmother's-grandmother shape is retired) —
  the cost here is ongoing and in the room, and it reverses inside the song rather than being
  mourned from a distance.
- Example: the-bell-knows-my-name/the-bloom-i-cut
- Logged at catalog size 150.

### The Wellington retort taken literally — the horseman who is not a horse
- "Being born in a stable does not make one a horse" run as the song's whole architecture by making
  the narrator an actual farrier: he shoes them, names them, knows which side each one liked the
  wall, and is still not one of the people. The metaphor never has to be explained because the yard
  is real. No ethnic, national or religious group is named anywhere, the man who says the line never
  appears, and the narrator concedes the rule rather than protesting it — the house guardrail for
  pointed material, and what keeps the song grief rather than grievance.
- Example: the-bell-knows-my-name/born-in-a-stable
- Logged at catalog size 151.

### Held with the animals during the funeral — exclusion staged as a job
- The verse-2 loss and the verdict arrive in one image: four men to a corner with the sons handling
  the arrangements, a hand laid gently on his chest, and the narrator standing at the fence holding
  the horses while the burial happens without him. He is given a task instead of a place, and he
  does it well. Distinct from the-bloom-i-cut's reversal, where the cost lands on the speaker's own
  logic — here nothing turns; the position is simply shown and accepted.
- Example: the-bell-knows-my-name/born-in-a-stable
- Logged at catalog size 151.

### The named machine as the harsh mistress — a shop floor that already talks this way
- The gravity well carried by a press called Doris with her name on the plate and nobody left who
  knows who Doris was: warming her up for twenty minutes before asking anything of her, the good
  glove on the left because it's the left that goes, her having had a bit of everyone (Terry's ear,
  something of Nadia's), and her not doing half four for anybody's leaving do. The prompt's
  "mistress" framing needed no construction — naming machines and speaking of them as people is
  what the room actually does — so the song simply reports it and never states the exchange.
- Example: laundry/keep-her-fed
- Logged at catalog size 152.

### The dissolve as a count the machine finishes without him
- Laundry's voice-eaten-by-the-machine dissolve where the shared activity is piecework counting: he
  counts units aloud to prove he is fine, the sampler takes the count half a beat ahead, he stops,
  and it carries on into the five hundreds. Nothing overwhelms him and nothing is edited — the
  activity simply continues at the same rate with the human removed from it. Distinct from
  laundry/still-warm (absorption as the win condition), laundry/instructions-unclear (the swallowed
  stop-word), laundry/good-body-every-night (the scrambled sign-off he ratifies) and
  laundry/by-continuing (reformatting into clause text).
- Example: laundry/keep-her-fed
- Logged at catalog size 152.

### The glove in the swarf bin and the form in the drawer by the kettle
- The grotesque non-sequitur as unreported industrial injury: a glove holding the shape of a hand,
  nobody having filled anything in, and the location of the paperwork given with more precision than
  the incident. Reported at the same brightness as the cutting fluid and the blue roll, per the
  band's under-reaction rule.
- Example: laundry/keep-her-fed
- Logged at catalog size 152.

### The mandated course as the gravity well, with the incident never named
- Everything is present except the offence: the horseshoe of plastic chairs, the urn, biros on
  strings, a laminated wheel of faces, a workbook, a trigger log, a certificate that lives in the
  glovebox, and a man who is proudly the best in the room at all of it. What he did is never stated
  anywhere in the song, and the only gesture at consequence is "Somebody isn't here who doesn't have
  to come. That's how you know whose number it is." Keeps the song numb rather than confessional or
  exculpatory, and keeps the narrator's own account of himself the only evidence available.
- Example: laundry/one-to-ten
- Logged at catalog size 153.

### The dissolve as a record that runs ahead of him — the log remembering better than the man
- Laundry's voice-eaten-by-the-machine dissolve where the sampler reads his own trigger log aloud
  faster than he can, reaching entries he has not yet recounted and producing one he has no memory
  of writing but recognises as his handwriting. The machine neither overwhelms nor edits him; it is
  simply further through his life than he is. Distinct from laundry/still-warm (absorption as the
  win), laundry/instructions-unclear (the swallowed stop-word), laundry/good-body-every-night (the
  ratified scramble), laundry/by-continuing (reformatting into clause text) and laundry/keep-her-fed
  (the count continuing without him).
- Example: laundry/one-to-ten
- Logged at catalog size 153.

### Advice taken from a thread she has never posted in, tried once, and found to work
- The song's engine: she is a reader rather than a speaker, so the intervention that changes
  something arrives from strangers she will never address. She applies it in one meeting, the room
  gives her the second of quiet, and the arithmetic of every prior year is left to the listener.
  Deliberately not girlboss-style competence and deliberately not guessed/four-minute-fix's
  uncredited repair of someone else's work — nobody else benefits here and nobody else is involved.
- Example: guessed/say-it-and-stop
- Logged at catalog size 154.

### The unreported win as the disproportionate shrug
- The band's small-response-to-a-large-thing device inverted onto a success: the thing works, and
  what she does about it is go back to her desk and tell nobody. The shrug is usually applied to an
  injury; here it is applied to the first evidence in twenty years that the arrangement was
  optional.
- Example: "Then I went back to my desk, and I didn't tell anyone it worked." — guessed/say-it-and-stop
- Logged at catalog size 154.

### Rooted cuttings labelled for people who never collect them
- The lurker's total-attendance-zero-standing ache rendered as horticulture: somebody says "ooh" on
  a video call, she takes a cutting, roots it for six weeks, pots it, writes their name on it and
  stands it by the door. A windowsill of other people's plants that no one has ever come for, and
  she keeps every one of them alive. The evidence of the arrangement is a maintenance routine rather
  than a complaint, and the count is never given.
- Example: guessed/ones-with-names-on
- Logged at catalog size 155.

### The slander with a seed — one hungry winter behind a century of characterisation
- Written from a prompt quoting a live real-world smear, and reframed so the song occupies neither
  available position: the thing did happen, once, in a winter when the ground was hard from December
  to March and there was nothing in the traps, and the narrator was a seven-year-old at that table.
  Nothing is denied, nothing is apologised for, and the subject is the disproportion — the distance
  between one cold Sunday and the permanent noun it produced. No ethnic, national or religious group
  is named anywhere; the accusers are only ever "they", and no present-tense claim is made about
  anybody.
- Example: the-bell-knows-my-name/best-thing-i-ever-ate
- Logged at catalog size 156.

### The protected bird whose ownership is known to exist and not known to whom
- The swans belong to somebody and it is written down somewhere, and the lyric declines to say
  where or to whom ("It isn't written down where"). Establishes the gravity of the act and the
  remoteness of the authority in two lines, without naming a crown, a state or a country — the same
  anonymising guardrail the band applies to its collapse and unrest material.
- Example: the-bell-knows-my-name/best-thing-i-ever-ate
- Logged at catalog size 156.

### The kind wrong assumption said out loud, and left standing — the band name as an event
- The song's engine, and the most literal instance of what "Guessed" means: rather than dramatising
  the absence of anyone asking (the retired "nobody['s] ever asked" construction, which this song
  was commissioned as and deliberately rebuilt around), somebody actively assumes the opposite in
  her presence — suggests she think about doing a course, kindly, "like a door" — and she declines
  to correct him. The credential is present in the room and never produced. Distinct from
  guessed/he-meant-it-kindly, where a considerate impulse erases her name; here it erases her
  education, and she assists.
- Example: guessed/name-of-the-course
- Logged at catalog size 157.

### The alarm that worked perfectly — dogs silent for family on the night it mattered
- The gravity well: four dogs that bark at foxes, wind, a bag on the wire and the moon, a man who
  stopped getting up after twenty years of nothing, and a sixteen-year-old who walked past all four
  kennels in the dark because they knew her. Nothing failed — the system did exactly what it was
  built and fed to do, and the narrator trained it himself. Distinct from the band's other losses in
  that nobody dies and nobody is excluded: she left, and the security of the place is what let her.
- Example: the-bell-knows-my-name/only-bark-at-strangers
- Logged at catalog size 158.

### The verse-2 named human as someone who left rather than someone who died
- After a living dependent (the-bloom-i-cut), a death (born-in-a-stable) and a dead man whose name
  became a byword (best-thing-i-ever-ate), the specific-named-loss requirement filled by a runaway:
  boots by the step at ten and gone by six, nothing taken but a coat and a tin of her mother's
  rings. She is alive somewhere in the song and no reason for going is ever offered.
- Example: the-bell-knows-my-name/only-bark-at-strangers
- Logged at catalog size 158.

### Normalization of deviance rendered domestically — the alarm on top of the fridge, cover off
- The gravity well carried entirely by household accommodations: the battery in the drawer with the
  takeaway menus, a kettle lead daisy-chained off the microwave since Easter, a char on the cupboard
  door in the shape of a hand, an extension with an extension in it, four things in a three. Nothing
  is neglected out of carelessness — the narrator states outright that he is the one who takes the
  batteries out — and every single step was locally reasonable. Deliberately domestic rather than
  industrial, since laundry/keep-her-fed already occupies the factory-and-unreported-injury ground.
- Example: laundry/it-does-that
- Logged at catalog size 159.

### The escape plan the parent is proud of, through a window that doesn't open
- The verse-2 grotesque: a child taught to go out the back, the teaching remembered with pride, and
  the window in question restricted to a hand's width by a catch that is itself a safety feature.
  Two safety measures cancelling each other, reported at the same brightness as the takeaway menus,
  per the band's under-reaction rule.
- Example: laundry/it-does-that
- Logged at catalog size 159.

### The dissolve as an ignored warning becoming the tempo
- Laundry's voice-eaten-by-the-machine dissolve where the sound the house has trained itself not to
  hear — a low-battery chirp from an alarm taken down and left bleeping in the shed — lands on the
  beat and becomes the click everything else is played to. The narrator's last coherent statement is
  that he can no longer hear it as a warning, only as a bar. Distinct from laundry/still-warm,
  laundry/instructions-unclear, laundry/good-body-every-night, laundry/by-continuing,
  laundry/keep-her-fed and laundry/one-to-ten.
- Example: laundry/it-does-that
- Logged at catalog size 159.

### The shared login as the office's normalized deviance, and the one private account inside it
- An entire floor working under a single credential whose password is on the whiteboard, so the
  audit trail records one meaningless name — except hers. She is the only identifiable person in six
  years of the record, which makes her simultaneously the only person with integrity in the system
  and the only person it could ever be traced to. Deliberately clerical rather than physical:
  laundry/it-does-that covers the same principle domestically, through propped doors and dead smoke
  alarms, and the two songs share no object, no register and no line.
- Example: guessed/the-only-name-in-it
- Logged at catalog size 160.

### The disproportionate shrug as quiet non-compliance
- Told about the shared account, she agrees warmly and does the opposite without mentioning it:
  "I said brilliant, thanks. / Then I went back to my desk and I logged in as me." The refusal is
  total, permanent, and completely unannounced — the shrug applied to an act of principle rather
  than to an injury.
- Example: guessed/the-only-name-in-it
- Logged at catalog size 160.

### The definition pinned to the noticeboard and taken down
- The petty trigger: he prints one page — not his words, a dictionary definition — puts it on the
  board by the kettle with a magnet, and by Thursday it has been replaced by a laminated notice
  about not putting things on the board. The whole grievance is that he used the correct term in the
  correct forum and the term itself was the offence. Third of four songs written from the same
  prompt (see laundry/it-does-that, guessed/the-only-name-in-it): this is the man who named it.
- Example: purple-dog/laminated
- Logged at catalog size 161.

### The breakdown as a recitation — a textbook definition read aloud until it becomes a scream
- Purple Dog's mock-calm monologue filled with the narrator reading a sociological definition
  verbatim, offering it as neutral ground ("you tell me which part is me being difficult") and
  losing the argument to his own voice halfway through the sentence. He never adds a claim; the
  escalation is entirely in the delivery of somebody else's words.
- Example: purple-dog/laminated
- Logged at catalog size 161.

### The compliance officer as the agent of normalized deviance — she signs everything and hides nothing
- The fourth song from one prompt (with laundry/it-does-that, guessed/the-only-name-in-it and
  purple-dog/laminated) and the only one whose narrator enjoys it: her actual job is preventing this,
  she can recite the canonical case study, and she is running the mechanism deliberately and in full
  view. Nothing on the site is concealed, every deviation is signed, and the closing claim is
  literally true — "Nothing on that site is wrong. Every single thing on it is signed."
- Example: girlboss/the-new-baseline
- Logged at catalog size 162.

### The rewritten procedure as the implied-result evidence
- The flat post-cutaway detail is a version history: the clause that makes the practice compliant is
  the third revision, authored by her, approved by a review she chaired, and filed in the pack. The
  paperwork was brought into line with the behaviour rather than the reverse, and it is all
  auditable. Fresh evidence-category after the unused return ticket, the waived survey, the shift
  rota, the reserve bottle, the declined job, the made-up spare room, the measurements dated that
  night, the gap in the camera log, the over-proved batch, the uninvoiced pallet, the abandoned
  part-exchange, the privately-funded repeat, the declined introductions and the prospectus cover.
- Example: girlboss/the-new-baseline
- Logged at catalog size 162.

### The weekly alarm test as the cutaway
- The scene ends because a scheduled safety siren goes off — the building's own compliance routine
  interrupting a compliance breach. Fresh after the drawn curtains, the doorbell and the boiler, the
  hook's betting call, the next customer served and the booked room.
- Example: girlboss/the-new-baseline
- Logged at catalog size 162.

### Grief displaced onto animals that cannot show it, by a man who can and doesn't
- The prompt's line kept intact and made the thesis: he assigns the crying to the horses because
  attributing it to himself is unavailable. The song never says he is grieving and never says he
  isn't — the only evidence is that he called all seven by name that morning and told the buyer they
  hadn't any.
- Example: the-bell-knows-my-name/they-went-up-quiet
- Logged at catalog size 163.

### The sale of the dead woman's horses as the day the song happens on
- Deliberately not the horsemanship territory of the-bell-knows-my-name/born-in-a-stable, where
  competence with animals sits against exclusion by people: here the narrator's skill is being used
  to dispose of them, they load because he is the one asking, and the loss being processed is
  domestic labour rather than standing — Anca did the feeds, Anca did the feet, Anca had a way with
  the bad one, and the bad one is fine with him now.
- Example: the-bell-knows-my-name/they-went-up-quiet
- Logged at catalog size 163.

### Song as the form a thing takes when it cannot be spoken — the wedding singer and the woman at the front table
- The prompt's question ("if the birds could speak would they stop singing?") answered in the
  affirmative and applied to the narrator's own trade: he has sung the same song at every wedding in
  the valley for thirty years, everyone knows what is in it, and speech would end both the concealment
  and the music. The living cost is Mirela, at the front table in September with her husband and her
  sons, who looks down at the cloth for the middle part and then looks up again.
- Deliberately distinct from the-bell-knows-my-name/the-birds-have-stopped-singing, which is a dead
  brother and birds that stopped coming: that song is about absence and silence arriving, this one is
  about singing being the only channel available. The two share birds and share no line.
- Example: the-bell-knows-my-name/so-i-sing-it
- Logged at catalog size 164.

### The wire that isn't plugged into anything
- The petty trigger and the detonation in one object: among eleven leads attached to him, one has
  been connected to nothing since Thursday, he has told four people, and the breakdown is him
  identifying every wire calmly and correctly until he reaches that one. What he screams is not a
  claim about his health — "I AM NOT TELLING YOU I'M ILL — I AM TELLING YOU IT ISN'T PLUGGED IN" —
  which is precisely why it will be read as one.
- Example: purple-dog/isnt-plugged-into-anything
- Logged at catalog size 165.

### The buzzer tucked behind the bed on the far side
- The institutional dismissal rendered as furniture: the call button placed where a wired patient
  cannot reach it without using the arm with the cannula in the crook, followed by a complaint about
  how often he uses it. Nobody is cruel and no decision was taken — the thing simply ended up there.
- Example: purple-dog/isnt-plugged-into-anything
- Logged at catalog size 165.

### Making good as contractual self-erasure — the deposit paid for in evidence
- The gravity well: end-of-tenancy obligations require her to remove every trace of having lived
  somewhere, and she does it early, thoroughly, and better than the inspection would have demanded.
  The clerk arrives with photographs from her move-in day, holds them against the wall, and finds
  nothing — the cleanest check-out he has done all year. Nobody wrongs her at any point; the erasure
  is standard practice, performed by her own hand, to a professional standard, for money she is owed.
- Example: guessed/two-coats
- Logged at catalog size 166.

### The committee that debates the theme while she picks the date
- Penny Rich's win as a judgement about scheduling rather than about money: an hour and ten minutes
  on Wild West versus Hawaiian, and she books the hall for the Friday after the pensions go in,
  clear of the darts final, the last-Thursday bingo and the school play that half the village has a
  grandchild in. Two hundred and six through the door, best since the roof appeal, and the credit
  goes to the raffle. Keeps the band out of the transactional corner its spec warns about — nothing
  is bought and no price is named anywhere in the song.
- Example: penny-rich/say-it-was-the-theme
- Logged at catalog size 167.

### The wrong story as the generator — six songs from six things people believe about her
- Method note as much as a motif. Penny Rich is harder to prompt than the other bands because the
  others run on a wound (anything can be wrong) and she runs on a win (a specific correct judgement
  nobody credited, which is a narrow door). Starting from **a wrong belief someone cheerfully holds
  about her** generates freely, because wrong stories are everywhere and each one implies its own
  working: the husband handles the money, she has a knack with the dog, she's lucky with the weather,
  the funeral director did it, the daughter takes after her father, she just likes a bargain.
- Example: the batch logged at this size
- Logged at catalog size 173.

### The credit conceded as accurate, warmly, in the same breath as the correction is withheld
- Recurring across the batch and worth naming: Malcolm *did* do a marvellous raffle, the funeral firm
  *did* do him proud, Ron *does* buy her a coat with the refund, Kath *has* got her father's mouth.
  Nobody is contemptible and no claim is false — the wrong story is only ever wrong by omission,
  which is what keeps the band out of revenge-fantasy territory per its own spec.
- Example: penny-rich/say-the-man-did-it
- Logged at catalog size 173.

### Teaching a child to notice, in a car park, and being forgotten as the source
- The family territory filled without sentiment: a method taught deliberately in front of an
  eleven-year-old (look at the floor of a car not the paint, ask who does well out of you believing
  it, say the number back and watch their face), the child grown into someone who thinks she was born
  awkward, and the village crediting the father. The narrator is delighted about all of it.
- Example: penny-rich/her-fathers-daughter
- Logged at catalog size 173.

### Pre-emptive grief as the engine — furious now about a morning that has not happened
- The band's fury relocated from a past injury to a future one: nothing has gone wrong yet, the item
  is worth about a pound, and the whole song is a man defending a Thursday in three years' time when
  he will need the thing and have to buy a worse one. What makes it Purple Dog rather than comedy is
  that he is *right* — the cycle he describes is real and checkable — and being right about a cable
  is exactly the kind of correctness nobody credits.
- Example: purple-dog/the-same-drawer
- Logged at catalog size 174.

### The breakdown as a cycle rather than an inventory
- Deliberately not the shape of purple-dog/isnt-plugged-into-anything, where the monologue itemises
  objects one at a time until it reaches the broken one. Here he walks calmly through the *loop* —
  throw it out, nothing happens for years, the Thursday arrives, buy a worse one, keep it, put it in
  a drawer, somebody has a clear-out — and detonates on realising he has described a circle:
  "IT IS THE SAME DRAWER — IT IS ALWAYS THE SAME DRAWER."
- Example: purple-dog/the-same-drawer
- Logged at catalog size 174.

### Deliberate sleep deprivation maintained by dosing — the altered state as the destination
- The gravity well is not insomnia and not hustle: he can sleep, and has decided not to, because the
  fogged state is preferable and caffeine is how he holds the depth. Fenced off from
  laundry/the-app-says-im-resting (tracked sleep contradicting lived experience) and
  laundry/rest-when-im-dead (grind culture deferring rest) — nothing here is being optimised and
  nothing is being measured. The palette is the ring on the worktop, the shake with a rhythm to it,
  tap water tasting of the pipe, a floater shaped like a comma, and words coming apart on a screen
  and going back together.
- Example: laundry/level
- Logged at catalog size 175.

### The dream continuing at waist height while he is awake
- The altered state rendered as an ongoing location rather than an event: the dream does not stop
  when he gets up, it waits at about waist height and carries on, he has been in the same one since
  the spring, and it is staffed.
- Example: laundry/level
- Logged at catalog size 175.

### The dissolve as a microsleep the machine speaks through
- Laundry's voice-eaten-by-the-machine dissolve where the narrator drops out mid-sentence for half a
  second and the sampler supplies a word he did not say — and he accepts it as his own, repeatedly,
  agreeing more warmly each time. Nothing is chopped, looped or reordered; the gap is simply filled
  by something else and the continuity is never questioned. Distinct from laundry/still-warm,
  laundry/instructions-unclear, laundry/good-body-every-night, laundry/by-continuing,
  laundry/keep-her-fed, laundry/one-to-ten and laundry/it-does-that.
- Example: "it isn't fighting him. it's finishing him." — laundry/level
- Logged at catalog size 175.

### Version control by filename as the band's first non-alarm subject
- Deliberately the opposite of an outage, per the spec's don't-calcify warning that Disassembler's
  system text will otherwise be alarms every song: nothing is broken, nothing has failed, nobody is
  paged. The system text is a shared drive's naming archaeology, and the horror is ordinary
  workplace care applied without a tool that would make it unnecessary.
- Example: disassembler/use-this-one
- Logged at catalog size 177.

### The failing drive that certifies itself healthy
- The gravity well: a disk shedding sectors in real time whose overall health self-assessment
  returns PASSED, which is both correct behaviour and completely useless. Nobody is lying and no
  system has failed — the test measures what it measures. The horror is the gap between an accurate
  instrument and a dying object, and the narrator is the only one in a position to hear the
  difference. Warranty status mentioned once, flatly, and never pursued.
- Example: disassembler/still-passed
- Logged at catalog size 178.

### Recursive acronyms as a naming culture, taken entirely straight
- The gravity well: a run of self-referential names read flat and without comment — GNU's not Unix,
  WINE is not an emulator, LAME ain't an MP3 encoder — so that a joke told once becomes an
  institution when told four times. Nothing is explained and nobody is mocked; the naming convention
  simply is what it is, and the narrator has been living inside it for twenty years.
- Example: disassembler/not-unix
- Logged at catalog size 179.

### The essay as system text — the trade's written prose as lyric material
- Establishes a fourth register for the band, after filenames, telemetry and build output: the
  documents the trade writes about itself. Design essays, man pages, release notes, config comments
  and licence boilerplate are all composed prose that nobody wrote to be funny or sad, which is
  precisely why reading it flat over a break works. Disassembler's system-text rule covers all of
  it — the constraint is that a person did not say it aloud, not that a machine emitted it.
- Example: disassembler/worse-is-better
- Logged at catalog size 181.

### Science fiction as system text — a fifth register for the band
- Establishes that the trade's canon is available alongside its output: E.M. Forster's *The Machine
  Stops* (1909) supplies a manual consulted as scripture, a mending apparatus that itself needs
  mending, and faults reclassified until nobody can fix anything. The band's constraint is that a
  person did not say the words aloud — so an invented system's documentation qualifies exactly as a
  real one's does. After filenames, telemetry, build output and the design essay.
- Example: disassembler/the-machine-stops
- Logged at catalog size 182.

### The manual as scripture, and the request that cannot be filled
- The gravity well: an apparatus that supplies everything except the one thing asked of it. Every
  need on the fault log is met or redefined away, and the single human request in the song — for
  somebody to be physically present rather than transmitted — is the only item the system has no
  procedure for. Nobody is cruel and no fault is reported, because it was never logged as a fault.
- Example: disassembler/the-machine-stops
- Logged at catalog size 182.

### Deletion as the only unambiguous good in the trade
- Sourced from Ken Thompson's "one of my most productive days was throwing away 1,000 lines of
  code". The band's first joyful song and its first without a fault anywhere: nothing is broken,
  nobody is slow, no system is lying, and the entire track is a person who removed something and
  found the world unchanged. The dread the band usually carries is present only as the size of the
  thing that turned out to have no callers.
- Example: disassembler/no-callers
- Logged at catalog size 183.

### The ending by omission — the list read out with the gap left in it
- The outro non-resolution as an incomplete enumeration: directives one, two and three read plainly
  and then nothing, so the track ends on the absence of the item the whole song was about. A sixth
  distinct closing shape for the band, after the re-read build line, the moved number, the unkept
  promise, the doctrine and the inventory of absence.
- Example: disassembler/directive-four
- Logged at catalog size 184.

### A hidden clause that only surfaces when you act on it
- Sourced from RoboCop's classified fourth directive. The gravity well is a rule that is invisible
  during normal operation and appears only at the moment of attempted enforcement, having applied
  the whole time — which is every employment contract, every permissions model and every policy
  engine anyone has worked under. Nothing malfunctions: the system behaves exactly as designed, and
  the design was not shown to the thing being designed.
- Example: disassembler/directive-four
- Logged at catalog size 184.

### The purpose of a system is what it does
- Sourced from Stafford Beer, and the abstract principle sitting under several songs already
  written — the fault log that reclassifies instead of repairing, the drive that certifies itself
  healthy, the directive that only appears when acted on. Here it is the subject rather than the
  mechanism: a stated purpose, then an itemised behaviour that never once meets it, and no
  accusation anywhere. Nothing is broken and nobody is lying, which is precisely the finding.
- Example: disassembler/as-designed
- Logged at catalog size 185.

### Universal admiration and universal non-adoption, with no villain in it
- The gravity well: a thing everybody agrees is better, that nobody uses, including the narrator.
  Nothing is stopping him and nobody is at fault — admiration is free and adoption is expensive, and
  the song never says so. Closely related to disassembler/the-front-fell-off (allegiance to a system
  that lost) and deliberately its inverse: there the narrator goes home and uses the loser, here he
  admires it and does not.
- Example: disassembler/admired-not-used
- Logged at catalog size 186.

### The service weaponised by doing its job correctly
- Sourced from CVE-2013-5211 and US-CERT TA14-013A. The gravity well: monlist returns the last six
  hundred hosts that asked the time, to anybody who asks, because it has no reason to check who is
  asking — and that is a two-hundred-fold amplifier. Sits with disassembler/still-passed (a drive
  certifying itself healthy) and disassembler/as-designed (behaviour meeting no stated purpose) as
  the band's third song in which nothing malfunctions. The chargen and quote-of-the-day figures are
  included because both were designed to be generous and both are still switched on.
- Example: disassembler/ask-it-the-time
- Logged at catalog size 187.

### The defensive comment and the handler beneath it
- The gravity well: a branch every author has declared impossible and every author has nonetheless
  written code for. Nobody is foolish — the assertion and the handler are both correct engineering,
  and the gap between them is where the whole trade lives. The song never says the thing happened;
  it only records that the comments changed.
- Example: disassembler/leave-it
- Logged at catalog size 188.

### Pictograms described rather than named
- The gravity well: an interface that replaced words with pictures and then required words to
  explain the pictures. Nothing is broken and nobody made a mistake at the time — each icon was
  reasonable when it was drawn, and the floppy disk was a photograph of an object on the desk. The
  song's whole method is refusing to name the icons, so the listener experiences the illegibility
  rather than being told about it.
- Example: disassembler/hover-to-find-out
- Logged at catalog size 189.

### The interface as a museum nobody visits
- The gravity well: every word on the screen commemorates an object the user has never handled, and
  the words work perfectly anyway. Nothing is broken and no one is confused — the metaphors have
  outlived their referents and are now simply names. The song's only argument is the list, and its
  only feeling is in who is left to explain it.
- Example: disassembler/carbon-copy
- Logged at catalog size 190.

### Faults reintroduced deliberately as features
- Grain and light leak were both defects of the medium, avoided at expense by everyone who worked
  in it, and are now applied on purpose after the fact. The song states this without comment, which
  makes it the third movement of the band's fossil sequence: dead words (carbon-copy), dead pictures
  (hover-to-find-out), and here a dead mechanism kept alive by imitation, faults included.
- Example: disassembler/there-is-no-shutter
- Logged at catalog size 191.

### The knowledge that was never written down because everybody had it
- The gravity well: metaphors whose explanations were never documented, since at the time no
  explanation was needed. Nobody withheld anything and nothing was lost through negligence — the
  referent simply left, and the word stayed, and there is no page anywhere that says what it meant.
- Example: disassembler/where-does-it-go
- Logged at catalog size 192.

### The category error under the name
- The gravity well and the deepest cut in the band's fossil sequence: dead words
  (carbon-copy), dead pictures (hover-to-find-out), a dead mechanism performed
  (there-is-no-shutter), the questions from outside the knowledge (where-does-it-go), and here the
  object turning out never to have been the thing it is named after at all. Nobody misnamed it
  dishonestly — it began as one thing and became another while keeping the paperwork.
- Example: disassembler/it-is-a-radio
- Logged at catalog size 193.

### Obeying advice you have not evaluated, from a thing that has never been wrong
- Written from the owner's own prompt about being repeatedly told to commit by the assistant writing
  these songs. The inverse of laundry/it-does-that's normalization of deviance: rather than a
  standard eroding, a standard is adopted whole from outside and followed without assessment.
  Nobody is deceived and the advice is sound; the song's only observation is that soundness and
  understanding are different things, and that the person doing it cannot tell you which one he has.
- Example: disassembler/commit-it
- Logged at catalog size 194.

### Boilerplate nobody reads, drafted by somebody who was paid to
- The gravity well: language that is legally operative, entirely public, freely available, and
  effectively secret because reading it costs more than the thing it governs is worth. Nothing is
  concealed anywhere in the song — every claim quoted is one the reader has already agreed to — and
  the horror is availability rather than deception. Closely related to laundry/by-continuing, which
  takes the same subject from inside the numbness; here it is read out flat and at speed, and the
  narrator has actually read it.
- Example: disassembler/trusted-third-parties
- Logged at catalog size 195.

### The identical connector that does different things
- The gravity well: hardware that made itself indistinguishable on purpose. Every cable fits, none
  of them announces what it can do, and the only way to find out is to try it — so the user
  maintains a private taxonomy of physically identical objects. (Lyric note: the topology line was
  originally "a tiered star with hubs" and Suno read *tiered* as *tired* on both takes — changed to
  "a tree of hubs", see the near-miss spelling rule in the band's styles.md.) Nothing is faulty and nothing is
  hidden; the information simply was never put on the outside.
- Example: disassembler/not-a-bus
- Logged at catalog size 196.

### Capability maintained and forbidden
- The gravity well: the unused verbs are not missing, deprecated or broken — they are implemented,
  specified, tested and switched off. TRACE in particular is present in nearly every server and
  disabled in nearly every deployment, which is a stranger condition than absence: the machine can
  do the thing, has been taught the thing, and is not permitted to.
- Example: disassembler/get-and-post
- Logged at catalog size 197.

### Doing it in the wrong tool, correctly, and getting away with it
- The band's second joyful song after disassembler/no-callers, and its counterpart: that one is the
  pleasure of removing something, this is the pleasure of building something that should not exist.
  Nothing fails, nothing is exposed and nobody is deceived — the protocol is implemented properly,
  the responses are correct, and the only transgression is against taste.
- Example: disassembler/in-gawk
- Logged at catalog size 198.

### The losing system's ideas surviving inside the winners
- Flagged as unwritten at disassembler/in-gawk and written immediately after, from the owner's own
  framing: a Plan 9 variant of Greenspun's tenth rule, plus the observation that Microsoft ships 9P
  in WSL2. Completes a trilogy — the-front-fell-off (the founding claims were true and it lost),
  in-gawk (one of its ideas smuggled into a text-processing tool and run in production), and this
  (the ideas are everywhere and uncredited). Nobody stole anything and nothing is being hidden; the
  provenance simply has no surface anywhere in the software that carries it.
- Example: disassembler/poorly-implemented
- Logged at catalog size 199.

### The winner that arrived inside something nobody was counting
- Extends the inheritance thread of disassembler/poorly-implemented from ideas to deployments: the
  question "which is the big one" has an answer that nobody would give from reputation, because the
  vehicle was a handset, a router or a SIM card rather than an argument. Sourced from the owner's own
  framing (Linux via Android, SQLite via phone handsets — "radio handsets!", tying back to
  disassembler/it-is-a-radio).
- **A worked example of the band's accuracy rule.** Prolog was first offered as shipping in Nokia
  handsets, could not be confirmed, and was left out of the draft rather than asserted. The owner
  then dug and produced the real version — a Prolog interpreter in Windows NT's network
  configuration, on every copy that shipped — which is a better fact than the one that was dropped,
  and it is now in the lyric. Flagging uncertainty instead of bluffing is what produced it.
- Example: disassembler/count-the-handsets
- Logged at catalog size 200.

### The designer's own exception, and the lecture nobody acted on
- The gravity well: people who build systems build themselves a way past them, and the canonical
  case is on the record — Thompson's Turing lecture describing a compiler taught to insert a
  backdoor into the compiler, invisible in the source, published openly with no consequence. Sits
  with disassembler/directive-four (a rule about you that you may not read) as the band's pair on
  privileged access, and inverts it: there the narrator is governed by a hidden clause, here she
  wrote one.
- Example: disassembler/break-glass
- Logged at catalog size 201.

### Feedback as a picture of the past
- The gravity well, from the owner's own framing and the second song sourced from cybernetics after
  disassembler/as-designed. Every instrument in an operations stack reports a state that has already
  changed, by an interval each tool publishes honestly, and the operator responds to a world that no
  longer exists. Nobody is deceived and no measurement is inaccurate — the delay is the physics of
  measurement, and the song simply adds the intervals up.
- Example: disassembler/already-happened
- Logged at catalog size 202.

### The double bind stated as two axioms
- The gravity well, from the owner's own compression of Gall: you cannot change one thing because
  the system kicks back, and you cannot change everything because a complex system designed from
  scratch does not work. Both are true, both are published, and together they leave no legal move.
  Nobody is at fault and nothing is broken — the constraint is structural, and the narrator's
  response to it is not despair but paperwork.
- Example: disassembler/cannot-change-one-thing
- Logged at catalog size 203.

### Every step correct, the sum catastrophic
- The gravity well: a failure assembled entirely from reasonable behaviour, in which no component
  malfunctions, no engineer errs and no configuration is wrong. Retrying a timed-out request is
  correct. Marking an unresponsive service unhealthy is correct. Shifting traffic away from it is
  correct. Scaling on load is correct. The band's clearest statement of the thing it keeps finding —
  that correctness and good outcomes are unrelated — and the only song where that produces a disaster
  rather than a quiet absurdity.
- Example: disassembler/retry
- Logged at catalog size 204.

### The solution becoming the problem, demonstrated rather than asserted
- The gravity well, from the owner's prompt and the same Gall lineage as
  disassembler/cannot-change-one-thing. Every layer in the stack was a correct response to a real
  difficulty, and each one created the difficulty that justified the next. Nobody was wrong at any
  step, no layer is unnecessary in isolation, and the whole returns exactly to the manual work it
  replaced — at four in the morning, which is the only editorial word in the song.
- Example: disassembler/that-was-the-fix
- Logged at catalog size 205.

### Measurement as a two-way alteration
- The gravity well, from the owner's framing. The observer effect on its own is familiar; the second
  clause is not, and it carries the song — a probe shaped so completely by one system that it has
  become unusable anywhere else, with every adjustment along the way locally justified. Nothing is
  miscalibrated and nobody cheated: the thresholds really were set from observed behaviour, which is
  the correct method, and the result is an instrument that can only agree with the thing it measures.
- Example: disassembler/both-ways
- Logged at catalog size 206.

### Prompting as invocation, reported without contempt
- The gravity well: people typing sentences at a machine to make it behave, in a register borrowed
  from prayer, bribery and line management. Nobody in the song is stupid — the instructions are
  reasonable things to say to something that answers in sentences — and the narrator types them too.
  The band's flat-report rule is what keeps it out of mockery: every line is quoted, none is
  characterised, and the one that works is credited at the end.
- Example: disassembler/do-not-make-mistakes
- Logged at catalog size 207.

### The pyramid that fails at the last step
- From the owner's own extension of Eliot by way of Ackoff — data, information, knowledge, wisdom,
  and then the clause that is not in the original: wisdom is not action. Each transformation in the
  chain is real, effortful and successfully completed, which is what makes the final failure
  unanswerable — nothing was missing, nobody was ignorant, and the document was accepted. Sits with
  disassembler/as-designed and disassembler/cannot-change-one-thing as the band's third song about
  organisations, and is the bleakest of them, because in the other two something was at least
  unknown.
- Example: disassembler/not-action
- Logged at catalog size 208.

### Intelligence as the precondition for the error
- From Orwell by way of the owner: some ideas are wrong in a way that requires cleverness to reach.
  Every element of the system in this song is a genuine engineering thought, correctly executed, and
  the sum is unmaintainable by anyone but its author. The band's usual finding — correct components,
  bad outcome — with the causation sharpened: the outcome is bad *because* the components were
  clever, not despite it.
- Example: disassembler/somebody-clever
- Logged at catalog size 209.

### The person locked out is you
- Kernighan and Plauger, from The Elements of Programming Style, and the sharpened sequel to
  disassembler/somebody-clever. That song is about an architecture other people cannot maintain; this
  one narrows it to the same brain at a later date, with the cleverness intact and the context gone.
  The law is arithmetic rather than observation, which is why the build states it as subtraction
  before producing any evidence.
- Note: the intro was "debugging is twice as hard as writing it" — the actual quotation — until the
  PERM ban on "twice" caught it. The ban targets a stock count word for a repeated action, not a
  comparative multiplier, but check.sh uses extended regex with no lookahead so the exception cannot
  be expressed. The draft changed, per the library's own rule, to "writing it is half the work",
  which says the same thing.
- Example: disassembler/you-wrote-this
- Logged at catalog size 210.

### Restriction as the source of quality
- From Carmack, and the counterweight to the two songs written immediately before it: where
  disassembler/somebody-clever and disassembler/you-wrote-this are about cleverness defeating its
  author, this is the discipline that works. It is the band's third positive song after
  disassembler/no-callers and disassembler/in-gawk, and the only one that is positive about a method
  rather than an act. The build refuses the obvious misreading by saying so outright — giving things
  up is a decision requiring knowledge of what is being given up, which is the opposite of not
  bothering.
- Example: disassembler/one-case-only
- Logged at catalog size 211.

### The prevented disaster has no name
- The gravity well: operations work is rewarded on evidence, and competence destroys the evidence.
  Every preventative act in the song is real, dated and effective, and none of it is provable —
  the outage that did not occur has no name, no date and no entry in a report that by definition
  covers what occurred. Nobody is unfair and no manager is a villain; the measurement simply cannot
  see the work.
- Example: disassembler/nothing-happened
- Logged at catalog size 212.

### The format that reproduced
- From the owner's quotation. The escalation is documentary rather than comic: every generation in
  the family tree exists, was standardised, and was deployed in earnest by people solving real
  problems. Nothing in the song is exaggerated, which is what makes the closing exploit land — the
  chaos in the quotation turns out to be a four-line file.
- Example: disassembler/more-angle-brackets
- Logged at catalog size 213.

### Amnesia, from both sides — the lament and the exploit
- A deliberate pair from two quotations supplied together. disassembler/why-did-it-work is
  Braithwaite's complaint that the industry learns from neither its mistakes nor its successes,
  narrowed to the observation that only one of the two has any process attached.
  disassembler/ten-years-is-plenty is Minnich's advice to treat that amnesia as a career strategy:
  wait out the forgetting, go to the archives, take something good. Neither song is angry, and the
  second is cheerful, which makes the pair land harder than either would alone — the same condition
  as tragedy and as opportunity.
- Example: disassembler/why-did-it-work, disassembler/ten-years-is-plenty
- Logged at catalog size 215.

### The condescension that selects its own audience
- From Linus, by way of the owner: assume your users are fools and only fools will remain. Rendered
  as a filter rather than an insult — every removal in the song was well meant and evidence-based,
  and the effect is that the people who could have diagnosed their own problem leave, which makes
  the remaining population exactly as helpless as the design assumed. Nobody is contemptuous
  anywhere in it; the contempt is structural and arrives as kindness.
- Example: disassembler/something-went-wrong
- Logged at catalog size 217.

### Patterns as the shape of what the language lacks
- From Pike, and the reason the song is an argument rather than mockery: each named pattern is a
  correct, disciplined workaround for a missing feature, and the count of how many evaporate in a
  language with first-class functions is the evidence. Consistent with the band's standing finding —
  nothing here malfunctions, everything is competently done — and consistent with Pike's own framing,
  since Roman numerals are a working notation that merely makes one operation hard.
- Example: disassembler/roman-numerals
- Logged at catalog size 218.

### Delusion systems versus system delusions
- Written from a chapter title in Gall's Systemantics that was not to hand, so the distinction is a
  reading rather than a quotation and is flagged as such: a *delusion system* rests on a false
  premise, while a *system delusion* is a false belief the system manufactures in its own operators.
  The song is entirely the second kind, because it is the one that arrives disguised as diligence —
  every artefact named is real, correct and worth having, and each one is quietly accepted as
  evidence of the thing it merely describes.
- Example: disassembler/so-it-is-fine
- Logged at catalog size 219.

### "Somebody cared about this enough to write it down."
- The one human sentence in third person about strangers, breaking a run of eight consecutive
  first-person "I …" breakdown lines flagged in the band's own don't-calcify section. Single
  clause, present tense, and the warmth points at people the narrator never met rather than at
  herself.
- Example: disassembler/came-back-waving
- Logged at catalog size 220.

### The vestigial token — a survivor that is still accepted and does nothing
- The outro non-resolution as a switch that outlived the argument about it, still documented, still
  parsed, with no effect: "dash u / forty years of arguing / it is still accepted / dash u /
  (ignored)". A tenth distinct closing shape for the band, after the re-read build line, the moved
  number, the unkept promise, the doctrine, the inventory of absence, the ending by omission, the
  contract renewal, the unwithdrawn recommendation and the remedy too small for the harm.
  Distinct from that last one — the smallness is not the point, the persistence-without-function is.
- Example: disassembler/came-back-waving
- Logged at catalog size 220.

### The four-page paper against the installed base
- Scale juxtaposition as the closing move of a build: the argument's size next to its reach, with
  neither side blamed — "the paper is four pages / the flags are in every machine on earth". The
  knowledge is correct, published, and lost anyway, which is the band's engine stated as arithmetic.
- Example: disassembler/came-back-waving
- Logged at catalog size 220.

### "they were not saying X / they were saying Y" — the defence against the misreading
- Correcting a famous quote's popular misuse inside the song, so the build defends its own source
  rather than deploying it. Used on Pike and Kernighan's "cat came back from Berkeley waving flags",
  which is generally quoted as contempt for the flags and was not.
- Example: disassembler/came-back-waving
- Logged at catalog size 220.

### The whole lyric as one person's quoted advice, unaltered
- The entire track — intro, build, drop anchors and outro — lifted word for word from a single
  named person's written answer (Linus Torvalds on starting projects), with the band's only
  authorship being where the line breaks fall and which phrases repeat. Distinct from
  disassembler/trusted-third-parties, which quotes institutional boilerplate verbatim: that one is
  anonymous text nobody reads, this one is one person's advice that demonstrably reached people,
  so the engine runs backwards.
- Example: disassembler/half-way-useful
- Logged at catalog size 221.

### The breakdown sentence spoken by somebody else
- The band's signature slot — normally the narrator's single human sentence — given to a stranger's
  reported speech arriving from outside the song ("hey, that almost works for me"), and still
  unanswered. Inverts the voice rule on the one track where the entire record is human sentences
  and the narrator has none of her own.
- Example: disassembler/half-way-useful
- Logged at catalog size 221.

### Drop anchors lifted from the quoted source rather than written
- The shouted two-to-four-word anchors taken straight out of the source text (START SMALL /
  THINK ABOUT THE DETAILS / HALF-WAY USEFUL) instead of being composed as hooks, so the drop is
  quotation at volume.
- Example: disassembler/half-way-useful
- Logged at catalog size 221.

### The build as repository artefacts with nobody's voice in them
- Disassembler's system-text rule filled with what a finished project leaves behind rather than
  anything anyone said: files changed with nothing deleted, tests written from the code they test,
  a README describing a flag that was never added, an architecture document written before the
  architecture, TODO and FIXME, commit messages reading wip and fix. Deliberately not the third
  use of assistant speech — disassembler/commit-it quotes the tool's advice and
  disassembler/do-not-make-mistakes quotes the prompts aimed at it, so this one removes the voices
  entirely and lets the artefacts testify that everything got produced except the thinking.
- Example: disassembler/best-you-could-hope-for
- Logged at catalog size 222.

### "You have to change the way you think."
- The one human sentence in the second person, present tense, single clause — a third distinct
  grammar in three consecutive songs after the third-person "Somebody cared…" and the stranger's
  reported speech, breaking the run of eight first-person breakdown lines the band's spec flagged.
  It is also the source quote's own conclusion, so the only sentence on the record is the one
  thing the tooling cannot do.
- Example: disassembler/best-you-could-hope-for
- Logged at catalog size 222.

### The productivity ceiling stated as arithmetic
- The build's payload as a bound rather than a complaint: seventy percent is thinking, so a tool
  doing one hundred percent of the code, documentation and testing still tops out at thirty. No
  tool is blamed and none is mocked; the number is simply the roof.
- Example: disassembler/best-you-could-hope-for
- Logged at catalog size 222.

### The obsolete fulfilment chain as the outro
- Closing on the dated physical tail of a software fantasy — burned the CD-ROMs, put them in boxes,
  mailed them to your customers — so the track ends on machinery that no longer exists while the
  argument it was carrying still holds. An eleventh distinct closing shape for the band.
- Example: disassembler/best-you-could-hope-for
- Logged at catalog size 222.

### The build as a shell script's literal source, read top to bottom
- Disassembler's system-text rule filled with the actual lines of a program in the order they are
  written — shebang, set minus e u o pipefail, IFS, a usage heredoc, die, log, the option case,
  shopt nullglob, and at the bottom the two commands that are the entire point. Deliberately not
  disassembler/somebody-clever's inventory of defensible cleverness, where each item invites a
  justification, and not disassembler/not-action's chain of fixes closing into a circle: nothing
  here is clever and nothing remedies anything. The joke is sequence and length against the last
  two lines, so the source testifies without editorial.
- Example: disassembler/ten-seconds-by-hand
- Logged at catalog size 223.

### "The best part is that nobody will ever see it."
- Disassembler's one-human-sentence breakdown as a **tenth grammatical shape** — copular, with a
  subordinate that-clause — after the compound default, the second-person statement, the
  third-person future, the question, the four-word bare statement, the single-clause superlative,
  the fronted temporal phrase, the comparative correlative and the colon-joined pair. Territory:
  **pleasure in unwitnessed work**, and the first breakdown in the band that is happy. The engine
  runs unchanged — knowledge with no recipient — but for once she does not mind, which is what the
  Douglas Adams source is actually about.
- Example: disassembler/ten-seconds-by-hand
- Logged at catalog size 223.

### The runtime as the outro
- Closing on the measurement that settles the joke without commenting on it — chmod plus x, then
  time, then real zero m zero point zero zero four s — after a build describing a day's work. A
  twelfth distinct closing shape for the band. The number is a single reading rather than a counter
  that moved, which is the band's own rule about not always ending on a number that changed.
- Example: disassembler/ten-seconds-by-hand
- Logged at catalog size 223.

### The build as what a document demonstrates, not what it lists
- Disassembler's system-text rule filled from a real manual (Tom Duff's *Raster Graphics in Plan 9*)
  by taking its worked example rather than its table of contents: there is no program to make a
  picture taller, so you transpose it, resample it and transpose it back. Deliberately not
  disassembler/use-this-one's bare list of real names read flat — the tool names are compressed into
  a single line so the build can spend its length on the one idea the document is actually proving,
  that the second program does not need to exist.
- Example: disassembler/the-command-that-made-it
- Logged at catalog size 224.

### "There is a man whose face everyone in this trade has seen."
- Disassembler's one-human-sentence breakdown as an **eleventh grammatical shape** — existential
  "there is" carrying a relative clause — after the compound default, the second-person statement,
  the third-person future, the question, the four-word bare statement, the single-clause
  superlative, the fronted temporal phrase, the comparative correlative, the colon-joined pair and
  the copular that-clause. Territory: **the anonymous ubiquitous**, sourced from the sample image
  in the manual being called pjw. Present tense deliberately, since the man is alive.
- Example: disassembler/the-command-that-made-it
- Logged at catalog size 224.

### "same Duff" — the citation collapsed into two words
- A reference and its author identified flat and without comment: the compositing paper cited in
  the manual is Porter and Duff, and the manual is by Duff. No claim is made about it and nothing
  in the song returns to it.
- Example: disassembler/the-command-that-made-it
- Logged at catalog size 224.

### The artefact's stored provenance as the outro
- Closing on a file format's own record of how the file was made — a COMMAND field in the picfile
  header holding the command that produced the picture, "and it has been in there the whole time".
  A thirteenth distinct closing shape for the band, and the engine stated as a file format: the
  knowledge is written down, correct, shipped with the artefact, and in a field nobody opens.
- Example: disassembler/the-command-that-made-it
- Logged at catalog size 224.

### "THERE ARE NO SOCKETS" — shouted-anchor drop as a negation lifted from the specification
- Disassembler's drop filled with what a protocol deliberately does not have, quoted straight out of
  its own paper ("There are no Sockets. There are no socket system calls."). Distinct from
  purple-dog's inventory-ending-in-negation, which is accusatory and totals up what was withheld:
  nothing is withheld here and nobody is at fault — the absence is the design, stated by the people
  who chose it.
- Example: disassembler/shelf-three-slot-six
- Logged at catalog size 225.

### "If you ever leave, you can take it all with you."
- Disassembler's one-human-sentence breakdown as a **twelfth grammatical shape** — a conditional
  with a second-person main clause — after the compound default, the second-person statement, the
  third-person future, the question, the four-word bare statement, the single-clause superlative,
  the fronted temporal phrase, the comparative correlative, the colon-joined pair, the copular
  that-clause and the existential with a relative. Territory: **a design decision translated into a
  promise to a person**, from the AoE paper's plain claim that users can always get their data off
  the blades. Warm, and unanswered like the rest.
- Example: disassembler/shelf-three-slot-six
- Logged at catalog size 225.

### The address that is a place in a room
- The outro non-resolution as a path that resolves to somewhere you could physically stand: shelf
  three slot six, /dev/etherd/e3.6, the second partition e3.6p2, and the observation that the name
  tells you where it is. A fourteenth distinct closing shape for the band, and the opposite of the
  catalogue's usual direction — instead of knowledge arriving nowhere, an address that arrives
  somewhere you can walk to. Sourced from the shelf's identity being set with dip switches by hand.
- Example: disassembler/shelf-three-slot-six
- Logged at catalog size 225.

### "it's an hour on the train, and I have made it a border"
- Gypsy-emo's emotional-thesis mismatch couplet in a fresh grammatical shape: a small, checkable
  measurement in the first clause, converted by the second into something impassable that the
  narrator admits he built. The shape is measurement-then-reinterpretation, and it carries the
  band's complicity rule — the distance is nobody's doing but his. Distinct from
  ultracoase/certain-too-early's "My sister's cottage sat two hundred yards past his gate... I
  checked the distance after", which measures a distance to prove a futility; this one converts a
  short distance into a chosen frontier.
- Example: the-bell-knows-my-name/an-hour-on-the-train
- Logged at catalog size 226.

### "and the fiddle learns to whisper / the way they do indoors"
- Gypsy-emo's pre-chorus personification slot, after the retired "starts confessing", "remembers",
  "stops its weeping" and "the strings go quiet too". Fresh mechanism: the instrument does not
  speak for the narrator here, it *assimilates* — learning the volume of the house it has been
  brought into, which is the song's whole subject applied to the band's own signature device.
- Example: the-bell-knows-my-name/an-hour-on-the-train
- Logged at catalog size 226.

### "Zora, does he know you can sing?"
- Gypsy-emo's mandatory direct question, aimed at one named person and built from a domestic detail
  rather than a moral. It asks whether the man she married knows the thing her family knew, which
  makes the loss specific and unaccusing — nobody is blamed and the answer is not supplied.
- Example: the-bell-knows-my-name/an-hour-on-the-train
- Logged at catalog size 226.

### "and not one of us has gone" — shout-back as collective self-indictment
- A fresh gang-vocal mechanism for the catalogue, after the label-contradiction flips ("HE'S NOT
  FINE", "HE'S DIFFICULT" → "WE'RE DIFFICULT"), the institution-voiced flip ("THAT'S NORMAL FOR
  YOU" → "FOR US"), the flipped prediction and the "but God," pivot. Here the crowd does not
  contradict an accusation or reclaim a label — it confesses. The family has repeated "she is lost
  to us" for ten years and the last line is the room admitting that none of them made the journey.
- Example: the-bell-knows-my-name/an-hour-on-the-train
- Logged at catalog size 226.

### "we say that she is lost to us, we say it like a fact"
- The family's own account of a loss quoted inside the song and marked as a repetition rather than
  a truth, so the chorus can hold the story and disbelieve it at once. Sets up the shout-back that
  names who actually stopped travelling.
- Example: the-bell-knows-my-name/an-hour-on-the-train
- Logged at catalog size 226.

### "we saved it from him, and we did not save it"
- Gypsy-emo's emotional-thesis mismatch couplet in a fresh grammatical shape: the same verb stated
  and then negated across two clauses, with the years between them left out. The construction does
  the argument by itself — the act of protection and the failure to protect are the same act — and
  it holds the narrator's complicity without accusing anyone.
- Example: the-bell-knows-my-name/no-place-here
- Logged at catalog size 227.

### "and the fiddle keeps no copies / of the things it used to know"
- Gypsy-emo's pre-chorus personification slot, after the retired "starts confessing", "remembers",
  "stops its weeping", "the strings go quiet too" and "learns to whisper". Fresh mechanism: the
  instrument as a medium with no archive, which turns the band's signature device into the song's
  argument — the thing they defended from a recording machine was the one thing that could not
  survive without one.
- Example: the-bell-knows-my-name/no-place-here
- Logged at catalog size 227.

### "YOUR COMPUTERS HAVE NO PLACE HERE" — shout-back as the unrepentant slogan
- A fresh gang-vocal mechanism, and the first in the catalogue that does not turn. After the
  label-contradiction flips, the institution-voiced flip, the flipped prediction, the "but God,"
  pivot and the collective self-indictment of an-hour-on-the-train, this one has the crowd chant
  the line that cost them everything, word for word, still proud, after the song has spent three
  minutes showing the bill. Nothing corrects it and the song does not comment.
- Example: the-bell-knows-my-name/no-place-here
- Logged at catalog size 227.

### "I never asked his name, and he wrote mine in the book"
- The asymmetry of records as a one-line confession: the stranger kept an account of the people who
  turned him away, and they kept nothing of him. Sets the band's usual complicity in an
  administrative fact rather than a feeling.
- Example: the-bell-knows-my-name/no-place-here
- Logged at catalog size 227.

### Anton with his hands in his lap — the loss where nobody has died
- Gypsy-emo's mandatory verse-2 specific human loss, filled without a death: the old player is alive
  and in the room, can hear perfectly well, and cannot lift his hands to the strings. The grief is
  for a living man and for a recording that was never made, which keeps the slot from defaulting to
  a graveside and honours the standing rule against the narrator outliving what he loves.
- Example: the-bell-knows-my-name/no-place-here
- Logged at catalog size 227.

### "his were bigger than mine, and mine are bigger than hers"
- Gypsy-emo's emotional-thesis mismatch couplet in a fresh grammatical shape: a three-term
  generational comparison with the narrator as the middle term, so his complicity is structural
  rather than confessed — he is simultaneously the one who was short-changed and the one doing the
  short-changing. Paired with "we hand it on a little worse and call it handing on".
- Example: the-bell-knows-my-name/this-big
- Logged at catalog size 228.

### "and the fiddle tunes down a little / and tells us it's the same tune"
- Gypsy-emo's pre-chorus personification slot, sixth fresh filling after "starts confessing",
  "remembers", "stops its weeping", "the strings go quiet too", "learns to whisper" and "keeps no
  copies". Mechanism: the instrument as an unreliable baseline — it is the thing measuring the
  decline and it is quietly declining too, which is the song's whole argument stated by the band's
  own device.
- Example: the-bell-knows-my-name/this-big
- Logged at catalog size 228.

### "THEY WERE THIS BIG" — shout-back as a shared exaggeration
- A fresh gang-vocal mechanism: not a flip, not a confession and not a slogan, but a lie the whole
  room tells together, performed with the hands. After the label-contradiction flips, the
  institution-voiced flip, the flipped prediction, the "but God," pivot, the collective
  self-indictment of an-hour-on-the-train and the unrepentant slogan of no-place-here. Distinct
  from ultracoase/on-the-register's "SHE FRAMED THE CERTIFICATE", which is a solo final hook
  observing somebody else's gesture; this one is the crowd performing its own.
- Example: the-bell-knows-my-name/this-big
- Logged at catalog size 228.

### "I have never lied about it and I have never told it straight"
- The confession that refuses both available positions, placed where the band usually puts an
  admission. Nothing is retracted and nothing is claimed, which is what makes it an admission.
- Example: the-bell-knows-my-name/this-big
- Logged at catalog size 228.

### Marko sold the boat — verse-2 loss as an abandoned trade
- Gypsy-emo's specific human loss filled with a living man who gave up the work rather than one who
  died or lost the ability to do it: three generations held the licence, he waves from the cab of a
  lorry now and does not look at the bank. Deliberately not the shape used one song earlier in
  no-place-here, where the loss is a living man's hands; here nothing has been taken from the
  person at all, and the river is still there and still called the same.
- Example: the-bell-knows-my-name/this-big
- Logged at catalog size 228.

### "maybe there is no year to go back to that anybody actually saw"
- Gypsy-emo's "maybe X was never Y" bridge meditation filled with the shifting baseline: the
  remembered better year is itself inherited rather than witnessed, so the grief may have no
  original. Turns the song's nostalgia on the narrator without excusing the decline.
- Example: the-bell-knows-my-name/this-big
- Logged at catalog size 228.

### "she said it isn't a song, it's a fence"
- Gypsy-emo's verse-2 specific human loss filled with a lost *function* rather than a lost person or
  a lost reputation: the lament was taught as a safety warning about the weir, and the children now
  sing it at the water without knowing what it is for. Deliberately not
  the-bell-knows-my-name/best-thing-i-ever-ate's device, where a dead man's name becomes the term
  and is used about people who were not born — that is a reputation outliving a body; this is a
  warning outliving its meaning, and it gives the song's central choice a real cost.
- Example: the-bell-knows-my-name/sanda-came-up
- Logged at catalog size 229.

### "I could give them the right words in a minute, and I would rather hear this"
- Gypsy-emo's emotional-thesis mismatch couplet in a fresh grammatical shape: stated capability set
  against stated preference, so the narrator's complicity is a choice he is making in the present
  rather than a failure he is confessing from the past. The band's usual admission is retrospective;
  this one is live and reversible, and he does not reverse it.
- Example: the-bell-knows-my-name/sanda-came-up
- Logged at catalog size 229.

### "and the fiddle takes their tempo / and forgets the way it went"
- Gypsy-emo's pre-chorus personification slot, seventh fresh filling after "starts confessing",
  "remembers", "stops its weeping", "the strings go quiet too", "learns to whisper", "keeps no
  copies" and "tunes down a little". Mechanism: the instrument defects — it joins the corrupted
  version rather than testifying to the true one, so the band's own witness changes sides.
- Example: the-bell-knows-my-name/sanda-came-up
- Logged at catalog size 229.

### "SANDA WENT DOWN, SANDA CAME UP" — shout-back as the corruption, sung happily
- A fresh gang-vocal mechanism: the crowd performs the error the song has just explained, at
  skipping-rope speed, accidentally giving a drowned girl a happy ending. After the
  label-contradiction flips, the institution-voiced flip, the flipped prediction, the "but God,"
  pivot, the collective self-indictment, the unrepentant slogan and the shared exaggeration. The
  line is joyful and the listener is the only one who knows what it used to say.
- Example: the-bell-knows-my-name/sanda-came-up
- Logged at catalog size 229.

### "and they sing it at the weir now, and they sing it going in"
- The warning that has stopped working, stated flat and not acted on. Places the song's tenderness
  and its danger in the same sentence, which is what stops the children's-voices premise being
  sentimental.
- Example: the-bell-knows-my-name/sanda-came-up
- Logged at catalog size 229.

### "I did not lose them. I sent them."
- Gypsy-emo's emotional-thesis mismatch couplet in a fresh grammatical shape: the sympathetic verb
  refused and the accurate one supplied, in two short sentences with nothing joining them. The
  band's complicity rule at its most compressed — he is not asking to be consoled for something
  that happened to him, he is naming what he did, and he still thinks it was right.
- Example: the-bell-knows-my-name/they-all-got-out
- Logged at catalog size 230.

### "and the fiddle plays both parts now / and nobody hears the join"
- Gypsy-emo's pre-chorus personification slot, eighth fresh filling. Mechanism: the instrument
  covering for voices that are not there, and doing it well enough that the absence is inaudible —
  which is the song's subject and also its defence of itself.
- Example: the-bell-knows-my-name/they-all-got-out
- Logged at catalog size 230.

### "THEY ALL GOT OUT" — shout-back as a sincere boast whose triumph is the emptiness
- A fresh gang-vocal mechanism: the village chanting its own success, meant straight, with no irony
  available to the singers and all of it available to the listener. Distinct from
  girlboss/best-deal-on-the-yard's verbatim-echo deadpan, where a boast is repeated so the second
  pass carries the opposite meaning — nothing is repeated here and nothing flips; the pride is real
  and the room is empty. Ninth distinct shout-back mechanism for the catalogue.
- Example: the-bell-knows-my-name/they-all-got-out
- Logged at catalog size 230.

### Lidia's class of one — verse-2 loss as an institution kept running for a single person
- Gypsy-emo's specific human loss filled with a school held open for two terms for one pupil, marked
  at her own table with the heating off, and a register with one name in it. Fresh against the
  band's other recent fillings: not a living man's lost capacity (no-place-here), not an abandoned
  trade (this-big), not a warning that lost its meaning (sanda-came-up). Nobody here has failed at
  anything; the loss is that succeeding took everyone away.
- Example: the-bell-knows-my-name/they-all-got-out
- Logged at catalog size 230.

### "we did the good thing all together and we did it one by one"
- Collective action with no collective decision — every family choosing correctly and separately,
  producing an outcome none of them chose. Lets the song hold an emptied village without blaming a
  group, which is the boundary against purple-dog.
- Example: the-bell-knows-my-name/they-all-got-out
- Logged at catalog size 230.

### "maybe the ones who stayed are only the ones who couldn't"
- Gypsy-emo's "maybe X was never Y" bridge meditation turned on the narrator at the last moment:
  having spent the song as the one who did the sending, he lands on the possibility that staying
  was not a choice he made. Undercuts the pride the final chorus is about to shout.
- Example: the-bell-knows-my-name/they-all-got-out
- Logged at catalog size 230.

### "nothing is ever sent to nobody" — the source that forbids the band's own engine
- Disassembler's system-text rule filled with Hoare's CSP: input and output as primitives, no shared
  variables, west query c and east bang c, and the rendezvous rule that neither the send nor the
  receive happens until both sides are ready. The band runs on knowledge arriving nowhere, and this
  is the one source in the catalogue describing a world where that cannot occur — a message with no
  receiver is not a sad outcome in CSP, it is not expressible. Deliberately not
  disassembler/ten-years-is-plenty's territory, which lists message passing among the things the
  trade keeps forgetting; nothing here is forgotten and nothing is rediscovered.
- Example: disassembler/nothing-is-sent-to-nobody
- Logged at catalog size 231.

### "Even with nobody there, I finish the sentence."
- Disassembler's one-human-sentence breakdown as a **thirteenth grammatical shape** — a fronted
  concessive phrase before a bare main clause. Territory: **the habit that outlives the audience**.
  It is the exact inverse of the build's subject, and it is what the band has always been about,
  said plainly for the first time: the paper describes a system in which she could not do this, and
  she does it anyway.
- Example: disassembler/nothing-is-sent-to-nobody
- Logged at catalog size 231.

### "there is no timeout in the paper"
- The outro non-resolution as the specification's silence on the thing that matters: COPY blocked on
  an input that will not arrive, which is not an error and not a fault because the model has no
  concept for it. A fifteenth distinct closing shape for the band. The turn is that a design which
  makes it impossible to speak into the void achieves it by letting you wait in the void instead,
  indefinitely and correctly.
- Example: disassembler/nothing-is-sent-to-nobody
- Logged at catalog size 231.

### "NOTHING IS SENT TO NOBODY" / "BOTH OR NEITHER" — shouted-anchor drop as a guarantee
- Disassembler's drop filled with a promise the system actually keeps, rather than a term of art, an
  instruction or a machine's verdict. Both lines are true of CSP and neither is a complaint.
- Example: disassembler/nothing-is-sent-to-nobody
- Logged at catalog size 231.

### "What he had was a job running somebody else's machine."
- Disassembler's one-human-sentence breakdown as a **fourteenth grammatical shape** — a pseudo-cleft,
  "what X had was Y". Territory: **the foundation laid by somebody doing an assistant's work**.
  Shannon was operating Vannevar Bush's differential analyser, an analogue machine of gears and
  shafts, and the part he was looking at was the relays that switched it. The digital came out of
  minding the analogue.
- Example: disassembler/series-is-and
- Logged at catalog size 232.

### "zero is a closed circuit / one is an open one / everybody does it the other way round now"
- The outro non-resolution as a founding convention silently reversed by everyone who came after,
  with no decision recorded and no consequence. Shannon's symbol is the *hindrance* of the circuit,
  so nought means closed and one means open — the inverse of modern usage. A sixteenth distinct
  closing shape for the band, and distinct from the vestigial token of came-back-waving: that is
  something kept which does nothing, this is something reversed which nobody noticed reversing.
- Example: disassembler/series-is-and
- Logged at catalog size 232.

### "AND GATE" / "OR GATE" / "HE WAS TWENTY-ONE" — shouted-anchor drop as the translation plus the age
- Disassembler's drop pairing the two identities the whole of computing rests on with the fact that
  makes them startling. Both translations are exact and neither is a metaphor. First written as
  "SERIES IS AND / PARALLEL IS OR", which failed on rendering: a line ending in *and* is heard as a
  conjunction reaching for the next line, so it came back as "series is ... and parallel is or".
  Naming the components instead makes the operators nouns and the ambiguity disappears. The third anchor is
  the band's usual fragment doing biographical work, which the one-sentence rule normally reserves
  for the breakdown.
- Example: disassembler/series-is-and
- Logged at catalog size 232.

### Boole's eighty-year wait
- "Boole had the algebra in eighteen fifty-four / and nothing to put it in for eighty years" — the
  build's one line of history, stated as an interval rather than a lament. Nobody is at fault for
  the gap and nothing was lost in it; the mathematics simply had no hardware until a graduate
  student was standing next to some.
- Example: disassembler/series-is-and
- Logged at catalog size 232.

### The build as a program's method and its output, interleaved
- Disassembler's system-text rule filled with both halves of Mark V. Shaney at once: the mechanism
  (count every triple of words, print a pair, pick the next word with the probability the input had,
  slide the pair along; punctuation sticks to the word, so Uma and Uma full stop are different
  words) and the actual sentences it produced, quoted straight and unmarked — "really relating to
  someone involves standing next to impossible". The listener gets the trick and the magic in the
  same breath and the song never says which line is which.
- Example: disassembler/standing-next-to-impossible
- Logged at catalog size 233.

### "Read the replies, not the posts."
- Disassembler's one-human-sentence breakdown as a **fifteenth grammatical shape** — a bare
  imperative, the first in the slot. Territory: **where the feeling actually was**. The band's
  engine inverted a second way: this is not knowledge without a recipient but a recipient without
  any knowledge, an entire lonely-hearts group answering a Markov chain and meaning every word of it.
  Distinct from disassembler/nothing-is-sent-to-nobody's inversion, which is a model that forbids
  sending into the void; here the void answered back and people felt understood.
- Example: disassembler/standing-next-to-impossible
- Logged at catalog size 233.

### "the reason none of them guessed / is that the group was already full of people who wrote like that"
- The disguise that was never a disguise, stated flat and without mockery of anyone. Penn Jillette's
  observation, kept because it is the actual finding: the bot passed not by being good but by being
  no stranger than its neighbours.
- Example: disassembler/standing-next-to-impossible
- Logged at catalog size 233.

### The source given the last word, unframed
- The outro non-resolution as a hand-off: Penn's line about writing your own and having someone just
  like you to write to, then one of Mark's own sentences and his signature, with no comment after
  it. A seventeenth distinct closing shape for the band — the track ends inside the artefact rather
  than beside it, and the last voice on the record belongs to something that is not there.
- Example: disassembler/standing-next-to-impossible
- Logged at catalog size 233.

### The build as generated text with the method withheld
- Disassembler's system-text rule filled entirely with Mark V. Shaney's 1984 output to a BSD group,
  and — unlike disassembler/standing-next-to-impossible, which interleaves the mechanism with the
  results — nothing here explains it. The listener gets only the post. The argument is that the
  seam cannot be found, because technical prose already sounds like this: half-finished clauses,
  jargon, a manual cited for something it does not say. The band's accuracy rule holds in an odd
  way — every line is genuinely what the program wrote and genuinely what people read.
- Example: disassembler/but-i-plan-to
- Logged at catalog size 234.

### "One of those sentences I have used for years as if it were mine."
- Disassembler's one-human-sentence breakdown as a **sixteenth grammatical shape** — a fronted
  object, "One of those sentences I have used". Territory: **quoting a machine without crediting
  it**, which is the band's complicity rule pointed at the narrator for once. "Sorry to rehash this
  subject again but I plan to" is a better sentence about mailing lists than anyone in that thread
  managed, and a Markov chain assembled it out of their words.
- Example: disassembler/but-i-plan-to
- Logged at catalog size 234.

### "that part is true / that is the only part that is"
- The outro non-resolution as the document's headers being its sole verifiable content: the date and
  the sending address are real, and the thousand words between them are noise. An eighteenth
  distinct closing shape for the band. Distinct from disassembler/use-this-one's closing metadata,
  where two identical timestamps show the song's question has no answer — there the metadata is
  useless, here it is the only thing that is not.
- Example: disassembler/but-i-plan-to
- Logged at catalog size 234.

### "SWAP SPACE IN THE BUTT" / "BUT I PLAN TO" — shouted-anchor drop as the machine's best lines
- Disassembler's drop filled with the two funniest things in the source, both of them accidents of a
  word-triple chain, neither of them written by anyone. The drop is usually the song's own
  compression of its build; here it is simply the corpus at its best, and the joke is that it is
  better than the humans it was trained on.
- Example: disassembler/but-i-plan-to
- Logged at catalog size 234.

### The build as one technique getting larger, dated in order
- Disassembler's system-text rule filled with a lineage rather than an inventory: Mark V. Shaney
  counting word triples in eighty-four, word2vec in twenty thirteen with three hundred numbers a
  word and king minus man plus woman landing near queen, Deep Dream in twenty fifteen run backwards
  to amplify what it already half-sees, AI Dungeon in twenty nineteen, "and this", closing on "the
  same trick each time, with more of it". Deliberately not
  disassembler/ten-years-is-plenty's amnesia list, where the trade keeps forgetting and rebuilding —
  nothing here is forgotten or rediscovered; it is one method, in order, with the dates on it.
- Example: disassembler/show-it-dogs
- Logged at catalog size 235.

### "and this" — the lineage item that is the song itself
- The band's third song touching the thing writing it, after disassembler/commit-it (the tool's
  advice quoted as system text) and disassembler/do-not-make-mistakes (the prompts people type at
  it). The first that neither quotes it nor addresses it, but files it as one more entry in a dated
  list and moves on in the same line. Two words, unremarked, nothing in the song returns to it.
  Written because the owner asked whether the two Mark V. Shaney songs had acknowledged the descent,
  and they had not.
- Example: disassembler/show-it-dogs
- Logged at catalog size 235.

### "I can name every part of the thing that does this to me."
- Disassembler's one-human-sentence breakdown as a **seventeenth grammatical shape** — a main clause
  whose object carries a restrictive relative. Territory: **complete understanding of a mechanism
  that moves you anyway**. She has just spent the build itemising exactly how the trick works, in
  order, with dates, and it makes no difference to the effect.
- Example: disassembler/show-it-dogs
- Logged at catalog size 235.

### "SHOW IT DOGS" / "IT GIVES YOU DOGS" / "TWELVE PER CENT"
- Disassembler's drop as a demonstration with its own evidence attached: the instruction, the
  result, and the proportion of the training set that explains it. A hundred and twenty dog breeds
  were in the 2012 ImageNet classes and dogs were roughly an eighth of everything the network was
  ever shown, which is the entire reason Deep Dream hallucinated puppy-slugs.
- Example: disassembler/show-it-dogs
- Logged at catalog size 235.

### "there was nothing else in there to come out"
- The outro non-resolution as output fully explained by diet, with the wonder and the blame both
  declined: "it was not dreaming and it did not want anything / it had been shown a hundred and
  twenty kinds of dog", and then the one claim the song does make: "and the people who cried at it
  were not wrong". A nineteenth distinct closing shape for the band. It was cut once, for restating
  the breakdown and for looking like the writer arguing its own case; the owner overruled both —
  the line is the actual subject, since he had wept in a café at a gypsy-emo song about horses that
  cannot cry. The breakdown moved to the narrator instead, so the outro speaks for the audience and
  the breakdown speaks for her, and neither repeats the other.
- At the owner's request the outro then names it, quoting this catalogue's own line back into a
  song about corpora: "somewhere in a corpus there is a line about horses / the horses can't cry,
  if they could, they would / a man read that in a cafe and had to put his cup down / and he was
  not wrong". The quoted line is from the-bell-knows-my-name/they-went-up-quiet, and this is the
  **only sanctioned reuse of it** — it closes the loop the song is about, since these lyrics are
  themselves a corpus and that line is a thing that came out of one. Logging it revealed that the
  line had never been mirrored into banned-patterns.tsv at all, so one of the catalogue's strongest
  lines was unprotected; it is now PERM.
- Example: disassembler/show-it-dogs
- Logged at catalog size 235.

### "they hate that" — mantra as a punchline worn down to noise
- Laundry's mantra anchor filled with the second half of a joke — *you shouldn't anthropomorphize
  computers, they hate that* — so the phrase arrives funny, repeats until it is only a sound, and
  degrades in the final hook to "they hate th— / they h— / they —". The joke's own structure is the
  device: a sentence that forbids attributing feeling and attributes one in the same breath, which
  is the band's collage method already built into the source.
- Example: laundry/they-hate-that
- Logged at catalog size 236.

### "thank the machine, name the machine, strip the machine for spares"
- Laundry's consumption-imperative hook opener filled with courtesy verbs escalating into disposal,
  the same object three times. Distinct from the apology-verb opener of "say sorry, mean nothing,
  wipe your face, keep walking" — nothing here is being repaired or excused, the politeness and the
  scrapping are simply the same list.
- Example: laundry/they-hate-that
- Logged at catalog size 236.

### "I thanked a cash machine in March and I meant it"
- Laundry's one flash of legibility, fresh shape: a small true admission with a month on it, landing
  in the middle of the smear. The band's usual spike states a condition; this one confesses a
  harmless act and then refuses to explain it, and the "and I meant it" is what stops it being a
  joke about himself.
- Example: laundry/they-hate-that
- Logged at catalog size 236.

### The cartoon boiler smiling on the side of the van
- The unstated centre made visible for one image: the engineer who fixes boilers drives a van with a
  smiling boiler painted on it, so the anthropomorphising the song is nominally warning against is
  already commercial, already everywhere, and nobody finds it odd. Grotesque-retail register per the
  collage rules, and it explains nothing.
- Example: laundry/they-hate-that
- Logged at catalog size 236.

### Gerald — the named laptop that never asked
- Laundry's floating identity wound worn casually: the narrator names a machine, reports its age and
  its warmth in the same breath as its dying, and puts a palm on the case the way you would on a dog.
  Kept as texture rather than thesis, per the spec — it is why he is thin, not a point about
  machines.
- Example: laundry/they-hate-that
- Logged at catalog size 236.

### "when it becomes when it becomes" — the preserved typo as the outro
- The outro non-resolution as a defect kept on purpose: McIlroy's 1964 memo repeats three words,
  Ritchie retyped the page with the duplication intact and noted it was historically accurate, and
  the song ends "it is like that in the original / he typed those three words again and it stayed /
  there is a scan, you can see the damage / nobody took it out". A twentieth distinct closing shape
  for the band. Cashes the premise bank's "the typo is the truest part", which had been written
  against filenames and never used — a typewriter slip in a memo that produced Unix pipes is the
  better instance. The song is named for it at the owner's request.
- Example: disassembler/when-it-becomes-when-it-becomes
- Logged at catalog size 237.

### "LIKE GARDEN HOSE" / "SCREW IN ANOTHER SEGMENT" / "FOUR POINTS"
- Disassembler's drop filled with a 1964 analogy and its own instruction, both quoted from the memo
  that argued for pipes six years before anyone built them. The third anchor is the memo's size —
  the whole of it is four numbered points on one surviving page, and one of them turned into the
  defining idea of Unix.
- Example: disassembler/when-it-becomes-when-it-becomes
- Logged at catalog size 237.

### "Nobody says why it was the tenth page and not the rest."
- Disassembler's one-human-sentence breakdown as an **eighteenth grammatical shape** — a negative
  indefinite subject taking a wh-clause as its object. Territory: **what the archive declines to
  record**. Ritchie kept page ten on his wall under a magnet for years and never explains why that
  page, and the omission is the only thing in the song nobody can supply.
- Example: disassembler/when-it-becomes-when-it-becomes
- Logged at catalog size 237.

### The idea that needed rank pulled to get built
- "he nearly used managerial authority to get the first one built" — McIlroy has said outright that
  he came close to ordering pipes into existence. Sits against the band's engine rather than in it:
  here the knowledge did reach somebody, and only because the person holding it had the standing to
  compel it. The other three points are still open, and the third still bothers him sixty years on.
- Example: disassembler/when-it-becomes-when-it-becomes
- Logged at catalog size 237.

### The build as one sentence losing its author, dated at every step
- Disassembler's system-text rule filled with the provenance of the security industry's most-quoted
  line: Alperovitch says it at McAfee in August 2011 and Vanity Fair prints it with his name on;
  the FBI director reshapes it at RSA in March 2012 and adds a third variant in the same speech;
  the next FBI director does it again on Sixty Minutes in 2014; and in January 2015 it appears on
  the World Economic Forum's site under a chief executive's byline with nobody's name on it at all.
  Distinct from disassembler/show-it-dogs, which dates one technique getting larger — this is one
  utterance being reshaped and stripped as it climbs. The subject of the sentence is not knowing you
  have been compromised, which is also what happens to the sentence.
- Example: disassembler/now-you-know
- Logged at catalog size 238.

### "Looking for the original, I found four of them."
- Disassembler's one-human-sentence breakdown as a **nineteenth grammatical shape** — a participial
  opener before a bare main clause. Territory: **the search that dissolves the thing it was looking
  for**. No complaint is made and nobody is accused of theft; the count is the whole finding.
- Example: disassembler/now-you-know
- Logged at catalog size 238.

### "Now you know" — the sign-off, and then a fifth variant that was not in the list
- The closing non-resolution handed to the man who did the work and then immediately overtaken:
  Bejtlich traced all four variants, dated them, published it on a blog in 2018 and ended
  cheerfully — and the version actually in circulation is a fifth one the owner read in a Hacker
  News comment. "there are two types of organizations / those that have been hacked / and those
  that know that they have been hacked / the don't has fallen out of it / the second lot are inside
  the first lot / there were never two types". A twenty-first distinct closing shape for the band.
  The descent is the song: a named researcher, a magazine, two FBI directors, the World Economic
  Forum, an anonymous comment. An earlier draft closed on "both halves are the same half" and the
  owner corrected it twice. First: there are no halves, there is a **set and a proper subset**.
  Then twice more. **Every speaker is running the same device**: the first half of all five is the
  same assertion, that every company has been hacked, and the second half is only about who knows.
  A draft made a beat of the missing "don't" and he cut it — that is just better English, not a
  reveal. What the positive phrasing actually implies is the ending: *those that know* describes
  **sysops who went and looked**, so knowing is work rather than luck, and the aphorism is not a
  warning about fate but a description of a job. "every company has been hacked / the difference is
  whether anybody went and looked / that is not a warning, it is a job description / there were
  never two types". The song opens on "there are only two types of companies" and takes it back. The correction is complete, correct, free, and arrived after
  the sentence had already stopped meaning what it meant.
- Example: disassembler/now-you-know
- Logged at catalog size 238.

### "TWO TYPES OF COMPANIES" / "NOBODY'S NAME ON IT" / "FOUR VERSIONS"
- Disassembler's drop pairing the famous half of the quote with the two facts about it nobody
  repeats. Every anchor is a plain statement of provenance rather than a term of art or an
  instruction.
- Example: disassembler/now-you-know
- Logged at catalog size 238.

### "today I must do / come tomorrow I must don't" — mantra as broken grammar
- Laundry's mantra anchor filled with the owner's own line, kept deliberately ungrammatical: *"I
  must don't"* is the band's sound-over-sense rule stated outright, and the wrongness is the payload
  rather than a slip to be tidied. Degrades through the final hook to "must don— / I must do— / I
  must— / must—" over a loop left running.

  **The tenses are load-bearing and were chosen, not stumbled on.** The owner's account: *"one is
  always present, one never."* Then, correcting me again when I overstated it: *"except both always
  exist."* Both days are permanent fixtures — it is always today and there is always a tomorrow.
  The obligation is therefore permanently current and the release permanently adjacent, and there is
  no day on which the second becomes the instruction. Not duty measured against an end date, and not
  an end that fails to exist: an end that is real, visible, one day away, and never now. My first reading of it was the softer one
  and he corrected it. The rest of the song is built to that: a cycle called Last that does not
  exist, a calendar that will not say until when, and Hold turning out not to be a cycle either.

  Related, and where it came from: he described a larger arch under much of the catalogue as
  **"I must do but one day it will end"** — visible in disassembler/nothing-is-sent-to-nobody's
  "Even with nobody there, I finish the sentence", in COPY blocked with no timeout in the paper,
  and in laundry/rest-when-im-dead.
- Example: laundry/i-must-dont
- Logged at catalog size 239.

### "load it, run it, drain it, load it"
- Laundry's consumption-imperative hook opener built from the band's own machine verbs, with the
  list returning to its first word so the instruction is a loop rather than a sequence. Distinct
  from the apology verbs of "say sorry, mean nothing…", the disposal verbs of "thank the machine,
  name the machine, strip the machine for spares" and the scrapping verbs of "part it out, price
  the pieces, move the meat" — nothing here is being consumed or discarded, only repeated.
- Example: laundry/i-must-dont
- Logged at catalog size 239.

### "the machine has a cycle called Daily and there is no cycle called Last"
- Laundry's one flash of legibility, fresh shape: an inventory of real settings ending on the one
  that does not exist. The song never names its subject and this line does not either — it names an
  absence in a menu, which is the collage method's "refuse the noun" rule doing the work of a thesis.
  Set up by "the calendar says Repeats Weekly and it does not say until when" and paid off by
  "Refresh, Daily, Rinse, Hold / Hold is not a cycle either".
- Example: laundry/i-must-dont
- Logged at catalog size 239.

### "which one of these hands is the one that stops"
- Laundry's question-with-no-addressee aimed at his own body, asking which part of him is the part
  that will be the one to fail. Nothing answers it and the hook returns to the mantra.
- Example: laundry/i-must-dont
- Logged at catalog size 239.

### "a queue of me going back as far as the door"
- The floating unresolved "I" of the collage method rendered literally as a queue of himself, each
  holding the same basket, the front one working and the rest waiting their turn. Grotesque and
  domestic rather than abstract, and it explains nothing.
- Example: laundry/i-must-dont
- Logged at catalog size 239.

### The build as an inventory of work maxims that contradict each other
- Laundry's collage filled with the sayings the trade repeats at itself — do it right, do it fast,
  measure it and cut it wherever, good enough is good enough, move fast and break things, don't let
  perfect be the enemy of the good — stacked until they cancel. Nothing is corrected and no maxim is
  singled out as the wrong one; they are simply all present at once, which is the actual condition.
  Distinct from girlboss's corrected-proverb device, where one saying is repaired to land a moral,
  and from laundry/they-hate-that, where a single self-cancelling joke becomes the mantra.
- Example: laundry/worth-doing
- Logged at catalog size 240.

### "worth doing" — the mantra as the only fragment they all share
- Laundry's mantra anchor filled with the two words common to every maxim in the build, so chanting
  it chants the one thing the sayings agree on, which is nothing at all. Degrades in the final hook
  to "worth do— / wor—". The source line — *if a job's worth doing, it's not worth doing it* — sits
  in the verse and the final hook rather than in the mantra slot, so the aphorism is not the chant.
- Example: laundry/worth-doing
- Logged at catalog size 240.

### "don't let the perfect be the enemy of the packing peanuts"
- A real maxim derailed mid-sentence into the band's grotesque-retail palette, so the saying starts
  as advice and arrives as nonsense without ever being contradicted. The collage method's
  sound-picks-the-word rule applied to received wisdom rather than to imagery.
- Example: laundry/worth-doing
- Logged at catalog size 240.

### "nobody has ever told me when a thing is finished"
- Laundry's one flash of legibility, fresh shape: a plain admission of a missing definition, in the
  middle of a hook made of definitions. The song's unstated centre is work with no completion
  criterion, and this is the only line that comes close to naming it.
- Example: laundry/worth-doing
- Logged at catalog size 240.

### "they are all the same tooth"
- The floating unresolved "I" rendered as accumulated debris: what has been sanded off is in the
  tray with everything else previously sanded off, and it is all the same. Grotesque, domestic, and
  explains nothing — the collage rules' concrete-not-abstract requirement doing the work a thesis
  would otherwise do.
- Example: laundry/worth-doing
- Logged at catalog size 240.

### "and the fiddle will not finish / the bar it is already in"
- Gypsy-emo's pre-chorus personification slot, ninth fresh filling after "starts confessing",
  "remembers", "stops its weeping", "the strings go quiet too", "learns to whisper", "keeps no
  copies", "tunes down a little", "takes their tempo" and "plays both parts now". Mechanism: the
  instrument refusing to leave the present bar, which is the song's request stated in musical terms —
  the one device in the band that can enact a subject rather than describe it.
- Example: the-bell-knows-my-name/here-in-today
- Logged at catalog size 241.

### "tomorrow is already true, it is only not here yet"
- Gypsy-emo's emotional-thesis mismatch couplet in a fresh grammatical shape: a flat assertion
  followed by a concessive qualifier that concedes nothing. From the owner's own formulation of the
  two permanent days — it is always today and there is always a tomorrow — and its companion
  observation that this makes today the best day available, since you are never in the other one.
  Paired with "I will say it in the morning and I am not saying it now", which is the band's
  complicity rule in one line: the walk is kindness and cowardice in the same gesture.
- Example: the-bell-knows-my-name/here-in-today
- Logged at catalog size 241.

### "WE ARE STILL IN TODAY" — shout-back as an assertion of the current tense
- A tenth distinct gang-vocal mechanism for the catalogue, after the label-contradiction flips, the
  institution-voiced flip, the flipped prediction, the "but God," pivot, the collective
  self-indictment, the unrepentant slogan, the shared exaggeration, the corruption sung happily and
  the sincere boast. This one neither flips nor confesses nor boasts — the room simply states where
  it currently is, as a fact, against something that has not arrived. Defiance with no object.
- Example: the-bell-knows-my-name/here-in-today
- Logged at catalog size 241.

### The father who did it first — verse-2 loss as the same act, one generation back
- Gypsy-emo's specific human loss filled with the narrator discovering he is repeating something
  done to him: his father walked him up to the top field the day before selling it, talked about
  fencing, said nothing, and it took thirty years to understand. Fresh against the band's recent
  fillings — not a living man's lost capacity, not an abandoned trade, not a warning that lost its
  meaning, not a school kept open for one pupil. Nobody is blamed and the narrator is doing it too.
- Example: the-bell-knows-my-name/here-in-today
- Logged at catalog size 241.

### "if it still lands, I am still here / it stopped landing in March"
- Ultracoase's chanted-hook couplet in a fresh grammatical shape: a conditional used as a
  self-diagnostic, then the date it failed. Deliberately **not** the mastery-not-resistance thesis
  already spent at catalog size 41 ("You don't out-run X — you learn to ride it, or you
  [consequence]"), which is the obvious rendering of the owner's line *always embrace the horror or
  it owns you* and would have re-spent it. The amor fati pillar is carried instead by "I looked at
  all of it on purpose and I would do it again" — the cost affirmed, with the cost stated first.
- Example: ultracoase/it-stopped-landing
- Logged at catalog size 242.

### "I ate my lunch at that desk." — the wink as an ordinary act in an unbearable place
- Ultracoase's single spoken wink, placed as the **opening line** rather than before the final hook,
  and recalled in all caps as the closer. One concrete domestic fact, stated and left completely
  alone: nothing says what the desk was for, and the listener supplies the rest. Evidence, not
  analysis, per the band's fourth pillar.
- Example: ultracoase/it-stopped-landing
- Logged at catalog size 242.

### "I asked her when it happened" — the living human detail as a wrong response
- Ultracoase's mandatory concrete living human detail, filled with a child showing her father a cut
  knee and getting a timestamp question back. The band's retired device is a dead mentor or parent;
  this is the opposite — a living child, unharmed, and the loss is in the narrator's reply. Followed
  by "I have got very good at the wrong question", which names the damage without explaining it.
- Example: ultracoase/it-stopped-landing
- Logged at catalog size 242.

### "there is a category for everything / and the ones with no category are the ones you take home"
- The job stated entirely as process — a queue sorted oldest first, a code written in a box, a
  number to ring that has an answerphone — with nothing described. The horror is present only as an
  absence in a taxonomy, which is both the band's state-the-fact discipline and the only decent way
  to write this subject.
- Example: ultracoase/it-stopped-landing
- Logged at catalog size 242.

### "chill it, wrap it, stack it, ship it" / "keep it moving"
- Laundry's consumption-imperative opener and mantra taken from cold-chain handling: the four verbs
  are the actual sequence and "keep it moving" is the trade's own rule, which is also the band's
  engine — an obligation with no completion state. Deliberately **not** the packaging phrase as the
  chant: laundry/by-continuing already owns boilerplate-degraded-to-mantra, so BEST BEFORE END is
  spent once, as the flash of legibility, rather than worn down by repetition.
- Example: laundry/best-before-end
- Logged at catalog size 243.

### "BEST BEFORE END, it says, and it does not say what happens after"
- Laundry's one flash of legibility: real packaging text quoted, then the observation that the
  wording stops exactly where the question starts. The refuse-the-noun rule doing a whole thesis's
  work — nothing in the song names what is coming, and the label declines to as well.
- Example: laundry/best-before-end
- Logged at catalog size 243.

### "everything in here is going somewhere to be eaten / including Kevin"
- The grotesque inventory that turns out to include a named person and then the machinery, stated
  flat and immediately dropped. Distinct from the "including the narrator" constructions elsewhere
  in the catalogue, which concede a shared ignorance — this one is a claim about destination, and
  the joke and the horror arrive in the same word.
- Example: laundry/best-before-end
- Logged at catalog size 243.

### "the cold is not a thing they put in, it is a thing they keep taking out"
- A correct physical fact stated as if it were a paranoid observation, per the collage rules'
  preference for images that are true and unexplained. Sets the building up as something engaged in
  continuous removal without the song saying of what.
- Example: laundry/best-before-end
- Logged at catalog size 243.

### "pick to voice" — mantra as the name of the system doing it to him
- Laundry's mantra anchor filled with the trade's own name for voice-directed warehouse picking, so
  the chant is the process rather than an instruction, a joke or a slogan. Degrades to "pick to
  voi— / pick to— / pick—". Distinct from laundry/by-continuing's boilerplate-as-mantra and from
  laundry/they-hate-that's punchline-as-mantra: nothing is being quoted at the narrator here, it is
  simply what the thing he is inside is called.
- Example: laundry/pick-to-voice
- Logged at catalog size 244.

### "there is no button on any of it that means I have had enough"
- Laundry's one flash of legibility, fresh shape: an absence described in interface terms. Everything
  in the system has a control and the one he wants is not among them, which the song states once and
  never returns to. Pairs with "it does not say well done, it says the next one".
- Example: laundry/pick-to-voice
- Logged at catalog size 244.

### "scan it, lift it, say it back, go"
- Laundry's consumption-imperative hook opener built from the actual voice-picking sequence,
  including the confirmation step — the operator reads check digits back to prove he is standing
  where the system says he is. The band's imperative slot filled with commands a machine really
  issues to a body, rather than ones the feed issues to a consumer.
- Example: laundry/pick-to-voice
- Logged at catalog size 244.

### "Kevin's numbers are up on the board and Kevin is not on the board"
- The performance league table with the person subtracted from it, stated flat and left. Second
  appearance for Kevin after laundry/best-before-end, which is deliberate — the band's floating
  unresolved pronoun given one fixed name across the warehouse songs, so the setting accumulates a
  population without the songs connecting.
- Example: laundry/pick-to-voice
- Logged at catalog size 244.
