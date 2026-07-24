#!/bin/bash
# check.sh — deterministic pre-save trope check (write-song step 5, mechanical layer).
#
# Usage: check.sh <draft.txt>
#
# Greps the draft against every pattern in banned-patterns.tsv (case-insensitive ERE).
#   BAN hit   -> the draft must change. Exit 1.
#   WATCH hit -> allowed only with a stated, song-specific justification. Exit 0, but listed.
#
# This is the mechanical layer only: a clean run proves nothing about constructions-with-slots
# or imagery motifs — those still need the fuzzy read of library.md (Constructions + Imagery).
# Run against NEW drafts before saving; existing catalog songs are the *sources* of these
# patterns and will of course hit their own entries.

DIR="$(cd "$(dirname "$0")" && pwd)"
PATTERNS="$DIR/banned-patterns.tsv"
DRAFT="$1"

[ -f "$DRAFT" ] || { echo "usage: check.sh <draft.txt>" >&2; exit 2; }
[ -f "$PATTERNS" ] || { echo "missing $PATTERNS" >&2; exit 2; }

ban_hits=0
watch_hits=0

while IFS=$'\t' read -r severity pattern note; do
  case "$severity" in ''|'#'*) continue ;; esac
  matches=$(grep -inE "$pattern" "$DRAFT")
  if [ -n "$matches" ]; then
    if [ "$severity" = "BAN" ]; then
      ban_hits=$((ban_hits + 1))
      echo "BAN   [$note]"
    else
      watch_hits=$((watch_hits + 1))
      echo "WATCH [$note]"
    fi
    echo "      pattern: $pattern"
    echo "$matches" | sed 's/^/      line /'
  fi
done < "$PATTERNS"

echo ""
if [ "$ban_hits" -gt 0 ]; then
  echo "FAIL: $ban_hits banned pattern(s) hit — the draft changes, not the library."
  exit 1
elif [ "$watch_hits" -gt 0 ]; then
  echo "PASS with $watch_hits watch hit(s) — each needs a stated, song-specific justification."
  exit 0
else
  echo "CLEAN: no mechanical hits. (Fuzzy check of Constructions + Imagery still required.)"
  exit 0
fi
