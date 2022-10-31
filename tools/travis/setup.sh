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
# Use a fixed commit to run the tests, to explicitly control when changes are consumed.
# Commit: minor version bump of azure-storage-blob to fix builds (#5150)
git checkout 92f5d870bdecf01ccf0bf46baac582955fdbdfa6

# setup the openwhisk environment
./tools/travis/setup.sh

# Also build required test artifacts
./gradlew :tests:buildArtifacts
