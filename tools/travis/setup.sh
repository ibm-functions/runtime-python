#!/bin/bash
set -e

# Build script for Travis-CI.

SCRIPTDIR=$(cd $(dirname "$0") && pwd)
ROOTDIR="$SCRIPTDIR/../.."
HOMEDIR="$SCRIPTDIR/../../../"

# clone openWhisk
cd $HOMEDIR
git clone --depth=1 https://github.com/apache/openwhisk.git openwhisk

# setup the openwhisk environment
cd openwhisk
./tools/travis/setup.sh

# Also build required test artifacts
./gradlew :tests:buildArtifacts
