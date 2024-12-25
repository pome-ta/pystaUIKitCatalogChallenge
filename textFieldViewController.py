'''
note: wip 項目
  - `ObjCProtocol` 不要？
  - `CustomTextField` class の`init` って機能してる？
  - 標準キーボードのみ機能するものあり
'''

from enum import Enum
from pathlib import Path

from pyrubicon.objc.api import ObjCClass, ObjCInstance, ObjCProtocol
from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.runtime import send_super, objc_id, SEL
from pyrubicon.objc.types import NSInteger, CGRect, CGFloat, CGRectMake, UIEdgeInsetsMake

from rbedge.enumerations import (
  UITextAutocorrectionType,
  UIReturnKeyType,
  UITextFieldViewMode,
  UIUserInterfaceIdiom,
  UIKeyboardType,
  UITextBorderStyle,
  UIButtonType,
  UIControlState,
  UIControlEvents,
)

from rbedge import pdbr

from caseElement import CaseElement
from pyLocalizedString import localizedString

from baseTableViewController import BaseTableViewController
from storyboard.textFieldViewController import prototypes

UISearchTextField = ObjCClass('UISearchTextField')  # todo: 型確認用
UIColor = ObjCClass('UIColor')
UITextFieldDelegate = ObjCProtocol('UITextFieldDelegate')

UIImageView = ObjCClass('UIImageView')
UIImage = ObjCClass('UIImage')
UISearchToken = ObjCClass('UISearchToken')
UIScreen = ObjCClass('UIScreen')
NSURL = ObjCClass('NSURL')
NSData = ObjCClass('NSData')
UIButton = ObjCClass('UIButton')


# Cell identifier for each text field table view cell.
# 各テキスト フィールド テーブル ビュー セルのセル識別子。
class TextFieldKind(Enum):
  textField = 'textField'
  tintedTextField = 'tintedTextField'
  secureTextField = 'secureTextField'
  specificKeyboardTextField = 'specificKeyboardTextField'
  customTextField = 'customTextField'
  searchTextField = 'searchTextField'


