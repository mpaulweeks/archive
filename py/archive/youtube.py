
import youtube_dl

# https://www.genyoutube.net/formats-resolution-youtube-videos.html
format_prefs = [
    {
        'format': '137', # mp4 1080p
        'ext': 'mp4',
    },
    {
        'format': '136', # mp4 720p
        'ext': 'mp4',
    },
    {
        'format': '135', # mp4 480p
        'ext': 'mp4',
    },
    {
        'format': '134', # mp4 360p
        'ext': 'mp4',
    },
]

def extract_youtube(vid, save_as):
    print('downloading youtube: %s' % save_as)
    url = 'https://youtube.com/watch?v=%s' % vid
    for format in format_prefs:
        filename = '%s.%s' % (save_as, format['ext'])
        ydl_opts = {
            'outtmpl': 'temp/%s' % filename,
            'format': format['format'],
        }
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
