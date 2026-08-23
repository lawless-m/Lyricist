#!/usr/bin/env python3
"""Mirror your Suno library to local WAVs, foldered the way you organise it.

Usage:
  tools/suno-download.py              # sync everything new
  tools/suno-download.py --dry-run    # list what would be fetched
  tools/suno-download.py --prune      # also move files whose project changed
  tools/suno-download.py --playlists  # organise by playlist instead, keeping order

Your Suno *projects* are the filter and the folder. A track you have filed
under Rejects lands in audio/rejects/ and nowhere else; move it out of Rejects
in Suno and the next run refiles it. The LIKE flag is ignored — it is a working
filter on the Suno site, not a statement about what belongs here.

My Workspace is a filing decision too — it means still in progress — so it
gets audio/in-progress/ rather than being scattered among the finished work.
Anything in no project at all falls back to the repo lyric files: first by matching the Suno title to a
filename, then by looking for the title inside a lyric (many titles are the
hook line, not the filename — "Act Like It's News" is guessed/four-minute-fix).
Still unresolved, including the non-band personal songs, goes to audio/unsorted/.

Refiling is free: a track already on disk is hard-linked to its new folder, not
downloaded again. Without --prune the old copy stays put, so nothing is deleted
behind your back.

Audio comes from Suno's WAV master, not the mp3 the feed advertises: the master
is rendered on demand and downloaded as 48 kHz PCM, then resampled to the 44.1 kHz
the rest of the archive and the mixing tools already use. audio/.masters.json
records which clips arrived this way, so a re-run replaces anything still left
over from the old mp3 path and leaves the rest alone. Reckon on ~25 MB per track.

That record is the one piece of state worth keeping: lose it and the next run
reads it as "nothing is a master" and re-fetches everything, which from
3 September 2026 is months of a 60-a-month download allowance. audio/ is not in
git, so it is a symlink to suno-masters.json in the repo root, which is.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
AUDIO = REPO / "audio"
BROKER = "https://dw.ramsden-international.com/bridge"
TOKEN = "BRIDGE"
JOB_TIMEOUT_MS = 180_000

PLAYLISTS = r"""
const tok = await window.Clerk.session.getToken();
const H = {Authorization: 'Bearer ' + tok};
const sleep = ms => new Promise(r => setTimeout(r, ms));
const meta = await (await fetch('https://studio-api-prod.suno.com/api/playlist/me?page=0', {headers: H})).json();
const rows = [];
for (const p of (meta.playlists || [])) {
  let page = 0;
  const seen = new Set();
  while (page < 50 && seen.size < (p.song_count || 0)) {
    const r = await fetch(`https://studio-api-prod.suno.com/api/playlist/${p.id}?page=${page}`, {headers: H});
    if (r.status === 429) { await sleep(3000); continue; }
    if (!r.ok) break;
    const d = await r.json();
    const pcs = d.playlist_clips || [];
    if (!pcs.length) break;
    let fresh = 0;
    for (const pc of pcs) {
      const c = pc.clip || {};
      if (!c.id || seen.has(c.id)) continue;   // page is 1-based: page 0 and 1 repeat
      seen.add(c.id); fresh++;
      rows.push(JSON.stringify({
        playlist: p.name, index: pc.relative_index, id: c.id, title: c.title,
        status: c.status, audio_url: c.audio_url || (c.media_urls && c.media_urls[0]) || null
      }));
    }
    if (!fresh) break;
    page++;
    await sleep(300);
  }
}
return rows.join('\n');
"""

# Suno's feed only carries lossy mp3/m4a. The WAV master is generated on demand:
# POST convert_wav, then poll wav_file until it hands back a URL. A null test put
# the mp3 only 21.8 dB below the master — it is a real encode of it, not a decode
# the other way round, so the mp3 path throws away audio we can still have.
WAV_URLS = r"""
const tok = await window.Clerk.session.getToken();
const H = {Authorization: 'Bearer ' + tok, 'Content-Type': 'application/json'};
const B = 'https://studio-api-prod.suno.com';
const sleep = ms => new Promise(r => setTimeout(r, ms));
const ids = IDS;
const out = {}, pending = new Set(ids);
for (const id of ids) {
  try { await fetch(`${B}/api/gen/${id}/convert_wav`, {method: 'POST', headers: H, body: '{}'}); }
  catch (e) { }
  await sleep(120);
}
for (let round = 0; round < 30 && pending.size; round++) {
  for (const id of [...pending]) {
    try {
      const r = await fetch(`${B}/api/gen/${id}/wav_file`, {headers: H});
      if (!r.ok) continue;
      const d = await r.json();
      if (d.wav_file_url) { out[id] = d.wav_file_url; pending.delete(id); }
    } catch (e) { }
    await sleep(120);
  }
  if (pending.size) await sleep(4000);
}
return Object.entries(out).map(([id, url]) => JSON.stringify({id, url})).join('\n');
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
    let fresh = 0;
    for (const pc of pcs) {
      const c = pc.clip || {};
      if (!c.id || seen.has(c.id)) continue;
      seen.add(c.id); fresh++;
      rows.push(JSON.stringify({project: p.name, id: c.id}));
    }
    if (!fresh) break;
    page++;
    await sleep(250);
  }
}
return rows.join('\n');
"""

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
  id: c.id, title: c.title, liked: !!c.is_liked, status: c.status,
  audio_url: c.audio_url || (c.media_urls && c.media_urls[0]) || null
})).join('\n');
"""


