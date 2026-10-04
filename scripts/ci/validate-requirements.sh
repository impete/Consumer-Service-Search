#!/usr/bin/env bash
set -euo pipefail
fail=0
for req in $(grep -rhoE 'REQ-[0-9]{4}' docs/adr | sort -u); do
  if [ ! -f "docs/requirements/$req.md" ]; then echo "Missing docs/requirements/$req.md"; fail=1; fi
done
exit $fail
