import dazzl
import json
import os

@profile
def my_func():
    os.environ['USERNAME_DEVE']="user@dazzl.local"
    os.environ['PASSWORD_DEVE']="6tmseb"
    os.environ['URL_API_DEVE']="https://api.dazzl.local"

    path = os.path.dirname(os.path.realpath('__file__'))
    filename = 'tests/bucket_record.json'

    with open(os.path.join(path, filename)) as f:
        event = json.load(f)

    for record in event['Records']:
        path = '/cgus/5b96422ee76ed00001d0a9fa'
        body = {}
        dz = dazzl.Lambda(record)

        dz.send_request('GET', path, body)

if __name__ == '__main__':
    my_func()
