# Day08必須課題: 映画データの集計を行う

## 提出方法
- 各自1つの課題用のリポジトリを作成すること
    - ex: `s3projects/day08_kadai_mohira8888_movie_analysis`
- 提出の流れは次のステップになっています
    1. 自分で動作を確認する
    2. 課題用リポジトリのURLを、Classroom上で提出してください(採点に利用します)
    3. 採点結果は、Classroom上でお伝えします

### 提出期限
提出期限はコースごとに異なります。Classroomでの指示に従ってください。


### 解説およびレビューについて
- 解説は動画にておこないます
- 解説動画は **11/13(金) の自習時間 17:00-19:00** に収録および公開します 
    - 提出状況にもよりますが、ライブ講義の形式で行うかもしれません
    - 提出状況にもよりますが、代表者数名のレビューを行うかもしれません
- 解説以外にレビューがほしい場合は、別途issueを立ててください    

### 課題内容に対して質問がある場合は
課題内容に対して質問がある場合は、[Day08必須課題: 映画データの集計を行う Issue #223](https://github.com/s3project2020/QandA/issues/223)にコメントしてください。

### 実装に詰まった場合は
実装に詰まった場合は、いくつかの選択肢があります。

- ヒント: [s3project2020/day08_mohira8888_bob_okozukai](https://github.com/s3project2020/day08_mohira8888_bob_okozukai)
- issueをたてて、他の人に聞いてみる
- 解説動画を待つ
- 勉強会を開催して、みんなでやってみる


## 課題用リポジトリの準備
手順3については、下記のいずれか動画を参考にしてください。

- [2020年11月07日_第8回目講義_土曜日コース_パート10_実装課題の説明](https://vimeo.com/476587960)
- [2020年11月08日_第8回目講義_日曜日コース_パート10_Day08実装課題についての説明](https://vimeo.com/476797855) 
- [2020年11月10日_第8回目講義_火曜日コース_パート10_実装課題の説明 on Vimeo](https://vimeo.com/477502646)

1. `s3projects/day08_kadai_mohira8888_movie_analysis` を Clone する
2. GitHub上で自身のリポジトリをつくる。ex: `s3projects/tunamayo9999_movie_analysis` 
3. リモートリポジトリの origin を 自身のリポジトリに変更する(自身のリポジトリにpushするようにする) 
4. 必要があれば、ローカル上でのプロジェクト名を変更してください(変更しないと`day08_kadai_mohira8888_movie_analysis`になるのでちょっと分かりにくい)。


### 課題用リポジトリのディレクトリ構成
- ファイルおよびディレクトリ構成は次のようになっています。
- 下記の条件を満たせば、自由に他のモジュール(Pythonファイル)を追加して構いません

```
# ディレクトリ構成の例(Clone直後)
day08_kadai_mohira8888_movie_analysis
├── .gitignore
├── README.md
├── expected.csv
├── init.sql
├── main.py
└── my_movies.db # 自動で生成されます
```

```sh
# 実行手順
# 同一ディレクトリにある my_movies.db を読み込み、 output.csv を出力する
$ python main.py
```


### `main.py` の 内容
`main.py` は 最初から次のようなコードが記述されています。`initialize_database()` および `main()` の最初に `initialize_database()` を実行する部分は変更しないよう注意してください。

```python
import sqlite3
from pathlib import Path


def initialize_database() -> None:
    # このコードは改変しないこと
    root_path = Path(__file__).parent

    db_path = root_path / 'my_movies.db'
    conn = sqlite3.connect(db_path)

    init_sql_path = root_path / 'init.sql'
    conn.executescript(init_sql_path.read_text())

    conn.close()


def main():
    initialize_database()

    # 以下から書き始めること！


if __name__ == '__main__':
    main()
```

### `my_movies.csv` の内容
- `main.py` を 実行すればRDBに下記のようなデータが挿入されます。

```csv
id,title,genre,income
1,Arcobaleno selvaggio,Action,600000
2,Colpo basso,Action,63860
3,Dove l'erba si tinge di sangue,Action,1900000
4,A prova di proiettile,Action,807947
5,Race for Glory,Action,100326
...
...(省略)
...
37,Drawing Restraint 9,Fantasy,234743
38,Barbe bleue,Fantasy,33490
39,Cirque du Soleil - Mondi lontani,Fantasy,12512862
40,Ga-lyeo-jin si-gan,Fantasy,57759
```

## 必須要件の内容
映画のジャンル(genre)ごとの収入(income) の合計を`output.csv`に出力してください。正しく実装されていれば、`output.csv`は次のようになります。


```csv
Action,46932995
Fantasy,12838854
Animation,1032156
Crime,538586

```

### 実装できたかどうかの判定
`main.py` を事務局側で実行し、出力された`output.csv`が期待通りになっているかどうかで判断します。

`input()` などでユーザーがから入力を受け取るような実装はしてはいけません。
アプリケーションとして発展させたい場合は、課題合格後、もしくは別プロジェクトで実装しましょう。

完全一致するかどうかで決まるので、余計な出力はしないように気をつけましょう。
`output.csv`の末尾に空行は入っていても除去されていても合格とします。


また、`main.py` や `output.csv` といったファイル名も採点に利用するため、変更しないよう注意してください。



## 応用アイデアの例
必須要件が終わって余力がある人は、自由に拡張しましょう。

以下は、アプリを拡張するアイデアの例です。実装しなくても問題ありません。

もちろん、他のアイデアを実装してもかまいません。

- 新しいデータを追加できるようにする
- 登録済みの映画データを編集できるようにする
- 登録済みの映画データを削除できるようにする
- 他の集計機能を追加する(ex: 総額を計算する, 収益上位N件のみ抽出する など)


以上。
