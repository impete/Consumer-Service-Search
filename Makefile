.PHONY: local-up local-down lint test test-api test-search test-unit test-integration test-e2e logs
local-up:
	docker compose up --build -d
local-down:
	docker compose down -v
lint:
	npm --prefix apps/api run lint && black --check apps/search-service tests
test: test-api test-search
test-api:
	npm --prefix apps/api test
test-search:
	pytest tests/unit/search_service tests/integration -q
test-unit:
	pytest tests/unit -q && npm --prefix apps/api run test:unit
test-integration:
	pytest tests/integration -q && npm --prefix apps/api run test:integration
test-e2e:
	E2E=1 pytest tests/e2e -q
logs:
	docker compose logs -f
