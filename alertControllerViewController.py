'''
  note: Storyboard 未定義
'''

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, objc_id

from rbedge.enumerations import (
  UITableViewStyle,
  UIAlertControllerStyle,
  UIAlertActionStyle,
)

from rbedge import pdbr

from pyLocalizedString import localizedString

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UITableView = ObjCClass('UITableView')
UITableViewCell = ObjCClass('UITableViewCell')

UIAlertController = ObjCClass('UIAlertController')
UIAlertAction = ObjCClass('UIAlertAction')

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
    send_super(__class__, self, 'viewDidLoad')
    # --- Table set
    self.cell_identifier = 'customCell'
    tableView = UITableView.alloc().initWithFrame_style_(
      self.view.bounds, UITableViewStyle.grouped)
    tableView.registerClass_forCellReuseIdentifier_(UITableViewCell,
                                                    self.cell_identifier)
    tableView.delegate = self
    tableView.dataSource = self

    # --- Layout
    self.view.addSubview_(tableView)
    tableView.translatesAutoresizingMaskIntoConstraints = False
    #areaLayoutGuide = self.view.safeAreaLayoutGuide
    areaLayoutGuide = self.view
    NSLayoutConstraint.activateConstraints_([
      tableView.centerXAnchor.constraintEqualToAnchor_(
        areaLayoutGuide.centerXAnchor),
      tableView.centerYAnchor.constraintEqualToAnchor_(
        areaLayoutGuide.centerYAnchor),
      tableView.widthAnchor.constraintEqualToAnchor_multiplier_(
        areaLayoutGuide.widthAnchor, 1.0),
      tableView.heightAnchor.constraintEqualToAnchor_multiplier_(
        areaLayoutGuide.heightAnchor, 1.0),
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
  def tableView_cellForRowAtIndexPath_(self, tableView, indexPath) -> objc_id:
    cell = tableView.dequeueReusableCellWithIdentifier_forIndexPath_(
      self.cell_identifier, indexPath)

    contentConfiguration = cell.defaultContentConfiguration()
    contentConfiguration.text = style_items[indexPath.section][indexPath.row]

    cell.contentConfiguration = contentConfiguration
    return cell

  # --- UITableViewDelegate
  @objc_method
  def tableView_didSelectRowAtIndexPath_(self, tableView, indexPath):
    if (section := indexPath.section) == 0:
      # alertStyleSection
      if (row := indexPath.row) == 0:
        print(f'{section}: {row}')
        self.showSimpleAlert()
      elif row == 1:
        print(f'{section}: {row}')
      elif row == 2:
        print(f'{section}: {row}')
      elif row == 3:
        print(f'{section}: {row}')
      elif row == 4:
        print(f'{section}: {row}')

    elif section == 1:
      # actionStyleSection
      if (row := indexPath.row) == 0:
        print(f'{section}: {row}')
      elif row == 1:
        print(f'{section}: {row}')

    tableView.deselectRowAtIndexPath_animated_(indexPath, True)

  # MARK: - UIAlertControllerStyleAlert Style Alerts

  # Show an alert with an "OK" button.
  @objc_method
  def showSimpleAlert(self):
    title = localizedString('A Short Title is Best')
    message = localizedString(
      'A message needs to be a short, complete sentence.')
    cancelButtonTitle = localizedString('OK')
    print(title)
    print(message)
    print(cancelButtonTitle)
    alertController = UIAlertController.alertControllerWithTitle_message_preferredStyle_(title, message, UIAlertControllerStyle.alert)
    #UIAlertControllerStyle.alert
    #actionWithTitle:style:handler:
    #UIAlertActionStyle.cancel
    
    pdbr.state(alertController)


if __name__ == '__main__':
  from rbedge.functions import NSStringFromClass
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController

  main_vc = AlertControllerViewController.new()
  _title = NSStringFromClass(AlertControllerViewController)
  main_vc.navigationItem.title = _title
  style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, style)

