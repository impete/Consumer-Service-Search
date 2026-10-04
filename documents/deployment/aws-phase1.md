# AWS phase 1

- Region us-east-1; ECS clusters for staging and production
- PostgreSQL on RDS (Multi-AZ in production), Redis on ElastiCache, ALB in front
- Credentials via GitHub OIDC or Secrets; limit DB/cache access to app security groups
- Deploy steps: build images, push to a registry, update ECS task definitions, health check, roll back if needed
