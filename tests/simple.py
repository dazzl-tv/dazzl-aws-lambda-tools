import dazzl_aws_lambda_tools as aws_lambda
import json
import os

@profile
def my_func():
    path = os.path.dirname(os.path.realpath('__file__'))
    filename = 'tests/bucket_record.json'

    with open(os.path.join(path, filename)) as f:
        event = json.load(f)

    for record in event['Records']:
        aws_lambda.Tools(record)

if __name__ == '__main__':
    my_func()
