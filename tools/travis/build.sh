#!/bin/bash
set -ex

# Build script for Travis-CI.

SCRIPTDIR=$(cd $(dirname "$0") && pwd)
ROOTDIR="$SCRIPTDIR/../.."
WHISKDIR="$ROOTDIR/../openwhisk"
IMAGE_PREFIX="testing"

export OPENWHISK_HOME=$WHISKDIR

# Login to hub.docker.com to get user specific pull rate.
if [ ! -z "${DOCKER_USER}" ] && [ ! -z "${DOCKER_PASSWORD}" ]; then
  echo "Run docker login..."
  echo ${DOCKER_PASSWORD} | docker login -u "${DOCKER_USER}" --password-stdin
fi

# Build OpenWhisk
cd $WHISKDIR

# Pull down images
docker pull ibmfunctions/controller:nightly
docker tag ibmfunctions/controller:nightly ${IMAGE_PREFIX}/controller
docker pull ibmfunctions/invoker:nightly
docker tag ibmfunctions/invoker:nightly ${IMAGE_PREFIX}/invoker
docker pull openwhisk/nodejs6action:nightly
docker tag openwhisk/nodejs6action:nightly nodejs6action

TERM=dumb ./gradlew install

# Build IBM Python runtime images
cd $ROOTDIR
TERM=dumb ./gradlew distDocker -PdockerImagePrefix=${IMAGE_PREFIX}
