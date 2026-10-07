import os
import socket
from urllib.parse import urlparse

import pytest

pytestmark = pytest.mark.req("REQ-0002")


def _reachable(url, default_port):
    parsed = urlparse(url)
    try:
        with socket.create_connection(
            (parsed.hostname, parsed.port or default_port), timeout=2
        ):
            return True
    except OSError:
        return False


@pytest.mark.noncritical
@pytest.mark.skipif("REDIS_URL" not in os.environ, reason="REDIS_URL not set")
def test_redis_reachable():
    assert _reachable(os.environ["REDIS_URL"], 6379)


@pytest.mark.noncritical
@pytest.mark.skipif("DATABASE_URL" not in os.environ, reason="DATABASE_URL not set")
def test_postgres_reachable():
    assert _reachable(os.environ["DATABASE_URL"], 5432)
