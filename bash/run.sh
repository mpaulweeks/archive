#!/bin/bash

export LD_LIBRARY_PATH=/usr/lib:/usr/local/lib/
source venv_lambda/bin/activate
python -m py.main