# Project names that already have a differently-named folder in the repo.
PROJECT_FOLDER = {
    "Penny": "penny-rich",
    "CoaseGuard": "coase-guard",
    "Cherry": "girlboss",
    "Emosy": "the-bell-knows-my-name",
    "Rinse Cycle": "laundry",     # laundry's second album, after the first was mixed
    "My Workspace": "in-progress",
}

# Folders holding work made from the downloads, not downloads. Same clip ids
# turn up here under other names; --prune must never touch them.
DERIVED = {"playlists", "stems", "mixes", "fillers"}


def api(path, body=None):
    req = urllib.request.Request(
        BROKER + path,
        data=json.dumps(body).encode() if body else None,
        headers={"Authorization": "Bearer " + TOKEN, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=JOB_TIMEOUT_MS / 1000 + 15) as r:
        return json.load(r)


def fetch_clips(script=FEED):
    worker = next((w["connectionId"] for w in api("/workers")["workers"] if w.get("host") == "suno.com"), None)
    if not worker:
        sys.exit("No suno.com tab connected to the bridge — open suno.com and load the bridge client.")
    job = api("/jobs/sync", {"target": worker, "timeout": JOB_TIMEOUT_MS, "script": script})
    if job.get("status") != "done":
        sys.exit(f"Bridge job {job.get('status')}: {job.get('error')}")
    out = job["result"] or ""
    if out.startswith("ERROR"):
        sys.exit(out)
    return [json.loads(line) for line in out.splitlines() if line.strip()]


MASTERS = AUDIO / ".masters.json"


def masters():
    return set(json.loads(MASTERS.read_text())) if MASTERS.exists() else set()


def mark_master(clip_id):
    have = masters()
    have.add(clip_id)
    MASTERS.write_text(json.dumps(sorted(have), indent=0))


def wav_urls(ids, batch=25):
    """Ask Suno to render the WAV masters, in batches a bridge job can finish."""
    found = {}
    for i in range(0, len(ids), batch):
        chunk = ids[i:i + batch]
        script = WAV_URLS.replace("IDS", json.dumps(chunk))
        for row in fetch_clips(script):
            found[row["id"]] = row["url"]
        print(f"  wav urls: {len(found)}/{len(ids)}")
    return found


def fold(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode()
    return s.lower().replace("’", "'")


def slugify(t):
    t = fold(t).replace("&", " and ")
    t = re.sub(r"['`]", "", t)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def band_index():
    """(stem -> band) for filename matches, and (band, stem) -> lyric text for content matches."""
    stems, lyrics = {}, {}
    for template in REPO.glob("*/template.md"):
        band = template.parent.name
        for f in template.parent.glob("*.txt"):
            if f.name.endswith((".style.txt", ".stand.txt")):
                continue
            stems[f.stem] = band
            lyrics[(band, f.stem)] = fold(f.read_text(errors="ignore"))
    return stems, lyrics


def resolve_band(title, stems, lyrics):
    slug = slugify(title)
    if slug in stems:
        return stems[slug], slug
    needle = fold(title).strip()
    if needle:
        hits = {b for (b, stem), text in lyrics.items() if needle in text}
        if len(hits) == 1:
            return hits.pop(), slug
    return "unsorted", slug


def folder_for(clip, filed, stems, lyrics):
    """Your filing wins; where you haven't filed, fall back to matching the lyrics."""
    project = filed.get(clip["id"])
    if project:
        return PROJECT_FOLDER.get(project) or slugify(project)
    return resolve_band(clip["title"], stems, lyrics)[0]


def existing_by_clip():
    """clip-id prefix -> an existing wav, so a track already on disk is linked, not refetched."""
    found = {}
    for f in AUDIO.rglob("*--*.wav"):
        found.setdefault(f.stem.rsplit("--", 1)[-1], f)
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--prune", action="store_true",
                    help="move files whose project changed, instead of leaving a copy behind")
    ap.add_argument("--playlists", action="store_true",
                    help="organise by your Suno playlists, keeping their running order")
    args = ap.parse_args()

    if args.playlists:
        rows = fetch_clips(PLAYLISTS)
        wanted = [r for r in rows if r["audio_url"] and r["status"] == "complete"]
        targets = [(r, AUDIO / "playlists" / slugify(r["playlist"]) /
                    f"{int(r['index']):02d}-{slugify(r['title']) or 'untitled'}--{r['id'][:8]}.wav")
                   for r in wanted]
    else:
        stems, lyrics = band_index()
        filed = {r["id"]: r["project"] for r in fetch_clips(PROJECTS)}
        rows = fetch_clips()
        wanted = [r for r in rows if r["audio_url"] and r["status"] == "complete"]
        targets = [(r, AUDIO / folder_for(r, filed, stems, lyrics) /
                    f"{slugify(r['title']) or 'untitled'}--{r['id'][:8]}.wav")
                   for r in wanted]

    titles_path = AUDIO / "titles.json"
    AUDIO.mkdir(exist_ok=True)
    titles = json.loads(titles_path.read_text()) if titles_path.exists() else {}
    titles.update({r["id"][:8]: r["title"] for r in wanted if r.get("title")})
    titles_path.write_text(json.dumps(titles, indent=1, ensure_ascii=False))

    pool = existing_by_clip()
    have_master = masters()
    plan, skipped, linked, upgrades = [], 0, 0, 0
    for c, dest in targets:
        # Anything fetched down the old mp3 path is worth replacing, even though
        # a file is sitting there.
        if c["id"] not in have_master:
            plan.append((c, dest))
            if dest.exists():
                upgrades += 1
            continue
        if dest.exists():
            skipped += 1
            continue
        src = pool.get(c["id"][:8])
        if src and args.dry_run:
            linked += 1
        elif src:
            dest.parent.mkdir(parents=True, exist_ok=True)
            try:
                os.link(src, dest)          # same content, no second copy on disk
            except OSError:
                shutil.copy2(src, dest)
            linked += 1
        else:
            plan.append((c, dest))
    if linked:
        print(f"{linked} linked from audio already on disk")

    if args.prune:
        correct = {c["id"][:8]: dest for c, dest in targets}
        for stale in sorted(AUDIO.rglob("*--*.wav")):
            if stale.relative_to(AUDIO).parts[0] in DERIVED:
                continue
            dest = correct.get(stale.stem.rsplit("--", 1)[-1])
            if not dest or stale == dest:
                continue
            print(f"  refiled: {stale.relative_to(AUDIO)} -> {dest.relative_to(AUDIO)}")
            if args.dry_run:
                continue
            if dest.exists():
                stale.unlink()          # already linked across; this one is the duplicate
            else:
                dest.parent.mkdir(parents=True, exist_ok=True)
                stale.rename(dest)

    print(f"{len(rows)} clips; {len(wanted)} selected; {skipped} already local; "
          f"{len(plan)} to fetch ({upgrades} replacing mp3-sourced files)")
    if args.dry_run:
        for c, dest in plan:
            print(f"  {dest.relative_to(REPO)}   <- {c['title']}")
        return

    print("asking Suno to render WAV masters...")
    urls = wav_urls([c["id"] for c, _ in plan])
    missing = [c["title"] for c, _ in plan if c["id"] not in urls]
    if missing:
        print(f"{len(missing)} produced no WAV and are skipped: {', '.join(missing[:5])}",
              file=sys.stderr)
    plan = [(c, dest) for c, dest in plan if c["id"] in urls]

    for i, (c, dest) in enumerate(plan, 1):
        dest.parent.mkdir(parents=True, exist_ok=True)
        tmp_mp3 = dest.with_suffix(".src.part")
        tmp_wav = dest.with_suffix(".wav.part")
        print(f"[{i}/{len(plan)}] {c['title']} -> {dest.relative_to(REPO)}")
        try:
            urllib.request.urlretrieve(urls[c["id"]], tmp_mp3)
            subprocess.run(
                # -f wav is required: ffmpeg picks the muxer from the extension, and
                # the .part suffix tells it nothing.
                ["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-i", str(tmp_mp3),
                 "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le", "-f", "wav", str(tmp_wav)],
                check=True)
            # Rename only once complete, so an interrupted run leaves no half file
            # that a later run would mistake for done.
            tmp_wav.rename(dest)
            mark_master(c["id"])
        except Exception as e:
            print(f"    failed: {e}", file=sys.stderr)
            tmp_wav.unlink(missing_ok=True)
        finally:
            tmp_mp3.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
