#!/usr/bin/env python3

import json
import numpy as np
from tensorflow.keras.datasets import fashion_mnist

from lib.classifier import Classifier
from lib.publisher import Publisher
from lib.subscriber import Subscriber

class Predictor():
    def __init__(self):
        self.sub = Subscriber('calssification_requests')
        self.pub = Publisher('classification_responses')
        self.classifier = self.__get_predictor()

    def listen_requests(self):
        for message in self.sub.messages():
            decoded_message = json.loads(message.value)
            img = np.asarray(decoded_message['img'])
            uuid = decoded_message['uuid']
            print(f'Received message with uuid: {uuid}')
            prediction = int(self.classifier.classify(img))
            response = {'class': prediction, 'uuid': uuid}
            self.pub.send(json.dumps(response).encode('ascii'))
            print(f'Returned predction {prediction} to uuid {uuid}')

    def __get_predictor(self, model_name='model_1.2'):
        (x_train, y_train), (_, _) = fashion_mnist.load_data()
        classifier = Classifier(x_train, y_train)
        classifier.load(model_name)
        return classifier

def run_predictor():
    predictor = Predictor()
    predictor.listen_requests()

if __name__ == "__main__":
    run_predictor()
