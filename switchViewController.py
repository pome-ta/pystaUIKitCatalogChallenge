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
from rbedge import pdbr

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

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?

    self.navigationItem.title = localizedString('SwitchesTitle') if (
      title := self.navigationItem.title) is None else title

    self.testCells.extend([
      CaseElement(localizedString('DefaultSwitchTitle'),
                  SwitchKind.defaultSwitch.value,
                  self.configureDefaultSwitch_),
    ])
    # Checkbox switch is available only when running on macOS.
    # チェックボックス スイッチは、macOS で実行している場合にのみ使用できます。

    # todo: `if navigationController!.traitCollection.userInterfaceIdiom` `navigationController` が`None` なため`self` で判断
    if self.traitCollection.userInterfaceIdiom == UIUserInterfaceIdiom.mac:
      self.testCells_extend([
        CaseElement(localizedString('CheckboxSwitchTitle'),
                    SwitchKind.checkBoxSwitch.value,
                    self.configureCheckboxSwitch_),
      ])

    # Tinted switch is available only when running on iOS.
    # 色付きスイッチは、iOS で実行している場合にのみ使用できます。
    if self.traitCollection.userInterfaceIdiom != UIUserInterfaceIdiom.mac:
      self.testCells_extend([
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
  from rbedge.functions import NSStringFromClass
  from rbedge.enumerations import (
    UITableViewStyle,
    UIModalPresentationStyle,
  )
  from rbedge import present_viewController

  table_style = UITableViewStyle.grouped
  main_vc = SwitchViewController.alloc().initWithStyle_(table_style)
  _title = NSStringFromClass(SwitchViewController)
  main_vc.navigationItem.title = _title

  presentation_style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, presentation_style)

