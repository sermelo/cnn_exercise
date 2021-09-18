#!/bin/bash
set -e
docker build docker/. -t vector
docker run --rm -ti -v $PWD:/home/vector/workspace vector
