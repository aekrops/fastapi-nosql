from __future__ import annotations
from typing import List
from settings import STRATEGY
from .cloud import CloudManager
from .console import ConsoleManager
from .file import FileManager


class StrategyManager:
    def __init__(self, file_url: str):
        self._file_url = file_url
        self.__manager = StrategyManager.choose_strategy(self._file_url)

    @staticmethod
    def choose_strategy(filename):
        if STRATEGY == "console":
            return ConsoleManager()
        elif STRATEGY == "cloud":
            return CloudManager(filename)
        elif STRATEGY == "file":
            return FileManager("dataset")
        else:
            return "No strategy"

    def is_file_uploaded(self):
        return self.__manager.is_file_uploaded()

    def start_processing_data(self):
        self.__manager.start_processing()

    def finish_processing_data(self):
        self.__manager.finish_processing()

    async def process_data(self, data: List):
        await self.__manager.processing_data(data)



