from abstract_record_loader import AbstractRecordLoader
from collections import namedtuple


class SenseLoader(AbstractRecordLoader):
    def __init__(self):
        super().__init__()
        self.sense = namedtuple('Sense', 'synset wordid lang rank lexid freq src')

    def load_senses_with_synset(self, word):
        cur = self.conn.execute("select * from sense where wordid=?", (word.wordid,))
        return [self.sense(*row) for row in cur]

    def load_sense_with_synset(self, synset, lang='jpn'):
        cur = self.conn.execute("select * from sense where synset=? and lang=?",
                                (synset, lang))
        row = cur.fetchone()
        return row and self.sense(*row) or None
