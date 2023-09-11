#!/bin/bash
set -e

# Build script for Travis-CI.

SCRIPTDIR=$(cd $(dirname "$0") && pwd)
ROOTDIR="$SCRIPTDIR/../.."
HOMEDIR="$SCRIPTDIR/../../../"

# clone openWhisk
cd $HOMEDIR

# Clone and setup openwhisk to have a local test environment.
git clone  https://github.com/ibm-functions/openwhisk.git openwhisk
cd openwhisk

git checkout 9b768646b31928cd4ca02d2e4dcc5ba95ad5494b

# setup the openwhisk environment
./tools/travis/setup.sh

# Also build required test artifacts
./gradlew :tests:buildArtifacts
