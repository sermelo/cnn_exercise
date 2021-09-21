#!/bin/bash
set -e
docker build docker/base/. -t vector
docker run --rm -ti -v $PWD/docker/base/src:/home/vector/workspace --entrypoint /bin/bash vector
