#!/usr/bin/env python3
"""Train and test Neural network model to classify images"""

import numpy as np
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.layers import InputLayer, Conv2D, MaxPooling2D, \
     BatchNormalization, Dropout, Flatten, Dense
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import categorical_crossentropy
from tensorflow.keras.utils import to_categorical

class DataException(Exception):
    pass

class ModelException(Exception):
    pass

class Classifier(object):
    """Neural networks image classifier"""

    def __init__(self, x_data, y_data):
        """
        Construct classifier

        Parameters:
           x_data (numpy array): Images data to classify
           y_data (numpy array): Classification of x_data
        """
        self.model = None
        self.x_train = self.__reshape_x(x_data)
        self.number_of_classes = self.__get_number_of_classes(y_data)
        self.y_train = self.__one_hot_encoding(y_data)

    @classmethod
    def __reshape_x(cls, x_data):
        if len(x_data.shape) == 4:
            return x_data
        elif len(x_data.shape) == 3:
            return x_data.reshape(x_data.shape + (1,))
        else:
            raise DataException("X data shape not correct")

    def __one_hot_encoding(self, y_data):
        return to_categorical(y_data, self.number_of_classes)

    @classmethod
    def __get_number_of_classes(cls, y_data):
        return len(np.unique(y_data))

    def __get_model(self):
        data_shape = self.x_train.shape[1:]
        model = Sequential()
        model.add(InputLayer(data_shape))
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
        model.add(Dense(self.number_of_classes, activation='softmax'))
        model.compile(
            optimizer=Adam(),
            loss=categorical_crossentropy,
            metrics=['acc'])
        return model

    def train(self, verbose=0):
        """ Train CNN model
        Parameters:
           verbose (int): Training verbosity.
        """
        self.model = self.__get_model()
        history = self.model.fit(
            self.x_train,
            self.y_train,
            batch_size=32,
            epochs=40,
            shuffle=True,
            verbose=verbose,
            callbacks=[EarlyStopping(patience=3)],
            validation_split=0.3)
        return history

    def save(self, name):
        """ Save trained model
        Parameters:
            name (str): Name of the model to save.
        """
        if not self.model:
            raise ModelException("Model not trained") 
        self.model.save(name)

    def load(self, name):
        """ Load a pretrained model
        Parameters:
            name (str): Name of the model to save.
        """
        if self.model:
            raise ModelException("Model already trained") 
        self.model = load_model(name)

    def test(self, x_test, y_test):
        """ Test trained model
        Parameters:
           x_test (numpy array): Images data to classify
           y_test (numpy array): Classification of x_test

        Returns:
           float: accuracy
        """
        if not self.model:
            raise ModelException("Model not trained")
        x_test = self.__reshape_x(x_test)
        y_test = self.__one_hot_encoding(y_test)
        _, test_acc = self.model.evaluate(x_test, y_test, verbose=0)
        return test_acc

    def classify(self, image):
        """ Test trained model
        Parameters:
           image (numpy array): Images to classify

        Returns:
           int:
        """
        if not self.model:
            raise ModelException("Model not trained") 
        image = image.reshape((1, ) + image.shape)
        image = self.__reshape_x(image)
        return np.argmax(self.model.predict(image), axis=1)[0]
