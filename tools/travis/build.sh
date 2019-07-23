#!/bin/bash
set -ex

# Build script for Travis-CI.

SCRIPTDIR=$(cd $(dirname "$0") && pwd)
ROOTDIR="$SCRIPTDIR/../.."
WHISKDIR="$ROOTDIR/../openwhisk"
IMAGE_PREFIX="testing"

export OPENWHISK_HOME=$WHISKDIR

# Build OpenWhisk
cd $WHISKDIR

# Pull down images
docker pull openwhisk/controller:nightly
docker tag openwhisk/controller:nightly ${IMAGE_PREFIX}/controller
docker pull openwhisk/invoker:nightly
docker tag openwhisk/invoker:nightly ${IMAGE_PREFIX}/invoker
docker pull openwhisk/nodejs6action:nightly
docker tag openwhisk/nodejs6action:nightly nodejs6action
docker pull openwhisk/python2action
docker tag openwhisk/python2action python2action

TERM=dumb ./gradlew install

# Build IBM nodejs runtime
cd $ROOTDIR
TERM=dumb ./gradlew distDocker -PdockerImagePrefix=${IMAGE_PREFIX}
