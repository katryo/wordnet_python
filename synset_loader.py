from abstract_record_loader import AbstractRecordLoader
from collections import namedtuple


class SynsetLoader(AbstractRecordLoader):
    def __init__(self):
        super().__init__()
        self.synset = namedtuple('Synset', 'synset pos name src')

    def load_synset_with_synset(self, synset):
        cur = self.conn.execute("select * from synset where synset=?", (synset,))
        return self.synset(*cur.fetchone())
