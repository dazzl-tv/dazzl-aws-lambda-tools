# LIB Dazzl Lambda

Library python for simplify to create lambda function (AWS lambda) and Dazzl API service.

The authentication is automatically executed and use a environment variable.

## How to use

```python
# Import
import dazzl

# Initialize
# It's a bucket event
dz = dazzl.Lambda(record)

# Send a request to backend
path = '/super/path/with/id/and/another/data'
body = { 'foo' 'bar' }
dz.send('POST', path, body)

# Get name to bucket
dz.bucket_name

# Get key to bucket
dz.bucket_key
```

## Variables environments

| Name             | Value example    | Required                        |
| --               | --               | --                              |
| `LOG_LEVEL`      | info             | `false`                         |
| `URL_API__<env>` | https://dazzl.tv | `true` if you want send request |
| `USERNAME_<env>` | roger@dazzl.tv   | `true` if you want send request |
| `PASSWORD_<env>` | hidden_password  | `true` if you want send request |

`<env>` represente type environment :
- development : `DEVE`
- staging :  `STAG`
- production : `PROD`

## Convention bucket name

The bucket name exist for three environment :

| Environment | Example bucket name     |
| --          | --                      |
| development | suffix.name.development |
| staging     | suffix.name.staging     |
| production  | suffix.name             |
