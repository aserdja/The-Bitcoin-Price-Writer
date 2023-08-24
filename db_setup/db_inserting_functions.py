from datetime import datetime
import datetime as DT
from api_keys.binance_api_keys import binance_client, Client, CHART
from db_setup.db_settings import db, TABLE_NAME, START_DATE_STRING, END_DATE_STRING, START_DATE_DATETIME
import db_setup.db_functions as dbf

#CONSTANTS
SQL_QUERY_FOR_INSERT = f'insert into {TABLE_NAME} (datetime_of_price, open_price, max_price, min_price, close_price) values (%s, %s, %s, %s, %s);'
DATETIME_ITERATE_STEP = DT.timedelta(minutes=60)


def insert_data_to_db():
    date_to_insert = START_DATE_DATETIME
    for price in binance_client.get_historical_klines(CHART, Client.KLINE_INTERVAL_1HOUR, START_DATE_STRING, END_DATE_STRING):
        cursor = db.cursor()
        with cursor:
            if date_to_insert == DT.datetime(2023, 3, 24, 12, 59): #LAGTIME
                cursor.execute(SQL_QUERY_FOR_INSERT, (date_to_insert, price[1], price[2], price[3], price[4]))
                db.commit()
                date_to_insert += DATETIME_ITERATE_STEP
                date_to_insert += DATETIME_ITERATE_STEP
            else:
                cursor.execute(SQL_QUERY_FOR_INSERT, (date_to_insert, price[1], price[2], price[3], price[4]))
                db.commit()
                date_to_insert += DATETIME_ITERATE_STEP


def insert_one_row():
    try:
        last_date = dbf.get_last_date()
        last_date += DATETIME_ITERATE_STEP
    except:
        last_date = DT.datetime(datetime.now(DT.timezone.utc).year, datetime.now(DT.timezone.utc).month,
                                datetime.now(DT.timezone.utc).day, datetime.now(DT.timezone.utc).hour, 59) - DT.timedelta(minutes=60)

    for price in binance_client.get_historical_klines(CHART, Client.KLINE_INTERVAL_1HOUR, "2 hour ago UTC", END_DATE_STRING):
        cursor = db.cursor()
        with cursor:
            cursor.execute(SQL_QUERY_FOR_INSERT, (last_date, price[1], price[2], price[3], price[4]))
            db.commit()