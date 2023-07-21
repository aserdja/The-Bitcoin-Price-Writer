access_key = ''
secret_access_key = ''

import boto3
aws_client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)
