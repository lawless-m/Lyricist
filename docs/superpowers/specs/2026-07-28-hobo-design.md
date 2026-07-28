# hobo — New Band Design

## Problem

The catalog has eight wired bands, and none of them occupy the 90s hip-hop / guitar crossover
lane — the Whale "Hobo Humpin Slobo Babe" sound: a fuzz riff over a live breakbeat with cheap
sampled junk on top. A new band, **hobo**, carries that sound, following the established
`<band>/template.md` + `<band>/styles.md` pattern `write-song` already reads.

There is a second gap it fills, and it ends up driving the design harder than the genre does:
**no band in the catalog sings in harmony.** Every existing band is built on a single voice —
Laundry's preacher, girlboss's dry conversational narrator, Guessed's lurker — and Coase Guard's
two personas never share a song. hobo has no lead vocal at any point: stacked female voices sing
the same lyric in harmony from the first line to the last, ABBA rather than a gang chanting
behind a frontwoman.

The design problem is not the sound — it's the words. The requested method is collage, and
`laundry` already owns collage. hobo needs a collage engine that cannot be mistaken for
Laundry's.

## Goals

- Add one new band, **hobo**, in the established two-file format.
- Give it an engine distinct from all eight existing bands, and a lyric method that shares
  Laundry's mechanics without sharing its temperature.
- Fence it explicitly against `laundry` (collage) and `girlboss` (female-led hip-hop) — the two
  nearest neighbours — at the level of register, palette and instrumentation.
- Wire it into `write-song`'s band lookup table.
- Ship a reference example song in `template.md`, as every other band's template has.

## Non-goals

- Not drum'n'bass, and not the dry no-guitar indie hip-hop of `girlboss/styles.md`.
- Not a thesis band. The engine is an appetite, not an argument; nothing here is *about* poverty,
  homelessness or the economy, and no song should read as commentary on any of them.
- Not restructuring `laundry`, `girlboss`, or the trope library. (`girlboss` was wired into
  `write-song`'s roster separately while this design was being written; that is done and is not
  part of this work.)

## Architecture

### Folder

`hobo/` at the repo root, containing `template.md` and `styles.md`, matching the eight wired
bands' layout exactly (`styles.md` plural — the `write-song` workflow reads that filename).

### Engine — junk swagger

Collage as **appetite**. Every image is something they found, and they want it.

This is Laundry's method run at the opposite temperature, and that inversion is the whole design.
Laundry's images drift past a narrator who has stopped being able to feel them; hobo's pile up in
front of a narrator who wants all of them. Same mechanic — concrete nouns, missing joins, sound
picking the word — opposite charge. Laundry's collage is a symptom. hobo's is a boast.

Consequences that follow from the inversion, and must hold:

- **No comedown.** No rue, no numbness, no dawning awareness that the pile is worthless. The
  moment they suspect it, the song has become a different band's.
- **The joins are missing because they're moving too fast**, not because they dissolved. The
  drift has a cause and the cause is greed.
- **The song lands.** Against Laundry's no-landing rule: hobo ends hard, on the riff. They win.

### The unhinged rule

Sweet delivery, deranged content, and **the gap between them never closes**. The harmony stays
beautiful, in tune and completely untroubled while what it is singing goes past ordinary
bragging into something nobody sane would commit to at that volume: a dead pigeon inducted into
the family, a bin defended like territory, the pile addressed as though it can hear them.

Two constraints keep it from becoming mere whimsy:

- **The pitch never wavers.** No screaming, no strain, no wink. If the voices sound unstable the
  joke is gone — the horror-comedy is that they are *fine*, in harmony, and wrong.
- **Escalation past sense, once per song, in a fresh place.** Not a fixed device slot and not a
  punchline: somewhere in every song the claim gets bigger than the object can hold and the
  harmony agrees with it anyway. It never gets challenged, corrected or resolved, because there
  is no second voice available to challenge it — which is the point of having no lead.

