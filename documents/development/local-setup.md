# Local setup

```bash
make local-up     # start API, search service, Postgres, Redis
make test         # run API and search tests
make test-unit    # tests/unit (pytest + vitest)
make test-integration
make test-e2e     # needs `make local-up`
make local-down   # stop and remove volumes
```

Ports: API 3000, search 8000, Postgres 5432, Redis 6379.
