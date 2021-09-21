#!/usr/bin/env python3

import random

from tensorflow.keras.datasets import fashion_mnist

from lib.publisher import Publisher
from lib.subscriber import Subscriber

pub = Publisher('calssification_requests')
sub = Subscriber('classification_responses')

def get_prediction(image):
    pub.send(image.tobytes())
    prediction = next(sub.messages())
    return prediction.value

def test_ml_service(tests_number):
    (_, _), (x_test, y_test) = fashion_mnist.load_data()
    for _ in range(tests_number):
        image_index = random.randint(0, len(x_test))
        print(f'Predicting image number {image_index}')
        prediction = get_prediction(x_test[image_index])
        print(f'Prediction: {prediction}; Real value: {y_test[image_index]}')


if __name__ == "__main__":
    test_ml_service(5)
