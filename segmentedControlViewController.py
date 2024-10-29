from enum import Enum

from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.runtime import SEL, send_super

from rbedge.enumerations import UITableViewStyle
from rbedge.functions import NSStringFromClass

from caseElement import CaseElement
from pyLocalizedString import localizedString
from baseTableViewController import BaseTableViewController
from storyboard.segmentedControlViewController import prototypes


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
    ])

  
  # MARK: - Configuration
  @objc_method
  def configureDefaultSegmentedControl_(self, segmentedControl):
    segmentedControl.setEnabled_forSegmentAtIndex_(False, 0)
    #addTarget_action_forControlEvents_
    pdbr.state(segmentedControl,1)
    
    
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

