import os

from py.archive.aws import (
    get_bucket,
)

def upload_file(dest_dir, file_name, acl):
    file_path = "temp/%s" % file_name
    destination = "%s%s" % (dest_dir, file_name)
    print("uploading %s to %s" % (file_path, destination))
    with open(file_path, 'rb') as data:
        get_bucket().put_object(
            ACL=acl,
            Key=destination,
            Body=data,
        )
    print("done! now deleting: %s" % file_path)
    os.remove(file_path)

def download_file(s3_path, local_path):
    print ("downloading %s to %s" % (s3_path, local_path))
    get_bucket().download_file(Key=s3_path, Filename=local_path)

def upload_website_pdf(file_name):
    upload_file('website/', file_name, 'private')

def upload_website_zip(file_name):
    upload_file('website_zip/', file_name, 'private')

def upload_youtube(file_name):
    upload_file('youtube/', file_name, 'private')
