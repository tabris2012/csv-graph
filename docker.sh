#!/bin/bash

CONTAINER_NAME=cg-dev

if [ $1 = "up" ]; then
    docker-compose -f docker-compose.yml -f .devcontainer/docker-compose.yml up -d
elif [ $1 = "down" ]; then
    docker-compose -f docker-compose.yml -f .devcontainer/docker-compose.yml down
elif [ $1 = "build" ]; then
    docker-compose -f docker-compose.yml -f .devcontainer/docker-compose.yml build
elif [ $1 = "test" ]; then
    docker exec $CONTAINER_NAME python -m unittest discover test # testフォルダ内のテストを全て実行
else
    docker exec -it $CONTAINER_NAME $@
fi
