import json
import os
import urllib.request

import pytest

pytestmark = pytest.mark.req("REQ-0001")

API_URL = os.environ.get("API_URL", "http://localhost:3000")
SEARCH_URL = os.environ.get("SEARCH_URL", "http://localhost:8000")


def _get(url):
    with urllib.request.urlopen(url, timeout=10) as resp:
        return resp.status, json.load(resp)


@pytest.mark.skipif(not os.environ.get("E2E"), reason="set E2E=1 with stack running")
@pytest.mark.parametrize(
    "url,service",
    [(f"{API_URL}/health", "api"), (f"{SEARCH_URL}/health", "search-service")],
)
def test_service_health(url, service):
    status, body = _get(url)
    assert status == 200
    assert body["service"] == service
