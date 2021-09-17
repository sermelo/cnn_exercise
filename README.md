# Start the environment

A docker image has been created to run this application. To start it
start_docker.sh can be executed. start_docker.sh script will build and start
the docker image.

# Classifier usage

The classifier(lib/classifier.py), can be importer in python and used directly.
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
