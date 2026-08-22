# Disassembler — Song Style Spec

A reusable brief for the **Disassembler** style — drum & bass and neurofunk carrying words about
programming and operations. Hand this to Claude with the instruction **"song for Disassembler"** —
optionally with a topic — and it should produce a new, standalone lyric set sharing the voice,
structure and devices below.

**This spec is deliberately looser than its siblings, and that is on purpose.** Every other band
here was specified *after* its engine had been found by a song that worked. This one has no such
song yet. The genre, the voice rule and the fences are settled; the engine is a hypothesis marked
provisional below. Write songs, then tighten this file to match what the band keeps doing —
not the other way round.

**Stated purpose:** programming and devops based, for the owner's own enjoyment. It is allowed to
be funny. It does not need a covert engine under every song. If a topic is enjoyable and lands,
that is sufficient justification for it existing.

**The name is load-bearing.** A disassembler turns compiled machine code back into something a
human can nearly read — which is exactly the voice rule below. It also plainly means one who
takes things apart.

---

## The voice rule

This is the settled part and everything hangs off it.

**Everything on the record is system text.** Alert bodies, exit codes, runbook steps, graph
labels, commit messages, pager acknowledgements, log lines, config keys, error strings, the
contents of a filename. Real, accurate, checkable. Where another band would write an image, this
band quotes output.

**Exactly one complete human sentence per track.** One. It contains no tooling vocabulary at all,
it has a subject and a verb belonging to a person, and it is the only thing on the record with
those. It goes in the breakdown, where the beat drops out — which is the only place in a track at
this tempo with room for a sentence in it.

**Nothing responds to it.** The beat comes back and it is system text again. No answer arrives,
nobody acknowledges it, and the song does not return to it.

Fragments are allowed everywhere. Sentences are not. The human can manage two or three words at
speed — a swear, a name, a question with no verb — and gets one whole thought per track, once.

---

## The voice (settled 2026-08-22, by ear)

A **female MC**. Brisk, projected, level — she is reading a list aloud to a room at speed, not
confiding in anybody. The flatness is concentration, not exhaustion. A **warm echo delay** sits on
the vocal, thrown out over an otherwise dry and precise mix.

Three things it must never be, all of which are `guessed`: **close**, **intimate**, **fragile**,
**breathy**, **confessional**, or a **dry voice in a reverberant room**. Her flatness is
withholding; this one's is attention. If a take sounds like somebody telling you a secret, it is
the wrong band.

The earlier male take was fine and is not ruled out — but the voice is a decision to be made per
song, never a default that gets typed in without being chosen.

## Song structure (the template)

Drum & bass form, so hang it on that rather than fighting it.

1. **Intro** — atmos, sub, no break yet. One or two lines of system text read flat, almost bored.
2. **Build** — the break enters. Dense, fast, ranted system text. This is where the volume of
   words lives; it should be more than a listener can hold.
3. **Drop** — half-time bass under the fast break. Words thin to short shouted anchors, two to
   four words, repeated.
4. **The breakdown** — **the signature move.** Beat gone. Sub gone. One voice, not shouted — but
   **not whispered either**. Said flat, at the same projected level, into a silent room. A whisper
   is confiding and this narrator does not confide; that is `guessed`'s drop-out, which this
   otherwise resembles. The single human sentence. Then nothing.
5. **Second drop** — bigger, the anchors stacked and pitched. No new information.
6. **Outro** — strips back to the atmos it started on. Does not resolve.

The **one-sentence breakdown is the signature move** — the equivalent of gypsy-emo's
half-time-to-double-time bridge, institutional hardcore's mock-calm monologue, dissociative
hardcore's dissolve, lurker trip-hop's drop-out and Penny Rich's plain line. Don't skip it, don't
let a second sentence into it, and don't let anything in the song acknowledge it.

---

## Fences

**Against `laundry`.** The real risk, since both are fast and breakbeat-derived. The separation is
production temperature and the crowd, not tempo:

| | laundry | Disassembler |
|---|---|---|
| played by | two live drummers, against each other | programmed, edited, quantised |
| low end | blown out, clipping, overheated | clean sub, headroom, surgical |
| texture | lo-fi, hot, messy | cold, precise, dark |
| voices | gang chants, a crowd, a ranted preacher | no crowd at all — one voice and system text |
| the words | keep their images, lose their meaning | keep all their meaning, arrive too fast |

