from kafka import KafkaProducer

class Publisher():
    def __init__(self, kafka_server, topic):
        self.producer = KafkaProducer(bootstrap_servers=kafka_server)
        self.topic = topic

    def send(self, message):
        self.producer.send(self.topic, message.encode("ascii"))
