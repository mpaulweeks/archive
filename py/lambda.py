
from datetime import datetime
import os
import sys

from .bookmarks import (
    fetch_bookmarks_website,
    fetch_bookmarks_youtube,
)
from .state import (
    load_state,
    save_state,
)
from .s3 import (
    upload_website,
    upload_youtube,
)
from .pdf import (
    extract_website,
)
from .youtube import (
    extract_youtube,
)

def get_now():
    return datetime.utcnow().strftime("%Y/%m/%d")

def archive_website():
    now = get_now()
    bookmarks = fetch_bookmarks_website()
    state = load_state()
    website_state = state.get('website', {})
    remaining = 3

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
                    remaining -= 1
        if remaining < 1:
            break

    state['website'] = website_state
    save_state(state)

def archive_youtube():
    now = get_now()
    videos = fetch_bookmarks_youtube()
    state = load_state()
    youtube_state = state.get('youtube', {})
    remaining = 3

    for video in videos:
        print(video)
        vid = video.get('vid')

        # todo
        if vid != 'aiM5KDuHrR4':
            continue

        name = video.get('title')
        key = '%s - %s.mp4' % (
            vid, name
        )
        print(key)
        if key not in youtube_state:
            filename = extract_youtube(vid, key)
            if filename:
                upload_youtube(filename)
                youtube_state[key] = {
                    "vid": vid,
                    "name": name,
                    "fetched": now
                }
                remaining -= 1
        if remaining < 1:
            break

    state['youtube'] = youtube_state
    save_state(state)



def run(manual):
    # archive_website()
    archive_youtube()

def lambda_handler(json_input, context):
    manual = json_input.get('manual')
    return run(manual)

if __name__ == "__main__":
    manual = len(sys.argv) > 1
    run(manual)
