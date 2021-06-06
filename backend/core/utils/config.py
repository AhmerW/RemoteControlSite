from sys import exit

from fastapi import FastAPI

import json 
import logging

config = None
app = FastAPI(title = 'RCS', redoc_url = None)

logger = logging.getLogger(__name__)

if config is None:
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        logger.error("config.json file is missing. Required to run the application")
        exit()