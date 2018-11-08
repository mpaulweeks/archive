
import youtube_dl

# https://www.genyoutube.net/formats-resolution-youtube-videos.html
format_prefs = [
    '137', # mp4 1080p
    '136', # mp4 720p
    '135', # mp4 480p
]

def extract_youtube(vid, filename):
    url = 'https://youtube.com/watch?v=%s' % vid
    ydl_opts = {
        'outtmpl': 'temp/%s' % filename,
    }
    for format in format_prefs:
        ydl_opts['format'] = format
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                return filename
        except Exception as e:
            print(e)
            continue
    return False

import sys
if __name__ == '__main__':
    print(sys.argv[1])
    vid = sys.argv[1]
    extract_youtube(vid, vid + '.mp4')
