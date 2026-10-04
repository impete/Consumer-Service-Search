# GitHub Actions

- `ci.yml`: API lint/build/test, Python black/pytest, Docker image builds
- `adr-validate.yml`: ADR structure and requirement traceability
- `security-scan.yml`: npm audit and pip-audit (weekly and on PRs)
- `deploy-preview.yml`, `deploy-aws.yml`: placeholders to implement
- `release.yml`: manual release placeholder

Dependabot (`.github/dependabot.yml`) opens weekly update PRs.
