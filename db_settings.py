from datetime import datetime
import datetime as DT
import mysql.connector
from aws_access_keys import secret_dictionary
import os

# CONSTANTS
DB_NAME = secret_dictionary['dbname']
TABLE_NAME = secret_dictionary['tablename']
START_DATE_STRING = f"1 Jan, {str(datetime.now().year)}"
START_DATE_DATETIME = DT.datetime(datetime.now(DT.timezone.utc).year, 1, 1, 0, 59)
END_DATE_STRING = f"1 hour ago UTC"

#CONNECTION
db = mysql.connector.connect(host= secret_dictionary['host'],
                             username= secret_dictionary['username'],
                             password= secret_dictionary['password'])
cursor = db.cursor()