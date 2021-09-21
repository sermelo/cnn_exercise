#!/bin/bash
set -e
docker build docker/base/. -t vector
docker build docker/app/. -t vector_app
docker build docker/predictor/. -t vector_predictor
