from db_settings import db, DB_NAME, TABLE_NAME
from db_functions import use_db

def check_existence_of_db():
    cursor = db.cursor()
    with cursor:
        cursor.execute('show databases;')
        for database in cursor.fetchall():
            if database[0] == DB_NAME:
                return True

def check_existence_of_table():
    cursor = db.cursor()
    with cursor:
        cursor.execute(f'show tables from {DB_NAME};')
        for table in cursor.fetchall():
            if table[0] == TABLE_NAME:
                return True

def check_length_of_table():
    use_db()
    cursor = db.cursor()
    with cursor:
        cursor.execute(f'select count(id_history) from {TABLE_NAME};')
        for length in cursor.fetchone():
            return int(length)