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
${WHISK_CLI} action update echoPython ${ROOTDIR}/tests/dat/echo.py --kind "python:3.7"
${WHISK_CLI} action invoke echoPython -b
${WHISK_CLI} action update echoPython ${ROOTDIR}/tests/dat/echo.py --kind "python:3.9"
${WHISK_CLI} action invoke echoPython -b
${WHISK_CLI} action update echoPython ${ROOTDIR}/tests/dat/echo.py --kind "python:3.11"
${WHISK_CLI} action invoke echoPython -b

export OPENWHISK_HOME=$WHISKDIR
cd ${ROOTDIR}
TERM=dumb ./gradlew :tests:checkScalafmtAll
if [ "$TRAVIS_PULL_REQUEST" = "false" ]; then
  TERM=dumb ./gradlew :tests:test
else
  TERM=dumb ./gradlew :tests:testWithoutCredentials
fi

if [[ "$?" != "0" ]]; then
  cat /tmp/wsklogs/invoker0/invoker0_logs.log
  cat /tmp/wsklogs/controller0/controller0_logs.log
  exit 1
fi 

#For some reason there no activations, maybe index not ready
#${WHISK_CLI} activation get --last
