import datetime as DT
import time
from datetime import datetime
from db_setup.db_settings import db, DB_NAME, TABLE_NAME
import db_setup.db_inserting_functions as dbif


def create_database():
    cursor = db.cursor()
    with cursor:
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DB_NAME};')


def use_db():
    cursor = db.cursor()
    with cursor:
        cursor.execute(f'use {DB_NAME};')


def create_table_in_db():
    use_db()
    cursor = db.cursor()
    sql_query = f'''
                    create table if not exists {TABLE_NAME} (
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
        cursor.execute(f'truncate {TABLE_NAME};')


def get_last_date():
    cursor = db.cursor(buffered=True)
    with cursor:
        cursor.execute(f'select datetime_of_price from {DB_NAME}.{TABLE_NAME} order by datetime_of_price desc limit 1;')
        for row in cursor.fetchone():
            return row


def compare_last_date():
    utc_dt = datetime.now(DT.timezone.utc)
    date_hour_ago = datetime(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour, 59) - dbif.DATETIME_ITERATE_STEP

    if get_last_date() != date_hour_ago:
        if get_last_date().year != date_hour_ago.year:
            truncate_table()
            dbif.insert_one_row()
            prices_monitoring()
        else:
            dbif.insert_one_row()


def prices_monitoring():
    while True:
        if DT.datetime(datetime.now(DT.timezone.utc).year, datetime.now(DT.timezone.utc).month,
                       datetime.now(DT.timezone.utc).day, datetime.now(DT.timezone.utc).hour,
                       datetime.now(DT.timezone.utc).minute) == DT.datetime(datetime.now(DT.timezone.utc).year, 1, 1, 1, 1):
            truncate_table()
            dbif.insert_one_row()
            time.sleep(1000)
        elif datetime.now().minute == 1:
            dbif.insert_one_row()
            time.sleep(1000)


def check_current_date():
    if DT.datetime(datetime.now(DT.timezone.utc).year, datetime.now(DT.timezone.utc).month, datetime.now(DT.timezone.utc).day,
                   datetime.now(DT.timezone.utc).hour, datetime.now(DT.timezone.utc).minute) < DT.datetime(datetime.now(DT.timezone.utc).year, 1, 1, 1, 1):
        prices_monitoring()
    else:
        dbif.insert_data_to_db()