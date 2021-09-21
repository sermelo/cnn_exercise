from kafka import KafkaConsumer, KafkaProducer

class Publisher():
    def __init__(self, topic, kafka_server='kafka'):
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=kafka_server)

    def send(self, message):
        meta_data = self.producer.send(self.topic, message)
        self.producer.flush()
        return meta_data
