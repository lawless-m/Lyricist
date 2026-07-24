#!/bin/bash
# check.sh — deterministic pre-save trope check (write-song step 5, mechanical layer).
#
# Usage: check.sh <draft.txt>
#
# Greps the draft against every pattern in banned-patterns.tsv (case-insensitive ERE).
#   PERM hit   -> calcified house-style device; the draft must change. Never decays. Exit 1.
#   BAN hit    -> the draft must change — unless the entry has cooled. Exit 1.
#   COOLED hit -> a BAN whose last use is >= TROPE_COOL_THRESHOLD songs back (songs-since,
#                 catalogue-wide count; default 60). Treated as WATCH. Exit 0, but listed.
#   WATCH hit  -> allowed only with a stated, song-specific justification. Exit 0, but listed.
#
# Decay model (refactor step 3): fatigue is measured in songs written since last use, not
# elapsed time. LOGGED_AT in the TSV is the catalog song-count at the device's last use;
# cooling happens when (current catalog - LOGGED_AT) >= threshold. PERM entries never cool.
#
# This is the mechanical layer only: a clean run proves nothing about constructions-with-slots
# or imagery motifs — those still need the fuzzy read of library.md (Constructions + Imagery).
# Run against NEW drafts before saving; existing catalog songs are the *sources* of these
# patterns and will of course hit their own entries.

DIR="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$DIR/../.." && pwd)"
PATTERNS="$DIR/banned-patterns.tsv"
DRAFT="$1"
THRESHOLD="${TROPE_COOL_THRESHOLD:-60}"

[ -f "$DRAFT" ] || { echo "usage: check.sh <draft.txt>" >&2; exit 2; }
[ -f "$PATTERNS" ] || { echo "missing $PATTERNS" >&2; exit 2; }

# Current catalogue-wide song count (lyric files only, not style/stand sidecars).
catalog=0
for d in guessed laundry lucy-might purple-dog the-bell-knows-my-name coase-guard ultracoase; do
  n=$(ls "$REPO/$d"/*.txt 2>/dev/null | grep -vc -e '\.style\.txt' -e '\.stand\.txt')
  catalog=$((catalog + n))
done

hard_hits=0
soft_hits=0

while IFS=$'\t' read -r severity logged_at pattern note; do
  case "$severity" in ''|'#'*) continue ;; esac
  matches=$(grep -inE "$pattern" "$DRAFT")
  [ -z "$matches" ] && continue

  label="$severity"
  if [ "$severity" = "BAN" ] && [ "$logged_at" != "-" ]; then
    since=$((catalog - logged_at))
    if [ "$since" -ge "$THRESHOLD" ]; then
      label="COOLED"
    fi
  fi

  case "$label" in
    PERM|BAN) hard_hits=$((hard_hits + 1)) ;;
    *)        soft_hits=$((soft_hits + 1)) ;;
  esac

  echo "$label [$note]"
  echo "      pattern: $pattern"
  echo "$matches" | sed 's/^/      line /'
done < "$PATTERNS"

echo ""
echo "(catalog: $catalog songs; cooling threshold: $THRESHOLD songs-since)"
if [ "$hard_hits" -gt 0 ]; then
  echo "FAIL: $hard_hits banned pattern(s) hit — the draft changes, not the library."
  exit 1
elif [ "$soft_hits" -gt 0 ]; then
  echo "PASS with $soft_hits watch/cooled hit(s) — each needs a stated, song-specific justification."
  exit 0
else
  echo "CLEAN: no mechanical hits. (Fuzzy check of Constructions + Imagery still required.)"
  exit 0
fi
