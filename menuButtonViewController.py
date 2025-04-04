import ctypes
from enum import Enum

from pyrubicon.objc.api import ObjCClass, ObjCInstance, Block
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, objc_id
from pyrubicon.objc.types import NSInteger

from rbedge.enumerations import (
  UIMenuElementState,
  UIMenuElementAttributes,
  UIMenuOptions,
)
from rbedge.functions import NSStringFromClass
from rbedge import pdbr

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

    # --- Navigation
    self.navigationItem.title = localizedString('MenuButtonsTitle') if (
      title := self.navigationItem.title) is None else title

    self.testCellsAppendContentsOf_([
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('DropDownProgTitle'),
        MenuButtonKind.buttonMenuProgrammatic.value,
        'configureDropDownProgrammaticButton:'),
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('DropDownMultiActionTitle'),
        MenuButtonKind.buttonMenuMultiAction.value,
        'configureDropdownMultiActionButton:'),
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('DropDownButtonSubMenuTitle'),
        MenuButtonKind.buttonSubMenu.value, 'configureDropdownSubMenuButton:'),
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('PopupSelection'),
        MenuButtonKind.buttonMenuSelection.value,
        'configureSelectionPopupButton:'),
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
    print(f'{__class__}: didReceiveMemoryWarning')

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
    # todo: closure をblock 処理
    @Block
    def menuAction5_closure(_action: objc_id) -> None:
      print(f'Menu Action: {ObjCInstance(_action).title}')

    @Block
    def menuAction6_closure(_action: objc_id) -> None:
      print(f'Menu Action: {ObjCInstance(_action).title}')

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
      # todo: closure をblock 処理
      UIAction.actionWithTitle_image_identifier_handler_(
        localizedString('ItemTitle').replace('%@', '5'),
        UIImage.systemImageNamed('5.circle'), None, menuAction5_closure),
      # Use attributes to make the 6th action disabled.
      # > 属性を使用して 6 番目のアクションを無効にします。
      # todo: closure をblock 処理
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
    def sortClosure(_action: objc_id) -> None:
      print(f'Sort by: {ObjCInstance(_action).title}')

    @Block
    def refreshClosure(_action: objc_id) -> None:
      print('Refresh handler')

    @Block
    def accountHandler(_action: objc_id) -> None:
      print('Account handler')

    sortMenu: UIMenu
    # xxx: `#available(iOS 15, *)`
    if True:  # .singleSelection option only on iOS 15 or later
      # The sort sub menu supports a selection.
      # > 並べ替えサブメニューは選択をサポートします。

      sortMenu = sortMenu = UIMenu.menuWithTitle_image_identifier_options_children_(
        'Sort By', None, None, UIMenuOptions.singleSelection, [
          UIAction.alloc().initWithTitle('Date',
                                         image=None,
                                         identifier=None,
                                         discoverabilityTitle=None,
                                         attributes=0,
                                         state=UIMenuElementState.on,
                                         handler=sortClosure),
          UIAction.alloc().initWithTitle('Size',
                                         image=None,
                                         identifier=None,
                                         discoverabilityTitle=None,
                                         attributes=0,
                                         state=UIMenuElementState.off,
                                         handler=sortClosure),
        ])
    else:
      sortMenu = UIMenu.menuWithTitle_children_('Sort By', [
        UIAction.alloc().initWithTitle('Date',
                                       image=None,
                                       identifier=None,
                                       discoverabilityTitle=None,
                                       attributes=0,
                                       state=UIMenuElementState.on,
                                       handler=sortClosure),
        UIAction.alloc().initWithTitle('Size',
                                       image=None,
                                       identifier=None,
                                       discoverabilityTitle=None,
                                       attributes=0,
                                       state=UIMenuElementState.off,
                                       handler=sortClosure),
      ])

    topMenu = UIMenu.menuWithChildren_([
      UIAction.actionWithTitle_image_identifier_handler_(
        'Refresh', None, None, refreshClosure),
      UIAction.actionWithTitle_image_identifier_handler_(
        'Account', None, None, accountHandler),
      sortMenu,
    ])
    # This makes the button behave like a drop down menu.
    # > これにより、ボタンがドロップダウン メニューのように動作します。
    button.showsMenuAsPrimaryAction = True
    button.menu = topMenu

  # MARK: - Selection Popup Menu Button

  @objc_method
  def updateColor_(self, _title: ctypes.c_void_p) -> None:
    print(f'Color selected: {ObjCInstance(_title)}')

  @objc_method
  def configureSelectionPopupButton_(self, button):

    @Block
    def colorClosure(_action: objc_id) -> None:
      self.updateColor_(ObjCInstance(_action).title)

    button.menu = UIMenu.menuWithChildren_([
      UIAction.alloc().initWithTitle('Red',
                                     image=None,
                                     identifier=None,
                                     discoverabilityTitle=None,
                                     attributes=0,
                                     state=UIMenuElementState.off,
                                     handler=colorClosure),
      UIAction.alloc().initWithTitle('Green',
                                     image=None,
                                     identifier=None,
                                     discoverabilityTitle=None,
                                     attributes=0,
                                     state=UIMenuElementState.on,
                                     handler=colorClosure),
      UIAction.alloc().initWithTitle('Blue',
                                     image=None,
                                     identifier=None,
                                     discoverabilityTitle=None,
                                     attributes=0,
                                     state=UIMenuElementState.off,
                                     handler=colorClosure),
    ])
    # This makes the button behave like a drop down menu.
    # > これにより、ボタンがドロップダウン メニューのように動作します。
    button.showsMenuAsPrimaryAction = True

    if True:  # xxx: `#available(iOS 15, *)`
      button.changesSelectionAsPrimaryAction = True
      # Select the default menu item (green).
      # > デフォルトのメニュー項目 (緑色) を選択します。
      self.updateColor_(button.menu.selectedElements.firstObject().title)


if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import (
    UITableViewStyle,
    UIModalPresentationStyle,
  )

  table_style = UITableViewStyle.grouped
  main_vc = MenuButtonViewController.alloc().initWithStyle_(table_style)
  _title = NSStringFromClass(MenuButtonViewController)
  main_vc.navigationItem.title = _title

  # presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

