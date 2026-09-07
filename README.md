# Lyricist

A catalogue of song lyrics written to per-band specifications and rendered through Suno.

Each band is a folder with a spec, a set of Suno style prompts, and its lyrics. Nothing here is
generic: a band's spec describes a voice, an engine, a set of devices and a set of fences against
its siblings, and songs are written to that spec rather than to a genre.

## Layout

```
<band>/template.md          the spec — voice, engine, structure, devices, fences, don't-calcify rules
<band>/styles.md            Suno style-prompt variants, and everything learned about rendering them
<band>/<slug>.txt           a lyric
<band>/<slug>.style.txt     the exact prompt pasted into Suno for that song
```

Bands are discovered by the presence of `template.md`, so adding one is a matter of adding a
folder. `.claude/tropes/check.sh` prints the current catalogue size on every run if you want a
count.

Supporting directories:

```
.claude/tropes/             the trope library — see below
.claude/skills/write-song/  the workflow a new song follows, start to finish
tools/                      the toolchain — see below
docs/superpowers/           design docs and plans for the larger pieces
stats/                      periodic Suno account snapshots
audio/                      the local audio mirror — gitignored, see below
```

## The trope library

The catalogue's central problem is self-repetition across a large body of work, so devices are
tracked in two layers that must be updated together.

**`.claude/tropes/library.md`** is the human record. Every notable device gets an entry: what it
is, one example, the song it came from, and the catalogue size when it was logged. Entries are
cumulative and cross-band — a device logged from one band blocks its reuse in every other. Entries
are never edited or removed to let a draft through; the draft changes instead.

**`.claude/tropes/banned-patterns.tsv`** is the mechanical mirror: `SEVERITY⇥LOGGED_AT⇥regex⇥note`.
`check.sh` greps a draft against it. `PERM` never decays, `BAN` cools after sixty songs, `WATCH`
flags stock words that need a justification rather than a veto.

A library entry without a TSV pattern is invisible to the next song's check, which is why they are
written in the same commit. Two things worth knowing if you add patterns:

- `check.sh` matches **per line**, so a construction spanning a line break needs anchoring to one
  line or it silently never fires.
- The song that introduces a device will fail its own patterns from then on. That is correct.

The mechanical pass only catches exact anchors. A fresh sentence in a retired grammatical shape,
or a re-instantiated motif, passes the script and has to be caught by reading the library — which
is where most real collisions are found.

## Writing a song

`.claude/skills/write-song` has the full procedure. In outline: resolve the band, read its spec and
styles, read the trope library, draft, run the mechanical check, do the fuzzy check by hand, decide
and state the style adaptation, save the lyric and its style prompt, log every new device to both
trope files, then render.

## Rendering

Songs are rendered by Suno. `<band>/styles.md` carries what has been learned about making that
happen — including a catalogue-wide taxonomy of rendering faults in `disassembler/styles.md`, which
applies to every band. Its classes cover pronunciation (compound tokens, coined terms, transatlantic
defaults), orthography (initialisms, bare years, near-miss spellings), phrasing (a line ending in a
function word gets re-parsed across the break), and arrangement (name a gang vocal's placement, not
its character).

Every class in that file was found by listening to a render, never by predicting one. Two rules
follow from that and are worth keeping:

- **Check the other take before rewriting.** Differing across two takes of the same lyric means the
  fault is stochastic and a re-roll fixes it; identical in both means it is deterministic and the
  lyric has to change. Rewriting a stochastic miss throws away a good word for nothing.
- **Check the substitute is still true.** A replacement that renders correctly and states something
  false is a worse bug than the one it fixed.

## The audio mirror

`audio/` mirrors the Suno library locally and is gitignored. `suno-masters.json` is not — it records
which clips have been fetched as true WAV masters, and losing it means re-fetching everything, so it
lives in the repo root with a symlink into `audio/`.

Filing follows Suno, not the other way round: a clip's **project** decides its folder. Sorting
happens in Suno — render into the workspace, mark the take you want, move it to the artist project
and the rest to Rejects — and the next run reproduces that locally.

```
tools/suno-download.py              sync new tracks
tools/suno-download.py --dry-run    show what would happen
tools/suno-download.py --prune      move files whose project changed
tools/suno-download.py --mp3        write mp3s of the picks from the local masters
tools/suno-download.py --playlists  organise by playlist instead, keeping their order
```

