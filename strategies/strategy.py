from abc import ABC, abstractmethod
from typing import List


class Strategy(ABC):

    @abstractmethod
    def is_file_uploaded(self):
        pass

    @abstractmethod
    def start_processing(self):
        pass

    @abstractmethod
    def finish_processing(self):
        pass

    @abstractmethod
    async def processing_data(self, data: List):
        pass


