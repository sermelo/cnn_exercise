import time

from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

class Publisher():
    def __init__(self, topic, kafka_server='kafka'):
        self.topic = topic
        self.producer = self.get_producer(kafka_server)

    def get_producer(self, server):
        producer = None
        for _ in range(14): # Try to connect 4 + 1 times
            try:
                producer = KafkaProducer(bootstrap_servers=server)
            except NoBrokersAvailable:
                time.sleep(2)
                continue
            else:
                break
        if not producer:
            producer = KafkaProducer(bootstrap_servers=server)
        return producer

    def send(self, message):
        meta_data = self.producer.send(self.topic, message)
        self.producer.flush()
        return meta_data
