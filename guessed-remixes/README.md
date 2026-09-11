# guessed-remixes — the 4:30 versions

**What this folder is.** The Suno duration slider moved from 3:00 to 4:30, and the question was
whether the Guessed catalogue needs longer lyrics to fill it. **It does not, and writing them would
break the band.** This folder holds the alternative: the same words, a longer arrangement.

## Why not extended lyrics

`guessed/template.md` is explicit: *"A whole song is maybe 120 words. Portishead lyrics are tiny.
Most of the track is space, loop and voice. If a draft is a page of text, it's the wrong genre."*
The catalogue already runs 300 to 375 words a song, so it is two to three times over its own spec
before anything is added. And the structural rule is *"This style has no big moment. It gets closer,
colder and quieter."* A Guessed track with ninety more seconds of words in it is a different band.

The rest of the house is the opposite case and the contrast is the point. Disassembler and Unadopted
are **dense by finding** — word count is rhythm material there, and a thin lyric produces a thin
track. Guessed is **sparse by design**, and the loop is what fills the room. So the density finding
does not transfer, and the correct use of the extra ninety seconds is loop, not lyric.

## What the remix actually changes

Nothing that is sung. Every extension is a bracketed section tag, which is arrangement instruction
rather than words:

- an **intro** of the loop alone before she starts, eight bars
- an **instrumental** between the first hook and verse two, where the strings come and go and
  nobody enters
- the **wordless** section doubled from four bars to eight
- the **loop-returns** beat after the drop-out given eight bars before she comes back in, so the
  indifference has time to register as indifference
- an **outro** of sixteen bars alone rather than four

Each style prompt gains one clause, `long instrumental stretches between vocals`, which is already
proven in this catalogue on the Unadopted core prompt.

## The comparison this sets up

Every track in `guessed/` is being re-rendered unchanged at 4:30 in the same session. That is the
control, and it tests the other hypothesis: that Suno fills the time by itself. The recorded
behaviour is that it pads stochastically and per take, either by looping the last few lines (a stuck
loop) or by playing the whole song through again (which, for a band whose premise is a loop that
never stops for her, may read as the arrangement rather than a fault — see `unadopted/styles.md`).

So there are three possible outcomes and they need listening to, not predicting:

1. the plain re-render pads well and this folder is unnecessary
2. the plain re-render pads badly and the tagged arrangement is the fix
3. Suno ignores the tags and both sound the same, in which case the lever is elsewhere

**All 34 are built.** The owner's call, after the word-count argument above was put to him. The
transform is mechanical and was applied uniformly rather than hand-written per song, because the
catalogue's section structure is identical across all of them: Verse 1, Hook, Verse 2, optional
second Hook, Wordless, drop-out, loop-returns, Final hook, optional Outro.

Each file's intro and outro texture is lifted from that song's own Verse 1 tag, so a motorik song
gets a motorik intro and a dusty-breakbeat song gets Rhodes and crackle. Songs that already had an
Outro keep their own tail behaviour and only the bar count changes, which is why `four-minute-fix`
still cuts dead and `capacity` still has the crackle running on after the music.

**Verified: not one sung line differs from the original in any of the 34.** Strip the bracketed
tags from both folders and the files are identical. Every change is arrangement instruction.

They render under the same titles with `(Remix)` appended, so each one sits next to its own control
in the feed.
