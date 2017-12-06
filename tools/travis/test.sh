#!/bin/bash
set -ex

# Build script for Travis-CI.

SCRIPTDIR=$(cd $(dirname "$0") && pwd)
ROOTDIR="$SCRIPTDIR/../.."
WHISKDIR="$ROOTDIR/../openwhisk"

export OPENWHISK_HOME=$WHISKDIR

#Deployment
WHISK_CLI="${WHISKDIR}/bin/wsk -i"

# Run a simple action using the kind
${WHISK_CLI} action update echoPython ${ROOTDIR}/tests/dat/echo.py --kind "python-jessie:3"
${WHISK_CLI} action invoke echoPython -b

export OPENWHISK_HOME=$WHISKDIR
cd ${ROOTDIR}
TERM=dumb ./gradlew :tests:checkScalafmtAll
if [ "$TRAVIS_PULL_REQUEST" = "false" ]; then
  TERM=dumb ./gradlew :tests:test
else
  TERM=dumb ./gradlew :tests:testWithoutCredentials
fi




#For some reason there no activations, maybe index not ready
#${WHISK_CLI} activation get --last
