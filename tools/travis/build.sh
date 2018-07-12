#!/bin/bash
set -ex

# Build script for Travis-CI.

SCRIPTDIR=$(cd $(dirname "$0") && pwd)
ROOTDIR="$SCRIPTDIR/../.."
WHISKDIR="$ROOTDIR/../openwhisk"
IMAGE_PREFIX="testing"

export OPENWHISK_HOME=$WHISKDIR

# Build OpenWhisk deps before we run tests
cd $WHISKDIR
# Mock file (works around bug upstream)
echo "openwhisk.home=$WHISKDIR" > whisk.properties
echo "vcap.services.file=" >> whisk.properties

# Build runtime
cd $ROOTDIR
TERM=dumb ./gradlew distDocker
