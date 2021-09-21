from kafka import KafkaConsumer, KafkaProducer

class Subscriber():
    def __init__(self, kafka_server, topic):
        self.topic = topic
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=kafka_server)

    def receive(self):
        return next(self.consumer)

