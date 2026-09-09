# Unadopted — Suno Style Prompts

**Status: four songs, two confirmed renders.** `get-lifted` rendered and works — it is the founding
render and the source of the 303 finding. `chelsea-girl` rendered and is the better of the two
voices; see the exhaustion finding below. `a-six-six-six` and `beech-way-stops` both test the
unchanging variant and no finding is recorded for either.

**`beech-way-stops` changes exactly one thing against `chelsea-girl`: the arrangement.** Its vocal
terms are copied across word for word so that whether the exhaustion reproduces can be read off it,
and the acid 303 term is carried over unchanged. If the voice comes back tired again the effect
belongs to the female-voice request rather than to a lucky roll; if it does not, the arrangement is
the confound to suspect first. Findings in this file
are added by listening, never by predicting — the same rule the rest of the catalogue runs on.

**One note on provenance, since the prompts have been edited.** `get-lifted` was actually rendered
with the phrase *"Prodigy style"* in its prompt, and `chelsea-girl` was written with that plus a
named vocalist. Both have been stripped under the no-real-artists rule below. The `.style.txt` files
are paste-targets first, so they carry the corrected prompts rather than the historical ones — but
the founding render, and therefore the 303 finding, came off a prompt that had a band name in it.
Nothing about the finding depends on that term, and the acid line is still named in both, so the
comparison stands; it is recorded here so nobody later reads the files as a clean before-and-after.

## Why this band exists, in rendering terms

The catalogue-wide taxonomy in `disassembler/styles.md` applies here as everywhere. The specific
finding that produced this band is narrower and worth stating at the top, because it governs every
prompt in this file:

**Suno renders ensemble and performance. It does not render a signal chain.** Gabber failed in the
Disassembler spike because the genre lives in one processed kick — distortion curve, pitch envelope,
tail — which is production craft with no text-field equivalent. Laundry's three instrument probes
failed the same way from the other end: a sax was audible only when billed loudly enough to
unbalance the mix, a 303 never appeared at any setting, a Bass Station changed the grit. None of
them added a hearable instrument to a mix that dense.

Laundry's lead slot is therefore empty on the record — the spec bans guitars, bass as backbone,
solos and key, and the sampler it nominates as lead is a thing Suno will not insert. The collage has
been doing that job. **This band's whole premise is that giving Suno an actual riff to hold fixes
the thin-music problem, and `get-lifted` says it does.**

## The 303 appears here — and that corrects a catalogue-wide conclusion

**Found by listening, on the `get-lifted` render: the acid line is audible.** The same family of
term failed repeatedly in Laundry, where the recorded finding was that a 303 "never appeared at any
setting" and that an instrument name "behaves as a texture modifier here, not as an addition."

One caveat on the comparison, so nobody later reads it as a cleaner experiment than it was: the
wordings are near-equivalents rather than identical. Laundry's prompt says *distorted acid 303 under
the drums*; `get-lifted`'s says *acid squelch under the riff*. `chelsea-girl` names *distorted acid
303 line running under the riff* explicitly, which tests the exact Laundry term in this arrangement
and is worth listening for specifically.

That finding stands for Laundry. What is now clear is *why*, and the general rule drawn from it was
wrong. The two mixes differ in one obvious way: Laundry runs two drum kits played as separate parts,
sampler stabs, chopped vocal and gang chants; Unadopted runs one riff, one breakbeat and one voice.
**The blocker was arrangement density, not the prompt term.** Suno had nowhere to put a 303 in
Laundry and plenty of room for one here.

Two consequences worth carrying:

- **If an audible instrument is wanted, make room for it.** The lever is the arrangement, not a
  better-worded term. Three Laundry probes failed by trying to out-phrase a full mix.
- **This band can take additions that Laundry cannot.** Keep them subordinated anyway — the sax
  lesson (Suno foregrounds whatever you name, and billing is the problem, not the instrument) has
  not been retested here and should be assumed to still apply.

## The two prompts

