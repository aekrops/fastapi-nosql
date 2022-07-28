import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://data.sfgov.org/resource/yitu-d5am.json"
STRATEGY = os.environ.get("STRATEGY")
EVENTHUB_CONNECTION_URL = os.environ.get("EVENTHUB_CONNECTION_URL")
REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
REDIS_PORT = os.environ.get("REDIS_PORT")
EVENTHUB_NAME = os.environ.get("EVENTHUB_NAME")
