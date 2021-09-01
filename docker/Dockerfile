FROM tensorflow/tensorflow:latest

# Install needed packages
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y pylint \
    && rm -rf /var/lib/apt/lists/*

# Prepare needed user and directory
ENV WORKING_USER=vector
ENV WORKING_DIR=/home/${WORKING_USER}/workspace

RUN adduser --disabled-password --gecos "" --shell /bin/bash $WORKING_USER
USER $WORKING_USER

RUN mkdir -p $WORKING_DIR
WORKDIR $WORKING_DIR

# Download Mnist dataset
COPY download_fashion_mnist.py .
RUN ./download_fashion_mnist.py
RUN rm download_fashion_mnist.py
