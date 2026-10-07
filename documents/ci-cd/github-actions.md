# GitHub Actions

- `ci.yml`: lint, critical unit, integration and coverage-floor gate, Docker builds; e2e only on PRs labeled `critical`; reports uploaded as artifacts, summarized in a sticky PR comment and committed to `tests/*/testrpts/` on `main` (`[skip ci]`)
- `nightly.yml`: noncritical tests and e2e (informational, no coverage gate)
- `pr-links.yml`: validates every PR; injects `REQ-0009` into bot-authored PRs and verifies `security-scan` passed
- `pr-links.yml`: requires #issue/REQ/ADR references in PRs and posts a requirement→test table
- `adr-validate.yml`: ADR structure and requirement traceability
- `security-scan.yml`: npm audit and pip-audit (weekly and on PRs)
- `deploy-preview.yml`, `deploy-aws.yml`: placeholders to implement
- `release.yml`: manual release placeholder

Dependabot (`.github/dependabot.yml`) opens weekly update PRs.
