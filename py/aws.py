import os

import boto3

keys = os.environ

def set_lambda(zipped_code):
    lambda_client = boto3.client(
        'lambda',
        aws_access_key_id=keys['aws_access_key_id'],
        aws_secret_access_key=keys['aws_secret_access_key'],
        region_name='us-east-1',
    )
    lambda_client.update_function_code(
        FunctionName='arn:aws:lambda:us-east-1:988820348419:function:lambda-archive',
        ZipFile=zipped_code,
    )

def get_bucket():
    session = boto3.Session(
        aws_access_key_id=keys['aws_access_key_id'],
        aws_secret_access_key=keys['aws_secret_access_key'],
        region_name='us-east-1',
    )
    s3 = session.resource('s3')
    return s3.Bucket('mpaulweeks-archive')
