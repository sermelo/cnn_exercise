from kafka import KafkaConsumer, KafkaProducer

class PubSub():
    def __init__(self, kafka_server, topic):
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=kafka_server)
        self.consumer = KafkaConsumer(
            self.topic,
            auto_offset_reset='earliest',
            bootstrap_servers=kafka_server)

    def send(self, message):
        return self.producer.send(self.topic, message.encode("ascii"))

    def receive(self):
        return next(self.consumer)

