# 📝 2024/02/10

`ButtonViewController` をやるために`BaseTableViewController` の処理をする

そのために、`CaseElement` の挙動が必要


`CaseElement` の`configHandler` は、`ButtonViewController+Configs` で振り分けしたbutton 処理の関数情報を持ってる


つまり、、、？
- `BaseTableViewController` のセルごとの操作の時には、button の情報がある
  - `cell!.contentView.subviews[0]` と、`subviews` を待ち望んでいるので
- table は、button につき1つづつのbutton 情報しか持たない？
  - 事前に情報を持たせておく必要あり？


[コードベースでカスタムTableViewCellを作る #Swift - Qiita](https://qiita.com/Hyperbolic_____/items/e35cdac1c6b537202151)

これか？



## 階層整理

- `UITableViewCell` のsubclass を作る
- `subviews` へアクセスするため
- 事前につくる？


# 📝 2024/02/07

UISplitViewController ちょっと面倒だから、他サンプル機能を実装していく

モジュールの読み込み的に、直下に書いていく


[UIToolTipInteraction | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitooltipinteraction)

あとで考える


# 📝 2024/02/02

nav 系の詳細設定忘れたから、後にする

## OutlineViewController

面倒そうだから、先にサンプル実装を作っていく

本当はディレクトリで分けたいけど、モジュールのパスとか面倒だから直下に書いていく

# 📝 2024/01/31

## module 化

とりあえず、`main.py` が肥大するから、module 化した

### `_classes.py`で全部ストック？

`ObjCClass` で呼ぶものとかをまるっと入れてみる

# 📝 2024/01/30

- 最初から、左肩にViewController を生やすのか
- xcode からディレクトリツリーのキャプチャーを取って載せようとしたけど、GitHub クライアントからうまくうpできなかったので断念

# 📝 2024/01/29

[UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Base.lproj/Main.storyboard](https://github.com/pome-ta/pystaUIKitCatalogChallenge/blob/main/UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Base.lproj/Main.storyboard)

## `Main.storyboard`

- Navigation Controller が2つ？
  - View (Controller) ごとに分ける？
    - 「UIKitCatalog」と書かれるView
    - OutLine で出すView

## UISplitViewController

[UISplitViewController | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uisplitviewcontroller?language=objc)

[UISplitViewControllerについて学ぶ|山田良治 Yoshiharu Yamada](https://note.com/raiso/n/n23c156e360e5)

# 📝 2024/01/28

- `./captureSampleImage/` に、xcode 実行時のキャプチャを追加
- xcode だと、ディレクトリ構成が違うのでメモしておきたい
  - `./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog.xcodeproj/project.pbxproj` ここのやつ？
- iOS のportrait レイアウトのみで、まずは実装？
  - landscape の左上アイコンと、挙動は気になる
    - 何で呼び出すか？程度は調査予定とする
- とりあえず「UIKitCatalog」とview に書かれているものを探す
  - `./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Base.lproj/Main.storyboard`
  - `.storyboard` か、、、`.xml` として読み解く
    - `navigationController` のカラーとかある
    - `.xml` をPython 的に処理する？
