import json

from py.archive.s3 import (
    download_file,
    upload_file,
)

def load_state():
    download_file('data.json', 'temp/data.json')
    with open('temp/data.json', 'r') as f:
        return json.load(f)

def save_state(state):
    print(json.dumps(state, sort_keys=True, indent=4))
    with open('temp/data.json', 'w') as f:
        json.dump(state, f)
    upload_file('', 'data.json')
