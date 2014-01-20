from abstract_record_loader import AbstractRecordLoader
from collections import namedtuple


class SynlinkLoader(AbstractRecordLoader):
    def __init__(self):
        super().__init__()
        self.synlink = namedtuple('SynLink', 'synset1 synset2 link src')

    def load_synlinks_with_sense_and_link(self, sense, link):
        cur = self.conn.execute("select * from synlink where synset1=? and link=?",
                               (sense.synset, link))
        return [self.synlink(*row) for row in cur]

