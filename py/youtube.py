
import sys
import youtube_dl

def extract_youtube(url, filename):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
