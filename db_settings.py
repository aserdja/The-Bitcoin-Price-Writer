username_to_db = r'root'
password_to_db = r'12345678'
host = r'btc-price-logger.cdbhvtoh9vtx.eu-central-1.rds.amazonaws.com'
port = 3306

import mysql.connector
db = mysql.connector.connect(host= host, username= username_to_db, password= password_to_db)
cursor = db.cursor()