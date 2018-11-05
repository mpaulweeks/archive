import os

import boto3

FUNCTION_NAME = 'arn:aws:lambda:us-east-1:317856666432:function:archive'

keys = os.environ

def get_lambda():
    return boto3.client('lambda', 'us-east-1')

def get_bucket():
    session = boto3.Session(
        aws_access_key_id=keys['aws_access_key_id'],
        aws_secret_access_key=keys['aws_secret_access_key'],
        region_name='us-east-1',
    )
    s3 = session.resource('s3')
    return s3.Bucket('mpaulweeks-archive')
