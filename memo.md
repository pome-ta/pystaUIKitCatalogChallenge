# 📝 2024/11/12

## `UITextField` の`UITextInputTraits` ？


- `autocorrectionType`
- `returnKeyType`

あたりが、見つからん

[Instance properties defined by protocol on superclass are not autodiscovered · Issue #96 · beeware/rubicon-objc](https://github.com/beeware/rubicon-objc/issues/96)


> Hm, it seems like calls to `keyboardType` are handled dynamically. The `keyboardType` property does exist on `UITextField`, but there is no `keyboardType` method. Instead, `UITextField` overrides `forwardingTargetForSelector:`. When called with `SEL("keyboardType")` as an argument, it returns a `UITextInputTraits` object, which does have a statically provided `keyboardType` method. (The `UITextInputTraits` here is a class, apparently undocumented, and not the protocol of the same name.)


m、`keyboardType` への呼び出しが動的に処理されるようです。 `keyboardType` プロパティは`UITextField` に存在しますが、`keyboardType` メソッドはありません。代わりに、`UITextField` が `forwardingTargetForSelector:` をオーバーライドします。引数として `SEL("keyboardType")` を指定して呼び出すと、静的に提供される `keyboardType` メソッドを持つ `UITextInputTraits` オブジェクトが返されます。 (ここでの `UITextInputTraits` は明らかに文書化されていないクラスであり、同じ名前のプロトコルではありません。)




> When calling a method with Rubicon using Python method call syntax, the method is looked up on the class (in the attribute access) and then called later (when the `ObjCBoundMethod` object is called). This doesn't work for dynamic methods, since they don't exist on the class. On the other hand, `send_message` uses `objc_msgSend` and friends to send a method call to the object directly, which triggers the whole dynamic method call process.


Python メソッド呼び出し構文を使用して Rubicon でメソッドを呼び出す場合、メソッドは (属性アクセスで) クラスで検索され、後で (`ObjCBoundMethod` オブジェクトが呼び出されたときに) 呼び出されます。動的メソッドはクラスに存在しないため、これは機能しません。一方、`send_message` は、`objc_msgSend` とその仲間を使用してメソッド呼び出しをオブジェクトに直接送信し、動的メソッド呼び出しプロセス全体をトリガーします。



### 結果

`textInputTraits` で呼び出せばok？

## `textField_shouldChangeCharactersInRange_replacementString_` 落ちる？

[UITextFieldのshouldChangeCharactersInRange:replacementString:は使えない子かもしれない #iOS - Qiita](https://qiita.com/macneko/items/073015cdf8b303a536ca)




# 📝 2024/11/08

## `UISwitch` の`tintColor`

変わってない気がする、、、ペンディング


# 📝 2024/11/07

## `UISwitch` のStoryboard


`horizontalHuggingPriority` `verticalHuggingPriority`

が`750` で固定値ぽいから、既定の数値か？

# 📝 2024/11/04

## `sliderViewController` のStoryboard


```
<constraint firstItem="lhN-5T-HKR" firstAttribute="leading" secondItem="VfF-ru-LCc" secondAttribute="leading" constant="20" symbolic="YES" id="QnE-iU-5Qj"/>
```

`symbolic="YES"` とは？

[ios - What does symbolic="YES" mean in InterfaceBuilder's XML? - Stack Overflow](https://stackoverflow.com/questions/17522603/what-does-symbolic-yes-mean-in-interfacebuilders-xml)

うーん🤔

とりあえず、`symbolic` 気にせずに数値入れていく


## `BaseTableViewController` のオーバーライド


```python
  @objc_method
  def init(self):
    send_super(__class__, self, 'init')  # xxx: 不要?
    tableViewStyle = UITableViewStyle.grouped
    self.initWithStyle_(tableViewStyle)

    self.testCells = []
    self.initPrototype()

    return self

  @objc_method
  def initPrototype(self):
    [
      self.tableView.registerClass_forCellReuseIdentifier_(
        prototype['cellClass'], prototype['identifier'])
      for prototype in prototypes
    ]

```

`prototypes` 取り回しが面倒なので、継承先でやる

親の`init` で、ゴニョゴニョするのが少々面倒な気がしてるため



# 📝 2024/10/31


## `segmentedControlViewController`の`configureTintedSegmentedControl_`

```swift
segmentedControl.selectedSegmentTintColor = UIColor(named: "tinted_segmented_control")!
```


`UIColor(named: "tinted_segmented_control")` と、bundle（？）
から、呼び出す場面あり


`.bundle` は、ビルドしてから生成される？かもなので、どうやって取得するか、、、


[CFBundleとNSBundle [のふ処|NOFUDOKORO]](https://nofu.jp/wiki/translation/adc/cocoa/foundation/introduction_to_dynamically_loading_code/0400_cfbundle)


どうなんやろ、、、


とりま、

[./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/tinted_segmented_control.colorset/Contents.json](https://github.com/pome-ta/pystaUIKitCatalogChallenge/blob/main/UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/tinted_segmented_control.colorset/Contents.json)

から、無理矢理こねくり回して、処理させるか？



### 落ちる

```python
color_named = UIColor.alloc().initWithRed_green_blue_alpha_(*_srgb)
```
```python
color_named = UIColor.colorWithRed_green_blue_alpha_(*_srgb)
```

`alloc().init()` すると、要素書き換え（`_style`）したら落ちる



`autorelease` しても、落ちたので`alloc().init()` では呼ばないようにする


# 📝 2024/10/29

## `UISegmentedControl` に入る

[UISegmentedControl - iPhoneアプリ開発の虎の巻](https://iphone-tora.sakura.ne.jp/uisegmentedcontrol.html)

## Storyboard

buttom の時と同じようにする

tableView で並べていくため


# 📝 2024/10/26

## Safe Area 表記のメモ

相互的な数値の関係を整理。`Constraints` とすると、下から上にいく感じ？

最上階層の`View` は、`Autoresizing Mask` は、上と左？

`Margin` という概念が初で、調査が必要かも

- Safe Area 要素を小さくするというわけではなく、マージンで子要素をいじめる感じか
- 起点は Safe Area でいいはずだけど、なんか子要素（Page Control）起点っぽいところない？

### Constraints

```
SafeArea.centerX = ColorView.centerX
SafeArea.trailing = ColorView.trailing + 40
SafeArea.bottom = ColorView.bottom + 40
SafeArea.bottom = PageControl.bottom

ColorView.centerX = PageControl.centerX
ColorView.leading = SafeArea.leading + 40
ColorView.top = SafeArea.top + 35

PageControl.trailing = trailingMargin
PageControl.leading = leadingMargin

```

### Layout Guide

#### View

- Horizontal

```
Trailing Margin Space Page Control
Leading  Margin Space Page Control
```

#### Safe Area

- Horizontal

```
Align Center X to: Color View

Align Trailing to: Color View
           Equals: 40(constant)
Align Leading  to: Color View
           Equals: 40(constant)
```

- Vertical

```
Align Bottom to: Page Control
Align Bottom to: Color View
         Equals: 40(constant)
Align top    to: Color View
         Equals: 35(constant)
```

#### Page Control

- Horizontal

```
Trailing Space to: (Superview)
Leading Space to: (Superview)
Align Center X to: Color View

```

- Vertical

```
Align Bottom to: Safe Area
```

### Color View

- Horizontal

```
Align Center X to: Safe Area
Align Center X to: Page Control
Align Trailing to: Safe Area
           Equals: 40(constant)
Align Leading  to: Safe Area
           Equals: 40(constant)
```

- Vertical

```
Align Bottom to: Safe Area
         Equals: 40(constant)
Align top    to: Safe Area
         Equals: 35(constant)
```

# 📝 2024/10/25

## `PageControlViewController` を進める

### 断念

`outline` のやつが`UICollectionView` やら`UICollectionViewDiffableDataSource` の挙動が不明すぎるので

一旦パスして、こっちをはじめる

### 進め方？

Storyboard との連携を考えるのが面倒なので、1 ファイルでゴリっと書いてから、Storyboard との連携を考える

### 調べメモ

#### `autorelease` の宣言

```objc
UIPageControl *pc = [[[UIPageControl alloc] init] autorelease];
pc.frame = CGRectMake(0, 450, 320, 30);
pc.numberOfPages = 10;
pc.currentPage = 3;
[self.view addSubview:pc];
```

[UIPageControl - iPhone アプリ開発の虎の巻](https://iphone-tora.sakura.ne.jp/uipagecontrol.html)

`autorelease` つける判断って結局どうすりゃええんだっけ？

#### Storyboard の情報確認 & 取得

[UIKitCatalog/Base.lproj/DefaultPageControlViewController.storyboard](https://github.com/pome-ta/pystaUIKitCatalogChallenge/blob/main/UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Base.lproj/DefaultPageControlViewController.storyboard)

`viewController` の`view` に、`Page Control` と`Color View` が、ぶら下がっている感じ

（見た目では、順序的に逆だが、要素順番として揃えておきたい。）

要素は、`Safe Area` を基準として良い感じにやっているっぽい

# 📝 2024/10/14

## `UICollectionView`、`UICollectionViewDiffableDataSource` の rubicon(objc) 実装

[./OutlineViewController.swift](https://github.com/pome-ta/pystaUIKitCatalogChallenge/blob/main/UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/OutlineViewController.swift)

Swift から、Objective-C へ読み替えをして、rubicon へ書き直すプロセス。

空の状態は出せている感じだけど、要素が入ってくるとエラーもなく落ちる

ちょっとテキストで整理してみたい

# 📝 2024/10/13

Block の処理なのか、エラーの出所がわからない

# 📝 2024/10/07

なにが出来てなくて、なにを調べるのか思い出す

> - outline ?
>   - storyboard との組み合わせにする?
> - page ?
>   - 挙動がわからんのよな

これで、`outline` を進めてたぽい

## outline

### 最小構成？

[Diffable DataSource 入門 #Swift - Qiita](https://qiita.com/maiyama18/items/28039293b4bbf886ce8e)

[The Macro Behind Nil - Ben Ford](https://benford.me/blog/the-macro-behind-nil/)

[[Swift]UICollectionView の進化:Compositional Layouts 編](https://zenn.dev/chiii/articles/e487b32e787b59)

[AppStore in Objective-C with Compositional Layout | by Ravi Bastola | Medium](https://ravibastolaa.medium.com/appstore-in-objective-c-with-compositional-layout-71fb678f922)

[UICollectionViewCompositionalLayoutSectionProvider | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicollectionviewcompositionallayoutsectionprovider?language=objc)

### ここに逃す

一旦途中までのを逃す（Working Copy の`.iCloud` 消せない問題対策）

```.py
import ctypes

from pyrubicon.objc.api import ObjCClass, objc_method
from pyrubicon.objc.runtime import send_super
from pyrubicon.objc.types import NSInteger

from rbedge.enumerations import UISplitViewControllerStyle, UISplitViewControllerColumn, UICollectionLayoutListAppearance

#ObjCClass.auto_rename = True
UISplitViewController = ObjCClass('UISplitViewController')

UICollectionViewController = ObjCClass('UICollectionViewController')
#UICollectionViewLayout = ObjCClass('UICollectionViewLayout')
UICollectionViewCell = ObjCClass('UICollectionViewCell')
UICollectionViewListCell = ObjCClass('UICollectionViewListCell')

UICollectionViewCompositionalLayout = ObjCClass(
  'UICollectionViewCompositionalLayout')
UICollectionLayoutListConfiguration = ObjCClass(
  'UICollectionLayoutListConfiguration')

from rbedge.functions import NSStringFromClass

# --- UIViewController
UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UIView = ObjCClass('UIView')
UILabel = ObjCClass('UILabel')
UIFont = ObjCClass('UIFont')
UIColor = ObjCClass('UIColor')


class FirstViewController(UIViewController):

  @objc_method
  def viewDidLoad(self):
    # --- Navigation
    title = NSStringFromClass(__class__)
    self.navigationItem.title = title

    # --- View
    backgroundColor = UIColor.systemBlueColor()
    systemBlueColor

    self.view.backgroundColor = backgroundColor

    self.label = UILabel.new()
    self.label.text = title
    self.label.font = UIFont.systemFontOfSize_(26.0)
    self.label.sizeToFit()

    self.view.addSubview_(self.label)

    # --- Layout
    self.label.translatesAutoresizingMaskIntoConstraints = False

    NSLayoutConstraint.activateConstraints_([
      self.label.centerXAnchor.constraintEqualToAnchor_(
        self.view.centerXAnchor),
      self.label.centerYAnchor.constraintEqualToAnchor_(
        self.view.centerYAnchor),
    ])


class SecondViewController(UIViewController):

  @objc_method
  def viewDidLoad(self):
    # --- Navigation
    title = NSStringFromClass(__class__)
    self.navigationItem.title = title

    # --- View
    backgroundColor = UIColor.systemRedColor()
    self.view.backgroundColor = backgroundColor

    self.label = UILabel.new()
    self.label.text = title
    self.label.font = UIFont.systemFontOfSize_(26.0)
    self.label.sizeToFit()

    self.view.addSubview_(self.label)

    # --- Layout
    self.label.translatesAutoresizingMaskIntoConstraints = False

    NSLayoutConstraint.activateConstraints_([
      self.label.centerXAnchor.constraintEqualToAnchor_(
        self.view.centerXAnchor),
      self.label.centerYAnchor.constraintEqualToAnchor_(
        self.view.centerYAnchor),
    ])


class OutlineViewController(UISplitViewController):

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    '''
    self.setViewController_forColumn_(
      FirstViewController, UISplitViewControllerColumn.supplementary)
    '''
    view = self.view
    bg_view = UIView.new()
    bg_view.backgroundColor = UIColor.systemCyanColor()

    view.addSubview_(bg_view)

    bg_view.translatesAutoresizingMaskIntoConstraints = False
    NSLayoutConstraint.activateConstraints_([
      bg_view.centerXAnchor.constraintEqualToAnchor_(view.centerXAnchor),
      bg_view.centerYAnchor.constraintEqualToAnchor_(view.centerYAnchor),
      bg_view.widthAnchor.constraintEqualToAnchor_multiplier_(
        view.widthAnchor, 0.88),
      bg_view.heightAnchor.constraintEqualToAnchor_multiplier_(
        view.heightAnchor, 0.88),
    ])
    pdbr.state(UICollectionViewController)


# [UICollectionLayoutListConfigurationのheaderMode=.firstItemInSection観測隊](https://zenn.dev/samekard_dev/articles/2cbb0788915f01)
prefectures = [
  ['北海道', '北海道'],
  ['東北', '青森', '岩手', '秋田', '宮城', '山形', '福島'],
  ['関東', '茨城', '栃木', '群馬', '埼玉', '千葉', '東京', '神奈川'],
  ['甲信越', '新潟', '長野', '山梨'],
  ['北陸', '富山', '石川', '福井'],
  ['東海', '岐阜', '静岡', '愛知', '三重'],
  ['近畿', '滋賀', '京都', '奈良', '大阪', '和歌山', '兵庫'],
  ['中国', '鳥取', '島根', '岡山', '広島', '山口'],
  ['四国', '香川', '徳島', '愛媛', '高知'],
  ['九州', '福岡', '佐賀', '長崎', '大分', '熊本', '宮崎', '鹿児島'],
  ['沖縄', '沖縄'],
]


class CollectionViewController(UICollectionViewController):

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    self.identifier_str = 'customCell'
    self.collectionView.registerClass_forCellWithReuseIdentifier_(
      UICollectionViewListCell, self.identifier_str)

  @objc_method
  def numberOfSectionsInCollectionView_(self, collectionView) -> NSInteger:
    return len(prefectures)

  @objc_method
  def collectionView_numberOfItemsInSection_(self, collectionView,
                                             section: NSInteger) -> NSInteger:

    return len(prefectures[section])

  @objc_method
  def collectionView_cellForItemAtIndexPath_(self, collectionView,
                                             indexPath) -> ctypes.c_void_p:
    cell = collectionView.dequeueReusableCellWithReuseIdentifier_forIndexPath_(
      self.identifier_str, indexPath)


    cellConfiguration = cell.defaultContentConfiguration()
    cellConfiguration.text = prefectures[indexPath.section][indexPath.row]
    cell.contentConfiguration = cellConfiguration
    #cell.setBackgroundColor_(UIColor.systemRedColor())
    #pdbr.state(cell)
    #print(prefectures[indexPath.section][indexPath.row])
    return cell.ptr


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  listConfiguration = UICollectionLayoutListConfiguration.alloc(
  ).initWithAppearance_(1)
  layout = UICollectionViewCompositionalLayout.layoutWithListConfiguration_(
    listConfiguration)

  #main_vc = CollectionViewController.new()
  main_vc = CollectionViewController.alloc().initWithCollectionViewLayout_(
    layout)

  present_viewController(main_vc)
  #pdbr.state(main_vc)
  #layoutWithListConfiguration
  #listConfiguration = UICollectionLayoutListConfiguration.alloc().initWithAppearance_(0)
  #layout = UICollectionViewCompositionalLayout.layoutWithListConfiguration_(listConfiguration)

  #v = UICollectionViewController.alloc().initWithCollectionViewLayout_(layout)

  #pdbr.state(v.collectionView)
  #print(listConfiguration.appearance)
  #main_vc = CollectionViewController.alloc().initWithStyle_(UISplitViewControllerStyle.doubleColumn)
  #pdbr.state(main_vc)
  #print(main_vc.style)
  #pdbr.state(OutlineViewController.alloc())

  #style = UIModalPresentationStyle.fullScreen
  #style = UIModalPresentationStyle.pageSheet  # 1
  #present_viewController(main_vc, style, False)


```

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

[【Swift】UICollectionViewDiffableDataSource と NSDiffableDataSourceSnapshot](https://zenn.dev/dd_sho/articles/73393668e7c8e7)

# 📝 2024/06/17

## `UISplitViewController` が難しい

[iOS アプリを作ろう・スプリットビュー入門|快技庵 高橋政明](https://note.com/kaigian/n/n876e3bccb00b)

## `UIKit`

[UIKit について](https://zenn.dev/joo_hashi/articles/ea716867143aac)

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

以前まで、11 で行い、今回 SE3 のためサイズは違う

## `UISplitViewController` メモ

[ViewController の presentedViewController を辿る際の落とし穴 - 面白きことは良きことなり](https://aryzae.hatenablog.com/entry/2017/02/01/002723)

[UISplitViewController の優良サンプルソースコード #Swift - Qiita](https://qiita.com/jazzmaster/items/e0db46a9fa088da87de1)

[UISplitView に UINavigationController を実装する その 1: iPhone アプリ開発備忘録](http://iphone-app-developer.seesaa.net/article/229896783.html)

[UISplitView に UINavigationController を実装する その 2 - iPhone アプリ開発備忘録](http://iphone-app-developer.seesaa.net/article/229904600.html)

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

```.swift
button.setTitle("Button", for: [])
```

は、

```.py
- button.setTitle_forState_('Button', UIControlState.normal)
+ button.setTitle_('Button')
```

`[]` を無視する感じでええのか？

# 📝 2024/05/28

## `NSStrikethroughStyleAttributeName` の Global Variable

[Global variables and constants (e.g. NSFoundationVersionNumber) | Calling plain C functions from Python - Rubicon 0.4.9](https://rubicon-objc.readthedocs.io/en/stable/how-to/c-functions.html#global-variables-and-constants-e-g-nsfoundationversionnumber)

[NSStrikethroughStyleAttributeName | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nsstrikethroughstyleattributename)

```.py
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

[UITableViewHeaderFooterView を xib で生成する #iOS - Qiita](https://qiita.com/KikurageChan/items/e1847b54535df393d893)

[【Swift】UITableView のセクションヘッダーに独自の View を表示する|Hiromiick Tech Blog](https://hiromiick.com/swift-uitableview-custome-section-header-impl/)

`registerClass_forHeaderFooterViewReuseIdentifier_` 必要？

`dequeueReusableHeaderFooterViewWithIdentifier_`

[viewForHeaderInSection がめっちゃ呼ばれる | anz blog](https://blog.anzfactory.xyz/articles/20190423/swift-call-view-for-header-in-section-every-scroll/)

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

要素としては、1 つだけ

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

[UIButton.Configuration その 1 〜角の丸みもお手のもの](https://zenn.dev/samekard_dev/articles/64d8f1578a7bb6)

# 📝 2024/05/14

`0.4.9`

## storyboard

`ButtonViewController.storyboard`

`reuseIdentifier` をどう捌くか？

サイズはよしなにやってもらう？

# 📝 2024/05/09

[なぜ UITableViewController を使うなと言われるのか #iOS - Qiita](https://qiita.com/yosshi4486/items/33132718a0fb08273a45)

# 📝 2024/04/24

改めて storyboard について考えてみる

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
その場合には、値として Document で参照しやすい方にする。

`.` は、`_` で繋ぐ

[pystaUIKitCatalogChallenge/objcista/constants.py at objc_util · pome-ta/pystaUIKitCatalogChallenge · GitHub](https://github.com/pome-ta/pystaUIKitCatalogChallenge/blob/objc_util/objcista/constants.py)

基本的には、ここをコピペ、使用するタイミングで、都度 Document を参照する。

## `tests` ディレクトリ

```.py
parent_level = 3
sys.path.append(str(pathlib.Path(__file__, '../' * parent_level).resolve()))
```

無理やり module をブチ込む、`sandbox` として、test 前の実験の場合は、level を階層に応じて指定する（test の意味とは）

まぁ、iPhone と working copy との`.cloud` ファイル問題なんだけど、、、

# 📝 2024/04/19

## 運用想定

ディレクトリ直下には、Catalog としてのファイルを入れていく。Rubicon のためとしてのファイルは、`rbedge` にゴリゴリと入れていく

直下はあくまでも、Catalog のサンプル内容とイコールな関係としていきたい

## `rbedge`

独自の Rubicon のライブラリとして、作ったファイルを置いていく

### 命名理由

Rubicon が多分「川」の意味があると思われるので、川の「端」として、「edge」 で、Rubicon の「r」と「b」 を付けて「rbedge」 とした。
ざっとググって、名前が被らないかは確認した。

### 運用方法

Python として正しくはないかもだけど、`pyrubicon` モジュールを読み込みをするので、直下に`test` ディレクトリを作成して、そのディレクトリ内で挙動の確認をする。

読み込みは、`sys` モジュールで無理やり path を取得する流れ。

## ファイルの配置やら関連性について

rootNav 系を先に準備したが、実行するためとすると、裏側での動きだから、他のもの準備した方がいいのではないかと思う。

あと、定数ではなく enum をひとつひとつ書いていくしかないのかなぁというお気持ち

# 📝 2024/03/23

rubicon ver として main ブランチを進める予定なので

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

[https://github.com/tdamdouni/Pythonista/blob/master/\_2017/picker-wheel-for-lists.py](https://github.com/tdamdouni/Pythonista/blob/master/_2017/picker-wheel-for-lists.py)

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

[【UIKit】Cell に直接 addSubview してはいけない #Swift - Qiita](https://qiita.com/yusame0308/items/c7aee4190057f99b7bf4)

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

`CaseElement` の`configHandler` は、`ButtonViewController+Configs` で振り分けした button 処理の関数情報を持ってる

つまり、、、?

- `BaseTableViewController` のセルごとの操作の時には、button の情報がある
  - `cell!.contentView.subviews[0]` と、`subviews` を待ち望んでいるので
- table は、button につき 1 つづつの button 情報しか持たない?
  - 事前に情報を持たせておく必要あり?

[コードベースでカスタム TableViewCell を作る #Swift - Qiita](https://qiita.com/Hyperbolic_____/items/e35cdac1c6b537202151)

これか?

## 階層整理

- `UITableViewCell` の subclass を作る
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

- 最初から、左肩に ViewController を生やすのか
- xcode からディレクトリツリーのキャプチャーを取って載せようとしたけど、GitHub クライアントからうまくう p できなかったので断念

# 📝 2024/01/29

[UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Base.lproj/Main.storyboard](https://github.com/pome-ta/pystaUIKitCatalogChallenge/blob/main/UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Base.lproj/Main.storyboard)

## `Main.storyboard`

- Navigation Controller が 2 つ?
  - View (Controller) ごとに分ける?
    - 「UIKitCatalog」と書かれる View
    - OutLine で出す View

## UISplitViewController

[UISplitViewController | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uisplitviewcontroller?language=objc)

[UISplitViewController について学ぶ|山田良治 Yoshiharu Yamada](https://note.com/raiso/n/n23c156e360e5)

# 📝 2024/01/28

- `./captureSampleImage/` に、xcode 実行時のキャプチャを追加
- xcode だと、ディレクトリ構成が違うのでメモしておきたい
  - `./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog.xcodeproj/project.pbxproj` ここのやつ?
- iOS の portrait レイアウトのみで、まずは実装?
  - landscape の左上アイコンと、挙動は気になる
    - 何で呼び出すか?程度は調査予定とする
- とりあえず「UIKitCatalog」と view に書かれているものを探す
  - `./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Base.lproj/Main.storyboard`
  - `.storyboard` か、、、`.xml` として読み解く
    - `navigationController` のカラーとかある
    - `.xml` を Python 的に処理する?
