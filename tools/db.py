#!/usr/bin/env python3
"""The catalogue: one SQLite row per Suno clip, keyed by its GUID.

Usage:
  tools/db.py build              # (re)build from the local JSON stores and audio/
  tools/db.py sync               # refresh from Suno through the browser bridge
  tools/db.py queue              # GUIDs not yet fetched, newest first
  tools/db.py queue --project X  # ...limited to one Suno project
  tools/db.py fetched < ids      # stamp GUIDs read from stdin as fetched
  tools/db.py page               # write catalogue.html — the track list
  tools/db.py page --artifact    # ...the same page, shaped for publishing

Why this exists
---------------
Catalogue state was spread across audio/titles.json, audio/analysis.json,
audio/stems.json and stats/*.jsonl, three of which key on the first 8 characters
of the GUID. A truncated key is a lossy join, and none of those files knows about
any of the others. This is one store keyed on the whole GUID.

What it is not: it does not track where any audio lives. The downloader runs on
another machine and already fetches by GUID, so the useful thing to hand it is a
list of GUIDs, not a set of paths. `queue` is that list — a query over
`fetched_at IS NULL`, so there is no want-flag to keep in step with reality.

Nothing else reads this database yet, and nothing here writes the JSON stores.
They stay authoritative, so `build` can be re-run over a live database at any
time without losing anything — it only ever fills columns in. Deleting the file
first is different: everything comes back except `fetched_at`, which has no
source outside the database. Rewiring suno-download.py and the mixing tools to
read from here is a separate job, and the moment to lift the three bridge
scripts below into a shared module rather than copy them.

A GUID that reaches audio/ before it reaches any local JSON has no row to hang
its band on, so `build` also learns short ids from rows already in the table:
`sync` then `build` files anything the first build had to leave out.

lyricist.db is committed. audio/ is not, so analysis.json and stems.json are
currently the only expensive-to-recompute thing in the repo with no backup;
carrying them here gives them one.
"""

import argparse
import json
import re
import signal
import sqlite3
import sys
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

import page

REPO = Path(__file__).resolve().parent.parent
AUDIO = REPO / "audio"
STATS_DIR = REPO / "stats"
DB = REPO / "lyricist.db"

BROKER = "https://dw.ramsden-international.com/bridge"
TOKEN = "BRIDGE"
JOB_TIMEOUT_MS = 180_000

# Folders under audio/ holding work made from the downloads rather than
# downloads. The same clip ids turn up in them under other names, so a scan
# that treated them as projects would file clips under a band called "mixes".
DERIVED = {"playlists", "stems", "mixes", "fillers", "mp3"}

SHORT_ID = re.compile(r"^[0-9a-f]{8}$")

SCHEMA = """
CREATE TABLE IF NOT EXISTS clip (
  id          TEXT PRIMARY KEY,   -- Suno GUID, never truncated
  title       TEXT,
  created_at  TEXT,               -- ISO8601, as Suno reports it
  status      TEXT,
  model       TEXT,
  is_public   INTEGER,
  liked       INTEGER,
  project     TEXT,               -- Suno project name; decides the folder
  band        TEXT,               -- repo folder, when known
  slug        TEXT,               -- lyric slug, when known
  fetched_at  TEXT,               -- stamped once the remote fetcher has it
  first_seen  TEXT NOT NULL,       -- first date this database knew of the clip
  -- Date Suno last confirmed the clip exists. NULL means it never has: the id
  -- came off a local file and no sync has met it. That is a different thing
  -- from a clip Suno has since deleted, and conflating them would hide both.
  last_seen   TEXT
);
CREATE INDEX IF NOT EXISTS clip_created ON clip(created_at DESC);
CREATE INDEX IF NOT EXISTS clip_band ON clip(band, slug);
-- The legacy JSON stores key on the first 8 characters. This makes joining
-- them back onto a whole GUID cheap.
CREATE INDEX IF NOT EXISTS clip_short ON clip(substr(id, 1, 8));

CREATE TABLE IF NOT EXISTS playlist_member (
  playlist TEXT NOT NULL,
  clip_id  TEXT NOT NULL,
  idx      INTEGER,
  PRIMARY KEY (playlist, clip_id)
);

CREATE TABLE IF NOT EXISTS stat (
  clip_id   TEXT NOT NULL,
  taken_on  TEXT NOT NULL,        -- date of the snapshot, not a timestamp
  plays     INTEGER,
  likes     INTEGER,
  comments  INTEGER,
  is_public INTEGER,
  PRIMARY KEY (clip_id, taken_on)
);

CREATE TABLE IF NOT EXISTS analysis (
  clip_id     TEXT PRIMARY KEY,
  bpm         REAL,
  musical_key TEXT,
  camelot     TEXT,
  duration    REAL,
  data        TEXT                -- the whole analysis, beat grid included
);

CREATE TABLE IF NOT EXISTS stems (
  clip_id  TEXT PRIMARY KEY,
  bpm      REAL,
  duration REAL,
  data     TEXT
);
"""

