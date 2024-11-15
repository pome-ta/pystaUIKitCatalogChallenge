from enum import Enum
from pathlib import Path
import json

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.runtime import SEL, send_super, objc_id
from pyrubicon.objc.types import CGRect, CGFloat, CGRectMake, UIEdgeInsetsMake

from rbedge.enumerations import UITableViewStyle
from rbedge.functions import NSStringFromClass

from caseElement import CaseElement
from pyLocalizedString import localizedString
from baseTableViewController import BaseTableViewController
from storyboard.stepperViewController import prototypes

from rbedge.enumerations import (
  UIControlEvents,
  UIUserInterfaceIdiom,
  UIUserInterfaceStyle,
  UIControlState,
)

from rbedge import pdbr

UIColor = ObjCClass('UIColor')


def get_srgb_named_style(named: str,
                         userInterfaceStyle: UIUserInterfaceStyle) -> list:
  # todo: 本来`UIColor.colorNamed:` で呼び出す。asset(bundle) の取り込みが難しそうなので、独自に直で呼び出し
  _path = Path(
    f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/{named}.colorset/Contents.json'
  )
  _str = _path.read_text()
  _dict = json.loads(_str)

  def _pick_color(colors: list[dict], style: str | None = None) -> list:
    components: dict
    for color in colors:
      if color.get('idiom') != 'universal':
        continue
      appearance, *_ = appearances if (
        appearances := color.get('appearances')) is not None else [None]
      if style is None and appearance is None:
        components = color.get('color').get('components')
        break
      if appearance is not None and style == appearance.get('value'):
        components = color.get('color').get('components')
        break

    red, green, blue, alpha = (float(components.get(clr))
                               for clr in ('red', 'green', 'blue', 'alpha'))
    # wip: エラーハンドリング
    return [red, green, blue, alpha]

  color_dicts = _dict.get('colors')
  if userInterfaceStyle == UIUserInterfaceStyle.light:
    return _pick_color(color_dicts, 'light')
  elif userInterfaceStyle == UIUserInterfaceStyle.dark:
    return _pick_color(color_dicts, 'dark')
  else:
    return _pick_color(color_dicts)


# Cell identifier for each stepper table view cell.
# 各ステッパー テーブル ビュー セルのセル識別子。
class StepperKind(Enum):
  defaultStepper = 'defaultStepper'
  tintedStepper = 'tintedStepper'
  customStepper = 'customStepper'


class StepperViewController(BaseTableViewController):

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
      CaseElement(localizedString('DefaultStepperTitle'),
                  StepperKind.defaultStepper.value,
                  self.configureDefaultStepper_),
      CaseElement(localizedString('TintedStepperTitle'),
                  StepperKind.tintedStepper.value,
                  self.configureTintedStepper_),
    ])

  # MARK: - Configuration
  @objc_method
  def configureDefaultStepper_(self, stepper):
    # Setup the stepper range 0 to 10, initial value 0, increment/decrement factor of 1.
    # ステッパー範囲 0 ~ 10、初期値 0、増減係数 1 を設定します。
    stepper.value = 0.0
    stepper.minimumValue = 0.0
    stepper.maximumValue = 10.0
    stepper.stepValue = 1.0

    stepper.addTarget_action_forControlEvents_(self,
                                               SEL('stepperValueDidChange:'),
                                               UIControlEvents.valueChanged)

  @objc_method
  def configureTintedStepper_(self, stepper):
    # Setup the stepper range 0 to 20, initial value 20, increment/decrement factor of 1.
    # ステッパー範囲 0 ~ 20、初期値 20、増減係数 1 を設定します。
    stepper.value = 20.0
    stepper.minimumValue = 0.0
    stepper.maximumValue = 20.0
    stepper.stepValue = 1.0

    _style = self.traitCollection.userInterfaceStyle
    _srgb = get_srgb_named_style('tinted_stepper_control', _style)

    _color_named = UIColor.colorWithRed_green_blue_alpha_(*_srgb)
    stepper.tintColor = _color_named

    stepper.setDecrementImage_forState_(
      stepper.decrementImageForState_(UIControlState.normal),
      UIControlState.normal)
    stepper.setIncrementImage_forState_(
      stepper.incrementImageForState_(UIControlState.normal),
      UIControlState.normal)

    stepper.addTarget_action_forControlEvents_(self,
                                               SEL('stepperValueDidChange:'),
                                               UIControlEvents.valueChanged)

  # MARK: - Actions
  @objc_method
  def stepperValueDidChange_(self, stepper):
    print(f'A stepper changed its value: {stepper.value}')


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController

  main_vc = StepperViewController.new()
  #style = UIModalPresentationStyle.pageSheet
  style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, style)

