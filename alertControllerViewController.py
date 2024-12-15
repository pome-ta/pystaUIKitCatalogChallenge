'''
  note: Storyboard 未定義
'''

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super

from rbedge.enumerations import (
  UITableViewStyle, )

from rbedge import pdbr

from pyLocalizedString import localizedString

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UITableView = ObjCClass('UITableView')
UITableViewCell = ObjCClass('UITableViewCell')
'''
Alert Style
Simple
OK / Cancel
Three Buttons
Text Entry
Secure Text Entry

Action Sheet Style
Confirm / Cancel
Destructive
'''

styleSections = [
  'Alert Style',
  'Action Sheet Style',
]

alertStyle_items = [
  'Simple',
  'OK / Cancel',
  'Three Buttons',
  'Text Entry',
  'Secure Text Entry',
]

actionSheetStyle_items = [
  'Confirm / Cancel',
  'Destructive',
]

style_items = [
  alertStyle_items,
  actionSheetStyle_items,
]


class AlertControllerViewController(UIViewController):

  @objc_method
  def viewDidLoad(self):
    # --- Navigation
    send_super(__class__, self, 'viewDidLoad')
    # --- Table set
    self.cell_identifier = 'customCell'

    tableView = UITableView.alloc().initWithFrame_style_(
      self.view.bounds, UITableViewStyle.grouped)
    tableView.registerClass_forCellReuseIdentifier_(UITableViewCell,
                                                    self.cell_identifier)

    #tableView.delegate = self
    tableView.dataSource = self

    # --- Layout
    self.view.addSubview_(tableView)
    tableView.translatesAutoresizingMaskIntoConstraints = False
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide
    NSLayoutConstraint.activateConstraints_([
      tableView.centerXAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerXAnchor),
      tableView.centerYAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerYAnchor),
      tableView.widthAnchor.constraintEqualToAnchor_multiplier_(
        safeAreaLayoutGuide.widthAnchor, 1.0),
      tableView.heightAnchor.constraintEqualToAnchor_multiplier_(
        safeAreaLayoutGuide.heightAnchor, 1.0),
    ])

  # --- UITableViewDataSource
  @objc_method
  def numberOfSectionsInTableView_(self, tableView) -> int:
    return len(styleSections)

  @objc_method
  def tableView_titleForHeaderInSection_(self, tableView, section: int):

    return styleSections[section]

  @objc_method
  def tableView_numberOfRowsInSection_(self, tableView, section: int) -> int:
    return len(style_items[section])

  @objc_method
  def tableView_cellForRowAtIndexPath_(self, tableView, indexPath):
    cell = tableView.dequeueReusableCellWithIdentifier_forIndexPath_(
      self.cell_identifier, indexPath)

    contentConfiguration = cell.defaultContentConfiguration()
    contentConfiguration.text = style_items[indexPath.section][indexPath.row]

    cell.contentConfiguration = contentConfiguration

    return cell


if __name__ == '__main__':
  from rbedge.functions import NSStringFromClass
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController

  main_vc = AlertControllerViewController.new()
  _title = NSStringFromClass(AlertControllerViewController)
  main_vc.navigationItem.title = _title
  style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, style)

