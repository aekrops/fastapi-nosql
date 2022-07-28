from typing import List
import os
from .strategy import Strategy


class FileManager(Strategy):
    def __init__(self, filename):
        self.file_path = f"{filename}.txt"

    def start_processing(self):
        print("start write to file")

    def finish_processing(self):
        print("finish write to file")

    def is_file_uploaded(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    async def processing_data(self, data: List):
        with open(self.file_path, 'a', encoding="utf-8") as file:
            for line in data:
                file.write(f"{line}\n")
