"""This module contains the logic to store Tweet data in a sqlite3 database.
"""

import sqlite3


class Storage(object):
    """A helper class to access a sqlite3 database
    """

    def __init__(self, db_path):
        self.table_name = "tweets"
        self.connection = sqlite3.connect(db_path)
        self.create_schema()

    def create_schema(self):
        c = self.connection.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS {} (
                  AUTHOR_ID TEXT   NOT NULL,
                  TWEET     TEXT   NOT NULL)""".format(self.table_name))
        self.connection.commit()

    def __del__(self):
        self.connection.close()

    def insert(self, author_id, tweet_text):
        """Insert a author_id-tweet_text pair into the database
        """
        c = self.connection.cursor()
        c.execute('INSERT INTO {}(AUTHOR_ID, TWEET) VALUES (?,?)'.format(
                  self.table_name), (author_id, tweet_text))
        self.connection.commit()

    def insert_batch(self, batch):
        """Insert a batch of (author_id, tweet_text) tuples into the database
        """
        c = self.connection.cursor()
        c.executemany('INSERT INTO {} VALUES (?,?)'.format(self.table_name),
                      batch)
        self.connection.commit()

