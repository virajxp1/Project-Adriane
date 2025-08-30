import pytest
from fastapi.testclient import TestClient

from app.main import app  # your FastAPI app


@pytest.fixture(scope="session")
def api_client():
    """Session-scoped client hitting the app in-process (no real network)."""
    with TestClient(app) as client:
        yield client