**Drop-built core** (`get-lifted`, recommended default). The riff is front-loaded deliberately —
Suno appears to weight terms by position, and the riff is the entire point of the experiment:

```
big beat, huge distorted guitar riff carrying the hook, 140 BPM, hard live breakbeat drums with
room mics, riff-led rave-punk crossover, blown-out analogue synth stabs, acid squelch under the riff, shouted manic
male vocal ranted flat out, thick UK accent, gang shouts placed on the four-word chant in the drops,
siren rise into each drop, long riff-only stretches between vocals, gritty analogue distortion,
clipping, hard stop ending on the beat
```

**Unchanging variant** (`a-six-six-six`, `beech-way-stops`) — **superseded, do not paste.** The
original wording below caused the whole-song repeat documented further down; the revised version is
in that section. Kept here only as the record of what was actually pasted:

```
big beat, one distorted two-chord guitar riff repeated unchanged for the whole track, never
resolving, 138 BPM, hard live breakbeat drums with room mics, motorik repetition, blown-out analogue
synth stab on the offbeat, ranted deadpan male vocal, thick northern English accent, declamatory not
sung, no melody in the vocal anywhere, gang shouts placed on the number chant, dry close-miked
verses, lo-fi garage production, gritty analogue distortion, clipping, hard stop mid-bar
```

`no melody in the vocal anywhere` is load-bearing in both. Suno's default is to over-sing, which the
Guessed and Laundry notes both record, and a sung read kills the declamatory voice outright.

## Notation rules that apply here

- **Name a gang vocal's placement, not its character** — *"gang shouts placed on the number chant"*,
  per the catalogue-wide arrangement class.
- **Do not use Laundry's `(gang) line here` quirk.** That inline label makes Suno bark the literal
  word "GANG" as a percussive stab. In Laundry it has become a genuine feature and is kept on
  purpose; it is Laundry's texture, not this band's. Use bracketed tags here.
- **Spell numbers as words in a chant.** `FIVE EIGHT OH`, not `580` — per the orthography class on
  bare numerals. Same for initialisms: `C and A`, not `C&A`.
- **Never name a real band or artist in a style prompt.** Genre terms, instrumentation, delivery and
  production language only. The lineage belongs in `template.md`, where naming the reference is the
  whole point; it must not travel into the paste-target. Describe the thing instead — *riff-led
  rave-punk crossover* for the big-beat lineage, *brassy untrained female punk delivery* for the
  vocal.
  Note that Suno's own filter is not a reliable check on this: both offending prompts here passed
  unflagged, while a lyric elsewhere was rejected for the word *phosphate*. See the artist-name
  filter class in `disassembler/styles.md`. The rule is ours, not the renderer's.
- **Cap the `-ah` line ending at two per song.** Beyond that it reads as Mark E. Smith karaoke
  rather than as a voice.

## What to listen for

- **Does the riff actually arrive?** The band's founding question. Generic distortion instead of a
  riff would mean the diagnosis was right about the cause and wrong about the fix.
- **On the unchanging variant: does Suno hold the riff still?** Developing an arrangement is its
  strong default, and `repeated unchanged for the whole track` asks for the one thing it least wants
  to do. If the chants turn into proper drops, the Fall part is gone.
- **Near-homophones in the verses** (`drawer full of draw`). These are deliberate and Suno may
  flatten them. **Check the other take before rewriting** — differing across two takes means the
  fault is stochastic and a re-roll fixes it; identical in both means it is deterministic and the
  lyric has to change.
- **Dead brand names** (Bejam, Rumbelows, MFI) and UK-specific nouns (strimmer, hi-vis) are the
  pronunciation risks. Unverified.

## The female voice renders exhausted, and nothing asked it to

**Found by listening, on `chelsea-girl`: the owner's verdict was that the female version is better,
and that "she sounds like she hasn't slept."** Nothing in the prompt requested that. It asks for
*shouted female vocal ranted flat out*, *declamatory not sung*, *brassy untrained female punk
delivery* — energy and register, no fatigue anywhere. Suno supplied the exhaustion on its own.

