import time

from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable

class Subscriber():
    def __init__(self, topic, kafka_server='kafka'):
        self.topic = topic
        self.consumer = self.get_consumer(kafka_server)

    def get_consumer(self, server):
        consumer = None
        for _ in range(14): # Try to connect 4 + 1 times
            try:
                consumer = KafkaConsumer(
                    self.topic,
                    auto_offset_reset='earliest',
                    bootstrap_servers=server)
            except NoBrokersAvailable:
                time.sleep(1)
                continue
            else:
                break
        if not consumer:
            consumer = KafkaConsumer(
                self.topic,
                auto_offset_reset='earliest',
                bootstrap_servers=server)
        return consumer

    def messages(self):
        while True:
            yield next(self.consumer)
