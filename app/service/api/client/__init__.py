# app/client/__init__.py

"""
API Client package for Project-Adriane.
Provides a thin wrapper around httpx for making requests to the service.
"""

from .client import ApiClient

__all__ = ["ApiClient"]
