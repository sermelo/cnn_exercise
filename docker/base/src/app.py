#!/usr/bin/env python3

import random
import json
from json import JSONEncoder
import numpy as np
import uuid
import time
import threading

from tensorflow.keras.datasets import fashion_mnist

from lib.publisher import Publisher
from lib.subscriber import Subscriber


class App():
    def __init__(self):
        self.pub = Publisher('calssification_requests')
        self.sub = Subscriber('classification_responses')

    def __get_prediction(self, image):
        message_uuid = str(uuid.uuid4())
        self.__send_img(image, message_uuid)
        prediction_data = self.__get_response(message_uuid)
        return prediction_data['class']

    def __send_img(self, image, message_uuid):
        data = {'img': image.tolist(), 'uuid': message_uuid}
        encoded_data = json.dumps(data)
        self.pub.send(encoded_data.encode('ascii'))

    def __get_response(self, message_uuid):
        for message in self.sub.messages():
            prediction_data = json.loads(message.value)
            if prediction_data['uuid'] == message_uuid:
                print(f'Answered received for UUID {message_uuid}')
                break
        return prediction_data

    def test_ml_service(self, tests_number):
        (_, _), (x_test, y_test) = fashion_mnist.load_data()
        for _ in range(tests_number):
            image_index = random.randint(0, len(x_test))
            print(f'Predicting image number {image_index}')
            prediction = self.__get_prediction(x_test[image_index])
            print(f'Prediction: {prediction} - Real class: {y_test[image_index]}')
            time.sleep(random.randint(0, 5))

def run_app():
    app = App()
    app.test_ml_service(5)

def start_test():
    for _ in range(5):
        x = threading.Thread(target=run_app)
        x.start()

if __name__ == "__main__":
    start_test()
