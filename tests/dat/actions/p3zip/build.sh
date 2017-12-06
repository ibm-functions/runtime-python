#!/bin/bash

rm ../python3_jessie_virtualenv.zip
rm -r virtualenv
docker run --rm -v "$PWD:/tmp" action-python-v3 sh -c "cd tmp; virtualenv virtualenv; source virtualenv/bin/activate; pip install -r requirements.txt;"
zip -r ../python3_jessie_virtualenv.zip virtualenv __main__.py

