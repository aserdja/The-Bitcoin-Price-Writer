import boto3
import json


#SECRET KEYS
aws_client = boto3.client('secretsmanager', region_name='eu-central-1')
responce = aws_client.get_secret_value(SecretId='/btc-price-logger/db')
secret_dictionary = json.loads(responce['SecretString'])