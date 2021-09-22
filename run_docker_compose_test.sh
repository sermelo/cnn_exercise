#!/bin/bash
set -e

./build_all_docker_images.sh
docker-compose up --force-recreate --build --scale app=10
