#!/usr/bin/env bash
# Fails if a test references a REQ without a docs/requirements file.
# Warns for requirements that no test references yet.
set -euo pipefail
fail=0
for req in $(grep -rhoE --include='*.py' --include='*.ts' 'REQ-[0-9]{4}' tests | sort -u); do
  if [ ! -f "docs/requirements/$req.md" ]; then echo "Test references unknown $req"; fail=1; fi
done
for file in docs/requirements/REQ-*.md; do
  req=$(basename "$file" .md)
  if ! grep -rq --include='*.py' --include='*.ts' "$req" tests; then echo "::warning::$req has no linked test"; fi
done
exit $fail
