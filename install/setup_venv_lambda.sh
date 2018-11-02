#!/bin/bash

./install/create_venv.sh venv_lambda
. venv_lambda/bin/activate
pip install requests[security]
pip install boto3
pip install pdfkit
pip install youtube_dl
deactivate
