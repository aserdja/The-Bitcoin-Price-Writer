import time
from binance_api_keys import api_key, secret_api_key
from aws_access_keys import access_key, secret_access_key
from win32com.shell import shell, shellcon
from binance import Client
from datetime import datetime

def write_btc_prices_to_file():
    with open(shell.SHGetFolderPath(0, shellcon.CSIDL_DESKTOP, None, 0) + r'\btc-prices-history.txt', 'w') as file_to_write:
        for price in binance_client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, f"1 Jan, {str(datetime.now().year)}"):
            file_to_write.write(str(round(float(price[4]), 2)) + '\n')


############

binance_client = Client(api_key, secret_api_key)
write_btc_prices_to_file()

while True:
    if datetime.now().hour == 0 and datetime.now().minute == 1:
        write_btc_prices_to_file()
        time.sleep(86300)