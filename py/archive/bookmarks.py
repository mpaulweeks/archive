import requests

BASE_URL = "http://blog.mpaulweeks.com/data"

def fetch_bookmarks_websites():
    url = "%s/bookmarks.json" % BASE_URL
    response = requests.get(url)
    print(response.text)
    data = response.json()
    return [
        website
        if website.get('url') and website.get('category') != 'Video'
        for website in data.get('links', [])
    ]

def fetch_bookmarks_youtube():
    url = "%s/youtube.json" % BASE_URL
    response = requests.get(url)
    return response.json()
