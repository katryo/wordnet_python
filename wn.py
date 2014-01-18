# encoding: utf-8
# Python3.3
import sys
from sense_loader import SenseLoader
from word_loader import WordLoader
from synset_loader import SynsetLoader
from synlink_loader import SynlinkLoader


def getSynLinksRecursive(senses, link, lang='jpn', _depth=0):
    for sense in senses:
        synlink_loader = SynlinkLoader()
        synlinks = synlink_loader.load_multiple_records(sense, link)
        if synlinks:
            word_loader = WordLoader()
            synset_loader = SynsetLoader()
            print(''.join([' ' * 2 * _depth,
                           word_loader.load_one_record(sense.wordid).lemma,
                           ' ',
                           synset_loader.load_one_record(sense.synset).name]))
        _senses = []
        sense_loader = SenseLoader()
        for synLink in synlinks:
            sense = sense_loader.load_one_record(synLink.synset2, lang)
            if sense:
                _senses.append(sense)

        getSynLinksRecursive(_senses, link, lang, _depth + 1)


if __name__ == '__main__':
    if len(sys.argv) >= 3:
        word_loader = WordLoader()
        words = word_loader.load_multiple_records(sys.argv[1])
        if words:
            sense_loader = SenseLoader()
            senses = sense_loader.load_multiple_records(words[0])
            link = len(sys.argv) >= 3 and sys.argv[2] or 'hypo'
            lang = len(sys.argv) == 4 and sys.argv[3] or 'jpn'
            getSynLinksRecursive(senses, link, lang)
        else:
            print("(nothing found)", file=sys.stderr)
    else:
        print("""usage: wn.py word link [lang]
            word
              word to investigate

            link
              syns - Synonyms
              hype - Hypernyms
              inst - Instances
              hypo - Hyponym
              hasi - Has Instance
              mero - Meronyms
              mmem - Meronyms --- Member
              msub - Meronyms --- Substance
              mprt - Meronyms --- Part
              holo - Holonyms
              hmem - Holonyms --- Member
              hsub - Holonyms --- Substance
              hprt - Holonyms -- Part
              attr - Attributes
              sim - Similar to
              entag - Entails
              causg - Causes
              dmncg - Domain --- Category
              dmnug - Domain --- Usage
              dmnrg - Domain --- Region
              dmtcg - In Domain --- Category
              dmtug - In Domain --- Usage
              dmtrg - In Domain --- Region
              antsg - Antonyms

            lang (default: jpn)
              jpn - Japanese
              eng - English
           """)