class TextFieldViewController(BaseTableViewController,
                              protocols=[
                                UITextFieldDelegate,
                              ]):

  @objc_method
  def initWithStyle_(self, style: NSInteger) -> ObjCInstance:
    send_super(__class__,
               self,
               'initWithStyle:',
               style,
               restype=objc_id,
               argtypes=[
                 NSInteger,
               ])
    self.setupPrototypes_(prototypes)
    return self

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?

    self.navigationItem.title = localizedString('TextFieldsTitle') if (
      title := self.navigationItem.title) is None else title

    self.testCells.extend([
      CaseElement(localizedString('DefaultTextFieldTitle'),
                  TextFieldKind.textField.value, self.configureTextField_),
      CaseElement(localizedString('TintedTextFieldTitle'),
                  TextFieldKind.tintedTextField.value,
                  self.configureTintedTextField_),
      CaseElement(localizedString('SecuretTextFieldTitle'),
                  TextFieldKind.secureTextField.value,
                  self.configureSecureTextField_),
      CaseElement(localizedString('SearchTextFieldTitle'),
                  TextFieldKind.searchTextField.value,
                  self.configureSearchTextField_),
    ])

    if self.traitCollection.userInterfaceIdiom != UIUserInterfaceIdiom.mac:
      self.testCells.extend([
        # Show text field with specific kind of keyboard for iOS only.
        # iOS の場合のみ、特定の種類のキーボードを使用してテキスト フィールドを表示します。
        CaseElement(localizedString('SpecificKeyboardTextFieldTitle'),
                    TextFieldKind.specificKeyboardTextField.value,
                    self.configureSpecificKeyboardTextField_),
        # Show text field with custom background for iOS only.
        # iOS のみのカスタム背景を使用してテキスト フィールドを表示します。
        CaseElement(localizedString('CustomTextFieldTitle'),
                    TextFieldKind.customTextField.value,
                    self.configureCustomTextField_),
      ])

  # MARK: - Configuration
  @objc_method
  def configureTextField_(self, textField):
    textField.delegate = self
    textField.placeholder = localizedString('Placeholder text')

    textInputTraits = textField.textInputTraits()
    textInputTraits.autocorrectionType = UITextAutocorrectionType.yes
    textInputTraits.returnKeyType = UIReturnKeyType.done

    textField.clearButtonMode = UITextFieldViewMode.whileEditing

  @objc_method
  def configureTintedTextField_(self, textField):
    textField.delegate = self
    textField.tintColor = UIColor.systemBlueColor()
    textField.textColor = UIColor.systemGreenColor()

    textField.placeholder = localizedString('Placeholder text')
    textInputTraits = textField.textInputTraits()
    textInputTraits.returnKeyType = UIReturnKeyType.done
    textField.clearButtonMode = UITextFieldViewMode.never

  @objc_method
  def configureSecureTextField_(self, textField):
    textField.delegate = self
    textField.setSecureTextEntry_(True)  # xxx: `setSecureTextEntry_` しか見つからず

    textField.placeholder = localizedString('Placeholder text')

    textInputTraits = textField.textInputTraits()
    textInputTraits.returnKeyType = UIReturnKeyType.done
    textField.clearButtonMode = UITextFieldViewMode.always

  @objc_method
  def configureSearchTextField_(self, textField):
    if (searchField := textField).isMemberOfClass_(UISearchTextField):
      searchField.delegate = self
      searchField.placeholder = localizedString('Enter search text')

      textInputTraits = searchField.textInputTraits()
      textInputTraits.returnKeyType = UIReturnKeyType.done

      searchField.clearButtonMode = UITextFieldViewMode.always
      searchField.allowsDeletingTokens = True

      # Setup the left view as a symbol image view.
      # 左側のビューをシンボル イメージ ビューとして設定します。
      searchIcon = UIImageView.alloc().initWithImage_(
        UIImage.systemImageNamed_('magnifyingglass'))
      searchField.leftView = searchIcon
      searchField.leftViewMode = UITextFieldViewMode.always

      secondToken = UISearchToken.tokenWithIcon_text_(
        UIImage.systemImageNamed_('staroflife'), 'Token 2')
      searchField.insertToken_atIndex_(secondToken, 0)

      firstToken = UISearchToken.tokenWithIcon_text_(
        UIImage.systemImageNamed_('staroflife.fill'), 'Token 1')
      searchField.insertToken_atIndex_(firstToken, 0)

  '''
  There are many different types of keyboards that you may choose to use.
  The different types of keyboards are defined in the `UITextInputTraits` interface.
  This example shows how to display a keyboard to help enter email addresses.
  '''
  '''
  使用するキーボードにはさまざまな種類があります。
  さまざまなタイプのキーボードは `UITextInputTraits` インターフェイスで定義されます。
  この例では、電子メール アドレスの入力を支援するキーボードを表示する方法を示します。
  '''
  # todo: iOS 標準「英語」キーボード設定を入れてないと反映されない
  # xxx: 読み込み挙動がめちゃくちゃ遅くなる
  @objc_method
  def configureSpecificKeyboardTextField_(self, textField):
    textField.delegate = self
    textInputTraits = textField.textInputTraits()
    textInputTraits.keyboardType = UIKeyboardType.emailAddress

    textField.placeholder = localizedString('Placeholder text')
    textInputTraits.returnKeyType = UIReturnKeyType.done

  @objc_method
  def configureCustomTextField_(self, textField):
    textField.delegate = self
    # Text fields with custom image backgrounds must have no border.
    # カスタム画像の背景を持つテキストフィールドには枠線を付ける必要はありません。
    textField.borderStyle = UITextBorderStyle.none

    scale = int(UIScreen.mainScreen.scale)

    background_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/text_field_background.imageset/text_field_background_{scale}x.png'

    purpleImage_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/text_field_purple_right_view.imageset/text_field_purple_right_view_{scale}x.png'

    # xxx: `lambda` の使い方が悪い
    dataWithContentsOfURL = lambda path_str: NSData.dataWithContentsOfURL_(
      NSURL.fileURLWithPath_(str(Path(path_str).absolute())))

    background_img = UIImage.alloc().initWithData_scale_(
      dataWithContentsOfURL(background_str), scale)

    textField.background = background_img

    # Create a purple button to be used as the right view of the custom text field.
    # カスタム テキスト フィールドの右側のビューとして使用する紫色のボタンを作成します。
    purpleImage = UIImage.alloc().initWithData_scale_(
      dataWithContentsOfURL(purpleImage_str), scale)

    purpleImageButton = UIButton.buttonWithType_(UIButtonType.custom)
    purpleImageButton.bounds = CGRectMake(0.0, 0.0, purpleImage.size.width,
                                          purpleImage.size.height)
    purpleImageButton.imageEdgeInsets = UIEdgeInsetsMake(0.0, 0.0, 0.0, 5.0)

    purpleImageButton.setImage_forState_(purpleImage, UIControlState.normal)
    purpleImageButton.addTarget_action_forControlEvents_(
      self, SEL('customTextFieldPurpleButtonClicked'),
      UIControlEvents.touchUpInside)

    textField.rightView = purpleImageButton
    textField.rightViewMode = UITextFieldViewMode.always

    textField.placeholder = localizedString('Placeholder text')

    textInputTraits = textField.textInputTraits()
    textInputTraits.autocorrectionType = UITextAutocorrectionType.no

    textField.clearButtonMode = UITextFieldViewMode.never
    textInputTraits.returnKeyType = UIReturnKeyType.done

  # MARK: - Actions
  @objc_method
  def customTextFieldPurpleButtonClicked(self):
    print("The custom text field's purple right view button was clicked.")

  # MARK: - UITextFieldDelegate
  @objc_method
  def textFieldShouldReturn_(self, textField) -> bool:
    textField.resignFirstResponder()
    return True

  @objc_method
  def textFieldDidChangeSelection_(self, textField):
    # User changed the text selection.
    # ユーザーがテキストの選択を変更しました。
    pass

  '''# xxx: 落ちる
  @objc_method
  def textField_shouldChangeCharactersInRange_replacementString_(
      self, range, string) -> bool:
    # Return false to not change text.
    # テキストを変更しない場合は false を返します。
    return True
  '''


