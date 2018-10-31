import boto3

FUNCTION_NAME = 'arn:aws:lambda:us-west-2:317856666432:function:archive'


def get_lambda():
    return boto3.client('lambda', 'us-west-2')

def get_bucket():
    # todo
    pass
