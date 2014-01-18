from abstract_record_loader import AbstractRecordLoader
from collections import namedtuple


class WordLoader(AbstractRecordLoader):
    def __init__(self):
        super().__init__()
        self.word = namedtuple('Word', 'wordid lang lemma pron pos')

    def load_multiple_records(self, lemma):
        cur = self.conn.execute("select * from word where lemma=?", (lemma,))
        return [self.word(*row) for row in cur]

    def load_one_record(self, wordid):
        cur = self.conn.execute("select * from word where wordid=?", (wordid,))
        return self.word(*cur.fetchone())
