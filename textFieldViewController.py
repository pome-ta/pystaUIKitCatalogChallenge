"""
note: wip 項目
  - `ObjCProtocol` 不要？
  - `CustomTextField` class の`init` って機能してる？
  - 標準キーボードのみ機能するものあり
"""
import ctypes
from enum import Enum

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, objc_id, SEL
from pyrubicon.objc.types import (
  NSInteger,
  CGRect,
  CGFloat,
  CGRectMake,
  UIEdgeInsetsMake,
)

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
from rbedge.pythonProcessUtils import (
  mainScreen_scale,
  dataWithContentsOfURL,
)

from caseElement import CaseElement
from pyLocalizedString import localizedString

from baseTableViewController import BaseTableViewController
from storyboard.textFieldViewController import prototypes

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

UISearchTextField = ObjCClass('UISearchTextField')  # todo: 型確認用
UIColor = ObjCClass('UIColor')

UIImageView = ObjCClass('UIImageView')
UIImage = ObjCClass('UIImage')
UISearchToken = ObjCClass('UISearchToken')
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


class TextFieldViewController(BaseTableViewController):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t- {NSStringFromClass(__class__)}: dealloc')

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
    #print(f'\t{NSStringFromClass(__class__)}: initWithStyle_')
    return self

  @objc_method
  def loadView(self):
    send_super(__class__, self, 'loadView')
    #print(f'\t{NSStringFromClass(__class__)}: loadView')
    [
      self.tableView.registerClass_forCellReuseIdentifier_(
        prototype['cellClass'], prototype['identifier'])
      for prototype in prototypes
    ]

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    #print(f'\t{NSStringFromClass(__class__)}: viewDidLoad')

    self.navigationItem.title = localizedString('TextFieldsTitle') if (
      title := self.navigationItem.title) is None else title

    self.testCellsAppendContentsOf_([
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('DefaultTextFieldTitle'),
        TextFieldKind.textField.value, 'configureTextField:'),
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('TintedTextFieldTitle'),
        TextFieldKind.tintedTextField.value, 'configureTintedTextField:'),
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('SecuretTextFieldTitle'),
        TextFieldKind.secureTextField.value, 'configureSecureTextField:'),
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('SearchTextFieldTitle'),
        TextFieldKind.searchTextField.value, 'configureSearchTextField:'),
    ])

    if self.traitCollection.userInterfaceIdiom != UIUserInterfaceIdiom.mac:
      '''
      self.testCells_extend([
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
      '''
      self.testCellsAppendContentsOf_([
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('SpecificKeyboardTextFieldTitle'),
          TextFieldKind.specificKeyboardTextField.value,
          'configureSpecificKeyboardTextField:'),
        #CaseElement.alloc().initWithTitle_cellID_configHandlerName_(localizedString('CustomTextFieldTitle'), TextFieldKind.customTextField.value, 'configureCustomTextField:'),
      ])

  @objc_method
  def viewWillAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print(f'\t{NSStringFromClass(__class__)}: viewWillAppear_')

  @objc_method
  def viewDidAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print(f'\t{NSStringFromClass(__class__)}: viewDidAppear_')

  @objc_method
  def viewWillDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    # print(f'\t{NSStringFromClass(__class__)}: viewWillDisappear_')

  @objc_method
  def viewDidDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    print(f'\t{NSStringFromClass(__class__)}: viewDidDisappear_')

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'\t{NSStringFromClass(__class__)}: didReceiveMemoryWarning')

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

    scale = int(mainScreen_scale)
    background_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/text_field_background.imageset/text_field_background_{scale}x.png'

    purpleImage_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/text_field_purple_right_view.imageset/text_field_purple_right_view_{scale}x.png'

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
  #leftMarginPadding: CGFloat = objc_property(float)
  #rightMarginPadding: CGFloat = objc_property(float)

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
  from rbedge.app import App
  from rbedge.enumerations import (
    UITableViewStyle,
    UIModalPresentationStyle,
  )

  table_style = UITableViewStyle.grouped
  main_vc = TextFieldViewController.alloc().initWithStyle_(table_style)
  _title = NSStringFromClass(TextFieldViewController)
  main_vc.navigationItem.title = _title

  # presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

