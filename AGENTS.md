# Agent workflow

Applies to Copilot and any other automated agent opening PRs.

1. Read the issue and find the requirement (`docs/requirements/REQ-xxxx.md`) it relates to.
2. Find an existing test under `tests/` that validates the issue (`@pytest.mark.req("REQ-xxxx")`, `// REQ-xxxx` in Vitest files). If none exists, add one in the right suite (`tests/unit`, `tests/integration`, `tests/e2e`).
3. Open the PR with the issue (`Closes #N`), the requirement and the test path in the body (see the PR template's "Test reference" field).
4. Mark slow or service-dependent tests `@pytest.mark.noncritical` (Vitest: put `@noncritical` in the test name). They run nightly, not on every PR.
5. Keep coverage at or above `tests/coverage-floor.json`; the floor is raised automatically on merge to `main`.
6. Do not hand-edit `tests/*/testrpts/` or `tests/coverage-floor.json`; the CI bot commits them on `main` with `[skip ci]`.

Bot-authored PRs (Dependabot, Copilot) get `REQ-0009` injected into the body by `pr-links.yml`, which also verifies that `security-scan` passed.
