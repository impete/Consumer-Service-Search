export const config = {
  port: Number(process.env.PORT || 3000),
  databaseUrl: process.env.DATABASE_URL || "postgresql://postgres:postgres@localhost:5432/consumer_service_search",
  redisUrl: process.env.REDIS_URL || "redis://localhost:6379",
  env: process.env.NODE_ENV || "development",
};
