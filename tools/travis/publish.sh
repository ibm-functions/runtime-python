#!/bin/bash

set -eux

# Build script for Travis-CI.

SCRIPTDIR=$(cd $(dirname "$0") && pwd)
ROOTDIR="$SCRIPTDIR/../.."
WHISKDIR="$ROOTDIR/../openwhisk"

export OPENWHISK_HOME=$WHISKDIR

IMAGE_PREFIX=$1
RUNTIME_VERSION=$2
IMAGE_TAG=$3

if [ ${RUNTIME_VERSION} == "3.6" ]; then
  RUNTIME="python3.6"
elif [ ${RUNTIME_VERSION} == "3.7" ]; then
  RUNTIME="python3.7"
elif [ ${RUNTIME_VERSION} == "3.9" ]; then
  RUNTIME="python3.9"
fi

if [[ ! -z ${DOCKER_USER} ]] && [[ ! -z ${DOCKER_PASSWORD} ]]; then
docker login -u "${DOCKER_USER}" -p "${DOCKER_PASSWORD}"
fi

if [[ ! -z ${RUNTIME} ]]; then
TERM=dumb ./gradlew \
${RUNTIME}:pushImage \
-PdockerRegistry=docker.io \
-PdockerImagePrefix=${IMAGE_PREFIX} \
-PdockerImageTag=${IMAGE_TAG}
fi
