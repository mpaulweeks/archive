import json

from .s3 import (
    download_file,
    upload_file,
)

def load_state():
    download_file('data.json', 'temp/data.json')
    with open('temp/data.json', 'r') as f:
        return json.load(f)

def save_state(state):
    with open('temp/data.json', 'w') as f:
        return json.dump(state, f)
    upload_file('', 'data.json')
