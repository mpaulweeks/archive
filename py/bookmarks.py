import requests

# BASE_URL = "http://localhost:4000/data"
BASE_URL = "http://blog.mpaulweeks.com/data"

def fetch_bookmarks_website():
    url = "%s/bookmarks.json" % BASE_URL
    response = requests.get(url)
    print(response.text)
    return response.json()

def fetch_bookmarks_youtube():
    url = "%s/youtube.json" % BASE_URL
    response = requests.get(url)
    return response.json()

