import boto3

FUNCTION_NAME = 'arn:aws:lambda:us-west-1:317856666432:function:archive'


def get_lambda():
    return boto3.client('lambda', 'us-west-1')

def get_bucket():
    session = boto3.Session(region_name=keys['us-east-1'])
    s3 = session.resource('s3')
    return s3.Bucket(archive)
