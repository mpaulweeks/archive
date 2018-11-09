import requests

BASE_URL = "http://blog.mpaulweeks.com/data"

def fetch_bookmarks_website():
    url = "%s/bookmarks.json" % BASE_URL
    response = requests.get(url)
    print(response.text)
    data = response.json()
    return [
        website
        for website in data.get('links', [])
        if website.get('url') and website.get('category') != 'Video'
    ]

def fetch_bookmarks_youtube():
    url = "%s/youtube.json" % BASE_URL
    response = requests.get(url)
    return response.json()
