from enum import Enum

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
    #self.navigationItem.title = title
    self.navigationItem.title = localizedString('SwitchesTitle')

    self.testCells.extend([
      CaseElement(localizedString('DefaultSwitchTitle'),
                  SwitchKind.defaultSwitch.value,
                  self.configureDefaultSwitch_),
    ])
    # Checkbox switch is available only when running on macOS.
    # チェックボックス スイッチは、macOS で実行している場合にのみ使用できます。

    # todo: `if navigationController!.traitCollection.userInterfaceIdiom` `navigationController` が`None` なため`self` で判断
    if self.traitCollection.userInterfaceIdiom == UIUserInterfaceIdiom.mac:
      self.testCells.extend([
        CaseElement(localizedString('CheckboxSwitchTitle'),
                    SwitchKind.checkBoxSwitch.value,
                    self.configureCheckboxSwitch_),
      ])

    # Tinted switch is available only when running on iOS.
    # 色付きスイッチは、iOS で実行している場合にのみ使用できます。
    if self.traitCollection.userInterfaceIdiom != UIUserInterfaceIdiom.mac:
      self.testCells.extend([
        CaseElement(localizedString('TintedSwitchTitle'),
                    SwitchKind.tintedSwitch.value,
                    self.configureTintedSwitch_),
      ])

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
    #switchControl.setTintColor_(UIColor.systemPinkColor())
    switchControl.onTintColor = UIColor.systemGreenColor()
    switchControl.thumbTintColor = UIColor.systemPurpleColor()

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

