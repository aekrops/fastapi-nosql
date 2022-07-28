from typing import List

from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
from utils.redis import Redis
from .strategy import Strategy
from settings import EVENTHUB_CONNECTION_URL, EVENTHUB_NAME


class CloudManager(Strategy):
    """
    EventHub & Redis
    """
    def __init__(self, filename: str):
        self.filename = filename
        self.redis = Redis(self.filename)
        self.producer = EventHubProducerClient.from_connection_string(
            conn_str=EVENTHUB_CONNECTION_URL,
            eventhub_name=EVENTHUB_NAME
        )

    def is_file_uploaded(self):
        return self.redis.is_file_uploaded()

    def start_processing(self):
        self.redis.start_uploading_file()

    def finish_processing(self):
        self.redis.finish_uploading_file()

    async def processing_data(self, data: List):
        async with self.producer:
            for record in data:
                event_data_batch = await self.producer.create_batch()
                event_data_batch.add(EventData(str(record)))
            await self.producer.send_batch(event_data_batch)


