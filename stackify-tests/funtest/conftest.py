import pytest

from relation_store import Connection


@pytest.yield_fixture(scope="function")
def test_connection():
    return Connection(":memory:")

