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


