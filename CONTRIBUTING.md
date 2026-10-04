# Repository governance and contributor policy

This repository follows a small-team, ADR-first, open-source-friendly workflow. The intent is to keep architecture decisions well documented while reducing friction for contributors.

## Contributor model
This project uses a Developer Certificate of Origin (DCO) model. Contributors are expected to sign off on their commits:

```bash
git commit -s -m "Add real-time recommendation search update"
```

## Review expectations
- Most PRs require at least one review from a CODEOWNER or maintainer.
- Architecture and security-impacting changes require at least 2 reviews.
- New commits should dismiss stale review states.
- Changes affecting ADRs, security, deployment, or database schema need explicit review.

## Branch protection recommendation
On `main`, enforce:
- required pull request reviews
- required status checks
- dismiss stale reviews
- require branches to be up to date before merge
- restrict direct pushes to main

## Pull request template
Use the repository PR template and include:
- issue or ADR reference
- tests added or updated
- docs updated
- deployment or security considerations

## Reporting issues
Open an issue with the provided templates. For vulnerabilities, see `SECURITY.md`.
