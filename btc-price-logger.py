from db_setup.db_functions import (create_database, create_table_in_db, truncate_table, compare_last_date,
                                   prices_monitoring, check_current_date)


create_database()
create_table_in_db()
truncate_table()
check_current_date()
compare_last_date()
prices_monitoring()