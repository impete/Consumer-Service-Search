# Staging and preview

Each PR should get an isolated preview environment (for example pr-123.staging.<domain>) that is cleaned up when the PR closes. 

`deploy-preview.yml` always builds both images and smoke-tests `/health` (API :3000, search service :8000) with docker compose. The ECS preview job runs only when repo variable `AWS_PREVIEW_ENABLED` is `true` and the PR is not from a fork. It authenticates via GitHub OIDC (`vars.AWS_ROLE_ARN`), deploys ECS service `pr-<number>` and comments the URL; the service is deleted when the PR closes. Required variables: `AWS_ROLE_ARN`, `AWS_ECS_CLUSTER`, `AWS_ECS_TASK_FAMILY`, `AWS_ECR_REGISTRY_PREFIX`, `AWS_PREVIEW_DOMAIN`, `AWS_PREVIEW_SUBNETS`, `AWS_PREVIEW_SECURITY_GROUPS` (optional `AWS_REGION`).
