#!/usr/bin/env python3

import random
import json
from json import JSONEncoder
import numpy as np

from tensorflow.keras.datasets import fashion_mnist

from lib.publisher import Publisher
from lib.subscriber import Subscriber


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


class App():
    def __init__(self):
        self.pub = Publisher('calssification_requests')
        self.sub = Subscriber('classification_responses')

    def __get_prediction(self, image):
        self.__send_img(image)
        message = next(self.sub.messages())
        prediction_data = json.loads(message.value)
        return prediction_data['class']

    def __send_img(self, image):
        data = {"img": image}
        encoded_data = json.dumps(data, cls=NumpyArrayEncoder)
        self.pub.send(encoded_data.encode('ascii'))

    def test_ml_service(self, tests_number):
        (_, _), (x_test, y_test) = fashion_mnist.load_data()
        for _ in range(tests_number):
            image_index = random.randint(0, len(x_test))
            print(f'Predicting image number {image_index}')
            prediction = self.__get_prediction(x_test[image_index])
            print(f'Prediction: {prediction} - Real class: {y_test[image_index]}')

def run_app():
    app = App()
    app.test_ml_service(5)

if __name__ == "__main__":
    run_app()
