#!/usr/bin/bash

BUILD_TAG='latest'
ECD='example_cars_detection'

function build {
    DOCKERFILE='Dockerfile'
    IMAGE="${ECD}:${BUILD_TAG}"
    echo "Building $IMAGE from $DOCKERFILE"
    docker build -f "$DOCKERFILE" -t "$IMAGE" .
}

function run {
    docker run \
      --name=${ECD} \
      --detach=true \
      -p 8080:8080 \
  "${ECD}:${BUILD_TAG}"
}

function logs {
    docker logs -f ${ECD}
}

function ps {
    docker ps
}

function stop {
    docker stop ${ECD} || true
}

function remove {
docker rm -f ${ECD}    
}

"$@"
