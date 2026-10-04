# Test PR for deploy-preview workflow

This is a test pull request to verify the deploy-preview workflow triggers correctly and runs the smoke test.

## Changes
- Added this file to test the workflow

## Testing
- [ ] Smoke test passes (docker compose build and /health checks)
- [ ] PR comment appears with test results
- [ ] AWS preview job skipped (expected, AWS_PREVIEW_ENABLED not set)
