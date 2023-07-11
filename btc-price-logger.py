import time
from binance_api_keys import api_key, secret_api_key
from win32com.shell import shell, shellcon
from binance import Client
from datetime import datetime
# aws
from aws_access_keys import access_key, secret_access_key
import boto3
import os

def write_btc_prices_to_file():
    with open(shell.SHGetFolderPath(0, shellcon.CSIDL_DESKTOP, None, 0) + r'\btc-prices-history.txt', 'w') as file_to_write:
        for price in binance_client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, f"1 Jan, {str(datetime.now().year)}"):
            file_to_write.write(str(round(float(price[4]), 2)) + '\n')

def upload_file_to_s3bucket(name_of_bucket, name_of_directory):
    file_to_upload = shell.SHGetFolderPath(0, shellcon.CSIDL_DESKTOP, None, 0) + r'\btc-prices-history.txt'
    bucket_to_upload = str(name_of_bucket)
    upload_file_key = str(name_of_directory) + 'btc-prices-history.txt'
    aws_client.upload_file(file_to_upload, bucket_to_upload, upload_file_key)
############

binance_client = Client(api_key, secret_api_key)
aws_client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)

write_btc_prices_to_file()
upload_file_to_s3bucket('btc-prices-data', 'prices-history/')

while True:
    if datetime.now().hour == 0 and datetime.now().minute == 1:
        write_btc_prices_to_file()
        upload_file_to_s3bucket('btc-prices-data', 'prices-history/')
        time.sleep(86300)