This is where "we" earns itself. One woman insisting a broken lamp is priceless is a character;
five women agreeing about it in three-part harmony is a **cult**, and the unanimity is what
makes it funny and slightly frightening at once.

### Persona — the scavengers, plural

**First person plural, always.** Never "I". A gang of women who have collectively decided the
junk is treasure, singing as one, with nobody dissenting. They own a mountain of worthless
things and are genuinely thrilled about it.

**No lead vocal anywhere in the song.** Stacked female voices in close harmony, same words at
the same time, sweet and tight and in tune — ABBA, the Shangri-Las, girl-group thirds. Not a
frontwoman with backing, not call-and-response, not a shouted terrace chant. Verses are sung in
harmony exactly like the hooks; the only thing that changes across sections is the arrangement
under them.

**Consequence for the writing: harmony forces melody, and melody caps syllable density.** There
is no motormouth verse in this band and no rap. The collage runs *slow and repeated* — images
held, sung, doubled back on — rather than Laundry's fast clipped image-stream. Lines must be
singable in unison by five people: fewer syllables, open vowels, room for a phrase to be
repeated because it sounds good rather than because it means more the second time.

### Writing the words — sound first, sense optional

The lyric does not have to add up, and shouldn't. Two rules do most of the work:

- **Alliteration picks the word.** Choose for consonant runs and open vowels before choosing for
  meaning — five voices in unison make a hard consonant land like a drum hit, so the words are
  partly percussion. (Laundry has a phonetics-lead rule too, but it points the other way: there
  it produces near-malapropisms that erode sense. Here it produces something joyful and
  chantable. Same rule, opposite outcome.)
- **The nonsense refrain.** One invented phrase per song — alliterative, meaningless, sung in
  full harmony as though it were the title hook of a massive single. This is the
  "hobo humpin slobo babe" slot itself. It is **never explained, never glossed, and never
  reused**: a fresh invented phrase every song, logged in the trope library like any other
  device so the next song can't repeat it.

Beyond those, ordinary non-sequitur is welcome as texture — a line that doesn't follow from the
one before it needs no justification, provided every image is still a physical object they want.

### Device pool (checklist for `template.md`)

Four moves, **rotated, not mandatory**. Each song hits at least two, and never the same two as
the previous song — a fixed per-song device calcifies, which is what this pool exists to avoid.

- **The haul** — an inventory of found junk, sung as a **round** rather than rattled off:
  harmonised, repeated, stacking up the way the junk does. "Money, Money, Money" applied to a
  bin bag.
- **The drop-out** — guitar cuts dead mid-hook, breakbeat left naked or gone entirely, and what
  is left in the hole is **unaccompanied harmony**. Riff slams back in. With no lead voice to
  step forward, this is the band's loudest available gesture.
- **The appraisal** — a whole verse spent pricing one broken object, wrongly, at length, and
  with total confidence, sung beautifully.
- **The trade** — a line where something genuinely valuable goes out for something worthless,
  and they came out ahead.

### The bones (never rotate)

The swagger register with no comedown; the unhinged rule (sweet delivery, deranged content, gap
never closing); first person plural; all-harmony, no lead vocal, ever; collage assembled by
appetite rather than drift; the fuzz riff as backbone; the hard landing.

### Palette fence

hobo takes roadside, skip, car-boot and gutter junk. `laundry` keeps retail, shipping and
body-parts. Object for object, this is the main thing keeping the two collages from converging —
if a hobo draft reaches for a conveyor belt or a good kidney, it's drifting into Laundry.

### Song structure

Riff intro → sung verse (harmony) → hook carrying the nonsense refrain → verse → rotating device
slot → final hook with the riff doubled and the harmony widened → hard stop on the riff.

Sections are told apart by **arrangement, not by who is singing** — the vocal is the same stacked
harmony throughout, so the riff, the breakbeat and the drop-outs have to do all the structural
work that a lead/backing contrast would normally do.

### Sound / `styles.md`

