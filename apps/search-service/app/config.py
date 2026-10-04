from pydantic import BaseModel


class Settings(BaseModel):
    ENVIRONMENT: str = "development"
    DATABASE_URL: str = (
        "postgresql://postgres:postgres@localhost:5432/consumer_service_search"
    )
    REDIS_URL: str = "redis://localhost:6379"


settings = Settings()
