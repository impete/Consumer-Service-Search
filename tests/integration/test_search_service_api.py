import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.mark.req("REQ-0001")
def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["ok"] is True
    assert body["service"] == "search-service"


@pytest.mark.req("REQ-0001")
def test_search_endpoint_returns_results_list():
    response = client.get("/search")
    assert response.status_code == 200
    assert response.json()["results"] == []
