import redis
from settings import REDIS_HOST, REDIS_PASSWORD, REDIS_PORT
from enum import Enum
from datetime import datetime


class FileStatus(Enum):
    STARTED = "started"
    UPLOADED = "uploaded"
    IGNORED = "ignored"


class Redis:
    def __init__(self, filename: str):
        self.instance = redis.StrictRedis(host=REDIS_HOST, password=REDIS_PASSWORD, port=REDIS_PORT, ssl=True)
        self.filename = filename

    def is_file_uploaded(self):
        decode_item = lambda item: item.decode("utf-8")

        if decode_item(self.instance.get("name")) == self.filename \
                and decode_item(self.instance.get("status")) in (FileStatus.UPLOADED.value, FileStatus.IGNORED.value):
            self.instance.mset(
                {
                    "status": FileStatus.IGNORED.value,
                    "loading_start_time": str(datetime.now())[:19]
                }
            )
            return True
        return False

    def start_uploading_file(self):
        self.instance.mset(
            {
                "name": self.filename,
                "status": FileStatus.STARTED.value,
                "loading_start_time": str(datetime.now())[:19]
            }
        )

    def finish_uploading_file(self):
        self.instance.mset(
            {
                "status": FileStatus.UPLOADED.value,
                "loading_finish_time": str(datetime.now())[:19]
            }
        )
