import ctypes
from enum import Enum
#import re

from pyrubicon.objc.api import ObjCClass, ObjCInstance, objc_method, Block
from pyrubicon.objc.runtime import send_super, objc_id

from rbedge.enumerations import (
  UITableViewStyle,
  UIMenuElementState,
  UIMenuElementAttributes,
)
from rbedge.functions import NSStringFromClass

from caseElement import CaseElement
from pyLocalizedString import localizedString
from baseTableViewController import BaseTableViewController
from storyboard.menuButtonViewController import prototypes

UIMenu = ObjCClass('UIMenu')
UIAction = ObjCClass('UIAction')
UIImage = ObjCClass('UIImage')


# Cell identifier for each menu button table view cell.
# > 各メニュー ボタン テーブル ビュー セルのセル識別子。
class MenuButtonKind(Enum):
  buttonMenuProgrammatic = 'buttonMenuProgrammatic'
  buttonMenuMultiAction = 'buttonMenuMultiAction'
  buttonSubMenu = 'buttonSubMenu'
  buttonMenuSelection = 'buttonMenuSelection'


class ButtonMenuActionIdentifiers(Enum):
  item1 = 'item1'
  item2 = 'item2'
  item3 = 'item3'


class MenuButtonViewController(BaseTableViewController):

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
      CaseElement(localizedString('DropDownProgTitle'),
                  MenuButtonKind.buttonMenuProgrammatic.value,
                  self.configureDropDownProgrammaticButton_),
      CaseElement(localizedString('DropDownMultiActionTitle'),
                  MenuButtonKind.buttonMenuMultiAction.value,
                  self.configureDropdownMultiActionButton_),
      CaseElement(localizedString('DropDownButtonSubMenuTitle'),
                  MenuButtonKind.buttonSubMenu.value,
                  self.configureDropdownSubMenuButton_),
    ])

  # MARK: - Handlers
  @objc_method
  def menuHandler_(self, _action: ctypes.c_void_p) -> None:
    action = ObjCInstance(_action)
    switch_case = str(action.identifier)
    # xxx: `match` がPythonista3 (PEP8) だと、フォーマットできないため`if`
    if switch_case == ButtonMenuActionIdentifiers.item1.value:
      print('Menu Action: item 1')
    elif switch_case == ButtonMenuActionIdentifiers.item2.value:
      print('Menu Action: item 2')
    elif switch_case == ButtonMenuActionIdentifiers.item3.value:
      print('Menu Action: item 3')
    else:
      print('Menu Action: None')

  @objc_method
  def item4Handler_(self, _action: ctypes.c_void_p) -> None:
    action = ObjCInstance(_action)
    print(f'Menu Action: {action.title}')

  # MARK: - Drop Down Menu Buttons
  @objc_method
  def configureDropDownProgrammaticButton_(self, button):
    # xxx: 正規表現でやる？
    button.menu = UIMenu.menuWithChildren_([
      UIAction.actionWithTitle_image_identifier_handler_(
        localizedString('ItemTitle').replace('%@', '1'), None,
        ButtonMenuActionIdentifiers.item1.value,
        Block(self.menuHandler_, None, ctypes.c_void_p)),
      UIAction.actionWithTitle_image_identifier_handler_(
        localizedString('ItemTitle').replace('%@', '2'), None,
        ButtonMenuActionIdentifiers.item2.value,
        Block(self.menuHandler_, None, ctypes.c_void_p)),
    ])

    button.showsMenuAsPrimaryAction = True

  @objc_method
  def configureDropdownMultiActionButton_(self, button):

    @Block
    def menuAction5_closure(action: objc_id) -> None:
      print(f'Menu Action: {ObjCInstance(action).title}')

    @Block
    def menuAction6_closure(action: objc_id) -> None:
      print(f'Menu Action: {ObjCInstance(action).title}')

    # xxx: 正規表現でやる?
    buttonMenu = UIMenu.menuWithChildren_([
      # Share a single handler for the first 3 actions.
      # > 最初の 3 つのアクションに対して 1 つのハンドラーを共有します。
      UIAction.actionWithTitle_image_identifier_handler_(
        localizedString('ItemTitle').replace('%@', '1'),
        UIImage.systemImageNamed('1.circle'),
        ButtonMenuActionIdentifiers.item1.value,
        Block(self.menuHandler_, None, ctypes.c_void_p)),
      UIAction.actionWithTitle_image_identifier_handler_(
        localizedString('ItemTitle').replace('%@', '2'),
        UIImage.systemImageNamed('2.circle'),
        ButtonMenuActionIdentifiers.item2.value,
        Block(self.menuHandler_, None, ctypes.c_void_p)),
      UIAction.actionWithTitle_image_identifier_handler_(
        localizedString('ItemTitle').replace('%@', '3'),
        UIImage.systemImageNamed('3.circle'),
        ButtonMenuActionIdentifiers.item3.value,
        Block(self.menuHandler_, None, ctypes.c_void_p)),
      # Use a separate handler for this 4th action.
      # > この 4 番目のアクションには別のハンドラーを使用します。
      UIAction.actionWithTitle_image_identifier_handler_(
        localizedString('ItemTitle').replace('%@', '4'),
        UIImage.systemImageNamed('4.circle'), None,
        Block(self.item4Handler_, None, ctypes.c_void_p)),
      # Use a closure for the 5th action.
      # > 5 番目のアクションにはクロージャを使用します。
      UIAction.actionWithTitle_image_identifier_handler_(
        localizedString('ItemTitle').replace('%@', '5'),
        UIImage.systemImageNamed('5.circle'), None, menuAction5_closure),
      # Use attributes to make the 6th action disabled.
      # > 属性を使用して 6 番目のアクションを無効にします。
      UIAction.alloc().
      initWithTitle_image_identifier_discoverabilityTitle_attributes_state_handler_(
        localizedString('ItemTitle').replace('%@', '6'),
        UIImage.systemImageNamed('6.circle'), None, None,
        UIMenuElementAttributes.disabled, UIMenuElementState.off,
        menuAction6_closure),
    ])

    button.menu = buttonMenu
    button.showsMenuAsPrimaryAction = True

  @objc_method
  def configureDropdownSubMenuButton_(self, button):

    @Block
    def sortClosure(action: objc_id) -> None:
      print(f'Sort by: {ObjCInstance(action).title}')

    @Block
    def refreshClosure(action: objc_id) -> None:
      print('Refresh handler')

    @Block
    def accountHandler(action: objc_id) -> None:
      print('Account handler')

    sortMenu: UIMenu
    # xxx: `#available(iOS 15, *)`
    if True:  # .singleSelection option only on iOS 15 or later
      # The sort sub menu supports a selection.
      # > 並べ替えサブメニューは選択をサポートします。
      pdbr.state(UIMenu)
      #menuWithTitle_image_identifier_options_children__
      #menuWithTitle_imageName_identifier_options_children_


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  main_vc = MenuButtonViewController.new()
  #style = UIModalPresentationStyle.pageSheet
  style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, style)

