access_key = 'AKIAZNULNJTSHMW3EIKA'
secret_access_key = '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'

import boto3
aws_client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)