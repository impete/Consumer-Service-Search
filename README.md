# Consumer-Service-Search

Monorepo for a consumer service discovery platform (drycleaners, plumbers, restaurants, bookstores, etc.): a Node.js/TypeScript API, a Python search/recommendation service, and web and mobile clients.

## Architecture
- API: Node.js/TypeScript (Express)
- Search / ranking: Python (FastAPI)
- Web: React + Next.js; Mobile: React Native
- Data: PostgreSQL + Redis
- Deploy: Docker; AWS ECS pilot, Azure/self-hosted later

## Quick start
```bash
make local-up
make test
make logs
```

## Layout
- `apps/` api, search-service, web, mobile, admin
- `packages/` shared code
- `infra/` terraform, docker, kubernetes placeholders
- `scripts/` ADR and CI helpers
- `docs/` ADRs, requirements, design, architecture
- `documents/` CI/CD, deployment, development guides

## License
Dual licensed under Apache 2.0 or MIT. See `LICENSE`, `COPYING`, `LICENSE.MIT`.
