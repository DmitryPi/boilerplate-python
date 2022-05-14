import logging

from modules.db import Database
from modules.utils import load_config


if __name__ == '__main__':
    config = load_config()
    logging_fmt = '%(name)s - %(levelname)s - %(message)s'

    if config['MAIN']['debug']:
        logging.basicConfig(level=logging.INFO, format=logging_fmt)
    else:
        """TODO sentry setup"""
        logging.basicConfig(level=logging.WARNING, format=logging_fmt)

    # Database init
    db = Database()
    db_conn = db.db_create_connection()
    db.db_create_table(db_conn)
