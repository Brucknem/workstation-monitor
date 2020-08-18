#!/bin/bash

virtualenv --python=python3.7 --no-site-packages venv
source venv/bin/activate
pip install --no-cache-dir --upgrade --trusted-host pypi.org -r requirements.txt 