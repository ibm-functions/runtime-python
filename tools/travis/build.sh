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
docker pull openwhisk/controller
docker tag openwhisk/controller ${IMAGE_PREFIX}/controller
docker pull openwhisk/invoker
docker tag openwhisk/invoker ${IMAGE_PREFIX}/invoker
docker pull openwhisk/nodejs6action
docker tag openwhisk/nodejs6action nodejs6action
docker pull openwhisk/python2action
docker tag openwhisk/python2action python2action

TERM=dumb ./gradlew \
:common:scala:install \
:core:controller:install \
:core:invoker:install \
:tests:install

# Build IBM nodejs runtime
cd $ROOTDIR
TERM=dumb ./gradlew \
:python3:distDocker \
-PdockerImagePrefix=${IMAGE_PREFIX}
