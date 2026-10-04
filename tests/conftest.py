import pathlib

import pytest

TESTS_DIR = pathlib.Path(__file__).parent


def pytest_collection_modifyitems(items):
    """Auto-apply the suite marker from the directory a test lives in."""
    for item in items:
        parts = pathlib.Path(str(item.path)).relative_to(TESTS_DIR).parts
        if parts and parts[0] in ("unit", "integration", "e2e"):
            item.add_marker(getattr(pytest.mark, parts[0]))


@pytest.fixture(autouse=True)
def _record_links(request, record_property):
    """Write req/issue markers into the JUnit XML for traceability reports."""
    for name in ("req", "issue"):
        for marker in request.node.iter_markers(name):
            for arg in marker.args:
                record_property(name, str(arg))
