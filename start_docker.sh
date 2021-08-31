#!/bin/bash
set -e
docker build docker/. -t vector
docker run -ti -v $PWD:/home/vector/workspace vector
