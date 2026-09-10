# Unadopted — Suno Style Prompts

**Status: settled at four songs.** The owner's verdict is that this is the band's style. Both
arrangements and both voices have good renders behind them, and the singer is a swappable variation
rather than a property of the band — see `template.md`.

**Renders: four songs, two confirmed.** `get-lifted` rendered and works — it is the founding
render and the source of the 303 finding. `chelsea-girl` rendered and is the better of the two
voices; see the exhaustion finding below. `beech-way-stops` rendered and the verdict was a win,
though what it came back with was the whole-song repeat documented below rather than an answer to
the question it was built to ask. No finding is recorded for `a-six-six-six`.

**`beech-way-stops` changed exactly one thing against `chelsea-girl`: the arrangement.** Its vocal
terms were copied across word for word so that whether the exhaustion reproduces could be read off
it, and the 303 term carried over unchanged. That comparison is still available on the take — tired
again means the effect belongs to the female-voice request rather than a lucky roll — and so is the
riff question, neither of which the padding affects. Findings in this file
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

**Swapping the singer.** The voice is a dial (see `template.md`), and swapping it is a
find-and-replace on one clause in either prompt below, nothing else:

- male → `shouted manic male vocal ranted flat out, thick UK accent`
- female → `shouted female vocal ranted flat out, thick UK accent, declamatory not sung, no melody
  in the vocal anywhere, brassy untrained female punk delivery`

The female wording is longer because it is the one that produced the exhaustion, and it is kept
verbatim rather than tidied for that reason. `declamatory not sung` and `no melody in the vocal
anywhere` are worth carrying into the male form too — Suno's default is to over-sing either.

**Unchanging variant** (`a-six-six-six`, `beech-way-stops`). Paste as is; do not add structural
negatives to it, for the reasons in the padding section below:

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

## The whole-song repeat — a known Suno behaviour, stochastic and per-take

**`beech-way-stops` came back at 7:59 in both takes — Suno's maximum — with the entire song played
through three times. The owner's verdict: a total win.**

**It is a Suno issue, seen before across the catalogue, and it is not the result of prompting.**
Three earlier explanations attempted in this file are withdrawn; no mechanism is recorded because
none is known.

Two observations pin down its shape, and the second one matters most:

- **It crosses bands.** `laundry/permanence-is-temporary` did it too — a completely different spec,
  a much denser mix and a different arrangement. Nothing about this band's prompt is implicated.
- **It varies between takes of the same generation.** On `permanence-is-temporary` it hit **one of
  the two takes only**. So it is stochastic and decided per take, not per generation.

**Which means the two-take test applies here after all, and a re-roll is the response.** An earlier
version of this file claimed the opposite — that clip length was a per-generation setting both takes
inherit, so agreement across takes proved nothing about it. That was an inference, not an
observation, and one take of two contradicts it. It is withdrawn. If a padded clip is unwanted,
re-roll it; both takes agreeing, as they did here, is what a moderately-likely random event looks
like rather than evidence of a cause.

Still worth knowing:

- **It has two forms and they are not equally welcome.** The common one repeats the last few lines
  for several minutes — a stuck loop. The other restarts the whole song cleanly, which is what
  happened here, and for a band whose intent is a track that never develops it reads as the
  arrangement rather than a defect. Work out which you have before deciding it is a problem.
- **Do not prompt for it or against it.** An earlier revision added *one pass through the lyric
  only, do not repeat the song, ends on the final chant* to the unchanging variant, which would have
  done nothing about a stochastic renderer behaviour and might have suppressed a good outcome.
  Reverted; `beech-way-stops.style.txt` carries the original wording, and `never resolving` and
  `motorik repetition` stay. If you want the whole-song restart, the only route is re-rolling until
  it turns up.

**Status of the unchanging variant: a good render behind it, per the owner's verdict.** Whether Suno
held the riff genuinely unchanged has not been reported separately, so that specific question — the
one the variant exists to answer — is still open.

## `thats-seven` — sourcing notes

**The clubs are the real Scottish League One division, supplied by the owner.** This environment's
network policy refused the BBC table (`www.bbc.co.uk:443`, 403 at the proxy — the same block that
stops the Suno bridge working from here), so the first draft used clubs believed to have played at
that level and said so. The owner then pasted the table and the lyric was rewritten to use only
those ten, paired into the division's five fixtures.

**One club in the song is not in the division, on purpose.** *"East Fife four, Forfar five"* is the
famous almost-spoonerism of British football commentary, kept at the owner's instruction. It works
harder now than it did as filler: surrounded by verified fixtures it is plainly not today's result,
he offers no explanation, and a listener hears a joke he is not making.

**A factual correction the real table forced, and it changed the content.** The first draft had him
delighted by nil-nils. That is backwards: on a pools coupon a **no score draw** is 0-0 and a **score
draw** is 1-1 or 2-2, and the treble chance paid on score draws, so nil-nils were worth less. The
rewrite makes the good result a match where both sides scored and it cancelled out, and gives him
*"that is the wrong kind of nothing"* for a 0-0 — correct on a coupon, and perverse without it,
which is the band working as specified. The spec's rule is that a named thing must be real rather
than approximated, and that covers how a thing works as much as what it is called.

## Instrument roster check## Instrument roster check

A distorted guitar riff is the backbone here, which is shared ground with **hobo** — the only other
band in the catalogue built on a guitar. The fence is everything around it: hobo is a fuzz riff
under stacked female close harmony with no lead vocal at all; this is a big-beat riff under one
ranted male voice. Different bands by every audible measure, but if a render of one starts sounding
like the other, this is the collision to look at first.
