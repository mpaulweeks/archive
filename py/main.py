
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
from py.archive.website import (
    extract_website_zip,
)
from py.archive.youtube import (
    extract_youtube,
)

def get_today():
    return datetime.utcnow().strftime("%Y/%m/%d")

def sanitize(filename):
    return (
        filename
            .replace('/', '_')
            .replace(':', '-')
            .replace('?', '')
    )

def archive_website(state):
    bookmarks = fetch_bookmarks_websites()
    website_state = state.get('website', {})
    remaining = 3

    for website in bookmarks:
        url = website.get('url')
        name = website.get('title')
        key = url
        save_as = sanitize(name)
        if key not in website_state:
            filename = extract_website(url, save_as)
            if filename:
                upload_website(filename)
                website_state[key] = {
                    "url": url,
                    "name": name,
                    "fetched": get_today(),
                }
                remaining -= 1
        if remaining < 1:
            break
    state['website'] = website_state

def archive_website_zip(state):
    bookmarks = fetch_bookmarks_websites()
    zip_state = state.get('website_zip', {})
    remaining = 3

    for website in bookmarks:
        url = website.get('url')
        name = website.get('title')
        key = url
        save_as = sanitize(name)
        if key not in zip_state:
            filename = extract_website_zip(url, save_as)
            if filename:
                upload_website(filename)
                zip_state[key] = {
                    "url": url,
                    "name": name,
                    "fetched": get_today(),
                }
                remaining -= 1
        if remaining < 1:
            break
    state['website_zip'] = zip_state

def archive_youtube(state):
    videos = fetch_bookmarks_youtube()
    youtube_state = state.get('youtube', {})
    remaining = 1

    for video in videos:
        vid = video.get('vid')
        name = video.get('title')

        key = vid
        save_as = sanitize('%s - %s' % (
            vid, name
        ))
        if key not in youtube_state:
            filename = extract_youtube(vid, save_as)
            if filename:
                upload_youtube(filename)
                youtube_state[key] = {
                    "vid": vid,
                    "name": name,
                    "fetched": get_today(),
                }
                remaining -= 1
        if remaining < 1:
            break
    state['youtube'] = youtube_state

def run(manual):
    state = load_state()

    try:
        archive_website(state)
        pass
    except Exception as e:
        pass

    try:
        archive_youtube(state)
        pass
    except Exception as e:
        pass

    state['meta'] = {
        'updated': datetime.utcnow().isoformat(),
    }
    save_state(state)

if __name__ == "__main__":
    manual = len(sys.argv) > 1
    run(manual)
