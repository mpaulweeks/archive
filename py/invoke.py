import json
from py.archive.aws import (
    FUNCTION_NAME,
    get_lambda,
)

FORCE_TEST = """
{
  "manual": true
}
""".strip()


def invoke():
    lambda_client = get_lambda()
    res = lambda_client.invoke(
        FunctionName=FUNCTION_NAME,
        InvocationType="RequestResponse",
        Payload=FORCE_TEST,
    )
    res_json = json.loads(res['Payload'].read().decode("utf-8"))
    if res_json:
        print(res_json)
    else:
        raise Exception("archive failed")


if __name__ == "__main__":
    invoke()