# --- bridge scripts -------------------------------------------------------
# Copies of what suno-download.py and suno-stats.py run. Deliberate duplication:
# a database build has no business changing a downloader that works.

FEED = r"""
const tok = await window.Clerk.session.getToken();
const H = {Authorization: 'Bearer ' + tok};
const sleep = ms => new Promise(r => setTimeout(r, ms));
let page = 0, all = [];
while (page < 200) {
  let d = null;
  for (let attempt = 0; attempt < 6; attempt++) {
    const r = await fetch(`https://studio-api-prod.suno.com/api/feed/v2?page=${page}&_=` + Date.now(), {headers: H});
    if (r.status === 429) { await sleep(3000 * (attempt + 1)); continue; }
    if (!r.ok) return 'ERROR HTTP ' + r.status + ' at page ' + page;
    d = await r.json();
    break;
  }
  if (!d) return 'ERROR rate-limited out at page ' + page;
  all.push(...(d.clips || []));
  if (!d.has_more || (d.clips || []).length === 0) break;
  page++;
  await sleep(400);
}
return all.map(c => JSON.stringify({
  id: c.id, title: c.title, created_at: c.created_at, status: c.status,
  is_public: !!c.is_public, liked: !!c.is_liked, plays: c.play_count || 0,
  likes: c.upvote_count || 0, comments: c.comment_count || 0,
  model: c.model_name || null
})).join('\n');
"""

PROJECTS = r"""
const tok = await window.Clerk.session.getToken();
const H = {Authorization: 'Bearer ' + tok};
const sleep = ms => new Promise(r => setTimeout(r, ms));
const meta = await (await fetch('https://studio-api-prod.suno.com/api/project/me?page=0', {headers: H})).json();
const rows = [];
for (const p of (meta.projects || [])) {
  let page = 0;
  const seen = new Set();
  while (page < 60 && seen.size < (p.clip_count || 0)) {
    const r = await fetch(`https://studio-api-prod.suno.com/api/project/${p.id}?page=${page}`, {headers: H});
    if (r.status === 429) { await sleep(3000); continue; }
    if (!r.ok) break;
    const d = await r.json();
    const pcs = d.project_clips || [];
    if (!pcs.length) break;
    for (const pc of pcs) {
      const c = pc.clip || {};
      if (!c.id || seen.has(c.id)) continue;
      seen.add(c.id);
      rows.push(JSON.stringify({project: p.name, id: c.id,
        liked: !!(c.reaction && c.reaction.reaction_type === 'L')}));
    }
    // Page 0 and page 1 return identical rows — the endpoint is 1-based — so a
    // page with nothing fresh in it is not the end. Only an empty page is.
    page++;
    await sleep(250);
  }
}
return rows.join('\n');
"""

