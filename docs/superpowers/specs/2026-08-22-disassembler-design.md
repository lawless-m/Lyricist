# Disassembler — New Band Design

## Problem

The catalogue has ten bands and none of them is about the work most of the listener's life is
spent doing: programming and operations. The stated purpose is unusually plain and worth
recording, because it should govern how tightly this band is specified — **"programming and
devops based, for my own enjoyment"**. It is not solving a gap in the roster's emotional
coverage. It is a band the owner wants to listen to.

That difference matters. Every other spec in this repo was written *after* its engine had been
found — usually by a song that worked, sometimes by accident (ultracoase span out of a Bell
draft; girlboss was described as joining a roster it was already writing songs for). Disassembler
has no such song yet. Specifying its engine in advance would be inventing a theory and then
arguing songs into it.

## What the spike established

One song was written and rendered before any spec existed: `disassembler/what-file.txt`, from the
prompt *"file not found" — what fucking file, moron?*

Three findings, in ascending order of importance.

1. **The sparse form renders.** Roughly forty words over a mostly instrumental track worked
   mechanically: Suno held the long instrumental stretches, genuinely emptied the breakdown, and
   kept the vocal stabs percussive rather than sung.
2. **Gabber does not.** The genre's quality lives almost entirely in the kick — its distortion
   curve, pitch envelope and tail — which is production craft unreachable through a text field.
   Suno returns the *idea* of a kick every time. Adjusting tempo and genre vocabulary (190 →
   152 BPM, "gabber, Rotterdam" → "mainstream hardcore, Angerfist style") improved the terms but
   not the ceiling.
3. **And therefore the sparse form is wrong here anyway.** The owner's diagnosis, which reversed
   the design: *"our lyrical complexity in the other material has papered over what's missing in
   the music — laundry saves itself through the collage."* If the words are what rescue these
   tracks from a generic renderer, a band built on forty of them has removed its own compensator.
   Sparse is an honest form and the wrong one for this toolchain.

`what-file` is kept as the founding recording and as a record of the failure. Its engine —
fury at a system that could tell you and won't — is **Purple Dog's**, not this band's, and the
template says so.

## Goals

- Add **Disassembler** in the established two-file format, wired into `write-song`'s band table.
- Give it a genre that supports dense fast words and does not tread on `laundry`.
- Fence it explicitly against `laundry` (its nearest musical neighbour) and `purple-dog` (its
  nearest emotional one).
- **Deliberately under-specify the engine**, marked provisional, and tighten the spec once three
  or four songs have shown what the band actually keeps doing.

## Decisions

**Name.** *Disassembler* — a disassembler turns compiled machine code back into something a human
can nearly read, which is the band's voice rule made literal. It also plainly means one who takes
things apart. Chosen by the owner.

**Genre.** Drum & bass / neurofunk, around 174 BPM, half-time bass under fast breaks. Chosen
because dense fast vocals are native to it rather than fought for, and because its quality lives
in break editing and bass design rather than in one hand-tuned sound, so a generic renderer
degrades gracefully instead of collapsing.

**Voice rule.** Everything is system text — alert bodies, exit codes, runbook steps, graph
labels, commit messages, pager acknowledgements. Exactly **one complete human sentence per
track**, containing no tooling vocabulary, placed in the breakdown where the beat drops out.
Nothing in the song responds to it.

**Provisional temperature.** Accelerated and dislocated — she processes faster than the world
responds, so everything human arrives late. Recorded as a hypothesis, not a rule. The premise
bank deliberately contains fond, dreadful and joyful topics, and if the songs keep landing
somewhere else, the spec follows the songs.

## Fences

Against **laundry**, which is the real risk since both are fast and breakbeat-derived:

| | laundry | Disassembler |
|---|---|---|
| played by | two live drummers, against each other | programmed, edited, quantised |
| low end | blown out, clipping, overheated | clean sub, headroom, surgical |
| texture | lo-fi, hot, messy | cold, precise, dark |
| voices | gang chants, a crowd, a ranted preacher | no crowd at all — one voice and system text |
| the words | keep their images, lose their meaning | keep all their meaning, arrive too fast |

The voices row is the load-bearing one and it is structural rather than cosmetic: laundry's hooks
*are* a room chanting. If a Disassembler draft wants a gang vocal, it is a laundry song in the
wrong folder.

Against **purple-dog**: no grievance. Purple Dog is a reasonable man not believed by an
institution, and anger at a system is his. (That narrator is a man; this one is a woman.) Disassembler's register is impatience — not "you are
doing this to me" but "you are all so slow". Provisional, like the temperature.

## Non-goals

- Authentic gabber. Abandoned on evidence; see the spike.
- A tight engine before the songs exist.
- Any claim that these renders are the genre done properly. They are demos of the words.
