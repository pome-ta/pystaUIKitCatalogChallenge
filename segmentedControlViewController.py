from enum import Enum

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import SEL, send_super

from rbedge.enumerations import UITableViewStyle
from rbedge.functions import NSStringFromClass

from caseElement import CaseElement
from pyLocalizedString import localizedString
from baseTableViewController import BaseTableViewController
from storyboard.segmentedControlViewController import prototypes

from rbedge.enumerations import UIControlEvents

UIImage = ObjCClass('UIImage')


class SegmentKind(Enum):
  segmentDefault = 'segmentDefault'
  segmentTinted = 'segmentTinted'
  segmentCustom = 'segmentCustom'
  segmentCustomBackground = 'segmentCustomBackground'
  segmentAction = 'segmentAction'


class SegmentedControlViewController(BaseTableViewController):

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
      CaseElement(localizedString('DefaultTitle'),
                  SegmentKind.segmentDefault.value,
                  self.configureDefaultSegmentedControl_),
      CaseElement(localizedString('CustomSegmentsTitle'),
                  SegmentKind.segmentCustom.value,
                  self.configureCustomSegmentsSegmentedControl_),
      #CaseElement(localizedString('CustomBackgroundTitle'),SegmentKind.segmentCustomBackground.value,self.configureCustomBackgroundSegmentedControl_),
    ])

  # MARK: - Configuration
  @objc_method
  def configureDefaultSegmentedControl_(self, segmentedControl):
    segmentedControl.setEnabled_forSegmentAtIndex_(False, 0)
    segmentedControl.addTarget_action_forControlEvents_(
      self, SEL('selectedSegmentDidChange:'), UIControlEvents.valueChanged)

  @objc_method
  def configureCustomSegmentsSegmentedControl_(self, segmentedControl):
    airplaneImage = UIImage.systemImageNamed_('airplane')
    airplaneImage.accessibilityLabel = localizedString('Airplane')
    segmentedControl.setImage_forSegmentAtIndex_(airplaneImage, 0)

    giftImage = UIImage.systemImageNamed_('gift')
    giftImage.accessibilityLabel = localizedString('Gift')
    segmentedControl.setImage_forSegmentAtIndex_(giftImage, 1)

    burstImage = UIImage.systemImageNamed_('burst')
    burstImage.accessibilityLabel = localizedString('Burst')
    segmentedControl.setImage_forSegmentAtIndex_(burstImage, 2)

    segmentedControl.selectedSegmentIndex = 0

    segmentedControl.addTarget_action_forControlEvents_(
      self, SEL('selectedSegmentDidChange:'), UIControlEvents.valueChanged)

  # Configure the segmented control with a background image, dividers, and custom font.
  # セグメント化されたコントロールに、背景画像、仕切り、カスタム・フォントを設定する。
  # The background image first needs to be sized to match the control's size.
  # 背景画像は、まずコントロールのサイズに合わせた大きさにする必要があります。
  @objc_method
  def configureCustomBackgroundSegmentedControl_(self, placeHolderView):
    pass

  # MARK: - Actions
  @objc_method
  def selectedSegmentDidChange_(self, segmentedControl):
    print(f'The selected segment: {segmentedControl.selectedSegmentIndex}')


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  main_vc = SegmentedControlViewController.new()
  #style = UIModalPresentationStyle.pageSheet
  style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, style)

