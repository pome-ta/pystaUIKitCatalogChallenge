'''
  note: Storyboard 未定義
    - index 呼び出しよりenum か？
'''
from pyrubicon.objc.api import ObjCClass, ObjCInstance, Block
from pyrubicon.objc.api import objc_method, objc_property, objc_const
from pyrubicon.objc.runtime import send_super, objc_id, load_library

from rbedge.enumerations import (
  UITableViewStyle,
  UIAlertControllerStyle,
  UIAlertActionStyle,
)

from rbedge import pdbr

from pyLocalizedString import localizedString

UIKit = load_library('UIKit')  # todo: `objc_const` 用

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UITableView = ObjCClass('UITableView')
UITableViewCell = ObjCClass('UITableViewCell')

UIAlertController = ObjCClass('UIAlertController')
UIAlertAction = ObjCClass('UIAlertAction')
NSNotificationCenter = ObjCClass('NSNotificationCenter')
NSOperationQueue = ObjCClass('NSOperationQueue')

UITextField = ObjCClass('UITextField')

UITextFieldTextDidChangeNotification = objc_const(
  UIKit, 'UITextFieldTextDidChangeNotification')

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
  textDidChangeObserver = objc_property()
  #secureTextAlertAction: UIAlertAction = objc_property(weak=True)
  secureTextAlertAction: UIAlertAction = objc_property()

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
        #print(f'{section}: {row}')
        self.showTextEntryAlert()
      elif row == 4:
        #print(f'{section}: {row}')
        self.showSecureTextEntryAlert()

    elif section == 1:
      # actionStyleSection
      if (row := indexPath.row) == 0:
        #print(f'{section}: {row}')
        self.showOkayCancelActionSheet_(indexPath)
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

    # Create the action.
    cancelAction = UIAlertAction.actionWithTitle_style_handler_(
      cancelButtonTitle, UIAlertActionStyle.cancel,
      Block(lambda: print("The simple alert's cancel action occurred."), None))

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

    # Create the action.
    cancelAction = UIAlertAction.actionWithTitle_style_handler_(
      cancelButtonTitle, UIAlertActionStyle.cancel,
      Block(lambda: print("The 'OK/Cancel' alert's cancel action occurred."),
            None))
    otherAction = UIAlertAction.actionWithTitle_style_handler_(
      otherButtonTitle, UIAlertActionStyle.default,
      Block(lambda: print("The 'OK/Cancel' alert's other action occurred."),
            None))

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

    # Create the action.
    cancelAction = UIAlertAction.actionWithTitle_style_handler_(
      cancelButtonTitle, UIAlertActionStyle.cancel,
      Block(lambda: print("The 'Other' alert's cancel action occurred."),
            None))
    otherButtonOneAction = UIAlertAction.actionWithTitle_style_handler_(
      otherButtonTitleOne, UIAlertActionStyle.default,
      Block(
        lambda: print("The 'Other' alert's other button one action occurred."),
        None))
    otherButtonTwoAction = UIAlertAction.actionWithTitle_style_handler_(
      otherButtonTitleTwo, UIAlertActionStyle.default,
      Block(
        lambda: print("The 'Other' alert's other button two action occurred."),
        None))

    # Add the action.
    alertController.addAction_(cancelAction)
    alertController.addAction_(otherButtonOneAction)
    alertController.addAction_(otherButtonTwoAction)

    self.presentViewController(alertController, animated=True, completion=None)

  # Show a text entry alert with two custom buttons.
  @objc_method
  def showTextEntryAlert(self):
    title = localizedString('A Short Title is Best')
    message = localizedString(
      'A message needs to be a short, complete sentence.')

    alertController = UIAlertController.alertControllerWithTitle_message_preferredStyle_(
      title, message, UIAlertControllerStyle.alert)

    # Add the text field for text entry.
    @Block
    def configurationHandler(textField: objc_id) -> None:
      # If you need to customize the text field, you can do so here.
      pass

    alertController.addTextFieldWithConfigurationHandler_(configurationHandler)

    # Create the actions.
    cancelButtonTitle = localizedString('Cancel')
    cancelAction = UIAlertAction.actionWithTitle_style_handler_(
      cancelButtonTitle, UIAlertActionStyle.cancel,
      Block(lambda: print("The 'Text Entry' alert's cancel action occurred."),
            None))

    otherButtonTitle = localizedString('OK')
    otherAction = UIAlertAction.actionWithTitle_style_handler_(
      otherButtonTitle, UIAlertActionStyle.default,
      Block(lambda: print("The 'Text Entry' alert's other action occurred."),
            None))

    # Add the action.
    alertController.addAction_(cancelAction)
    alertController.addAction_(otherAction)

    self.presentViewController(alertController, animated=True, completion=None)

  # Show a secure text entry alert with two custom buttons.
  @objc_method
  def showSecureTextEntryAlert(self):
    title = localizedString('A Short Title is Best')
    message = localizedString(
      'A message needs to be a short, complete sentence.')
    cancelButtonTitle = localizedString('Cancel')
    otherButtonTitle = localizedString('OK')

    alertController = UIAlertController.alertControllerWithTitle_message_preferredStyle_(
      title, message, UIAlertControllerStyle.alert)

    @Block
    def configurationHandler(_textField: objc_id) -> None:
      textField = ObjCInstance(_textField)
      if (observer := self.textDidChangeObserver) is not None:
        NSNotificationCenter.defaultCenter.removeObserver_(observer)

      @Block
      def usingBlock(_notification: objc_id) -> None:
        notification = ObjCInstance(_notification)
        if (textField := notification.object).isKindOfClass_(UITextField):

          # Enforce a minimum length of >= 5 characters for secure text alerts.
          # セキュア テキスト アラートの最小長は 5 文字以上にする必要があります。
          if (alertAction := self.secureTextAlertAction):
            if (text := textField.text):
              alertAction.setEnabled_(text.length >= 5)
            else:
              alertAction.setEnabled_(False)

      # Listen for changes to the text field's text so that we can toggle the current action's enabled property based on whether the user has entered a sufficiently secure entry.
      # ユーザーが十分に安全なエントリを入力したかどうかに基づいて、現在のアクションの有効なプロパティを切り替えることができるように、テキスト フィールドのテキストへの変更をリッスンします。

      self.textDidChangeObserver = NSNotificationCenter.defaultCenter.addObserverForName(
        UITextFieldTextDidChangeNotification,
        object=textField,
        queue=NSOperationQueue.mainQueue,
        usingBlock=usingBlock)
      textField.setSecureTextEntry_(True)

    # Add the text field for the secure text entry.
    alertController.addTextFieldWithConfigurationHandler_(configurationHandler)
    # Create the actions.
    cancelAction = UIAlertAction.actionWithTitle_style_handler_(
      cancelButtonTitle, UIAlertActionStyle.cancel,
      Block(
        lambda: print("The 'Secure Text Entry' alert's cancel action occurred."
                      ), None))
    otherAction = UIAlertAction.actionWithTitle_style_handler_(
      otherButtonTitle, UIAlertActionStyle.default,
      Block(
        lambda: print("The 'Secure Text Entry' alert's other action occurred."
                      ), None))
    # The text field initially has no text in the text field, so we'll disable it for now. It will be re-enabled when the first character is typed.
    # テキストフィールドには最初はテキストがないため、ここでは無効にします。最初の文字が入力されると再び有効になります。
    otherAction.setEnabled_(False)

    # Hold onto the secure text alert action to toggle the enabled / disabled state when the text changed.
    # セキュア テキスト アラート アクションを押し続けると、テキストが変更されたときに有効/無効状態が切り替わります。
    self.secureTextAlertAction = otherAction

    # Add the actions.
    alertController.addAction_(cancelAction)
    alertController.addAction_(otherAction)

    self.presentViewController(alertController, animated=True, completion=None)

  # MARK: - UIAlertControllerStyleActionSheet Style Alerts
  # Show a dialog with an "OK" and "Cancel" button.
  @objc_method
  def showOkayCancelActionSheet_(self, IndexPath):
    message = localizedString(
      'A message needs to be a short, complete sentence.')
    cancelButtonTitle = localizedString('Cancel')
    destructiveButtonTitle = localizedString('Confirm')

    alertController = UIAlertController.alertControllerWithTitle_message_preferredStyle_(
      None, message, UIAlertControllerStyle.actionSheet)

    # Create the actions.
    cancelAction = UIAlertAction.actionWithTitle_style_handler_(
      cancelButtonTitle, UIAlertActionStyle.cancel,
      Block(
        lambda: print(
          "The 'OK/Cancel' alert action sheet's cancel action occurred."),
        None))
    destructiveAction = UIAlertAction.actionWithTitle_style_handler_(
      destructiveButtonTitle, UIAlertActionStyle.default,
      Block(
        lambda: print(
          "The 'Confirm' alert action sheet's destructive action occurred."),
        None))

    # Add the actions.
    alertController.addAction_(cancelAction)
    alertController.addAction_(destructiveAction)

    # Configure the alert controller's popover presentation controller if it has one.
    # アラート コントローラーのポップオーバー プレゼンテーション コントローラーがある場合は、それを構成します。
    if (popoverPresentationController :=
        alertController.popoverPresentationController()) is not None:
      print('# popovers あり')
      print('\t- wip')
      print(popoverPresentationController)
      # Note for popovers the Cancel button is hidden automatically.
      # ポップオーバーの場合、「キャンセル」ボタンは自動的に非表示になることに注意してください。
      # wip: popovers の出る条件が不明なため、ペンディング
    self.presentViewController(alertController, animated=True, completion=None)


if __name__ == '__main__':
  from rbedge.functions import NSStringFromClass
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController

  main_vc = AlertControllerViewController.new()
  _title = NSStringFromClass(AlertControllerViewController)
  main_vc.navigationItem.title = _title

  style = UIModalPresentationStyle.fullScreen
  #style = UIModalPresentationStyle.pageSheet
  #style = UIModalPresentationStyle.popover

  present_viewController(main_vc, style)