Fuzz guitar riff as the backbone over a live-sounding 90s breakbeat, cheap sampled junk on top
(vinyl crackle, horn stabs, a wrong-speed sample), and **stacked female harmony vocals with no
lead**. Reference points: Whale, *Mellow Gold*-era Beck, Luscious Jackson, the *Judgment Night*
soundtrack, with ABBA/girl-group vocal architecture bolted on top.

**Suno risk to write against explicitly:** Suno defaults to putting a single lead vocal in front
and treating harmony as backing. The prompt has to insist — harmonised/stacked/unison throughout,
girl-group thirds, no solo vocal, no ad-libs — and per the workflow's position-weighting note,
the harmony terms belong at the **front** of the prompt, not the tail, because they are the
thing most likely to be dropped.

**The locked core — this band's rotation guidance is the strictest in the catalog.** hobo has to
sound like one group across its whole catalogue, not a different band per track, so `styles.md`
is built as a **fixed head plus a short rotating tail** rather than a set of freely-adapted
variants:

- **Locked, word-for-word identical in every song's `.style.txt`, always at the front:** the
  vocal architecture (stacked female harmony, girl-group thirds, no lead vocal, no ad-libs), the
  fuzz guitar riff, and the live 90s breakbeat. These terms are never reordered, reworded,
  swapped out or trimmed — not for emphasis, not for length. They *are* the group.
- **Rotating, and only here:** one cheap sample texture per song (vinyl crackle, horn stab,
  wrong-speed sample, tambourine, cheap organ) and the tempo/heaviness lean. This is the same
  discipline `girlboss/styles.md` already uses for its stab texture, including the corollary —
  don't let any one rotating texture recur often enough to become part of the core by accident.

This deliberately narrows `write-song` step 6 for this band: the graduated
reorder → swap → rewrite ladder applies **only to the rotating tail**. A hobo song whose style
prompt reorders or drops a locked term is wrong even if it sounds good on its own, because the
cost lands on the next song, not that one.

Consistency of the *voice itself* across generations is the part the prompt can only partly
control. Identical wording every time is the baseline lever; if the Suno tooling in this repo
supports carrying a persona forward from a generation that landed, that is the stronger lever and
should be used — to be confirmed against the automation skill at build time rather than assumed
here.

### `write-song` integration

Add a row to the band lookup table in `.claude/skills/write-song/SKILL.md`:

| Band folder | Persona / genre aliases                                              |
|-------------|----------------------------------------------------------------------|
| `hobo`      | hobo, junk swagger, the scavengers, 90s hip-hop guitar crossover     |

The skill's description line also names the bands it triggers on; it needs updating from eight to
nine so a bare "write me a hobo song" resolves. No other change to the workflow — it already
treats band folders as interchangeable reference content.

## What hobo is not

- **Not `laundry`.** Its exact inverse; read them against each other. Laundry's narrator can't
  feel the objects, hobo's want them; Laundry withholds catharsis and refuses to land, hobo
  lands hard; Laundry decoheres on purpose, hobo is nonsensical out of enthusiasm. One preacher
  versus five women in harmony.
- **Not `girlboss`.** girlboss's narrator is knowing, covert, competent and singular, and the
  engine is trust-transgression. hobo is plural, loud, transparent and working nobody. Nothing is
  being got over on anyone; they are simply delighted with a broken lamp. The vocal architecture
  is the hard fence: girlboss is one dry voice in front of the beat, hobo has no lead at all.
- **Not `coase-guard`.** No politics, no friend/enemy line, no crew — and although both bands
  sing "we", Coase Guard's is a disciplined outfit with an enemy, while hobo's is a gang with no
  opponent at all. They are outside the thing, not against it.

## Open questions / accepted gaps

- `template.md` needs a full reference example song, per the pattern every other band follows.
  It is produced through the normal `write-song` flow (draft → `check.sh` → fuzzy trope check →
  style prompt → log devices into `library.md` and `banned-patterns.tsv`), not authored inside
  this design doc.
- Whether the reference example leads with the haul or the appraisal is left to the
  implementation plan; it should demonstrate the two-device rotation rule rather than a fixed
  spine.
