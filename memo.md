# 📝 2024/07/01


[NSDiffableDataSourceSnapshot | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot?language=objc)

[NSDiffableDataSourceSectionSnapshot | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshot?language=objc)


## simulator

```
--- snapshot01
print
NSDiffableDataSourceSnapshot<Int, String>(_implWrapper: UIKit.NSDiffableDataSourceSnapshot<Swift.Int, Swift.String>.(unknown context at $7ff8066d32e4).ImplWrapper)
dump
▿ UIKit.NSDiffableDataSourceSnapshot<Swift.Int, Swift.String>
  ▿ _implWrapper: UIKit.NSDiffableDataSourceSnapshot<Swift.Int, Swift.String>.(unknown context at $7ff8066d32e4).ImplWrapper #0
    - impl: <__UIDiffableDataSourceSnapshot 0x600003e24400: sectionCounts=<_UIDataSourceSnapshotter: 0x600000240fa0; 0 sections with item counts: [] >; sections=[0x60000001c020]; identifiers=[0x60000001c020]> #1
      - super: __UIDiffableDataSource
        - super: NSObject
--- snapshot02
print
NSDiffableDataSourceSnapshot<Int, String>(_implWrapper: UIKit.NSDiffableDataSourceSnapshot<Swift.Int, Swift.String>.(unknown context at $7ff8066d32e4).ImplWrapper)
dump
▿ UIKit.NSDiffableDataSourceSnapshot<Swift.Int, Swift.String>
  ▿ _implWrapper: UIKit.NSDiffableDataSourceSnapshot<Swift.Int, Swift.String>.(unknown context at $7ff8066d32e4).ImplWrapper #0
    - impl: <__UIDiffableDataSourceSnapshot 0x600003e24400: sectionCounts=<_UIDataSourceSnapshotter: 0x60000023c7e0; 1 section with item counts: [0] >; sections=[0x60000023c7c0]; identifiers=[0x60000023c780]> #1
      - super: __UIDiffableDataSource
        - super: NSObject
--- snapshot03
print
NSDiffableDataSourceSnapshot<Int, String>(_implWrapper: UIKit.NSDiffableDataSourceSnapshot<Swift.Int, Swift.String>.(unknown context at $7ff8066d32e4).ImplWrapper)
dump
▿ UIKit.NSDiffableDataSourceSnapshot<Swift.Int, Swift.String>
  ▿ _implWrapper: UIKit.NSDiffableDataSourceSnapshot<Swift.Int, Swift.String>.(unknown context at $7ff8066d32e4).ImplWrapper #0
    - impl: <__UIDiffableDataSourceSnapshot 0x600003e24400: sectionCounts=<_UIDataSourceSnapshotter: 0x60000023c820; 1 section with item counts: [7] >; sections=[0x60000023c800]; identifiers=[0x60000023c6c0]> #1
      - super: __UIDiffableDataSource
        - super: NSObject
```


```
--- Section.main
main
- UICollectionViewSimpleList1.ViewController.Section.main

--- snapshot01
NSDiffableDataSourceSnapshot<Section, String>(_implWrapper: UIKit.NSDiffableDataSourceSnapshot<UICollectionViewSimpleList1.ViewController.Section, Swift.String>.(unknown context at $7ff8066d32e4).ImplWrapper)

▿ UIKit.NSDiffableDataSourceSnapshot<UICollectionViewSimpleList1.ViewController.Section, Swift.String>
  ▿ _implWrapper: UIKit.NSDiffableDataSourceSnapshot<UICollectionViewSimpleList1.ViewController.Section, Swift.String>.(unknown context at $7ff8066d32e4).ImplWrapper #0
    - impl: <__UIDiffableDataSourceSnapshot 0x600003e0d600: sectionCounts=<_UIDataSourceSnapshotter: 0x6000002390a0; 0 sections with item counts: [] >; sections=[0x600000010100]; identifiers=[0x600000010100]> #1
      - super: __UIDiffableDataSource
        - super: NSObject

--- snapshot02
NSDiffableDataSourceSnapshot<Section, String>(_implWrapper: UIKit.NSDiffableDataSourceSnapshot<UICollectionViewSimpleList1.ViewController.Section, Swift.String>.(unknown context at $7ff8066d32e4).ImplWrapper)

▿ UIKit.NSDiffableDataSourceSnapshot<UICollectionViewSimpleList1.ViewController.Section, Swift.String>
  ▿ _implWrapper: UIKit.NSDiffableDataSourceSnapshot<UICollectionViewSimpleList1.ViewController.Section, Swift.String>.(unknown context at $7ff8066d32e4).ImplWrapper #0
    - impl: <__UIDiffableDataSourceSnapshot 0x600003e0d600: sectionCounts=<_UIDataSourceSnapshotter: 0x600000231640; 1 section with item counts: [0] >; sections=[0x600000231620]; identifiers=[0x6000002315e0]> #1
      - super: __UIDiffableDataSource
        - super: NSObject

--- snapshot03
NSDiffableDataSourceSnapshot<Section, String>(_implWrapper: UIKit.NSDiffableDataSourceSnapshot<UICollectionViewSimpleList1.ViewController.Section, Swift.String>.(unknown context at $7ff8066d32e4).ImplWrapper)

▿ UIKit.NSDiffableDataSourceSnapshot<UICollectionViewSimpleList1.ViewController.Section, Swift.String>
  ▿ _implWrapper: UIKit.NSDiffableDataSourceSnapshot<UICollectionViewSimpleList1.ViewController.Section, Swift.String>.(unknown context at $7ff8066d32e4).ImplWrapper #0
    - impl: <__UIDiffableDataSourceSnapshot 0x600003e0d600: sectionCounts=<_UIDataSourceSnapshotter: 0x600000240680; 1 section with item counts: [7] >; sections=[0x600000240660]; identifiers=[0x60000022d9a0]> #1
      - super: __UIDiffableDataSource
        - super: NSObject
```


