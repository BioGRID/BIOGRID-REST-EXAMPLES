"""
Shared HTTP client helpers for talking to the BioGRID REST service
"""

import httpx

from core import config as cfg

# Fail fast if the service can't be reached, but give large result sets time to stream back
TIMEOUT = httpx.Timeout(30.0, connect=10.0)


def get(path: str, params: dict[str, str | int]) -> httpx.Response:
    """Send a GET request to the BioGRID REST service and raise on any non-2xx response"""
    with httpx.Client(base_url=cfg.BASE_URL, timeout=TIMEOUT) as http:
        response = http.get(path, params=params)
    response.raise_for_status()
    return response
