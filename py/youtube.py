
import youtube_dl

def extract_youtube(vid, filename):
    url = 'https://youtube.com/watch?v=%s' % vid
    ydl_opts = {
        'outtmpl': 'temp/%s' % filename,
        'format': '137', # mp4 1080p
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        out = ydl.download([url])
        print(out)

import sys
if __name__ == '__main__':
    print(sys.argv[1])
    vid = sys.argv[1]
    extract_youtube(vid, vid + '.mp4')
