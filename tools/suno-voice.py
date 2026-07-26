#!/usr/bin/env python3
"""Select or clear the Suno voice (persona) on the open /create form.

Usage:
  tools/suno-voice.py                 # report which voice is applied
  tools/suno-voice.py Ultracoase      # apply that voice
  tools/suno-voice.py --off           # clear the applied voice

Ultracoase songs are meant to carry the custom "Ultracoase" voice; every other
band must not. The form remembers the last voice across generations, so check
before pressing Create rather than assuming — a leftover voice silently colours
the next band's song.

Drives a bridge-connected suno.com tab (see the Suno-Automation skill). Confirm
after the fact with metadata.persona_id on the generated clip, which is the
only ground truth.
"""

import argparse
import json
import sys
import urllib.request

BROKER = "https://dw.ramsden-international.com/bridge"
TOKEN = "BRIDGE"
JOB_TIMEOUT_MS = 30_000

# The applied voice replaces the "Add Voice" button with a chip plus a
# "Remove selected Voice" button — that button's presence is the state flag.
STATE = r"""
const btn = document.querySelector('button[aria-label="Remove selected Voice"]');
if (!btn) return JSON.stringify({applied: false, name: null});
// The remove button sits in an empty flex row; the nearest ancestor holding
// any text is the chip, and its first line is the voice name.
let p = btn, name = '';
for (let i = 0; i < 6 && p.parentElement && !name; i++) {
  p = p.parentElement;
  name = (p.innerText || '').trim().split('\n')[0];
}
return JSON.stringify({applied: true, name: name || '(unknown)'});
"""

CLEAR = r"""
const btn = document.querySelector('button[aria-label="Remove selected Voice"]');
if (!btn) return 'already-clear';
btn.click();
await new Promise(r => setTimeout(r, 1200));
return document.querySelector('button[aria-label="Remove selected Voice"]') ? 'FAILED' : 'cleared';
"""

# %s is the voice name. Clicking the card applies immediately; the dialog stays
# open for browsing, so close it explicitly afterwards.
SELECT = r"""
const sleep = ms => new Promise(r => setTimeout(r, ms));
const txt = e => (e.innerText || e.textContent || '').trim();
const WANT = %s;
const open = [...document.querySelectorAll('button[aria-label="Add Voice"]')].filter(e => e.offsetParent !== null)[0];
if (!open) {
  const cur = document.querySelector('button[aria-label="Remove selected Voice"]');
  if (cur) return 'a voice is already applied — clear it first with --off';
  return 'no Add Voice button on the page (is this /create?)';
}
open.click();
await sleep(1800);
const dlg = [...document.querySelectorAll('[role="dialog"]')].find(d => /Personas/.test(txt(d)));
if (!dlg) return 'voice picker did not open';
const card = [...dlg.querySelectorAll('div.cursor-pointer')]
  .filter(e => txt(e).toLowerCase().startsWith(WANT.toLowerCase()))[0];
if (!card) {
  const names = [...dlg.querySelectorAll('div.cursor-pointer')].map(e => txt(e).split('\n')[0]);
  dlg.querySelector('button[aria-label="Close"]')?.click();
  return 'no voice named ' + WANT + '; available: ' + JSON.stringify(names);
}
card.click();
await sleep(1500);
dlg.querySelector('button[aria-label="Close"]')?.click();
await sleep(1200);
return document.querySelector('button[aria-label="Remove selected Voice"]') ? 'applied' : 'FAILED';
"""


def api(path, body=None):
    req = urllib.request.Request(
        BROKER + path,
        data=json.dumps(body).encode() if body else None,
        headers={"Authorization": "Bearer " + TOKEN, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=JOB_TIMEOUT_MS / 1000 + 15) as r:
        return json.load(r)


def run(script):
    worker = next((w["connectionId"] for w in api("/workers")["workers"] if w.get("host") == "suno.com"), None)
    if not worker:
        sys.exit("No suno.com tab connected to the bridge — open suno.com/create and load the bridge client.")
    job = api("/jobs/sync", {"target": worker, "timeout": JOB_TIMEOUT_MS, "script": script})
    if job.get("status") != "done":
        sys.exit(f"Bridge job {job.get('status')}: {job.get('error')}")
    return job["result"]


def state():
    return json.loads(run(STATE))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("voice", nargs="?", help="voice/persona name to apply, e.g. Ultracoase")
    ap.add_argument("--off", action="store_true", help="clear the applied voice")
    args = ap.parse_args()

    if args.off:
        print(run(CLEAR))
    elif args.voice:
        if state()["applied"]:
            run(CLEAR)
        print(run(SELECT % json.dumps(args.voice)))

    s = state()
    print(f"voice: {s['name']}" if s["applied"] else "voice: none")


if __name__ == "__main__":
    main()
