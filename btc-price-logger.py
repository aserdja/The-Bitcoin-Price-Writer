import time
from binance_api_keys import api_key, secret_api_key
from win32com.shell import shell, shellcon
from binance import Client
from datetime import datetime
# aws
from aws_access_keys import access_key, secret_access_key
import boto3
import os
from db_settings import host, username_to_db, password_to_db
from db_functions import create_and_choose_database, create_table_in_db, usedb
import mysql.connector


def write_btc_prices_to_file():
    with open(shell.SHGetFolderPath(0, shellcon.CSIDL_DESKTOP, None, 0) + r'\btc-prices-history.txt', 'w') as file_to_write:
        for price in binance_client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, f"1 Jan, {str(datetime.now().year)}"):
            file_to_write.write(f'{price[1]}, {price[2]}, {price[3]}, {price[4]}' + '\n')


def upload_file_to_s3bucket(name_of_bucket, name_of_directory):
    file_to_upload = shell.SHGetFolderPath(0, shellcon.CSIDL_DESKTOP, None, 0) + r'\btc-prices-history.txt'
    bucket_to_upload = str(name_of_bucket)
    upload_file_key = str(name_of_directory) + 'btc-prices-history.txt'
    aws_client.upload_file(file_to_upload, bucket_to_upload, upload_file_key)
############

binance_client = Client(api_key, secret_api_key)
aws_client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)

create_and_choose_database()
usedb()
create_table_in_db()
