from .aws import (
    get_bucket,
)

def upload_file(dest_dir, file_name):
    file_path = "temp/%s" % file_name
    destination = "%s%s" % (dest_dir, file_name)
    print("uploading %s to %s" % (file_path, destination))
    with open(file_path, 'rb') as data:
        get_bucket().put_object(Key=destination, Body=data)

def download_file(s3_path, local_path):
    print ("downloading %s to %s" % (s3_path, local_path))
    get_bucket().download_file(Key=s3_path, Filename=local_path)

def upload_website(file_name):
    upload_file('website/', file_name)

def upload_youtube(file_name):
    upload_file('youtube/', file_name)
