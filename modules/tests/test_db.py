from unittest import TestCase
from pathlib import Path

from modules.db import Database


class TestDatabase(TestCase):
    def setUp(self):
        db = Database()
        self.test_db = 'testdb.sqlite3'
        self.db_conn = db.db_create_connection(db_file=self.test_db)

    def tearDown(self):
        """Delete test associated files"""
        pass

    def test_db_create_connection(self):
        self.assertTrue(self.db_conn)
        print(Path(self.test_db).is_file())
        self.assertTrue(Path(self.test_db).is_file())
