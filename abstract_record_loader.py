import sqlite3


class AbstractRecordLoader(object):
    def __init__(self):
        self.conn = sqlite3.connect('wnjpn.db')
