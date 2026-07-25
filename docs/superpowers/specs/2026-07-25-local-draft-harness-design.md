# Local draft harness — EVA-Qwen2.5-32B via text-generation-webui API

2026-07-25. Approved in conversation.

## Purpose

Let a local model (EVA-Qwen2.5-32B-v0.2-Q4_K_M.gguf, ~19.9 GB, on the RTX 3090) take a run at
lyric drafts for the seven bands, driven programmatically, so its output can be compared with
the normal write-song workflow. Drafts are raw material for curation — they do not enter the
catalog or the trope system unless promoted by hand.

## Approach

text-generation-webui headless (`--api --nowebui`) exposing its OpenAI-compatible endpoint on
**port 5005** (5000 is taken by pony). Rejected: raw llama-server (extra build to maintain),
Ollama import (duplicates the 20 GB GGUF into its blob store).

## Components

- `tools/local-draft.py` — the whole harness, stdlib only.
  1. **VRAM handshake**: if the API isn't already up, POST `{"unload_models": true,
     "free_memory": true}` to ComfyUI at `http://10.99.0.3:8188/free`, wait for headroom,
     then launch `server.py` with the webui's own env python:
     `--api --nowebui --api-port 5005 --model EVA-... --ctx-size 16384 --cache-type q8_0`.
     Wait until `/v1/models` answers (model load ~ a few minutes).
  2. **Draft generation**: read `<band>/template.md`, send it as the system prompt with the
     theme as the user message to `/v1/chat/completions` (ChatML template comes from
     `config-user.yaml`). Sampling tuned for a creative finetune: temperature ~1.0, min_p 0.05.
  3. **Output**: `drafts/<band>/<theme-slug>-eva32b-<n>.txt`, N drafts per run (default 3).
  4. `--stop`: kill the server so ComfyUI can have the VRAM back.

## Interface

```
tools/local-draft.py <band-folder> "<theme>" [-n N] [--port 5005]
tools/local-draft.py --stop
```

## Error handling

Fail with a clear message if the band folder/template is missing, the server doesn't come up
within the timeout, or VRAM headroom never appears. No retry logic — this is an interactive tool.

## Testing

Smoke test end to end: free VRAM, cold-start the server, generate drafts for one band,
eyeball output quality. Verify `--stop` returns the VRAM.
