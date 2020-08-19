#!/bin/bash

virtualenv --python=python3.8 --no-site-packages ${BASH_SOURCE%/*}/venv
source venv/bin/activate
pip install --no-cache-dir --upgrade -r ${BASH_SOURCE%/*}/requirements.txt 