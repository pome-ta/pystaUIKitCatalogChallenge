'''
  note: Storyboard 未定義
    - index 呼び出しよりenum か？
'''

from pyrubicon.objc.api import ObjCClass, Block
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
    self.navigationItem.title = localizedString('AlertControllersTitle')
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
        #print(f'{section}: {row}')
        self.showSimpleAlert()
      elif row == 1:
        #print(f'{section}: {row}')
        self.showOkayCancelAlert()
      elif row == 2:
        #print(f'{section}: {row}')
        self.showOtherAlert()
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

    alertController = UIAlertController.alertControllerWithTitle_message_preferredStyle_(
      title, message, UIAlertControllerStyle.alert)

    #@Block
    def actionHandler() -> None:
      print("The simple alert's cancel action occurred.")

    # Create the action.
    #cancelAction = UIAlertAction.actionWithTitle_style_handler_(cancelButtonTitle, UIAlertActionStyle.cancel, Block(actionHandler))

    cancelAction = UIAlertAction.actionWithTitle_style_handler_(
      cancelButtonTitle, UIAlertActionStyle.cancel,
      Block(lambda: print("The simple alert's cancel action occurred."), None))
    '''
    cancelAction = UIAlertAction.actionWithTitle(
      cancelButtonTitle,
      style=UIAlertActionStyle.cancel,
      handler=Block(
        lambda: print("The simple alert's cancel action occurred."), None))
    '''

    # Add the action.
    alertController.addAction_(cancelAction)

    self.presentViewController(alertController, animated=True, completion=None)

  # Show an alert with an "OK" and "Cancel" button.
  @objc_method
  def showOkayCancelAlert(self):
    title = localizedString('A Short Title is Best')
    message = localizedString(
      'A message needs to be a short, complete sentence.')
    cancelButtonTitle = localizedString('Cancel')
    otherButtonTitle = localizedString('OK')

    alertController = UIAlertController.alertControllerWithTitle_message_preferredStyle_(
      title, message, UIAlertControllerStyle.alert)

    @Block
    def cancelActionHandler() -> None:
      print("The 'OK/Cancel' alert's cancel action occurred.")

    @Block
    def otherActionHandler() -> None:
      print("The 'OK/Cancel' alert's other action occurred.")

    # Create the action.
    cancelAction = UIAlertAction.actionWithTitle_style_handler_(
      cancelButtonTitle, UIAlertActionStyle.cancel, cancelActionHandler)
    otherAction = UIAlertAction.actionWithTitle_style_handler_(
      otherButtonTitle, UIAlertActionStyle.default, otherActionHandler)

    # Add the action.
    alertController.addAction_(cancelAction)
    alertController.addAction_(otherAction)

    self.presentViewController(alertController, animated=True, completion=None)

  # Show an alert with two custom buttons.
  @objc_method
  def showOtherAlert(self):
    title = localizedString('A Short Title is Best')
    message = localizedString(
      'A message needs to be a short, complete sentence.')
    cancelButtonTitle = localizedString('Cancel')
    otherButtonTitleOne = localizedString('Choice One')
    otherButtonTitleTwo = localizedString('Choice Two')

    alertController = UIAlertController.alertControllerWithTitle_message_preferredStyle_(
      title, message, UIAlertControllerStyle.alert)

    @Block
    def cancelActionHandler() -> None:
      print("The 'Other' alert's cancel action occurred.")

    @Block
    def otherOneActionHandler() -> None:
      print("The 'Other' alert's other button one action occurred.")

    @Block
    def otherTwoActionHandler() -> None:
      print("The 'Other' alert's other button two action occurred.")

    # Create the action.
    cancelAction = UIAlertAction.actionWithTitle_style_handler_(
      cancelButtonTitle, UIAlertActionStyle.cancel, cancelActionHandler)
    otherButtonOneAction = UIAlertAction.actionWithTitle_style_handler_(
      otherButtonTitleOne, UIAlertActionStyle.default, otherOneActionHandler)
    otherButtonTwoAction = UIAlertAction.actionWithTitle_style_handler_(
      otherButtonTitleTwo, UIAlertActionStyle.default, otherTwoActionHandler)

    # Add the action.
    alertController.addAction_(cancelAction)
    alertController.addAction_(otherButtonOneAction)
    alertController.addAction_(otherButtonTwoAction)

    self.presentViewController(alertController, animated=True, completion=None)


if __name__ == '__main__':
  from rbedge.functions import NSStringFromClass
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController

  main_vc = AlertControllerViewController.new()
  _title = NSStringFromClass(AlertControllerViewController)
  main_vc.navigationItem.title = _title
  style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, style)

