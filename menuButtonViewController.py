import ctypes
from enum import Enum
#import re

from pyrubicon.objc.api import ObjCClass, ObjCInstance, objc_method, Block
from pyrubicon.objc.runtime import send_super

from rbedge.enumerations import (
  UITableViewStyle, )
from rbedge.functions import NSStringFromClass

from caseElement import CaseElement
from pyLocalizedString import localizedString
from baseTableViewController import BaseTableViewController
from storyboard.menuButtonViewController import prototypes

UIMenu = ObjCClass('UIMenu')
UIAction = ObjCClass('UIAction')

#UIMenuElement = ObjCClass('UIMenuElement')


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


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  main_vc = MenuButtonViewController.new()
  #style = UIModalPresentationStyle.pageSheet
  style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, style)

