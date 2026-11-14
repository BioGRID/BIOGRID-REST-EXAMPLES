"""
Configure loguru once for every example script.

All output (including the API results) is written to stdout through loguru.
Set the LOG_LEVEL environment variable (e.g. LOG_LEVEL=DEBUG) to see request diagnostics.
"""

import os
import sys

from loguru import logger

LOG_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)

logger.remove()
logger.add(sys.stdout, level=os.getenv("LOG_LEVEL", "INFO").upper(), format=LOG_FORMAT)

__all__ = ["logger"]
