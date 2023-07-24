import mysql.connector
from aws_access_keys import secret_dictionary
import os

db = mysql.connector.connect(host= secret_dictionary['host'],
                             username= secret_dictionary['username'],
                             password= secret_dictionary['password'])
cursor = db.cursor()