That fourth row is load-bearing and structural: laundry's hooks *are* a room chanting. **If a
Disassembler draft wants a gang vocal, it is a laundry song in the wrong folder.** And the fifth
row is the craft difference — laundry's collage drains sense out on purpose; here every line is
true and useful and there are simply too many of them arriving too fast.

**Against `purple-dog`.** No grievance. A reasonable man not believed by an institution is Purple
Dog's, and so is fury at a system. The founding recording `what-file` breaks this rule — it is
angry at a machine for withholding a filename it plainly has — and it is kept as a record, not as
a model. This band's register is impatience rather than accusation: not "you are doing this to
me", but "you are all so slow".

---

## Provisional engine

**Accelerated and dislocated.** He processes faster than the world responds, so everything human —
meetings, replies, reviews, his own hands — arrives late. The dislocation is a clock problem
rather than a cruelty problem: nobody is withholding and nobody is at fault.

Recorded as a hypothesis. The premise bank below deliberately spans fond, dreadful and joyful, and
if the songs keep landing somewhere other than dislocation, **rewrite this section to follow
them.**

---

## Premise bank

- **git blame finds you.** Three years ago, a Sunday, and the commit message is "fix".
- **`// this should never happen`** — and the line underneath it, which handles it.
- **The comment that says don't delete this.** Unsigned, dated 2014, and nobody ever will.
- **The one box everybody is frightened of.** It has a name. It has never been rebooted. It runs
  payroll.
- **The maintainer in Nebraska.** One bloke, unpaid, and half the internet is downstream.
- **Deleting nine hundred lines**, and the pull request being the best day of the year.
- **The certificate expires on a Saturday.** Everyone knows. Nobody moves it.
- **`temp2`** has been in production since before the child who is now at school.
- **Works on my machine**, said sincerely, by someone who is correct.
- **`lastest_new_thisone.doc`** — version control by filename, the archaeology of a shared drive,
  and the fact that the newest file is never the one called new. The typo is the truest part.
- **The deploy takes forty minutes** and he read the whole diff in the first two.
- **It resolved itself an hour ago** and the incident call is still going.

One topic per song. Spend them.

---

## What the spike established (read before changing the form)

The first song, `what-file`, was written to a different design: roughly forty words over a mostly
instrumental gabber track. The form rendered — Suno held the instrumental stretches, emptied the
breakdown, kept the stabs percussive — but the genre did not, because gabber's whole quality lives
in a kick that cannot be specified in a text field.

**And density does mechanical work, not just compensatory work.** The first song written to this
spec — `use-this-one`, nineteen filenames read flat over a rolling break — came back with the
owner's verdict: *"it worked well, enough lyrics to drive the percussion and bass."* In a genre
where the vocal is percussive, the word count *is* rhythm material. Suno builds the groove out of
what it has been given to say, so a thin lyric produces a thin track for reasons that have nothing
to do with meaning. Write long.

Also established there, against both our expectations: **it can render filenames.** Underscores,
version suffixes and bracketed duplicates all survived. Punctuation-dense text was assumed
unspeakable and is not — do not pre-emptively translate system text into how a person would say it
aloud without testing first.

The finding that changed the design is broader than this band: **the words are what rescue these
renders from a generic tool.** laundry survives Suno because its collage is doing so much work
that the listener stops auditing the production. A band built on forty words has removed its own
compensator. So Disassembler is **dense** — that is not a stylistic preference, it is what makes
the tracks survive.

Full reasoning in `docs/superpowers/specs/2026-08-22-disassembler-design.md`.

---

## Don't let it calcify

Too early for real rules. Two to watch from the start:

- **The one human sentence.** It will want to be about time every single song, because the
  provisional engine is about latency. Vary what it is about, or the engine will calcify before
  it has been tested.
- **The system text.** Reaching for the same registers — errors, alerts, exit codes — will make
  every song sound like an outage. Commit messages, variable names, filenames, code comments, a
  README and a changelog are all system text too, and none of them are alarms.
- **Counting.** Flagged after three songs, two of which end on a numeric field that has changed
  while the track played (`use-this-one`'s identical timestamps, `still-passed`'s pending sector
  going from sixteen to seventeen). System text is mostly numbers, so the default is a voice
  reading counters over a break, forever. **Alternate deliberately: a song whose system text is
  countable should be followed by one whose system text is prose** — a comment, a commit message,
  a ticket title, a line of documentation — where the payload is the wording rather than the value.
  And the closing move must not always be a number that moved.
