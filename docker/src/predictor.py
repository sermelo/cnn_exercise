#!/usr/bin/env python3

from tensorflow.keras.datasets import fashion_mnist

from lib.classifier import Classifier
from lib.publisher import Publisher
from lib.subscriber import Subscriber

sub = Subscriber('calssification_requests')
pub = Publisher('classification_responses')

def listen_requests(predictor):
    for message in sub.messages():
        print(f'Received message {message.value}')
        pub.send(b'3')

def get_predictor():
    (x_train, y_train), (_, _) = fashion_mnist.load_data()
    classifier = Classifier(x_train, y_train)
    classifier.load("model_1.2")
    return classifier

def run_predictor():
    predictor = get_predictor()
    listen_requests(predictor)

if __name__ == "__main__":
    run_predictor()
