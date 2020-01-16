#!/bin/bash

set -e

# build the pythone.zip for the test
(cd python-zip && zip ../python.zip -r .)
