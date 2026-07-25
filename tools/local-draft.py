#!/usr/bin/env python3
"""Generate lyric drafts with a local model via text-generation-webui's OpenAI API.

Usage:
  tools/local-draft.py <band-folder> "<theme>" [-n N] [--port 5005]
  tools/local-draft.py --stop

Starts the webui headless on first use (freeing ComfyUI's VRAM first); --stop
kills it so ComfyUI can reclaim the card. Drafts land in drafts/<band>/.
"""

import argparse
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
WEBUI = Path.home() / "text-generation-webui"
PYTHON = WEBUI / "installer_files/env/bin/python"
MODEL = "EVA-Qwen2.5-32B-v0.2-Q4_K_M.gguf"
COMFY_FREE_URL = "http://10.99.0.3:8188/free"
API_HOST = "10.99.0.3"  # webui binds the API to the LAN IP, not loopback
LOG_FILE = WEBUI / "user_data/api-server.log"
NEEDED_FREE_MIB = 21500  # ~19.9 GB weights + 16k q8_0 KV cache + buffers
LOAD_TIMEOUT_S = 360

SYSTEM_FRAME = (
    "You are the sole lyricist for the band specified below. Write one complete, "
    "original song lyric that follows the band spec: its persona, voice, structure "
    "and devices. Output only the lyric, with section headers in square brackets "
    "(e.g. [Verse 1], [Chorus]). No commentary before or after.\n\n"
    "=== BAND SPEC ===\n"
)


def api(port, path, payload=None, timeout=30):
    req = urllib.request.Request(
        f"http://{API_HOST}:{port}{path}",
        data=json.dumps(payload).encode() if payload is not None else None,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read())


def api_up(port):
    try:
        api(port, "/v1/models")
        return True
    except (urllib.error.URLError, OSError):
        return False


def free_mib():
    out = subprocess.run(
        ["nvidia-smi", "--query-gpu=memory.free", "--format=csv,noheader,nounits"],
        capture_output=True, text=True, check=True,
    ).stdout
    return int(out.split()[0])


def free_comfyui_vram():
    req = urllib.request.Request(
        COMFY_FREE_URL,
        data=json.dumps({"unload_models": True, "free_memory": True}).encode(),
        headers={"Content-Type": "application/json"},
    )
    try:
        urllib.request.urlopen(req, timeout=15).read()
    except (urllib.error.URLError, OSError) as e:
        print(f"warning: could not reach ComfyUI to free VRAM ({e})")


def ensure_server(port):
    if api_up(port):
        return
    print("Server not running; freeing ComfyUI VRAM...")
    free_comfyui_vram()
    for _ in range(30):
        if free_mib() >= NEEDED_FREE_MIB:
            break
        time.sleep(2)
    else:
        sys.exit(f"error: only {free_mib()} MiB free after 60s; need {NEEDED_FREE_MIB}. "
                 "Something else is holding the card (nvidia-smi will say who).")

    print(f"Starting {MODEL} on port {port} (log: {LOG_FILE})...")
    log = open(LOG_FILE, "ab")
    subprocess.Popen(
        [str(PYTHON), "server.py", "--api", "--nowebui",
         "--api-port", str(port), "--model", MODEL,
         "--ctx-size", "16384", "--cache-type", "q8_0"],
        cwd=WEBUI, stdout=log, stderr=subprocess.STDOUT,
        start_new_session=True,
    )
    deadline = time.time() + LOAD_TIMEOUT_S
    while time.time() < deadline:
        if api_up(port):
            print("Server up.")
            return
        time.sleep(5)
    sys.exit(f"error: API not up after {LOAD_TIMEOUT_S}s — check {LOG_FILE}")


def stop_server(port):
    r = subprocess.run(["pkill", "-f", f"server.py --api --nowebui --api-port {port}"])
    print("Server stopped." if r.returncode == 0 else "No server was running.")


def slugify(text):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]", "-", text.lower())).strip("-")[:60]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("band", nargs="?", help="band folder name, e.g. guessed")
    p.add_argument("theme", nargs="?", help="theme / prompt for the song")
    p.add_argument("-n", type=int, default=3, help="number of drafts (default 3)")
    p.add_argument("--port", type=int, default=5005)
    p.add_argument("--stop", action="store_true", help="stop the API server and exit")
    args = p.parse_args()

    if args.stop:
        stop_server(args.port)
        return
    if not args.band or not args.theme:
        p.error("band and theme are required (or use --stop)")

    template = REPO / args.band / "template.md"
    if not template.exists():
        bands = sorted(d.name for d in REPO.iterdir() if (d / "template.md").exists())
        sys.exit(f"error: no {template}. Bands: {', '.join(bands)}")

    ensure_server(args.port)

    out_dir = REPO / "drafts" / args.band
    out_dir.mkdir(parents=True, exist_ok=True)
    slug = slugify(args.theme)
    existing = len(list(out_dir.glob(f"{slug}-eva32b-*.txt")))

    system = SYSTEM_FRAME + template.read_text()
    for i in range(existing + 1, existing + args.n + 1):
        print(f"Draft {i - existing}/{args.n}...", flush=True)
        resp = api(args.port, "/v1/chat/completions", {
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": f"Write a song about: {args.theme}"},
            ],
            "temperature": 1.0,
            "min_p": 0.05,
            "max_tokens": 1500,
        }, timeout=600)
        text = resp["choices"][0]["message"]["content"].strip() + "\n"
        out = out_dir / f"{slug}-eva32b-{i}.txt"
        out.write_text(text)
        print(f"  -> {out.relative_to(REPO)}")


if __name__ == "__main__":
    main()
