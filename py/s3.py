from .aws import (
    get_bucket,
)

def upload_file(destination, filename):
    s3_client = get_bucket()
    with open('temp/%s' % filename, 'rb') as f:
        # todo
        pass


def upload_website(filename):
    upload_file('website', filename)

def upload_youtube(filename):
    upload_file('youtube', filename)