# 📝 2024/06/30

```
NSDiffableDataSourceSnapshot<Section, String>(_implWrapper: UIKit.NSDiffableDataSourceSnapshot<UICollectionViewSimpleList1.ViewController.Section, Swift.String>.(unknown context at $7ff8066d32e4).ImplWrapper)
---
▿ UIKit.NSDiffableDataSourceSnapshot<UICollectionViewSimpleList1.ViewController.Section, Swift.String>
  ▿ _implWrapper: UIKit.NSDiffableDataSourceSnapshot<UICollectionViewSimpleList1.ViewController.Section, Swift.String>.(unknown context at $7ff8066d32e4).ImplWrapper #0
    - impl: <__UIDiffableDataSourceSnapshot 0x600003e21e00: sectionCounts=<_UIDataSourceSnapshotter: 0x60000023b9a0; 1 section with item counts: [7] >; sections=[0x60000023b940]; identifiers=[0x60000023b5c0]> #1
      - super: __UIDiffableDataSource
        - super: NSObject
```

# 📝 2024/06/25



[UICollectionViewCellRegistration | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicollectionviewcellregistration)

[UICollectionViewDiffableDataSource | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource?language=objc)


[【Swift】UICollectionViewDiffableDataSourceとNSDiffableDataSourceSnapshot](https://zenn.dev/dd_sho/articles/73393668e7c8e7)

# 📝 2024/06/17

## `UISplitViewController` が難しい

[iOSアプリを作ろう・スプリットビュー入門|快技庵 高橋政明](https://note.com/kaigian/n/n876e3bccb00b)



## `UIKit`

[UIKitについて](https://zenn.dev/joo_hashi/articles/ea716867143aac)



# 📝 2024/06/14


## `Buttons` 完了

とりあえず終えた


## つぎは、何やるか？

- outline ?
  - storyboard との組み合わせにする？
- page ?
  - 挙動がわからんのよな

## simulator のキャプチャ

- プレビュー開く
- ツール -> サイズを調整
  - 幅: `720` で「ピクセル」に指定

以前まで、11 で行い、今回SE3 のためサイズは違う

## `UISplitViewController` メモ

[ViewControllerのpresentedViewControllerを辿る際の落とし穴 - 面白きことは良きことなり](https://aryzae.hatenablog.com/entry/2017/02/01/002723)


[UISplitViewControllerの優良サンプルソースコード #Swift - Qiita](https://qiita.com/jazzmaster/items/e0db46a9fa088da87de1)


[UISplitViewにUINavigationController を実装する その1: iPhoneアプリ開発備忘録](http://iphone-app-developer.seesaa.net/article/229896783.html)

[UISplitViewにUINavigationController を実装する その2 - iPhoneアプリ開発備忘録](http://iphone-app-developer.seesaa.net/article/229904600.html)

# 📝 2024/06/11


## `attributes` ?

[pystaUIKitCatalogChallenge/UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/MenuButtonViewController.swift at e24fc0024857e9c4a63b08a9161815b70f7c7e76 · pome-ta/pystaUIKitCatalogChallenge · GitHub](https://github.com/pome-ta/pystaUIKitCatalogChallenge/blob/e24fc0024857e9c4a63b08a9161815b70f7c7e76/UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/MenuButtonViewController.swift#L83)


`attributes: []` や`attributes: [UIMenuElement.Attributes.disabled]` の`attributes` はなんだ？


## 実装できてないやつ

実装できてないやつを、まとめないと忘れそう

## `closure` 処理

`lambda` でインラインは、型がつけられずでダメか？

### `@Block` 内の引数型

`objc_id` としている。`Block()` 構文だと、`ctypes.c_void_p` でないとエラー



# 📝 2024/06/09

storyboard 用のベースのものを分けようとしたけど、取り回しが面倒かもで、断念

したら、Working Copy 上でゴミファイルできちゃったよ、、、


# 📝 2024/05/30

## UIButton

``` .swift
button.setTitle("Button", for: [])
```
は、

``` .py
- button.setTitle_forState_('Button', UIControlState.normal)
+ button.setTitle_('Button')
```

`[]` を無視する感じでええのか？




# 📝 2024/05/28

## `NSStrikethroughStyleAttributeName` のGlobal Variable

[Global variables and constants (e.g. NSFoundationVersionNumber) | Calling plain C functions from Python - Rubicon 0.4.9](https://rubicon-objc.readthedocs.io/en/stable/how-to/c-functions.html#global-variables-and-constants-e-g-nsfoundationversionnumber)


[NSStrikethroughStyleAttributeName | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nsstrikethroughstyleattributename)


``` .py
UIKit = load_library('UIKit')

NSStrikethroughStyleAttributeName = objc_const(UIKit, 'NSStrikethroughStyleAttributeName')
```

# 📝 2024/05/25


## index のずれ

extension とリスト格納の順番違うから、extension を先にする


# 📝 2024/05/23



## view

`self.view == self.tableView`

## style

- `init` の中で、`initWithStyle_` を呼ぶ
- storyboard で`style` 設定があるので
- `.new()` で、style が定義されている状況



# 📝 2024/05/22

## cell の色

グレーぽいのって、何の設定だっけか？


`headerView.contentConfiguration`

```
ObjCInstance: UIListContentConfiguration at 0x122030580: <UIListContentConfiguration: 0x3036b8d20; text = 'Default'; Base Style = Grouped Header; directionalLayoutMargins = {17, 8, 6, 8}; axesPreservingSuperviewLayoutMargins = [Horizontal]; imageToTextPadding = 16; textToSecondaryTextVerticalPadding = 3>>

```

```
 
<b'UIListContentConfiguration': <UIListContentConfiguration: 0x3020ed570; text = 'D...t' (length = 7); Base Style = Grouped Header; directionalLayoutMargins = {17, 8, 6, 8}; axesPreservingSuperviewLayoutMargins = [Horizontal]; imageToTextPadding = 16; textToSecondaryTextVerticalPadding = 3>>
```

# 📝 2024/05/21

## 各自セルの`UITableViewHeaderFooterView`

[UITableViewHeaderFooterViewをxibで生成する #iOS - Qiita](https://qiita.com/KikurageChan/items/e1847b54535df393d893)


[【Swift】UITableViewのセクションヘッダーに独自のViewを表示する|Hiromiick Tech Blog](https://hiromiick.com/swift-uitableview-custome-section-header-impl/)

`registerClass_forHeaderFooterViewReuseIdentifier_` 必要？

`dequeueReusableHeaderFooterViewWithIdentifier_`



[viewForHeaderInSectionがめっちゃ呼ばれる | anz blog](https://blog.anzfactory.xyz/articles/20190423/swift-call-view-for-header-in-section-every-scroll/)


```
numberOfSectionsInTableView
numberOfSectionsInTableView
numberOfRowsInSection
numberOfSectionsInTableView
numberOfRowsInSection
numberOfRowsInSection
numberOfSectionsInTableView
numberOfRowsInSection
numberOfSectionsInTableView
numberOfRowsInSection
cellForRowAtIndexPath
viewForHeaderInSection
titleForHeaderInSection

```



# 📝 2024/05/20


## `UITableViewDataSource` 実行順

要素としては、1つだけ


`tableView_viewForHeaderInSection_` を除く

```
numberOfSectionsInTableView
numberOfSectionsInTableView
numberOfRowsInSection
numberOfSectionsInTableView
numberOfRowsInSection
titleForHeaderInSection
numberOfRowsInSection
numberOfSectionsInTableView
titleForHeaderInSection
numberOfRowsInSection
numberOfSectionsInTableView
titleForHeaderInSection
numberOfRowsInSection
cellForRowAtIndexPath
titleForHeaderInSection
titleForHeaderInSection
titleForHeaderInSection
```


# 📝 2024/05/17


## ユーティリティ的な

### `pyLocalizedString.py`

## `BaseTableViewController`

ベースを作るより先に`ButtonViewController` を作る。そこから分割





# 📝 2024/05/16


## storyboard

### デコレータ

[Python Tips: デコレータに引数を渡したい](https://www.lifewithpython.com/2016/09/python-decorator-with-arguments.html)

```.py
prototypes: list = []


def add_prototype(identifier: str):

  def _create_reuse_dict(cellClass: UITableViewCell):
    prototypes.append({
      'cellClass': cellClass,
      'identifier': identifier,
    })

  return _create_reuse_dict
```

`@add_prototype('buttonSystemAddContact')` で、辞書として格納



### 単体のテスト

一つだけ挙動確認。みたいのをできるようにしたいので

```.py
from storyboard.buttonViewController import prototypes

_test_p = prototypes
test_prototypes = _test_p if isinstance(_test_p, list) else [_test_p]
```


と、無理やり感で`test_prototypes` を読ませるようにしてみてる


### `UIControlState`

sample では、`UIButtonConfiguration` じゃないっぽいから、直接やってみるか？



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


# 📝 2024/03/23

rubicon ver としてmain ブランチを進める予定なので

objc_util ブランチを切る

# 📝 2024/03/03

button 並べたけど、ズレ確認

変な挙動のもピックアップしていく

# 📝 2024/03/01

`Localizable.strings`, `Localizable.stringsdict` は、独自パーサーで書いてみる

[GitHub - chrisballinger/python-localizable: Localizable.strings parser for Python](https://github.com/chrisballinger/python-localizable)

こんなのはある

# 📝 2024/02/23

```
<b'UIImage':
<UIImage:0x282e55320 symbol(system: person) {19, 17.5} baseline=2.5,contentInsets={1, 2, 1, 2},alignmentRectInsets={-1, 0, -1.5, 0} 
config=<traits=(UserInterfaceIdiom = Phone, DisplayScale = 2, DisplayGamut = P3, HorizontalSizeClass = Compact, VerticalSizeClass = Regular, UserInterfaceStyle = Dark, UserInterfaceLayoutDirection = LTR, PreferredContentSizeCategory = XS, AccessibilityContrast = Normal)>
renderingMode=automatic(template)>>
```

```
<b'UIImage':
<UIImage:0x282e7d440 symbol(system: person) {20.5, 19.5} baseline=4.5,contentInsets={1.5, 2.5, 1.5, 2.5},alignmentRectInsets={1.5, 0, 1, 0} 
config=<textStyle=UICTFontTextStyleBody, scale=L, (null), traits=(UserInterfaceIdiom = Phone, DisplayScale = 2, DisplayGamut = P3, HorizontalSizeClass = Compact, VerticalSizeClass = Regular, UserInterfaceStyle = Dark, UserInterfaceLayoutDirection = LTR, PreferredContentSizeCategory = XS, AccessibilityContrast = Normal)>
renderingMode=automatic(template)>>
```

# 📝 2024/02/22

[https://github.com/tdamdouni/Pythonista/blob/master/_2017/picker-wheel-for-lists.py](https://github.com/tdamdouni/Pythonista/blob/master/_2017/picker-wheel-for-lists.py)

# 📝 2024/02/19

storyboard を終え、`ButtonKind` での実装

# 📝 2024/02/17

- ButtonSystemAddContact
- ButtonDetailDisclosure
- ButtonStyleGray
- ButtonUpdateActivityHandler
- ButtonAttrText
- ButtonSymbol
- AddToCartButton
- ButtonMultiTitle
- ButtonSystem
- ButtonTitleColor
- ButtonUpdateHandler
- ButtonToggle
- ButtonImageUpdateHandler
- ButtonTextSymbol
- ButtonSymbolText
- ButtonBackground
- ButtonClose
- ButtonLargeSymbol
- ButtonStyleTinted
- ButtonStyleFilled
- ButtonImage
- ButtonCornerStyle

# 📝 2024/02/16

[【UIKit】Cellに直接addSubviewしてはいけない #Swift - Qiita](https://qiita.com/yusame0308/items/c7aee4190057f99b7bf4)

# 📝 2024/02/15

## `super` 処理

出来たっぽい

[draftPythonistaScripts/Pythonista3App/modulesMaster/pythonista/objc_util.py at main · pome-ta/draftPythonistaScripts · GitHub](https://github.com/pome-ta/draftPythonistaScripts/blob/main/Pythonista3App/modulesMaster/pythonista/objc_util.py)

[rubicon-objc/src/rubicon/objc/runtime.py at main · beeware/rubicon-objc · GitHub](https://github.com/beeware/rubicon-objc/blob/main/src/rubicon/objc/runtime.py#L863)

[objc_msgSendSuper | Apple Developer Documentation](https://developer.apple.com/documentation/objectivec/1456716-objc_msgsendsuper)

[objc_super | Apple Developer Documentation](https://developer.apple.com/documentation/objectivec/objc_super?language=objc)

rubicon ありがたい

## `.storyboard` との考え方

buttonSystemAddContact

# 📝 2024/02/11

UITableViewCell の`super` を呼びたいが、、、

オーバーライドできないから、個別で作る?

[UIKit/UITableViewCell.m at master · enormego/UIKit](https://github.com/enormego/UIKit/blob/master/UITableViewCell.m)

かなり古いから、新しいの見つけたい

# 📝 2024/02/10

`ButtonViewController` をやるために`BaseTableViewController` の処理をする

そのために、`CaseElement` の挙動が必要

`CaseElement` の`configHandler` は、`ButtonViewController+Configs` で振り分けしたbutton 処理の関数情報を持ってる

つまり、、、?

- `BaseTableViewController` のセルごとの操作の時には、button の情報がある
  - `cell!.contentView.subviews[0]` と、`subviews` を待ち望んでいるので
- table は、button につき1つづつのbutton 情報しか持たない?
  - 事前に情報を持たせておく必要あり?

[コードベースでカスタムTableViewCellを作る #Swift - Qiita](https://qiita.com/Hyperbolic_____/items/e35cdac1c6b537202151)

これか?

## 階層整理

- `UITableViewCell` のsubclass を作る
- `subviews` へアクセスするため
- 事前につくる?

# 📝 2024/02/07

UISplitViewController ちょっと面倒だから、他サンプル機能を実装していく

モジュールの読み込み的に、直下に書いていく

[UIToolTipInteraction | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitooltipinteraction)

あとで考える

# 📝 2024/02/02

nav 系の詳細設定忘れたから、後にする

## OutlineViewController

面倒そうだから、先にサンプル実装を作っていく

本当はディレクトリで分けたいけど、モジュールのパスとか面倒だから直下に書いていく

# 📝 2024/01/31

## module 化

とりあえず、`main.py` が肥大するから、module 化した

### `_classes.py`で全部ストック?

`ObjCClass` で呼ぶものとかをまるっと入れてみる

# 📝 2024/01/30

- 最初から、左肩にViewController を生やすのか
- xcode からディレクトリツリーのキャプチャーを取って載せようとしたけど、GitHub クライアントからうまくうpできなかったので断念

# 📝 2024/01/29

[UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Base.lproj/Main.storyboard](https://github.com/pome-ta/pystaUIKitCatalogChallenge/blob/main/UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Base.lproj/Main.storyboard)

## `Main.storyboard`

- Navigation Controller が2つ?
  - View (Controller) ごとに分ける?
    - 「UIKitCatalog」と書かれるView
    - OutLine で出すView

## UISplitViewController

[UISplitViewController | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uisplitviewcontroller?language=objc)

[UISplitViewControllerについて学ぶ|山田良治 Yoshiharu Yamada](https://note.com/raiso/n/n23c156e360e5)

# 📝 2024/01/28

- `./captureSampleImage/` に、xcode 実行時のキャプチャを追加
- xcode だと、ディレクトリ構成が違うのでメモしておきたい
  - `./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog.xcodeproj/project.pbxproj` ここのやつ?
- iOS のportrait レイアウトのみで、まずは実装?
  - landscape の左上アイコンと、挙動は気になる
    - 何で呼び出すか?程度は調査予定とする
- とりあえず「UIKitCatalog」とview に書かれているものを探す
  - `./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Base.lproj/Main.storyboard`
  - `.storyboard` か、、、`.xml` として読み解く
    - `navigationController` のカラーとかある
    - `.xml` をPython 的に処理する?

