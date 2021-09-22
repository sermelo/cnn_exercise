# ML environment

This environment is a docker image with all ML and kafka libraries.
The docker file of this environment is at:

    docker/base/

If it is initialized using start_ml_development_environment.sh script,
it will mount docker/base/src directory. This make it a good development
environment. start_ml_development_environment.sh also build the docker image

# Classifier usage

The classifier(docker/base/src/lib/classifier.py), can be importer in python and used directly.
This is an example of how to use it:

    classifier = Classifier(x_train, y_train)
    classifier.train(verbose=1)
    classifier.test(x_test, y_test)
    classifier.classify(image)

There are some other public methods that can be useful:

    classifier.load(name)
    classifier.save(name)

Some docstring have been added to detail the usage.

As an example the test_classifier.py script has been created

It is recommended to use start_ml_development_environment.sh to use this code

# Docker images

There are 3 docker images:

* vector: This is the base image and it contains everything needed except entrypoints
* vector_app: This uses the vector image and run ./app.py script as entrypoint
* vector_predictor: This uses the vector image and run ./predictor.py script as entrypoint

This 3 images can be built with this script:

    ./build_all_docker_images.sh

# Scripts

## build_all_docker_images.sh

Build all images

## start_ml_development_environment.sh

Start development environment

## docker/base/src/app.py

Get some examples from fashion mnist and request classification through Kafka

## docker/base/src/predictor.py

Load an ML model, and wait for messages from Kafka service to classify

## run_docker_compose_test.sh

Build all images and start docker compose environment with kafka, zookeeper, app and predictor to run
some tests

# Kafka integration

Docker compose is used to start the whole environment with 4 containers:
* Kafka
* Zookeepr
* App
* Predictor

The app comunicates with predictor using Kafka to do predictions
App code: docker/base/src/app.py
Predictor code: docker/base/src/predictor.py

To start the environment this docker-compose command is recomended:

    docker-compose up --force-recreate --build

For more extensive testing, we can run more app replicas with a command like this one:

    docker-compose up --force-recreate --build --scale app=5

run_docker_compose_test.sh can be run to do the same

# TODO
* Add docstrings
* Extend README
* Integration with google pub/sub
* Exit apps with 1 when at least one prediction fails
