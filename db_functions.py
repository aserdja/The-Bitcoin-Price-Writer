import datetime as DT
import time
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
                    datetime_of_price datetime not null unique,
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
    date_to_insert = DT.datetime(datetime.now(DT.timezone.utc).year, 1, 1, 0, 59)
    for price in binance_client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, f"1 Jan, {str(datetime.now().year)}",
                                                      f"1 hour ago UTC"):
        sql_query = 'insert into btc_prices_history_hour_interval (datetime_of_price, open_price, max_price, min_price, close_price) values (%s, %s, %s, %s, %s);'
        cursor = db.cursor()
        with cursor:
            if date_to_insert == DT.datetime(2023, 3, 24, 12, 59):
                cursor.execute(sql_query, (date_to_insert, price[1], price[2], price[3], price[4]))
                db.commit()
                date_to_insert += step_to_iterate
                date_to_insert += step_to_iterate
            else:
                cursor.execute(sql_query, (date_to_insert, price[1], price[2], price[3], price[4]))
                db.commit()
                date_to_insert += step_to_iterate
    return date_to_insert


def get_last_date():
    cursor = db.cursor(buffered=True)
    with cursor:
        cursor.execute('select datetime_of_price from btc_price_saver.btc_prices_history_hour_interval order by datetime_of_price desc limit 1;')
        for row in cursor.fetchone():
            return row
    

def insert_one_row():
    last_date = get_last_date()
    last_date += step_to_iterate
    sql_query = 'insert into btc_prices_history_hour_interval (datetime_of_price, open_price, max_price, min_price, close_price) values (%s, %s, %s, %s, %s);'
    for price in binance_client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, "2 hour ago UTC", '1 hour ago UTC'):
        cursor = db.cursor()
        with cursor:
            cursor.execute(sql_query, (last_date, price[1], price[2], price[3], price[4]))
            db.commit()


def compare_last_date():
    utc_dt = datetime.now(DT.timezone.utc)
    if get_last_date() != datetime(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour, 59) - DT.timedelta(minutes=60):
        insert_one_row()


def prices_monitoring():
    while True:
        if DT.datetime(datetime.now(DT.timezone.utc).year, datetime.now(DT.timezone.utc).month,
                       datetime.now(DT.timezone.utc).day, datetime.now(DT.timezone.utc).hour,
                       datetime.now(DT.timezone.utc).minute) == DT.datetime(datetime.now(DT.timezone.utc).year, 1, 1, 1, 1):
            usedb()
            truncate_table()
            usedb()
            insert_data_to_db()
        elif datetime.now().minute == 1 and datetime.now().second == 1:
            insert_one_row()
            time.sleep(1000)


step_to_iterate = DT.timedelta(minutes=60)