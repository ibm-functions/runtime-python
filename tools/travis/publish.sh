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
elif [ ${RUNTIME_VERSION} == "3.11" ]; then
  RUNTIME="python3.11"
fi

# run login in a subshell with disabled trace to avoid having credentials in the logs
# when trace is on (set -x)
(
  set +x # disable trace in this subshell
  # Login to hub.docker.com to get user specific pull rate.
  if [ ! -z "${DOCKER_USER}" ] && [ ! -z "${DOCKER_PASSWORD}" ]; then
    echo "Run docker login..."
    echo ${DOCKER_PASSWORD} | docker login -u "${DOCKER_USER}" --password-stdin
  fi
)


if [[ ! -z ${RUNTIME} ]]; then
TERM=dumb ./gradlew \
${RUNTIME}:pushImage \
-PdockerRegistry=docker.io \
-PdockerImagePrefix=${IMAGE_PREFIX} \
-PdockerImageTag=${IMAGE_TAG}
fi
