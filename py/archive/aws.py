
# import os
# keys = os.environ

import json
with open("local/s3.json") as f:
    keys = json.load(f)

import boto3
def get_bucket():
    session = boto3.Session(
        aws_access_key_id=keys['aws_access_key_id'],
        aws_secret_access_key=keys['aws_secret_access_key'],
        region_name='us-east-1',
    )
    s3 = session.resource('s3')
    return s3.Bucket('mpaulweeks-archive')
