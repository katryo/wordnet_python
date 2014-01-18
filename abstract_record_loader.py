import sqlite3


class AbstractRecordLoader(object):
    def __init__(self):
        self.conn = sqlite3.connect('../wnjpn.db')

    def __enter__(self):
        return self

    def __del__(self):
        self.conn.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
