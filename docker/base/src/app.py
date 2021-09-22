#!/usr/bin/env python3

import random

from tensorflow.keras.datasets import fashion_mnist

from lib.publisher import Publisher
from lib.subscriber import Subscriber

class App():
    def __init__(self):
        self.pub = Publisher('calssification_requests')
        self.sub = Subscriber('classification_responses')

    def get_prediction(self, image):
        self.pub.send(image.tobytes())
        prediction = next(self.sub.messages())
        return prediction.value

    def test_ml_service(self, tests_number):
        (_, _), (x_test, y_test) = fashion_mnist.load_data()
        for _ in range(tests_number):
            image_index = random.randint(0, len(x_test))
            print(f'Predicting image number {image_index}')
            prediction = self.get_prediction(x_test[image_index])
            print(f'Prediction: {prediction}; Real value: {y_test[image_index]}')

def run_app():
    app = App()
    app.test_ml_service(5)

if __name__ == "__main__":
    run_app()
