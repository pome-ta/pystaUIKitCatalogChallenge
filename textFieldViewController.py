import ctypes
from enum import Enum

from pyrubicon.objc.api import ObjCClass, ObjCProtocol
from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.runtime import SEL, send_super, objc_id
from pyrubicon.objc.types import CGRect, CGFloat
from rbedge import pdbr
'''
#UITextField = ObjCClass('UITextField')
# Custom text field for controlling input text placement.
# 入力テキストの配置を制御するためのカスタム テキスト フィールド。
class CustomTextField(ObjCClass('UITextField')):
  leftMarginPadding: CGFloat = objc_property(float)
  rightMarginPadding: CGFloat = objc_property(float)

  @objc_method
  def init(self) -> objc_id:
    send_super(__class__, self, 'init')  # xxx: この返り値を返さないと意味なし？
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
'''
from rbedge.enumerations import (
  UITableViewStyle,
  UITextAutocorrectionType,
  UIReturnKeyType,
  UITextFieldViewMode,
)
from rbedge.functions import NSStringFromClass

from caseElement import CaseElement
from pyLocalizedString import localizedString

from baseTableViewController import BaseTableViewController
from storyboard.textFieldViewController import prototypes

UIColor = ObjCClass('UIColor')
UITextFieldDelegate = ObjCProtocol('UITextFieldDelegate')


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

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?

    title = NSStringFromClass(__class__)
    self.navigationItem.title = title

    self.testCells.extend([
      CaseElement(localizedString('DefaultTextFieldTitle'),
                  TextFieldKind.textField.value, self.configureTextField_),
      CaseElement(localizedString('TintedTextFieldTitle'),
                  TextFieldKind.tintedTextField.value,
                  self.configureTintedTextField_),
      CaseElement(localizedString('SecuretTextFieldTitle'),
                  TextFieldKind.secureTextField.value,
                  self.configureSecureTextField_),
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
    textField.tintColor = UIColor.systemBlueColor()
    textField.textColor = UIColor.systemGreenColor()

    textField.placeholder = localizedString('Placeholder text')
    textInputTraits = textField.textInputTraits()
    textInputTraits.returnKeyType = UIReturnKeyType.done
    textField.clearButtonMode = UITextFieldViewMode.never

  @objc_method
  def configureSecureTextField_(self, textField):
    textField.setSecureTextEntry_(True)  # xxx: `setSecureTextEntry_` しか見つからず

    textField.placeholder = localizedString('Placeholder text')

    textInputTraits = textField.textInputTraits()
    textInputTraits.returnKeyType = UIReturnKeyType.done
    textField.clearButtonMode = UITextFieldViewMode.always

  # MARK: - Actions
  @objc_method
  def customTextFieldPurpleButtonClicked():
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

  '''  # xxx: 落ちる
  @objc_method
  def textField_shouldChangeCharactersInRange_replacementString_(
      self, range, string) -> bool:
    # Return false to not change text.
    # テキストを変更しない場合は false を返します。
    #print('shouldChangeCharactersInRange_replacementString')
    #print(range)
    #print(string)
    return True
  '''


# xxx: Storyboard 先へ遅延でimport させられるか？
#UITextField = ObjCClass('UITextField')
# Custom text field for controlling input text placement.
# 入力テキストの配置を制御するためのカスタム テキスト フィールド。
class CustomTextField(ObjCClass('UITextField')):
  leftMarginPadding: CGFloat = objc_property(float)
  rightMarginPadding: CGFloat = objc_property(float)

  @objc_method
  def init(self) -> objc_id:
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
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController

  main_vc = TextFieldViewController.new()
  #style = UIModalPresentationStyle.pageSheet
  style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, style)

