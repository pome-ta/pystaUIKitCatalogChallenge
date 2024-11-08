from enum import Enum
from pathlib import Path

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import SEL, send_super, objc_id

from rbedge.enumerations import (
  UITableViewStyle,
  UIControlEvents,
  UISwitchStyle,
  UIUserInterfaceIdiom,
)
from rbedge.functions import NSStringFromClass

from caseElement import CaseElement
from pyLocalizedString import localizedString

from baseTableViewController import BaseTableViewController
from storyboard.switchViewController import prototypes

UIScreen = ObjCClass('UIScreen')
NSURL = ObjCClass('NSURL')
NSData = ObjCClass('NSData')
UIImage = ObjCClass('UIImage')
UIImageSymbolConfiguration = ObjCClass('UIImageSymbolConfiguration')
UIColor = ObjCClass('UIColor')


# Cell identifier for each switch table view cell.
# 各スイッチ テーブル ビュー セルのセル識別子。
class SwitchKind(Enum):
  defaultSwitch = 'defaultSwitch'
  checkBoxSwitch = 'checkBoxSwitch'
  tintedSwitch = 'tintedSwitch'


class SwitchViewController(BaseTableViewController):

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

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?

    title = NSStringFromClass(__class__)
    self.navigationItem.title = title
    self.testCells.extend([
      CaseElement(localizedString('DefaultSwitchTitle'),
                  SwitchKind.defaultSwitch.value,
                  self.configureDefaultSwitch_),
    ])
    # Checkbox switch is available only when running on macOS.
    # チェックボックス スイッチは、macOS で実行している場合にのみ使用できます。
    pdbr.state(self.traitCollection,1)

  # MARK: - Configuration
  @objc_method
  def configureDefaultSwitch_(self, switchControl):
    switchControl.setOn_animated_(True, False)
    switchControl.preferredStyle = UISwitchStyle.sliding

    switchControl.addTarget_action_forControlEvents_(
      self, SEL('switchValueDidChange:'), UIControlEvents.valueChanged)

  # MARK: - Actions
  @objc_method
  def switchValueDidChange_(self, aSwitch):
    print(f'A switch changed its value: {aSwitch.isOn()}.')


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  main_vc = SwitchViewController.new()
  #style = UIModalPresentationStyle.pageSheet
  style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, style)

