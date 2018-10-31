from .aws import (
    FUNCTION_NAME,
    get_lambda,
)


def deploy():
    lambda_client = get_lambda()
    with open('build/lambda.zip', 'rb') as f:
        zipped_code = f.read()
    lambda_client.update_function_code(
        FunctionName=FUNCTION_NAME,
        ZipFile=zipped_code,
    )


if __name__ == "__main__":
    deploy()
