.PHONY: local-up local-down lint test test-api test-search logs
local-up:
	docker compose up --build -d
local-down:
	docker compose down -v
lint:
	npm --prefix apps/api run lint && black --check apps/search-service
test: test-api test-search
test-api:
	npm --prefix apps/api test
test-search:
	pytest apps/search-service/tests -q
logs:
	docker compose logs -f
