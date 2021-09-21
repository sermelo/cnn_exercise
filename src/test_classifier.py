#!/usr/bin/env python3
"""Test classifier"""

from tensorflow.keras.datasets import fashion_mnist

from lib.classifier import Classifier

def test_classifier():
    """Test classifier class with Mnist_fashion"""
    (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
    classifier = Classifier(x_train, y_train)
    classifier.train(verbose=1)
    classifier.test(x_test, y_test)

if __name__ == "__main__":
    test_classifier()
