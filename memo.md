# 📝 2024/05/15


`test_buttonViewController.py`



旧ブランチを参照するのがめんどうになった、、、



[UIButton.Configuration その1 〜角の丸みもお手のもの](https://zenn.dev/samekard_dev/articles/64d8f1578a7bb6)

# 📝 2024/05/14

`0.4.9`

## storyboard

`ButtonViewController.storyboard`


`reuseIdentifier` をどう捌くか？


サイズはよしなにやってもらう？



# 📝 2024/05/09


[なぜUITableViewControllerを使うなと言われるのか #iOS - Qiita](https://qiita.com/yosshi4486/items/33132718a0fb08273a45)






# 📝 2024/04/24

改めてstoryboard について考えてみる

- storyboard 内で完成をさせて、出せるようにする
  - 今回の場合は、`tests` の中で出せるようにしたい
  - 私の場合だと、`prototypes` の中を実装する
  - 




# 📝 2024/04/23

作業ログをしっかりとる

# 📝 2024/04/21

## `caseElement.py`

コピペした、呼び出し方法を書き換えないと

## 次は？storyboard かな？

作成手順を忘れた

# 📝 2024/04/20


## `enumerations.py` の命名定義

基本的に、objc の名前で揃える。

Swift だと`.` が入ったり、Document で、Enumeration として型表記になってない場合もある。
その場合には、値としてDocument で参照しやすい方にする。



`.` は、`_` で繋ぐ


[pystaUIKitCatalogChallenge/objcista/constants.py at objc_util · pome-ta/pystaUIKitCatalogChallenge · GitHub](https://github.com/pome-ta/pystaUIKitCatalogChallenge/blob/objc_util/objcista/constants.py)

基本的には、ここをコピペ、使用するタイミングで、都度Document を参照する。


## `tests` ディレクトリ

``` .py
parent_level = 3
sys.path.append(str(pathlib.Path(__file__, '../' * parent_level).resolve()))
```

無理やりmodule をブチ込む、`sandbox` として、test 前の実験の場合は、level を階層に応じて指定する（test の意味とは）

まぁ、iPhone とworking copy との`.cloud` ファイル問題なんだけど、、、





# 📝 2024/04/19

## 運用想定

ディレクトリ直下には、Catalog としてのファイルを入れていく。Rubicon のためとしてのファイルは、`rbedge` にゴリゴリと入れていく

直下はあくまでも、Catalog のサンプル内容とイコールな関係としていきたい

## `rbedge`

独自のRubicon のライブラリとして、作ったファイルを置いていく

### 命名理由

Rubicon が多分「川」の意味があると思われるので、川の「端」として、「edge」 で、Rubicon の「r」と「b」 を付けて「rbedge」 とした。
ざっとググって、名前が被らないかは確認した。

### 運用方法

Python として正しくはないかもだけど、`pyrubicon` モジュールを読み込みをするので、直下に`test` ディレクトリを作成して、そのディレクトリ内で挙動の確認をする。

読み込みは、`sys` モジュールで無理やりpath を取得する流れ。

## ファイルの配置やら関連性について

rootNav 系を先に準備したが、実行するためとすると、裏側での動きだから、他のもの準備した方がいいのではないかと思う。

あと、定数ではなくenum をひとつひとつ書いていくしかないのかなぁというお気持ち


