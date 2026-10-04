from fastapi import FastAPI

from .config import settings

app = FastAPI(title="Consumer Service Search")


@app.get("/health")
def health():
    return {"ok": True, "service": "search-service", "env": settings.ENVIRONMENT}


@app.get("/search")
def search():
    return {"results": [], "message": "search service placeholder"}
