#!/usr/bin/env python3
"""Watch the Suno tab for transient UI — toasts, challenges, dialogs, forms.

Usage:
  tools/suno-watch.py            # install the watcher (idempotent), then dump
  tools/suno-watch.py --dump     # just show what has been captured
  tools/suno-watch.py --clear    # reset the buffer
  tools/suno-watch.py --all      # include the noisy page-text diffs

Why this exists: the API lies by omission. A moderation kill returns
200 + "submitted" and then deletes the clips; a Cloudflare challenge shows the
same 200 on /api/c/check whether or not it fired. Both announce themselves only
in UI that appears and disappears before anything asks the page about it. This
records those moments as they happen, so a failed Create can be diagnosed from
what the screen actually said instead of guessed at.

Install it BEFORE pressing Create. It lives in the page, so a hard reload wipes
it — re-run then. Soft navigation is fine.
"""

import argparse
import json
import sys
import urllib.request

BROKER = "https://dw.ramsden-international.com/bridge"
TOKEN = "BRIDGE"
JOB_TIMEOUT_MS = 30_000

INSTALL = r"""
if (window.__sunoWatch) return 'already installed; ' + window.__sunoWatch.events.length + ' events';

const W = window.__sunoWatch = {events: [], seenText: new Set()};
const push = (kind, text, extra) => {
  const t = (text || '').trim();
  if (!t && kind === 'text') return;
  W.events.push(Object.assign({kind, text: t.slice(0, 300), at: new Date().toISOString()}, extra || {}));
  if (W.events.length > 500) W.events.splice(0, 200);
};

// Seed the current page text so the diff reports only what appears from now on.
(document.body.innerText || '').split('\n').forEach(l => W.seenText.add(l.trim()));

// Transient nodes: challenge iframes, dialogs, forms. React mounts these empty
// and fills them a tick later, so read on a delay rather than at insertion.
W.observer = new MutationObserver(muts => {
  for (const m of muts) for (const n of m.addedNodes) {
    if (n.nodeType !== 1) continue;
    setTimeout(() => {
      try {
        const frames = n.matches?.('iframe') ? [n] : [...(n.querySelectorAll?.('iframe') || [])];
        for (const f of frames) {
          if (/turnstile|challenges\.cloudflare|recaptcha|hcaptcha/i.test(f.src || '')) {
            push('challenge', f.src, {visible: f.offsetParent !== null});
          }
        }
        const dialogs = n.matches?.('[role="dialog"],[role="alertdialog"]') ? [n]
                      : [...(n.querySelectorAll?.('[role="dialog"],[role="alertdialog"]') || [])];
        for (const d of dialogs) push('dialog', d.innerText);
        const forms = n.matches?.('form') ? [n] : [...(n.querySelectorAll?.('form') || [])];
        for (const f of forms) {
          const fields = [...f.querySelectorAll('input,textarea,select')]
            .map(e => e.getAttribute('name') || e.getAttribute('placeholder') || e.type).filter(Boolean);
          push('form', f.innerText, {fields: fields.slice(0, 12)});
        }
        const live = n.matches?.('[role="status"],[role="alert"],[aria-live]') ? [n]
                   : [...(n.querySelectorAll?.('[role="status"],[role="alert"],[aria-live]') || [])];
        for (const e of live) push('toast', e.innerText);
      } catch (e) { /* a node vanished mid-inspection; nothing to record */ }
    }, 120);
  }
});
W.observer.observe(document.body, {childList: true, subtree: true});

// Catch-all: any line of page text that was not there before. Noisy, but it is
// what caught the moderation wording when nothing else did.
W.poll = setInterval(() => {
  for (const line of (document.body.innerText || '').split('\n')) {
    const l = line.trim();
    if (l && l.length < 200 && !W.seenText.has(l)) { W.seenText.add(l); push('text', l); }
  }
}, 250);

return 'watcher installed';
"""

DUMP = r"""
const W = window.__sunoWatch;
if (!W) return JSON.stringify({installed: false, events: []});
return JSON.stringify({installed: true, events: W.events});
"""

CLEAR = r"""
if (!window.__sunoWatch) return 'not installed';
window.__sunoWatch.events = [];
return 'cleared';
"""

# Anything matching these is worth surfacing without --all.
INTERESTING = ("challenge", "dialog", "form", "toast")
KEYWORDS = ("violat", "producer", "copyright", "moderat", "not allowed", "fail",
            "error", "unable", "cannot", "flag", "verify", "human", "try again",
            "limit", "credit")


def run(script):
    req = urllib.request.Request(
        BROKER + "/workers", headers={"Authorization": "Bearer " + TOKEN})
    with urllib.request.urlopen(req, timeout=20) as r:
        workers = json.load(r)["workers"]
    worker = next((w["connectionId"] for w in workers if w.get("host") == "suno.com"), None)
    if not worker:
        sys.exit("No suno.com tab connected to the bridge.")
    body = json.dumps({"target": worker, "timeout": JOB_TIMEOUT_MS, "script": script}).encode()
    req = urllib.request.Request(
        BROKER + "/jobs/sync", data=body,
        headers={"Authorization": "Bearer " + TOKEN, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=JOB_TIMEOUT_MS / 1000 + 15) as r:
        job = json.load(r)
    if job.get("status") != "done":
        sys.exit(f"Bridge job {job.get('status')}: {job.get('error')}")
    return job["result"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dump", action="store_true")
    ap.add_argument("--clear", action="store_true")
    ap.add_argument("--all", action="store_true", help="include routine page-text churn")
    args = ap.parse_args()

    if args.clear:
        print(run(CLEAR))
        return
    if not args.dump:
        print(run(INSTALL))

    data = json.loads(run(DUMP))
    if not data["installed"]:
        sys.exit("Watcher not installed — run without --dump first.")

    events = data["events"]
    if not args.all:
        events = [e for e in events
                  if e["kind"] in INTERESTING
                  or any(k in e["text"].lower() for k in KEYWORDS)]
    if not events:
        print(f"nothing notable ({len(data['events'])} raw events)")
        return
    for e in events:
        stamp = e["at"][11:19]
        extra = ""
        if e.get("fields"):
            extra = "  fields=" + ",".join(e["fields"])
        if "visible" in e:
            extra = f"  visible={e['visible']}"
        print(f"{stamp}  {e['kind']:9} {e['text'][:120]}{extra}")


if __name__ == "__main__":
    main()
