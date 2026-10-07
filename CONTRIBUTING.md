# Contributing

- Sign off commits (DCO): `git commit -s -m "message"`
- Open a PR using the template; link an issue or ADR
- Architecture or security changes need 2 reviews
- Changes to ADRs, security, deployment, or schema need explicit review
- Recommended branch protection on `main`: required reviews and status checks, dismiss stale reviews, up-to-date branches, no direct pushes

See `SECURITY.md` for vulnerability reporting.

## Traceability (issue → test → PR)

- Every PR references an issue (`#N`), `REQ-xxxx` or `ADR-xxxx`; `pr-links.yml` enforces it.
- Find an existing test that validates the issue and put its path in the PR template's **Test reference** field; add a test if none exists.
- Slow or service-dependent tests are marked `@pytest.mark.noncritical` (Vitest: `@noncritical` in the test name) and run nightly (`nightly.yml`). E2E runs on PRs labeled `critical` and nightly.
- Coverage may not drop below `tests/coverage-floor.json`; on merge to `main` a bot raises the floor 1% (toward 70%).
- Test reports are written to `tests/<suite>/testrpts/`; the bot commits them on `main` only.

See `AGENTS.md` for the agent workflow.
