#!/bin/bash
set -e
docker build docker/. -t vector
docker run --rm -ti --entrypoint /bin/bash vector
