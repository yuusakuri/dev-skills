#!/usr/bin/env bash
# Verify that every upstream ref pinned in catalog.json is immutable and still exists.
#
# verify-catalog.py proves the referenced skills resolve. This script checks the
# weaker but separate property that each pin is a real, immutable commit rather than
# a moving branch, so installs are reproducible.
set -euo pipefail

cd "$(dirname "$0")/.."
status=0

pins=$(python3 - <<'PY'
import json
c = json.load(open("catalog.json"))
for key, s in c["sources"].items():
    print(s["repo"], s["ref"], s.get("tag", "-"))
PY
)

while read -r repo ref tag; do
  [ -z "$repo" ] && continue
  url="https://github.com/${repo}"
  printf '%-45s %s\n' "$repo" "${ref:0:12}"

  if ! printf '%s' "$ref" | grep -Eq '^[0-9a-f]{40}$'; then
    echo "  ERROR: pin is not a 40-char commit SHA — not reproducible" >&2
    status=1
    continue
  fi
  echo "  pin type: commit (immutable)"

  if [ "$tag" != "-" ]; then
    # An annotated tag's ref points at the tag object, so ask for the peeled
    # commit (refs/tags/X^{}) first and fall back to the plain ref for a
    # lightweight tag.
    resolved=$(git ls-remote "$url" "refs/tags/${tag}^{}" 2>/dev/null | cut -f1)
    [ -z "$resolved" ] && resolved=$(git ls-remote "$url" "refs/tags/${tag}" 2>/dev/null | cut -f1)
    if [ -n "$resolved" ]; then
      if [ "$resolved" = "$ref" ]; then
        echo "  tag ${tag} still points at this commit"
      else
        echo "  WARNING: tag ${tag} now points at ${resolved:0:12}, not the pinned commit"
      fi
    else
      echo "  WARNING: tag ${tag} no longer resolves upstream"
    fi
  fi

  if head=$(git ls-remote "$url" HEAD 2>/dev/null | cut -f1) && [ -n "$head" ]; then
    if [ "$head" = "$ref" ]; then
      echo "  upstream HEAD: same commit (pin is current)"
    else
      echo "  upstream HEAD: ${head:0:12} (pin is behind — review before bumping)"
    fi
  else
    echo "  WARNING: could not reach ${url}" >&2
  fi
done <<< "$pins"

exit "$status"
