"""
Shared HTTP client helpers for talking to the BioGRID REST service
"""

import sys

import httpx

from core import config as cfg
from core.logger import logger

# Fail fast if the service can't be reached, but give large result sets time to stream back
TIMEOUT = httpx.Timeout(30.0, connect=10.0)


def get(path: str, params: dict[str, str | int]) -> httpx.Response:
    """GET a BioGRID REST endpoint, logging and exiting on connection errors or non-2xx responses"""
    # Never write the access key to the logs
    safe_params = {key: ("<redacted>" if key == "accesskey" else value) for key, value in params.items()}
    logger.debug("GET {}{} params={}", cfg.BASE_URL, path, safe_params)

    try:
        with httpx.Client(base_url=cfg.BASE_URL, timeout=TIMEOUT) as http:
            response = http.get(path, params=params)
        response.raise_for_status()
    except httpx.HTTPStatusError as error:
        logger.error(
            "BioGRID request to {} failed: {} {}", path, error.response.status_code, error.response.reason_phrase
        )
        if error.response.is_redirect:
            # The service redirects to its signup page when the access key is missing or invalid
            logger.error("Check the access_key in config/config.yml")
        sys.exit(1)
    except httpx.RequestError as error:
        logger.error("BioGRID request to {} failed: {}", path, type(error).__name__)
        sys.exit(1)

    logger.debug(
        "{} {} in {:.2f}s ({} bytes)",
        response.status_code,
        response.reason_phrase,
        response.elapsed.total_seconds(),
        len(response.content),
    )
    return response