# Custom text field for controlling input text placement.
# 入力テキストの配置を制御するためのカスタム テキスト フィールド。
class CustomTextField(ObjCClass('UITextField')):
  leftMarginPadding: CGFloat = objc_property(float)
  rightMarginPadding: CGFloat = objc_property(float)

  @objc_method
  def init(self) -> ObjCInstance:
    send_super(__class__, self, 'init')  # xxx: この返り値を返さないと意味なし?
    self.leftMarginPadding = 12.0
    self.rightMarginPadding = 36.0
    return self

  @objc_method
  def textRectForBounds_(self, bounds: CGRect) -> CGRect:
    send_super(__class__,
               self,
               'textRectForBounds:',
               bounds,
               argtypes=[
                 CGRect,
               ])
    rect = bounds
    rect.origin.x += self.leftMarginPadding
    rect.size.width -= self.rightMarginPadding

    return rect

  @objc_method
  def editingRectForBounds_(self, bounds: CGRect) -> CGRect:
    send_super(__class__,
               self,
               'editingRectForBounds:',
               bounds,
               argtypes=[
                 CGRect,
               ])
    rect = bounds
    rect.origin.x += self.leftMarginPadding
    rect.size.width -= self.rightMarginPadding

    return rect


if __name__ == '__main__':
  from rbedge.functions import NSStringFromClass
  from rbedge.enumerations import (
    UITableViewStyle,
    UIModalPresentationStyle,
  )
  from rbedge import present_viewController

  table_style = UITableViewStyle.grouped
  main_vc = TextFieldViewController.alloc().initWithStyle_(table_style)
  _title = NSStringFromClass(TextFieldViewController)
  main_vc.navigationItem.title = _title

  presentation_style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, presentation_style)

