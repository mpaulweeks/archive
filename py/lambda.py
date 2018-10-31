
from datetime import datetime
import os
import sys

import requests

from .aws import (
    get_bucket,
)


def upload_file(destination, filename):
    lambda_client = get_client()
    with open('temp/%s' % filename, 'rb') as f:
        # todo
        pass



def upload_website(filename):
    upload_file('website', filename)

def upload_youtube(filename):
    upload_file('youtube', filename)



def download_state():
    pass

def upload_state():
    pass



def fetch_bookmarks_website():
    url = "http://blog.mpaulweeks.com/data/bookmarks.json"
    response = requests.get(url)
    return response.json()

def fetch_bookmarks_youtube():
    url = "http://blog.mpaulweeks.com/data/youtube-generated.json"
    response = requests.get(url)
    return response.json()



def download_website(url, filename):
    pass

def download_youtube(url, filename):
    pass



def archive_website():
    now = datetime.utcnow().strftime("%Y/%m/%d")
    bookmarks = fetch_bookmarks_website()
    state = download_state()
    website_state = state.get('website', {})

    for website in bookmarks.get('links', []):
        url = website.get('url')
        if url:
            name = website.get('name')
            key = name
            print(key)
            if key not in website_state:
                download_website(url, key)
                upload_website(key)
                website_state[key] = {
                    "url": url,
                    "name": name,
                    "fetched": now
                }

    state['website'] = website_state
    upload_state(state)

def archive_youtube():
    pass



def run(manual):
    archive_website()
    archive_youtube()

def lambda_handler(json_input, context):
    manual = json_input.get('manual')
    return run(manual)

if __name__ == "__main__":
    manual = len(sys.argv) > 1
    return run(manual)
