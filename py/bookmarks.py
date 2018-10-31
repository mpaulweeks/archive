import requests

def fetch_bookmarks_website():
    url = "http://blog.mpaulweeks.com/data/bookmarks.json"
    response = requests.get(url)
    return response.json()

def fetch_bookmarks_youtube():
    url = "http://blog.mpaulweeks.com/data/youtube-generated.json"
    response = requests.get(url)
    return response.json()