It is worth having because it repairs a soft spot in the engine. The band's narrator is oblivious,
and obliviousness with no cause is just a device. A voice that has not slept gives it one: she is
not hearing what she is saying because she has been awake too long, which is a reason rather than a
rule. The male voice has no equivalent and is the weaker of the two for it.

**Do not go and name it in the next prompt without thinking.** The combination that landed is
*exhausted and still going at full pelt*, and those pull against each other. Asking for a tired
vocal will most likely buy a slow flat one, which kills the manic and takes the band with it. This
is the sax lesson in another costume — the instrument was not the problem, the billing was.

The cheap test, when there is a fourth song: render it twice off the same lyric, once with the
prompt exactly as it stands and once with one fatigue term added, and compare. If the unmodified
take is already exhausted, the effect belongs to the female-voice request and needs no help. If only
the modified take has it, the term is doing the work and can be kept deliberately.

## The whole-song repeat — Suno padding to its maximum length

**Found by listening: `beech-way-stops` came back as the same song three times inside one clip, in
both takes. Both renderings are 7:59, which is Suno's maximum.** The owner's account is that it does
this generally — usually by repeating the last few lines for five minutes rather than by replaying
the whole song.

**So this is Suno padding a clip to length, and it is not something this prompt caused.** An earlier
version of this section claimed the unchanging variant instructed the fault. That was too strong and
is withdrawn: a documented general behaviour explains it without any reference to our wording.

What remains open is why the generation targeted the maximum at all. The unchanging variant's
*never resolving* and *motorik repetition* are a plausible nudge toward a long track and are worth
removing on suspicion, but nothing observed establishes it, and the drop-built songs not doing it is
weak evidence at four renders.

**A caveat this fault exposes in our own diagnostic, and it matters beyond this band.** The two-take
test says differing across takes means stochastic and re-roll, identical in both means deterministic
and the lyric must change. **That inference does not hold for duration.** Clip length appears to be
decided once per generation and inherited by both takes, so two takes agreeing on a padded length is
the expected result whether the cause is stochastic or not. Both takes agreeing here proves nothing.
See the catalogue-wide note in `disassembler/styles.md`.

**Levers, in the order worth trying:**

- **Set a shorter target duration in Suno**, if the UI exposes it. This addresses the actual
  mechanism rather than guessing at prompt wording, and costs nothing.
- **Write longer.** A lyric that fills more of the clip leaves less to pad. Unadopted's songs run
  195-243 words against Laundry's 327 mean, so there is room, and the catalogue already holds that
  word count is rhythm material.
- **The revised variant below**, which removes the endlessness terms and states a plain structural
  negative. Speculative, harmless, and worth folding in while doing the other two.

**Revised unchanging variant — untested, and not claimed as the fix:**

```
big beat, one distorted two-chord guitar riff, the same riff throughout, hard live breakbeat drums
with room mics, 138 BPM, distorted acid 303 line running under the riff, long riff-only instrumental
stretches between vocal sections, shouted female vocal ranted flat out, thick UK accent, declamatory
not sung, no melody in the vocal anywhere, brassy untrained female punk delivery, gang shouts placed
on the chant, dry close-miked verses, lo-fi garage production, gritty analogue distortion, clipping,
one pass through the lyric only, do not repeat the song, ends on the final chant
```

`never resolving` is gone; long riff-only stretches are added on the Disassembler precedent, to give
the renderer something to fill time with that is not the lyric; and the plain negatives are added on
the gabber spike's finding that plainly-stated structural instructions are honoured.

**Status of the variant: unproven, and not yet fairly tested** — the one render it has was consumed
by a padding fault that had nothing to do with whether the riff stays still.

## Instrument roster check

A distorted guitar riff is the backbone here, which is shared ground with **hobo** — the only other
band in the catalogue built on a guitar. The fence is everything around it: hobo is a fuzz riff
under stacked female close harmony with no lead vocal at all; this is a big-beat riff under one
ranted male voice. Different bands by every audible measure, but if a render of one starts sounding
like the other, this is the collision to look at first.
