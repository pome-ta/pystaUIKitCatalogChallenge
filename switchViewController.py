import ctypes
from enum import Enum

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, objc_id, SEL
from pyrubicon.objc.types import NSInteger

from rbedge.enumerations import (
  UIControlEvents,
  UISwitchStyle,
  UIUserInterfaceIdiom,
)

from caseElement import CaseElement
from pyLocalizedString import localizedString

from baseTableViewController import BaseTableViewController
from storyboard.switchViewController import prototypes

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

UIColor = ObjCClass('UIColor')


# Cell identifier for each switch table view cell.
# 各スイッチ テーブル ビュー セルのセル識別子。
class SwitchKind(Enum):
  defaultSwitch = 'defaultSwitch'
  checkBoxSwitch = 'checkBoxSwitch'
  tintedSwitch = 'tintedSwitch'


class SwitchViewController(BaseTableViewController):

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

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')

    self.navigationItem.title = localizedString('SwitchesTitle') if (
      title := self.navigationItem.title) is None else title

    self.testCellsAppendContentsOf_([
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('DefaultSwitchTitle'), SwitchKind.defaultSwitch.value,
        'configureDefaultSwitch:'),
    ])
    # Checkbox switch is available only when running on macOS.
    # チェックボックス スイッチは、macOS で実行している場合にのみ使用できます。

    # todo: `if navigationController!.traitCollection.userInterfaceIdiom` `navigationController` が`None` なため`self` で判断
    if self.traitCollection.userInterfaceIdiom == UIUserInterfaceIdiom.mac:
      self.testCellsAppendContentsOf_([
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('CheckboxSwitchTitle'),
          SwitchKind.checkBoxSwitch.value, 'configureCheckboxSwitch:'),
      ])

    # Tinted switch is available only when running on iOS.
    # 色付きスイッチは、iOS で実行している場合にのみ使用できます。
    if self.traitCollection.userInterfaceIdiom != UIUserInterfaceIdiom.mac:
      self.testCellsAppendContentsOf_([
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('TintedSwitchTitle'), SwitchKind.tintedSwitch.value,
          'configureTintedSwitch:'),
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
  def configureDefaultSwitch_(self, switchControl):
    switchControl.setOn_animated_(True, False)
    switchControl.preferredStyle = UISwitchStyle.sliding

    switchControl.addTarget_action_forControlEvents_(
      self, SEL('switchValueDidChange:'), UIControlEvents.valueChanged)

  @objc_method
  def configureCheckboxSwitch_(self, switchControl):
    switchControl.setOn_animated_(True, False)

    switchControl.addTarget_action_forControlEvents_(
      self, SEL('switchValueDidChange:'), UIControlEvents.valueChanged)

    # On the Mac, make sure this control take on the apperance of a checkbox with a title.
    # Mac では、このコントロールがタイトル付きのチェックボックスの外観になるようにしてください。

    if self.traitCollection.userInterfaceIdiom == UIUserInterfaceIdiom.mac:
      switchControl.preferredStyle = UISwitchStyle.checkbox
      switchControl.title = localizedString('SwitchTitle')

  @objc_method
  def configureTintedSwitch_(self, switchControl):
    switchControl.tintColor = UIColor.systemBlueColor()
    switchControl.onTintColor = UIColor.systemGreenColor()
    switchControl.thumbTintColor = UIColor.systemPurpleColor()

    switchControl.addTarget_action_forControlEvents_(
      self, SEL('switchValueDidChange:'), UIControlEvents.valueChanged)

  # MARK: - Actions
  @objc_method
  def switchValueDidChange_(self, aSwitch):
    print(f'A switch changed its value: {aSwitch.isOn()}.')


if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import (
    UITableViewStyle,
    UIModalPresentationStyle,
  )

  table_style = UITableViewStyle.grouped
  main_vc = SwitchViewController.alloc().initWithStyle_(table_style)
  _title = NSStringFromClass(SwitchViewController)
  main_vc.navigationItem.title = _title

  # presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

