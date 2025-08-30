# app/client.py
import httpx


class ApiClient:
    """Minimal client for Project-Adriane."""

    def __init__(self, httpx_client: httpx.Client):
        self._client = httpx_client

    @classmethod
    def from_base_url(cls, base_url: str, *, timeout: float = 5.0):
        """Use this in production or local dev against a running server."""
        return cls(httpx.Client(base_url=base_url, timeout=timeout))

    # Convenience calls
    def get_root(self):
        return self._client.get("/api/v1/")

    def get_health(self):
        return self._client.get("/api/v1/health")

    def get_initiate(self):
        return self._client.get("/api/v1/initiate")

    # Optional generic helpers
    def get(
        self, path: str, *, params: dict | None = None, headers: dict | None = None
    ):
        return self._client.get(path, params=params, headers=headers)

    def close(self):
        self._client.close()

    def __enter__(self):  # context manager support
        return self

    def __exit__(self, *exc):
        self.close()
