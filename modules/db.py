import sqlite3
import logging

from modules.utils import load_config, handle_error


class Database:
    def __init__(self):
        self.config = load_config()
        self.sql_create_project_table = """
            CREATE TABLE IF NOT EXISTS {} (
                id integer PRIMARY KEY,
                uid integer NOT NULL UNIQUE,
                example_bool boolean NOT NULL,
                created text NOT NULL
            );""".format(self.config['DB']['table'])
        self.sql_insert_into_project = """
            INSERT OR IGNORE INTO {} (
                    uid,
                    example_bool,
                    created
                )
                VALUES(?,?)
            """.format(self.config['DB']['table'])

    def db_create_connection(self, db_file='db.sqlite3'):
        """Connect to db/Create `db.sqlite3` in root folder if not exist"""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            logging.info('Connected to db\n')
        except Exception as e:
            handle_error(e)
        return conn

    def db_create_table(self, conn, sql=''):
        """Create project table from `self.sql_create_project_table`
           Optional `sql` kwarg if you want to create new table
        """
        try:
            sql = sql if sql else self.sql_create_project_table
            cur = conn.cursor()
            cur.execute(sql)
        except Exception as e:
            handle_error(e)

    def db_insert_object(self, conn, sql, data):
        """Pass arguments: conn, sql, data; Execute sql; commit"""
        try:
            cur = conn.cursor()
            cur.execute(sql, data)
            conn.commit()
        except Exception as e:
            handle_error(e)

    def db_update_object(self, conn, table, column, field, values):
        """Update table object field values"""
        try:
            cur = conn.cursor()
            cur.execute(f'UPDATE {table} SET {column}=? WHERE {field}=?', values)
            conn.commit()
        except Exception as e:
            handle_error(e)

    def db_delete_object(self, conn, table, field, value):
        """Delete table object"""
        try:
            cur = conn.cursor()
            cur.execute(f'DELETE FROM {table} WHERE {field}=?', value)
            conn.commit()
        except Exception as e:
            handle_error(e)

    def db_get_objects_all(self, conn, table):
        """Return queryset of table objects"""
        try:
            cur = conn.cursor()
            cur.execute(f'SELECT * FROM {table}')
            return cur.fetchall()
        except Exception as e:
            handle_error(e)

    def db_get_objects_filter_by_value(self, conn, table, column, value):
        """Filter db table by column value"""
        try:
            cur = conn.cursor()
            cur.execute(f'SELECT * FROM {table} WHERE {column}=?', (value,))
            return cur.fetchall()
        except Exception as e:
            handle_error(e)

    def db_get_objects_field_values(self, conn, table, field):
        """Select field values from table"""
        try:
            conn.row_factory = lambda cursor, row: row[0]
            cur = conn.cursor()
            return cur.execute(f'SELECT {field} FROM {table}').fetchall()
        except Exception as e:
            handle_error(e)