PLAYLISTS = r"""
const tok = await window.Clerk.session.getToken();
const H = {Authorization: 'Bearer ' + tok};
const sleep = ms => new Promise(r => setTimeout(r, ms));
const meta = await (await fetch('https://studio-api-prod.suno.com/api/playlist/me?page=0', {headers: H})).json();
const rows = [];
for (const p of (meta.playlists || [])) {
  let page = 0;
  const seen = new Set();
  // No clip_count on a playlist object, so there is no total to count towards:
  // an empty page is the only end there is.
  while (page < 60) {
    const r = await fetch(`https://studio-api-prod.suno.com/api/playlist/${p.id}?page=${page}`, {headers: H});
    if (r.status === 429) { await sleep(3000); continue; }
    if (!r.ok) break;
    const d = await r.json();
    const pcs = d.playlist_clips || [];
    if (!pcs.length) break;
    for (const pc of pcs) {
      const c = pc.clip || {};
      if (!c.id || seen.has(c.id)) continue;
      seen.add(c.id);
      rows.push(JSON.stringify({playlist: p.name, index: pc.relative_index, id: c.id}));
    }
    page++;
    await sleep(250);
  }
}
return rows.join('\n');
"""


def api(path, body=None):
    req = urllib.request.Request(
        BROKER + path,
        data=json.dumps(body).encode() if body else None,
        headers={"Authorization": "Bearer " + TOKEN, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=JOB_TIMEOUT_MS / 1000 + 15) as r:
        return json.load(r)


def fetch_clips(script):
    worker = next((w["connectionId"] for w in api("/workers")["workers"]
                   if w.get("host") == "suno.com"), None)
    if not worker:
        sys.exit("No suno.com tab connected to the bridge — open suno.com and load the bridge client.")
    job = api("/jobs/sync", {"target": worker, "timeout": JOB_TIMEOUT_MS, "script": script})
    if job.get("status") != "done":
        sys.exit(f"Bridge job {job.get('status')}: {job.get('error')}")
    out = job["result"] or ""
    if out.startswith("ERROR"):
        sys.exit(out)
    return [json.loads(line) for line in out.splitlines() if line.strip()]


# --- build ----------------------------------------------------------------

def connect():
    db = sqlite3.connect(DB)
    db.row_factory = sqlite3.Row
    db.executescript(SCHEMA)
    return db


def load_json(path):
    return json.loads(path.read_text()) if path.exists() else {}


def short_map(db, ids):
    """first-8 -> whole GUID, refusing to guess if two GUIDs ever share a prefix.

    Three of the JSON stores key on the truncation, so this is the only way back
    to a real id. It has held for the whole catalogue so far, but a silent
    mis-join would be much worse than a stop.
    """
    seen = {}
    clash = {}
    for full in ids:
        s = full[:8]
        if s in seen and seen[s] != full:
            clash.setdefault(s, {seen[s]}).add(full)
        seen[s] = full
    for row in db.execute("SELECT id FROM clip"):
        seen.setdefault(row["id"][:8], row["id"])
    if clash:
        for s, fulls in clash.items():
            print(f"  {s} -> {' '.join(sorted(fulls))}", file=sys.stderr)
        sys.exit("Two GUIDs share an 8-character prefix; the legacy stores cannot be joined.")
    return seen


def upsert_clip(db, row):
    """Insert or update, keeping the earliest first_seen and the latest last_seen.

    Only overwrites a column when the caller has something to say about it, so a
    partial source (a stats snapshot with no project) cannot blank what a fuller
    one already recorded.

    `seen` means *observed in Suno on this date*, and only a stats snapshot or a
    sync may pass it. Reading a clip out of a local JSON file is not evidence
    Suno still has it — bumping last_seen from audio/titles.json would make
    everything on disk look present forever, and the point of the pair is to be
    able to ask what Suno has quietly deleted.
    """
    cols = [c for c in ("title", "created_at", "status", "model", "is_public",
                        "liked", "project", "band", "slug", "fetched_at")
            if row.get(c) is not None]
    sets = ", ".join(f"{c} = COALESCE(excluded.{c}, clip.{c})" for c in cols)
    seen = row.get("seen")
    # A row we only ever met locally gets dated by its own creation, falling back
    # to today, and its last_seen is left to the first sync that finds it.
    first = seen or (row.get("created_at") or today())[:10]
    updates = ([] if not seen else
               ["first_seen = MIN(clip.first_seen, excluded.first_seen)",
                "last_seen  = MAX(COALESCE(clip.last_seen, ''), excluded.last_seen)"])
    if sets:
        updates.append(sets)
    conflict = f"DO UPDATE SET {', '.join(updates)}" if updates else "DO NOTHING"
    db.execute(
        f"""INSERT INTO clip (id, first_seen, last_seen{''.join(', ' + c for c in cols)})
            VALUES (?, ?, ?{', ?' * len(cols)})
            ON CONFLICT(id) {conflict}""",
        [row["id"], first, seen] + [row[c] for c in cols])


def today():
    return date.today().isoformat()


def import_stats(db):
    """stats/*.jsonl — the only local source of whole GUIDs, and the time series."""
    clips = stats = 0
    for path in sorted(STATS_DIR.glob("suno-*.jsonl")):
        taken_on = path.stem.replace("suno-", "")
        for line in path.read_text().splitlines():
            if not line.strip():
                continue
            c = json.loads(line)
            upsert_clip(db, {**c, "seen": taken_on})
            db.execute("""INSERT INTO stat (clip_id, taken_on, plays, likes, comments, is_public)
                          VALUES (?, ?, ?, ?, ?, ?)
                          ON CONFLICT(clip_id, taken_on) DO UPDATE SET
                            plays = excluded.plays, likes = excluded.likes,
                            comments = excluded.comments, is_public = excluded.is_public""",
                       (c["id"], taken_on, c.get("plays"), c.get("likes"),
                        c.get("comments"), int(bool(c.get("is_public")))))
            clips += 1
            stats += 1
    return clips, stats


def import_titles(db, shorts):
    """audio/titles.json is rewritten on every download, so it is the freshest
    title we have locally — fresher than a months-old stats snapshot."""
    unresolved, n = [], 0
    for short, title in load_json(AUDIO / "titles.json").items():
        full = shorts.get(short)
        if not full:
            unresolved.append(short)
            continue
        upsert_clip(db, {"id": full, "title": title})
        n += 1
    return n, unresolved


def import_analysis(db, shorts):
    n = 0
    for short, a in load_json(AUDIO / "analysis.json").items():
        full = shorts.get(short)
        if not full:
            continue
        db.execute("""INSERT INTO analysis (clip_id, bpm, musical_key, camelot, duration, data)
                      VALUES (?, ?, ?, ?, ?, ?)
                      ON CONFLICT(clip_id) DO UPDATE SET
                        bpm = excluded.bpm, musical_key = excluded.musical_key,
                        camelot = excluded.camelot, duration = excluded.duration,
                        data = excluded.data""",
                   (full, a.get("bpm"), a.get("key"), a.get("camelot"),
                    a.get("duration"), json.dumps(a, separators=(",", ":"))))
        n += 1
    return n


def import_stems(db, shorts):
    n = 0
    for short, s in load_json(AUDIO / "stems.json").items():
        full = shorts.get(short)
        if not full:
            continue
        db.execute("""INSERT INTO stems (clip_id, bpm, duration, data)
                      VALUES (?, ?, ?, ?)
                      ON CONFLICT(clip_id) DO UPDATE SET
                        bpm = excluded.bpm, duration = excluded.duration, data = excluded.data""",
                   (full, s.get("bpm"), s.get("duration"),
                    json.dumps(s, separators=(",", ":"))))
        n += 1
    return n


def scan_audio(db, shorts):
    """Recover band and slug from the filenames the downloader already writes.

    Every fetched wav is <slug>--<first 8 of the GUID>.wav under the folder its
    Suno project chose, so the back catalogue's link to its lyrics is sitting in
    the filesystem. Nothing else records it: before create-time capture, band was
    re-derived by fuzzy-matching a clip title against lyric text on every run.
    """
    n = 0
    for wav in sorted(AUDIO.glob("*/*.wav")):
        band = wav.parent.name
        if band in DERIVED:
            continue
        slug, _, short = wav.stem.rpartition("--")
        if not slug or not SHORT_ID.match(short):
            continue
        full = shorts.get(short)
        if not full:
            continue
        upsert_clip(db, {"id": full, "band": band, "slug": slug})
        n += 1
    return n


def cmd_build(args):
    db = connect()
    with db:
        known = {json.loads(line)["id"]
                 for path in STATS_DIR.glob("suno-*.jsonl")
                 for line in path.read_text().splitlines() if line.strip()}
        # A roster of GUIDs, nothing more: it is the widest list of real ids on
        # this machine, which is what makes the truncated stores joinable offline.
        roster = REPO / "suno-masters.json"
        if roster.exists():
            known |= set(json.loads(roster.read_text()))
        shorts = short_map(db, known)

        clips, stats = import_stats(db)
        titled, unresolved = import_titles(db, shorts)
        analysed = import_analysis(db, shorts)
        stemmed = import_stems(db, shorts)
        filed = scan_audio(db, shorts)

    total = db.execute("SELECT COUNT(*) FROM clip").fetchone()[0]
    print(f"{DB.relative_to(REPO)}: {total} clips")
    print(f"  stats     {clips} rows over {stats and len(list(STATS_DIR.glob('suno-*.jsonl')))} snapshots")
    print(f"  titles    {titled}")
    print(f"  analysis  {analysed}")
    print(f"  stems     {stemmed}")
    print(f"  filed     {filed} wavs gave a band and slug")
    if unresolved:
        print(f"  {len(unresolved)} short ids in titles.json have no whole GUID to hang "
              f"on — run sync, and if they are still here after it, Suno has deleted "
              f"them: {' '.join(sorted(unresolved))}")


# --- sync -----------------------------------------------------------------

def cmd_sync(args):
    db = connect()
    now = datetime.now(timezone.utc).date().isoformat()

    print("reading the feed...")
    feed = fetch_clips(FEED)
    with db:
        for c in feed:
            upsert_clip(db, {**c, "is_public": int(bool(c.get("is_public"))),
                             "liked": int(bool(c.get("liked"))), "seen": now})
            db.execute("""INSERT INTO stat (clip_id, taken_on, plays, likes, comments, is_public)
                          VALUES (?, ?, ?, ?, ?, ?)
                          ON CONFLICT(clip_id, taken_on) DO UPDATE SET
                            plays = excluded.plays, likes = excluded.likes,
                            comments = excluded.comments, is_public = excluded.is_public""",
                       (c["id"], now, c.get("plays"), c.get("likes"),
                        c.get("comments"), int(bool(c.get("is_public")))))
    print(f"  {len(feed)} clips")

    print("reading projects...")
    projects = fetch_clips(PROJECTS)
    with db:
        for r in projects:
            upsert_clip(db, {"id": r["id"], "project": r["project"],
                             "liked": int(bool(r.get("liked"))), "seen": now})
    print(f"  {len(projects)} filed in {len({r['project'] for r in projects})} projects")

    print("reading playlists...")
    playlists = fetch_clips(PLAYLISTS)
    with db:
        # Replaced whole rather than merged: a clip removed from a playlist in
        # Suno has to disappear from here too, and an upsert would keep it.
        db.execute("DELETE FROM playlist_member")
        db.executemany("INSERT OR REPLACE INTO playlist_member (playlist, clip_id, idx) VALUES (?, ?, ?)",
                       [(r["playlist"], r["id"], r.get("index")) for r in playlists])
    print(f"  {len(playlists)} entries in {len({r['playlist'] for r in playlists})} playlists")

    total = db.execute("SELECT COUNT(*) FROM clip").fetchone()[0]
    # Suno deletes generations without saying so, which is exactly what a mirror
    # is for noticing. Anything the feed did not mention this time is stale.
    gone = db.execute("SELECT COUNT(*) FROM clip WHERE last_seen < ?", (now,)).fetchone()[0]
    never = db.execute("SELECT COUNT(*) FROM clip WHERE last_seen IS NULL").fetchone()[0]
    print(f"{total} clips in {DB.relative_to(REPO)}")
    if gone:
        print(f"  {gone} Suno has dropped since a previous sync — "
              f"SELECT id, title, last_seen FROM clip WHERE last_seen < '{now}'")
    if never:
        print(f"  {never} known only from local files, never confirmed by Suno — "
              f"SELECT id, title FROM clip WHERE last_seen IS NULL")


# --- queue ----------------------------------------------------------------

def cmd_queue(args):
    db = connect()
    sql = "SELECT id FROM clip WHERE fetched_at IS NULL"
    params = []
    if args.project:
        sql += " AND project = ?"
        params.append(args.project)
    sql += " ORDER BY created_at DESC"
    for row in db.execute(sql, params):
        print(row["id"])


def cmd_fetched(args):
    db = connect()
    ids = [line.strip() for line in sys.stdin if line.strip()]
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with db:
        db.executemany("UPDATE clip SET fetched_at = ? WHERE id = ?",
                       [(stamp, i) for i in ids])
    missing = [i for i in ids if not db.execute("SELECT 1 FROM clip WHERE id = ?", (i,)).fetchone()]
    print(f"stamped {len(ids) - len(missing)} clips")
    if missing:
        print(f"  {len(missing)} not in the catalogue, so not stamped: {' '.join(missing)}",
              file=sys.stderr)


# --- page -----------------------------------------------------------------

def cmd_page(args):
    db = connect()
    # Plays and likes live in the stat series, so take each clip's most recent
    # reading rather than carrying a denormalised copy on the clip itself.
    rows = db.execute("""
        SELECT c.id, c.title, c.band, c.project, c.created_at, c.slug,
               CASE WHEN c.is_public THEN 1 ELSE 0 END AS is_public,
               s.plays, s.likes
        FROM clip c
        LEFT JOIN stat s ON s.clip_id = c.id
             AND s.taken_on = (SELECT MAX(taken_on) FROM stat WHERE clip_id = c.id)
        WHERE c.last_seen IS NOT NULL
        ORDER BY c.created_at DESC""").fetchall()
    clips = [dict(r) for r in rows]

    # The rail's fraction is the point of it: published over total, per band,
    # which is the same thing as how much of each band you can actually download.
    bands = [(r["band"], r["n"], r["pub"]) for r in db.execute("""
        SELECT COALESCE(band, 'unfiled') AS band, COUNT(*) AS n,
               SUM(CASE WHEN is_public THEN 1 ELSE 0 END) AS pub
        FROM clip WHERE last_seen IS NOT NULL
        GROUP BY COALESCE(band, 'unfiled') ORDER BY n DESC""")]

    published = sum(c["is_public"] for c in clips)
    plays = sum(c["plays"] or 0 for c in clips)
    when = date.today().strftime("%-d %B %Y")

    markup = page.render(clips, bands, when, published, plays)
    default = "catalogue.artifact.html" if args.artifact else "catalogue.html"
    out = Path(args.output) if args.output else REPO / default
    out.write_text(markup if args.artifact else page.wrap(markup), encoding="utf-8")

    where = out.relative_to(REPO) if out.is_relative_to(REPO) else out
    print(f"{where}: {len(clips)} clips, {published} with an mp4, {len(bands)} bands")
    if args.artifact:
        print("  no <head> of its own — publish it, don't open it")
    skipped = db.execute("SELECT COUNT(*) FROM clip WHERE last_seen IS NULL").fetchone()[0]
    if skipped:
        print(f"  {skipped} left out — Suno has never confirmed them, so there is "
              f"nothing to link to")


def main():
    # `queue | head` closes the pipe under us, which is not an error.
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)

    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build", help="(re)build from the local JSON stores and audio/")
    sub.add_parser("sync", help="refresh from Suno through the browser bridge")
    q = sub.add_parser("queue", help="GUIDs not yet fetched, newest first")
    q.add_argument("--project", help="limit to one Suno project")
    sub.add_parser("fetched", help="stamp GUIDs read from stdin as fetched")
    p = sub.add_parser("page", help="write the track list as one HTML file")
    p.add_argument("-o", "--output", help="where to write it (default catalogue.html)")
    p.add_argument("--artifact", action="store_true",
                   help="emit the body alone, for publishing as an Artifact")

    args = ap.parse_args()
    {"build": cmd_build, "sync": cmd_sync, "queue": cmd_queue,
     "fetched": cmd_fetched, "page": cmd_page}[args.cmd](args)


if __name__ == "__main__":
    main()
