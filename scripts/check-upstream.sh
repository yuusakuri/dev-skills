#!/usr/bin/env bash
# Verify that the upstream refs pinned in .claude-plugin/marketplace.json still
# resolve, and report whether each upstream has moved ahead of the pin.
#
# This repository composes upstream skill collections rather than vendoring them,
# so a pin that no longer resolves means installs are broken. Run this in CI and
# before bumping a pin.
set -euo pipefail

cd "$(dirname "$0")/.."
MANIFEST=".claude-plugin/marketplace.json"
status=0

# Emit "<repo> <ref>" for every github-sourced plugin entry.
pins=$(python3 - "$MANIFEST" <<'PY'
import json, sys
for p in json.load(open(sys.argv[1]))["plugins"]:
    src = p.get("source")
    if isinstance(src, dict) and src.get("source") == "github":
        print(src["repo"], src.get("ref", "HEAD"))
PY
)

if [ -z "$pins" ]; then
  echo "No github-pinned upstreams found in $MANIFEST" >&2
  exit 1
fi

while read -r repo ref; do
  [ -z "$repo" ] && continue
  url="https://github.com/${repo}"
  printf '%-24s pinned at %s\n' "$repo" "$ref"

  # A 40-char hex ref is a commit; anything else is a tag or branch we can resolve.
  if printf '%s' "$ref" | grep -Eq '^[0-9a-f]{40}$'; then
    echo "  pin type: commit (immutable)"
  elif git ls-remote --exit-code "$url" "refs/tags/${ref}" >/dev/null 2>&1; then
    echo "  pin type: tag — resolves"
  elif git ls-remote --exit-code "$url" "refs/heads/${ref}" >/dev/null 2>&1; then
    echo "  pin type: branch — MUTABLE; prefer a tag or commit for reproducible installs"
    status=1
  else
    echo "  ERROR: ref '${ref}' does not resolve in ${url}" >&2
    status=1
    continue
  fi

  head=$(git ls-remote "$url" HEAD 2>/dev/null | cut -f1 || true)
  if [ -n "$head" ]; then
    echo "  upstream HEAD: ${head}"
    [ "$head" = "$ref" ] && echo "  (pin is at upstream HEAD)"
  fi
done <<< "$pins"

exit "$status"
