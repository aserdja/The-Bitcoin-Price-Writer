import unittest
from db_setup.db_inserting_functions import insert_one_row
from db_setup.db_functions import create_database, create_table_in_db, truncate_table
from db_setup.db_settings import db
from tests.test_functions import *


class TestPriceLogger(unittest.TestCase):

    def test_connect_to_database(self):
        self.assertTrue(db.is_connected())

    def test_create_database(self):
        create_database()
        self.assertTrue(check_existence_of_db())

    def test_create_table_in_db(self):
        create_table_in_db()
        self.assertTrue(check_existence_of_table())

    def test_insert_one_row(self):
        first_value = check_length_of_table()
        insert_one_row()
        self.assertTrue(check_length_of_table() > first_value)

    def test_truncate_table(self):
        truncate_table()
        self.assertTrue(check_length_of_table() == 0)