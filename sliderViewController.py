from enum import Enum
from pathlib import Path

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


UIScreen = ObjCClass('UIScreen')
NSURL = ObjCClass('NSURL')
NSData = ObjCClass('NSData')
UIImage = ObjCClass('UIImage')

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
    # todo: `@available(iOS 15.0, *)`
    self.testCells.extend([
      CaseElement(localizedString('CustomTitle'),
                  SliderKind.sliderCustom.value,
                  self.configureCustomSlider_),
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

  # todo: `@available(iOS 15.0, *)`
  @objc_method
  def configureCustomSlider_(self, slider):
    # To keep the look the same betwen iOS and macOS:
    #   For setMinimumTrackImage, setMaximumTrackImage, setThumbImage to work in Mac Catalyst, use UIBehavioralStyle as ".pad",
    #   Available in macOS 12 or later (Mac Catalyst 15.0 or later).
    #   Use this for controls that need to look the same between iOS and macOS.
    # iOSとmacOSで見た目を同じにするため:
    #  setMinimumTrackImage、setMaximumTrackImage、setThumbImageをMac Catalystで動作させるには、UIBehavioralStyleを".pad "として使用します。
    #  iOSとmacOSで同じ外観にする必要があるコントロールに使用します。
    
  
  
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

