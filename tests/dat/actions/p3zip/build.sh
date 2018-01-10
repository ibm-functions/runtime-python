#!/bin/bash

#helper file to create and test python zip action

ZIP_NAME="python3_jessie_virtualenv.zip"
IMAGE_NAME="ibmfunctions/action-python-v3:latest"
ACTION_NAME="zip_jessie"

rm ${ZIP_NAME}
rm -r virtualenv
set -ex

docker run --rm -v "$PWD:/tmp" ${IMAGE_NAME}  bash -c "cd /tmp && virtualenv virtualenv && source virtualenv/bin/activate && pip install -r requirements.txt"
zip -r ${ZIP_NAME} virtualenv __main__.py
bx wsk action update ${ACTION_NAME} ${ZIP_NAME} --docker ${IMAGE_NAME}
bx wsk action invoke ${ACTION_NAME} -b
