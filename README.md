wordnet_python
==============

[日本語WordNet](http://nlpwww.nict.go.jp/wn-ja/)をPythonで扱うためのラッパー。

[yanbeさんのコード](https://gist.github.com/yanbe/79057)をPython3.3で動くようにして、ついでにオブジェクト指向的に読みやすくしたもの。

[yanbeさんのブログ記事](http://subtech.g.hatena.ne.jp/y_yanbe/20090314/p2)に詳細が載っている。

Python3.3.1で動作確認。Python2.7.4では動かない。

## 使い方

SQLiteのファイル名をabstract_record_loader.pyに書き込んで（初期設定ではディレクトリ構造1つ上のwnjpn.db）、次のようにターミナル上で実行する。

```
$ python wn.py 夢 hype
```

こうすると、「夢」の上位語を以下のように出力してくれる。

```
夢 dreaming
  イマジネイション imagery
夢 aspiration
  渇き desire
    心緒 feeling
      動静 state
        属性 attribute
          抽象的実体 abstract_entity
夢 dream
夢 want
  渇き desire
    心緒 feeling
      動静 state
        属性 attribute
          抽象的実体 abstract_entity
夢 pipe_dream
  ファンタジー fantasy
    イマジネイション vision
      創造性 creativity
        才幹 ability
          了知 knowledge
```


## DB接続設定

SQLiteデータベースへの接続は、DBのファイル名 wnjpn.db を abstract_record_loader.pyに以下のように書き込む。


```python
import sqlite3


class AbstractRecordLoader(object):
    def __init__(self):
        self.conn = sqlite3.connect('wnjpn.db')
```