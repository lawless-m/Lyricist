#!/usr/bin/env python3
"""Snapshot Suno play/like/publish counts for the whole library.

Usage:
  tools/suno-stats.py            # write today's snapshot + print totals
  tools/suno-stats.py --print    # print totals only, write nothing

Reads the library through a logged-in suno.com tab connected to the Browser
Bridge (see the Suno-Automation skill) — the studio-api needs a Clerk session
token, so there is no way to do this from curl alone. Open suno.com, load the
bridge client, then run this.

Snapshots land in stats/suno-YYYY-MM-DD.jsonl, one JSON object per clip, so
re-running on later dates gives a time series to diff.
"""

import argparse
import json
import subprocess
import sys
import urllib.request
from collections import defaultdict
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
STATS_DIR = REPO / "stats"
BROKER = "https://dw.ramsden-international.com/bridge"
TOKEN = "BRIDGE"
JOB_TIMEOUT_MS = 180_000

# Paginates the feed, backing off on the 429 that a straight run reliably hits
# around page 12. Returns JSONL so a 300-clip library stays one manageable blob.
SCRIPT = r"""
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
  is_public: !!c.is_public, plays: c.play_count || 0, likes: c.upvote_count || 0,
  comments: c.comment_count || 0, model: c.model_name || null
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


def suno_worker():
    for w in api("/workers")["workers"]:
        if w.get("host") == "suno.com":
            return w["connectionId"]
    sys.exit("No suno.com tab connected to the bridge — open suno.com and load the bridge client.")


def fetch_clips():
    job = api("/jobs/sync", {"target": suno_worker(), "timeout": JOB_TIMEOUT_MS, "script": SCRIPT})
    if job.get("status") != "done":
        sys.exit(f"Bridge job {job.get('status')}: {job.get('error')}")
    out = job["result"] or ""
    if out.startswith("ERROR"):
        sys.exit(out)
    return [json.loads(line) for line in out.splitlines() if line.strip()]


def summarise(clips):
    by_title = defaultdict(lambda: {"clips": 0, "plays": 0, "likes": 0})
    for c in clips:
        t = by_title[c["title"] or "(untitled)"]
        t["clips"] += 1
        t["plays"] += c["plays"]
        t["likes"] += c["likes"]
    print(f"clips      {len(clips)}  ({len(by_title)} distinct titles)")
    print(f"plays      {sum(c['plays'] for c in clips)}")
    print(f"likes      {sum(c['likes'] for c in clips)}")
    print(f"comments   {sum(c['comments'] for c in clips)}")
    print(f"published  {sum(1 for c in clips if c['is_public'])}")
    print("\nmost played:")
    top = sorted(by_title.items(), key=lambda kv: (-kv[1]["plays"], kv[0]))[:10]
    for title, t in top:
        print(f"  {t['plays']:5}  {t['likes']:3} likes   {title}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--print", action="store_true", dest="print_only",
                    help="print totals without writing a snapshot")
    args = ap.parse_args()

    clips = fetch_clips()
    if not args.print_only:
        STATS_DIR.mkdir(exist_ok=True)
        path = STATS_DIR / f"suno-{date.today():%Y-%m-%d}.jsonl"
        path.write_text("".join(json.dumps(c) + "\n" for c in clips))
        print(f"wrote {path.relative_to(REPO)} ({len(clips)} clips)\n")
    summarise(clips)


if __name__ == "__main__":
    main()
