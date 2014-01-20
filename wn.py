# encoding: utf-8
# For Python3.3 or higher.
# You cannot use it with Python 2.7 or lower because of super() function.
import sys
from sense_loader import SenseLoader
from word_loader import WordLoader
from synset_loader import SynsetLoader
from synlink_loader import SynlinkLoader


def print_synlinks_recursively(senses, link, lang='jpn', _depth=0):
    for sense in senses:
        with SynlinkLoader() as synlink_loader:
            synlinks = synlink_loader.load_synlinks_with_sense_and_link(sense, link)
        if synlinks:
            with WordLoader() as word_loader:
                with SynsetLoader() as synset_loader:
                    print(''.join([
                        ' ' * 2 * _depth,
                        word_loader.load_word_with_wordid(sense.wordid).lemma,
                        ' ',
                        synset_loader.load_synset_with_synset(sense.synset).name]))
        _senses = []
        for synLink in synlinks:
            with SenseLoader() as sense_loader:
                sense = sense_loader.load_sense_with_synset(synLink.synset2, lang)
            if sense:
                _senses.append(sense)

        print_synlinks_recursively(_senses, link, lang, _depth + 1)


if __name__ == '__main__':
    if len(sys.argv) >= 3:
        with WordLoader() as word_loader:
            words = word_loader.load_words_with_lemma(sys.argv[1])
        if words:
            with SenseLoader() as sense_loader:
                senses = sense_loader.load_senses_with_synset(words[0])

            if len(sys.argv) >= 3:
                link = sys.argv[2]
            else:
                link = 'hypo'

            if len(sys.argv) == 4:
                lang = sys.argv[3]
            else:
                lang = 'jpn'

            print_synlinks_recursively(senses, link, lang)
            sys.exit()

        print("(nothing found)", file=sys.stderr)
        sys.exit()

    # 引数の書き方を間違えたときなどにはhelpを表示
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

        例(example)
          python wn.py 夢 hype
       """)
