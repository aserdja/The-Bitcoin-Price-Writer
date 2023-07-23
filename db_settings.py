import mysql.connector
import os


USERNAME_OF_DB = os.environ.get("DB_USER")
PASSWORD_OF_DB = os.environ.get("DB_PASSWORD")
HOST = os.environ.get("DB_HOST")
PORT = os.environ.get("DB_PORT")


db = mysql.connector.connect(host= HOST, username= USERNAME_OF_DB, password= PASSWORD_OF_DB)
cursor = db.cursor()