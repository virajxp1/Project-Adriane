# tests/test_server_setup.py
from collections.abc import Generator
from typing import Any

import httpx
import pytest
from httpx import ASGITransport

from app.main import app  # your FastAPI app
from app.service.api.client import ApiClient


@pytest.fixture(scope="session")
def api_client() -> Generator[ApiClient, Any, None]:
    transport = ASGITransport(app=app)
    httpx_client = httpx.Client(transport=transport, base_url="http://testserver")
    client = ApiClient(httpx_client)
    yield client
    client.close()
