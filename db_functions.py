from db_settings import db

def create_and_choose_database():
    cursor = db.cursor()
    with cursor:
        cursor.execute('CREATE DATABASE IF NOT EXISTS btc_prices_saver1;')

def usedb():
    cursor = db.cursor()
    with cursor:
        cursor.execute('use btc_prices_saver1;')

def create_table_in_db():
    cursor = db.cursor()
    sql_query = '''
                    create table if not exists btc_prices_history_1hour_interval (
                    id_history int auto_increment primary key,
                    datetime_of_price datetime not null unique,
                    open_price decimal(9,2) not null,
                    max_price decimal(9,2) not null,
                    min_price decimal(9,2) not null,
                    close_price decimal(9,2) not null
                    ) character set utf8;'''
    with cursor:
        cursor.execute(sql_query)