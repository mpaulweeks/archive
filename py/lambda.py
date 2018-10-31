
from datetime import datetime
import os
import sys

from .bookmarks import (
    fetch_bookmarks_website,
    fetch_bookmarks_youtube,
)
from .state import (
    download_state,
    upload_state,
)
from .s3 import (
    upload_website,
    upload_youtube,
)
from .extract import (
    extract_website,
    extract_youtube,
)


def archive_website():
    now = datetime.utcnow().strftime("%Y/%m/%d")
    bookmarks = fetch_bookmarks_website()
    state = download_state()
    website_state = state.get('website', {})

    for website in bookmarks.get('links', []):
        url = website.get('url')
        if url and website.get('category') != 'Video':
            name = website.get('title')
            key = name
            print(key)
            if key not in website_state:
                filename = extract_website(url, key)
                if filename:
                    upload_website(filename)
                    website_state[key] = {
                        "url": url,
                        "name": name,
                        "fetched": now
                    }

    state['website'] = website_state
    upload_state(state)

def archive_youtube():
    # todo
    pass



def run(manual):
    archive_website()
    archive_youtube()

def lambda_handler(json_input, context):
    manual = json_input.get('manual')
    return run(manual)

if __name__ == "__main__":
    manual = len(sys.argv) > 1
    run(manual)
