#!/usr/bin/env python3
"""Mirror liked Suno tracks to local WAVs, sorted by band.

Usage:
  tools/suno-download.py              # sync new liked tracks
  tools/suno-download.py --dry-run    # list what would be fetched
  tools/suno-download.py --all        # not just liked ones

Only tracks you have clicked LIKE on are fetched by default. Existing files are
left alone, so re-running only pulls what's new — safe to run any time.

Audio lands in audio/<band>/<slug>--<clipid>.wav. Band is resolved from the repo
lyric files: first by matching the Suno title to a filename, then by looking for
the title inside a lyric (many titles are the hook line, not the filename —
"Act Like It's News" is guessed/four-minute-fix). Anything unresolved, including
the non-band personal songs, goes to audio/unsorted/.

WAV because this feeds the mixing tools; Suno serves mp3, so ffmpeg converts.
Reckon on ~30 MB per track.
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


def existing_by_clip():
    """clip-id prefix -> an existing wav, so a track already on disk is linked, not refetched."""
    found = {}
    for f in AUDIO.rglob("*--*.wav"):
        found.setdefault(f.stem.rsplit("--", 1)[-1], f)
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--all", action="store_true", help="include tracks you haven't liked")
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
        rows = fetch_clips()
        wanted = [r for r in rows
                  if r["audio_url"] and r["status"] == "complete" and (args.all or r["liked"])]
        targets = [(r, AUDIO / resolve_band(r["title"], stems, lyrics)[0] /
                    f"{slugify(r['title']) or 'untitled'}--{r['id'][:8]}.wav")
                   for r in wanted]

    titles_path = AUDIO / "titles.json"
    AUDIO.mkdir(exist_ok=True)
    titles = json.loads(titles_path.read_text()) if titles_path.exists() else {}
    titles.update({r["id"][:8]: r["title"] for r in wanted if r.get("title")})
    titles_path.write_text(json.dumps(titles, indent=1, ensure_ascii=False))

    pool = existing_by_clip()
    plan, skipped, linked = [], 0, 0
    for c, dest in targets:
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

    print(f"{len(rows)} clips; {len(wanted)} selected; "
          f"{skipped} already local; {len(plan)} to fetch")
    if args.dry_run:
        for c, dest in plan:
            print(f"  {dest.relative_to(REPO)}   <- {c['title']}")
        return

    for i, (c, dest) in enumerate(plan, 1):
        dest.parent.mkdir(parents=True, exist_ok=True)
        tmp_mp3 = dest.with_suffix(".mp3.part")
        tmp_wav = dest.with_suffix(".wav.part")
        print(f"[{i}/{len(plan)}] {c['title']} -> {dest.relative_to(REPO)}")
        try:
            urllib.request.urlretrieve(c["audio_url"], tmp_mp3)
            subprocess.run(
                # -f wav is required: ffmpeg picks the muxer from the extension, and
                # the .part suffix tells it nothing.
                ["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-i", str(tmp_mp3),
                 "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le", "-f", "wav", str(tmp_wav)],
                check=True)
            # Rename only once complete, so an interrupted run leaves no half file
            # that a later run would mistake for done.
            tmp_wav.rename(dest)
        except Exception as e:
            print(f"    failed: {e}", file=sys.stderr)
            tmp_wav.unlink(missing_ok=True)
        finally:
            tmp_mp3.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
