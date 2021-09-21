FROM tensorflow/tensorflow:latest

# Install needed packages
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y pylint3 \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Prepare needed user and directory
ARG WORKING_USER=vector
ARG WORKING_DIR=/home/${WORKING_USER}/workspace

RUN adduser --disabled-password --gecos "" --shell /bin/bash $WORKING_USER
USER $WORKING_USER

RUN mkdir -p $WORKING_DIR
WORKDIR $WORKING_DIR

# Download Mnist dataset
COPY download_fashion_mnist.py .
RUN ./download_fashion_mnist.py
RUN rm download_fashion_mnist.py

# Copy apps code
COPY src src

ENTRYPOINT sleep infinity