Audio comes from Suno's WAV master, which is generated on demand — the mp3 the feed advertises is a
lossy encode of it, roughly 22 dB down.

## The rest of the toolchain

```
tools/db.py            the catalogue — one SQLite row per clip, keyed by GUID
tools/mixdown.py       plan and render a DJ mix
tools/mixtape.py       render one continuous mix per band or playlist, with a tracklist
tools/stems.py         separate stems via the Demucks server, then derive the bar grid the mixer needs
tools/analyse.py       tempo, beat grid and key for local WAVs, cached to audio/analysis.json
tools/fillers.py       cut a bank of loopable breakbeats from the isolated drum stems
tools/suno-stats.py    snapshot play/like/publish counts for the whole library
tools/suno-watch.py    watch the Suno tab for transient UI — toasts, challenges, dialogs
tools/suno-voice.py    select or clear the Suno voice (persona) on the open create form
tools/local-draft.py   generate drafts with a local model via text-generation-webui's API
bridge.js              browser bridge client — evaluates jobs in a logged-in Suno tab
```

Every tool with `suno` in its name drives a logged-in browser tab through that bridge rather than an
API key, so a tab has to be connected for them to work. `local-draft.py` is the exception and talks
to a local model instead, and `db.py` needs the bridge only for `sync`.

## The catalogue

`lyricist.db` is one SQLite row per Suno clip, keyed on the whole GUID. It exists because the same
state used to be spread across `audio/titles.json`, `audio/analysis.json`, `audio/stems.json` and
`stats/*.jsonl`, three of which key on the first eight characters — a lossy join, and none of them
aware of the others.

```
tools/db.py build              rebuild from the local JSON stores and audio/
tools/db.py sync               refresh from Suno — feed, projects, playlists
tools/db.py queue              GUIDs not yet fetched, newest first
tools/db.py fetched < ids      stamp GUIDs read from stdin as fetched
tools/db.py page               write catalogue.html, the track list
tools/db.py page --artifact    the same page, shaped for publishing
```

`page` writes a single self-contained track list — no server, no dependencies. One row per clip with
a search box, click-to-sort columns and an mp4 download link to right-click and save, over a band
rail whose fraction is published-over-total, so it doubles as the list of what to publish next.
Regenerate after a `sync`; both outputs are gitignored, being derivable from the database.

One template, two wrappers. The default writes `catalogue.html`, a standalone document for `file://`.
`--artifact` writes `catalogue.artifact.html` without a `<head>`, for anywhere that supplies its own.

Neither is what you actually read it through. `tools/catalogue.cgi` serves the same page from the
lighttpd already running on this box, built per request from the database, so a `sync` shows up on a
refresh with nothing to regenerate:

```
http://localhost/catalogue

/usr/lib/cgi-bin/catalogue                    symlink to tools/catalogue.cgi
/etc/lighttpd/conf-enabled/15-catalogue.conf  aliases /catalogue to it
```

It follows the shape the `glossy` endpoints in `10-cgi.conf` already use, and opens the database
`mode=ro` — the web server can read the repo and must never be able to write to it. Removing it is
`rm` on those two paths and a `systemctl reload lighttpd`.

The mp4 link only appears on published clips. `cdn1.suno.ai/<guid>.mp4` serves anything public and
403s the rest, and downloading what is already published is the route that neither spends the
download allowance nor looks like scraping. Unpublished clips are listed without a link.

It deliberately does not track where audio lives. The downloader runs on another machine and fetches
by GUID, so what it wants handed to it is a list of GUIDs — `queue` is that list, a query over
`fetched_at IS NULL` rather than a flag to keep in step with reality.

Nothing else reads it yet and nothing in it writes the JSON stores, so `build` is always safe to
re-run: it only fills columns in. The database is committed, which incidentally gives `analysis.json`
and `stems.json` the only backup they have — `audio/` is not in git.

`first_seen` and `last_seen` are worth knowing about. Suno deletes generations without saying so, and
a null `last_seen` (a clip known only from a local file) is a different state from a `last_seen`
older than the last sync (a clip Suno has dropped). `sync` reports both counts.
