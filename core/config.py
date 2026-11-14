"""
Load the config file and create any custom variables
that are available for ease of use purposes
"""

import sys
from pathlib import Path

import yaml

from core.logger import logger

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR / "config" / "config.yml"

if not CONFIG_FILE.is_file():
    logger.error(
        "Config file not found: {}. Copy config/config.sample.yml to config/config.yml and add your access key.",
        CONFIG_FILE,
    )
    sys.exit(1)

with CONFIG_FILE.open(encoding="utf-8") as config_file:
    data = yaml.safe_load(config_file)

# ACCESS KEY
ACCESS_KEY = data["biogrid"]["access_key"]
BASE_URL = data["biogrid"]["base_url"]
