import datetime
from binance_api_keys import Client, binance_client
from datetime import datetime
from db_settings import db

def create_db_and_table():
    create_database()
    usedb()
    create_table_in_db()
    truncate_table()

def create_database():
    cursor = db.cursor()
    with cursor:
        cursor.execute('CREATE DATABASE IF NOT EXISTS btc_price_saver;')

def usedb():
    cursor = db.cursor()
    with cursor:
        cursor.execute('use btc_price_saver;')

def create_table_in_db():
    cursor = db.cursor()
    sql_query = '''
                    create table if not exists btc_prices_history_hour_interval (
                    id_history int auto_increment primary key,
                    datetime_of_price datetime not null,
                    open_price decimal(9,2) not null,
                    max_price decimal(9,2) not null,
                    min_price decimal(9,2) not null,
                    close_price decimal(9,2) not null
                    ) character set utf8;'''
    with cursor:
        cursor.execute(sql_query)

def truncate_table():
    cursor = db.cursor()
    with cursor:
        cursor.execute('truncate btc_prices_history_hour_interval;')

def insert_data_to_db():
    dayy = 0
    for price in binance_client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, f"1 Jan, {str(datetime.now().year)}"):
        sql_query = 'insert into btc_prices_history_hour_interval (datetime_of_price, open_price, max_price, min_price, close_price) values (%s, %s, %s, %s, %s);'
        cursor = db.cursor()
        with cursor:
            cursor.execute(sql_query, (datetime.now(), price[1], price[2], price[3], price[4]))
            db.commit()