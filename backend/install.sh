#!/bin/bash

sudo apt-get install python3-dev libsystemd-dev -y
MY_PATH="$(dirname "$0")"
virtualenv --python=python3.8 "$MY_PATH/venv" || virtualenv --python=python3.7 "$MY_PATH/venv" || virtualenv --python=python3.6 "$MY_PATH/venv"
source "$MY_PATH/venv/bin/activate"
pip install --no-cache-dir --upgrade -r $MY_PATH/requirements.txt
