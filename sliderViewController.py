from enum import Enum

from pyrubicon.objc.api import ObjCClass, ObjCInstance, Block
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import SEL, send_super, objc_id
#from pyrubicon.objc.types import CGSize, CGFloat, CGRectMake, CGSizeMake

from rbedge.enumerations import (
  UITableViewStyle,
  UIControlEvents,
)
from rbedge.functions import NSStringFromClass

from caseElement import CaseElement
from pyLocalizedString import localizedString

from baseTableViewController import BaseTableViewController
from storyboard.sliderViewController import prototypes


# Cell identifier for each slider table view cell.
# スライダー テーブル ビューの各セルのセル識別子。
class SliderKind(Enum):
  sliderDefault = 'sliderDefault'
  sliderTinted = 'sliderTinted'
  sliderCustom = 'sliderCustom'
  sliderMaxMinImage = 'sliderMaxMinImage'


class SliderViewController(BaseTableViewController):

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
      CaseElement(localizedString('DefaultTitle'),
                  SliderKind.sliderDefault.value,
                  self.configureDefaultSlider_),
    ])

  # MARK: - Configuration
  @objc_method
  def configureDefaultSlider_(self, slider):
    slider.minimumValue = 0
    slider.maximumValue = 100
    slider.value = 42
    slider.isContinuous = True

    slider.addTarget_action_forControlEvents_(self,
                                              SEL('sliderValueDidChange:'),
                                              UIControlEvents.valueChanged)

  # MARK: - Actions
  @objc_method
  def sliderValueDidChange_(self, slider):
    formattedValue = f'{slider.value:.2f}'
    print(f'Slider changed its value: {formattedValue}')


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  main_vc = SliderViewController.new()
  #style = UIModalPresentationStyle.pageSheet
  style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, style)

