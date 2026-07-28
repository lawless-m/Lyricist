# hobo — Suno Style Prompts

## The locked core

This band's rotation rule is the strictest in the catalogue, and it exists for one reason: hobo
has to sound like **one group** across its whole catalogue, not a different band per track.

So the prompt is a **fixed head plus a short rotating tail**, not a set of freely-adapted
variants. The head below is pasted **word for word, in this order, at the front of every song's
`.style.txt`**:

```
close-harmony female group vocal, three and four part girl-group harmony on every single line,
all voices singing the same words at the same time, no lead vocal, no solo vocal, no ad-libs,
sung not rapped, sweet untroubled delivery, fuzz guitar riff backbone, live 90s hip-hop
breakbeat, big dumb downbeat, 90s alternative hip-hop guitar crossover
```

Never reordered, reworded, trimmed or swapped — not for emphasis, not for length. These terms
*are* the group. This narrows `write-song` step 6 deliberately: the graduated
reorder → swap → rewrite ladder applies **only to the rotating tail below**. A hobo song whose
prompt moves or drops a locked term is wrong even if that one take sounds good, because the cost
lands on the next song, not on that one.

## The rotating tail

Append two or three of these per song, after the locked head:

- **One cheap sample texture** — vinyl crackle, tambourine, a horn stab, a wrong-speed sample,
  handclaps, a cheap organ. Don't let any single one recur often enough to become part of the
  core by accident (girlboss learned this the hard way with its organ).
- **The lean** — `riff-forward` for the heavier songs, `sample-forward, looser` for the sparser
  ones.
- **Key/mood** — `major key hook` by default; a minor-key hook is available when the junk is
  grimmer, but the delivery stays sweet either way.
- **The ending** — `hard stop ending`. hobo lands; it does not fade, and it does not loop out.

## Suno notes

- **The harmony terms go at the front and stay there.** Suno defaults to putting a single lead
  vocal out in front and demoting harmony to backing, and long prompts lose their tail — so the
  one thing most likely to be dropped is the one thing that defines the band. Front-load it,
  every time. If a take still comes back with a frontwoman and backing singers, push harder on
  descriptive language (`no lead vocal`, `no solo vocal`, `all voices together`, `unison`) rather
  than reaching for a shortcut.
- **Naming real artists is off-limits**, in the prompt and in the lyric. The group-harmony
  reference points that inspired this band cannot be named — the sound has to be carried entirely
  by description.
- **The nonsense refrain must be made of real words in a daft order.** A *coined* word is exactly
  the shape of a producer tag, and tags get takes silently removed. The genre's own founding
  example is all real words; keep it that way, however odd the combination.
- **Paste the bracketed section tags.** They're doing more work here than in the other bands:
  since the vocal never changes and there is no lead/backing contrast, the tags plus the
  arrangement are the *only* things telling Suno where a section boundary is.
- **The drop-out is the least predictable section** — regenerate until the guitar genuinely
  vacates and the harmony is left bare. A take that keeps the band playing underneath kills the
  device outright.

## Worked example — `free-means-ours.style.txt`

```
close-harmony female group vocal, three and four part girl-group harmony on every single line,
all voices singing the same words at the same time, no lead vocal, no solo vocal, no ad-libs,
sung not rapped, sweet untroubled delivery, fuzz guitar riff backbone, live 90s hip-hop
breakbeat, big dumb downbeat, 90s alternative hip-hop guitar crossover, cheap sampled junk,
vinyl crackle, tambourine, major key hook, lo-fi, riff-forward, hard stop ending
```

Locked head verbatim; tail is `vinyl crackle, tambourine` (texture), `riff-forward` (lean),
`major key hook`, `hard stop ending`. The `.style.txt` on disk is a single unbroken paragraph —
the line breaks above are for reading only.
