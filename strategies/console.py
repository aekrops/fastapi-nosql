from typing import List
from .strategy import Strategy


class ConsoleManager(Strategy):
    def start_processing(self):
        pass

    def finish_processing(self):
        pass

    def is_file_uploaded(self):
        pass

    async def processing_data(self, data: List):
        for line in data:
            print(line)
