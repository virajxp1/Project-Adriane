# tests/test_api_status.py
import pytest

# Every path should return HTTP 200
ENDPOINTS = [
    "/api/v1/",
    "/api/v1/health",
    "/api/v1/initiate",
]

HEALTHY_STATYS_CODE = 200


@pytest.mark.parametrize("path", ENDPOINTS)
def test_endpoint_returns_200(api_client, path):
    resp = api_client.get(path)
    assert resp.status_code == HEALTHY_STATYS_CODE
    # Optional sanity: response JSON should be a dict
    assert isinstance(resp.json(), dict)
