#!/bin/bash

# ec2 had issues with python3 -m venv
# https://stackoverflow.com/a/26314477/6461842

### do these steps once
# python3 -m pip install virtualenv
# brew install pyenv
# pyenv install 3.6.7

venv_name=$1
virtualenv --python=/Users/mpaulweeks/.pyenv/versions/3.6.7/bin/python $venv_name
. $venv_name/bin/activate
curl https://bootstrap.pypa.io/get-pip.py | python
deactivate
