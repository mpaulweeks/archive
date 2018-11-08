
from datetime import datetime
import os
import sys

from py.archive.bookmarks import (
    fetch_bookmarks_website,
    fetch_bookmarks_youtube,
)
from py.archive.state import (
    load_state,
    save_state,
)
from py.archive.s3 import (
    upload_website,
    upload_youtube,
)
from py.archive.pdf import (
    extract_website,
)
from py.archive.youtube import (
    extract_youtube,
)

def get_now():
    return datetime.utcnow().strftime("%Y/%m/%d")

def archive_website(state):
    bookmarks = fetch_bookmarks_website()
    website_state = state.get('website', {})
    remaining = 3

    for website in bookmarks.get('links', []):
        url = website.get('url')
        if url and website.get('category') != 'Video':
            name = website.get('title')
            key = url
            save_as = name
            if key not in website_state:
                filename = extract_website(url, save_as)
                if filename:
                    upload_website(filename)
                    website_state[key] = {
                        "url": url,
                        "name": name,
                        "fetched": get_now(),
                    }
                    remaining -= 1
        if remaining < 1:
            break
    state['website'] = website_state

def archive_youtube(state):
    now = get_now()
    videos = fetch_bookmarks_youtube()
    youtube_state = state.get('youtube', {})
    remaining = 1

    for video in videos:
        vid = video.get('vid')
        name = video.get('title')

        # todo
        # if vid != 'aiM5KDuHrR4':
        #     continue

        key = vid
        save_as = '%s - %s.mp4' % (
            vid, name
        )
        if key not in youtube_state:
            filename = extract_youtube(vid, save_as)
            if filename:
                upload_youtube(filename)
                youtube_state[key] = {
                    "vid": vid,
                    "name": name,
                    "fetched": get_now(),
                }
                remaining -= 1
        if remaining < 1:
            break
    state['youtube'] = youtube_state



def run(manual):
    print('hello')
    return
    
    state = load_state()

    try:
        # archive_website(state)
        pass
    except Exception as e:
        pass

    try:
        archive_youtube(state)
    except Exception as e:
        pass

    save_state(state)

def lambda_handler(json_input, context):
    manual = json_input.get('manual')
    return run(manual)

if __name__ == "__main__":
    manual = len(sys.argv) > 1
    run(manual)
