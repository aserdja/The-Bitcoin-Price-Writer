# aws
from aws_access_keys import access_key, secret_access_key
import boto3
import os
from db_settings import host, username_to_db, password_to_db
from db_functions import create_db_and_table, insert_data_to_db

############


aws_client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)

create_db_and_table()
insert_data_to_db()
