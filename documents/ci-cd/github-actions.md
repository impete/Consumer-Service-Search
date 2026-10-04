# GitHub Actions

- `ci.yml`: lint, unit, integration (redis/postgres services), e2e (docker compose), Docker builds; JUnit/coverage reports uploaded as artifacts
- `pr-links.yml`: requires #issue/REQ/ADR references in PRs and posts a requirement→test table
- `adr-validate.yml`: ADR structure and requirement traceability
- `security-scan.yml`: npm audit and pip-audit (weekly and on PRs)
- `deploy-preview.yml`, `deploy-aws.yml`: placeholders to implement
- `release.yml`: manual release placeholder

Dependabot (`.github/dependabot.yml`) opens weekly update PRs.
