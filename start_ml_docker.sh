#!/bin/bash
set -e
docker build docker/base/. -t vector
docker run --rm -ti --entrypoint /bin/bash vector
