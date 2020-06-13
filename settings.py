import sys
import logging
import warnings
from decouple import config
from unipath import Path


PROJECT_DIR = Path(__file__).parent

SECRET_KEY = config("SECRET_KEY", "")

DEBUG = config("DEBUG", default=False, cast=bool)
SERVER_HOST = config("SERVER_URL", default="localhost")
SERVER_PORT = config("SERVER_PORT", default=5000, cast=int)

ADMINS = ("Joao Pedro Portela", "porthunt@gmail.com")
MANAGERS = ADMINS

MEDIA_ROOT = PROJECT_DIR.parent.parent.child("media")
MEDIA_URL = "/media/"

TIME_ZONE = "UTC"
LANGUAGE_CODE = "en-us"

if DEBUG and not SECRET_KEY:
    logging.error("Secret key is not defined, but DEBUG mode is in use.")
    sys.exit(1)

if not SECRET_KEY:
    warnings.warn("Secret key is not defined.")
