import os

import json
import logging

CONFIG_PATH = os.path.join('core', 'utils', 'config.json')
logger = logging.getLogger(__name__)


def loadConfig():
    try:
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(
            "config.json file is missing. Required to run the application")
        exit()


config = loadConfig()
