#!/usr/bin/env python3

import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer, Conv2D, MaxPooling2D, BatchNormalization, Dropout, Flatten, Dense
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import categorical_crossentropy

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1))

number_of_classes = len(np.unique(y_train))

y_train = keras.utils.to_categorical(y_train, number_of_classes)
y_test = keras.utils.to_categorical(y_test, number_of_classes)


def get_model():
    model = Sequential()
    model.add(InputLayer((28,28, 1)))
    model.add(Conv2D(64, (2, 2), activation='relu', padding='same'))
    model.add(MaxPooling2D((2, 2)))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    model.add(Conv2D(32, (2, 2), activation='relu', padding='same'))
    model.add(MaxPooling2D((2, 2)))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dropout(0.2))
    model.add(Dense(128, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dense(number_of_classes, activation='softmax'))

    model.compile(
        optimizer=Adam(),
        loss=categorical_crossentropy,
        metrics=['acc'])
    return model

def train(model, verbose=0):
    final_history = model.fit(
        x_train,
        y_train,
        batch_size=32,
        epochs=40,
        shuffle=True,
        verbose=verbose,
        callbacks = [EarlyStopping(patience=3)],
        validation_split=0.3)

    test_loss, test_acc = model.evaluate(x_test,  y_test, verbose=0)
    print(f'Test accuracy {test_acc}')

model = get_model()
train(model, verbose=1)
