#!/bin/bash

MY_PATH="`dirname \"$0\"`"
virtualenv --python=python3.8 --no-site-packages $MY_PATH/venv
source venv/bin/activate
pip install --no-cache-dir --upgrade -r $MY_PATH/requirements.txt 