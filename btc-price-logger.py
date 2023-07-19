import datetime

from db_functions import create_db_and_table, insert_data_to_db, prices_monitoring, compare_last_date, usedb

create_db_and_table()
insert_data_to_db()
compare_last_date()
prices_monitoring()