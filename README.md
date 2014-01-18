wordnet_python
==============

[日本語WordNet](http://nlpwww.nict.go.jp/wn-ja/)をPythonで扱うためのラッパー。

[yanbeさんのコード](https://gist.github.com/yanbe/79057)をPython3.3でも動くようにして、ついでにオブジェクト指向的に読みやすくしたもの。

[yanbeさんのブログ記事](http://subtech.g.hatena.ne.jp/y_yanbe/20090314/p2)に詳細が載っている。

SQLiteデータベースへの接続は、DBのファイル名 wnjpn.db を abstract_record_loader.pyに以下のように書き込む。


```python
import sqlite3


class AbstractRecordLoader(object):
    def __init__(self):
        self.conn = sqlite3.connect('wnjpn.db')
```