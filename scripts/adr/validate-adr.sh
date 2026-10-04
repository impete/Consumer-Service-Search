#!/usr/bin/env bash
set -euo pipefail
fail=0
for f in docs/adr/ADR-*.md; do
  for s in "## Context" "## Decision" "## Consequences" "## Related requirements"; do
    if ! grep -q "^$s" "$f"; then echo "$f: missing section '$s'"; fail=1; fi
  done
done
exit $fail
