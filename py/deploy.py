from archive.aws import (
    set_lambda,
)


def deploy():
    with open('build/lambda.zip', 'rb') as f:
        zipped_code = f.read()
        set_lambda(zipped_code)


if __name__ == "__main__":
    deploy()
