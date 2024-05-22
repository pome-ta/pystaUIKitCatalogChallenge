import ctypes
from enum import Enum

from pyrubicon.objc.api import ObjCClass, objc_method, objc_property
from pyrubicon.objc.runtime import SEL, send_super
from pyrubicon.objc.types import NSInteger

from rbedge.enumerations import UIControlState, UIControlEvents, UIListContentTextAlignment
from rbedge.functions import NSStringFromClass

from caseElement import CaseElement
from pyLocalizedString import localizedString

from storyboard.buttonViewController import prototypes

UITableViewController = ObjCClass('UITableViewController')
UITableViewHeaderFooterView = ObjCClass('UITableViewHeaderFooterView')
UIListContentConfiguration = ObjCClass('UIListContentConfiguration')


class BaseTableViewController(UITableViewController):

  testCells: list[CaseElement] = []

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    self.tableView.registerClass_forHeaderFooterViewReuseIdentifier_(
      UITableViewHeaderFooterView, 'customHeaderFooterView')

  '''
  @objc_method
  def centeredHeaderView_(self, title):
    # todo: let headerView: UITableViewHeaderFooterView = UITableViewHeaderFooterView()
    headerView = self.tableView.dequeueReusableHeaderFooterViewWithIdentifier_(
      'customHeaderFooterView')

    content = UIListContentConfiguration.groupedHeaderConfiguration()
    content.text = title
    content.textProperties.alignment = UIListContentTextAlignment.center
    headerView.contentConfiguration = content

    return headerView

  # MARK: - UITableViewDataSource

  @objc_method
  def tableView_viewForHeaderInSection_(self, tableView,
                                        section: NSInteger) -> ctypes.c_void_p:
    return self.centeredHeaderView_(self.testCells[section].title).ptr

  @objc_method
  def tableView_titleForHeaderInSection_(self, tableView, section: NSInteger):
    return self.testCells[section].title
  '''
  @objc_method
  def tableView_numberOfRowsInSection_(self, tableView,
                                       section: NSInteger) -> NSInteger:
    return 1

  @objc_method
  def numberOfSectionsInTableView_(self, tableView) -> NSInteger:
    return len(self.testCells)

  @objc_method
  def tableView_cellForRowAtIndexPath_(self, tableView,
                                       indexPath) -> ctypes.c_void_p:
    cellTest = self.testCells[indexPath.section]
    cell = tableView.dequeueReusableCellWithIdentifier_forIndexPath_(
      cellTest.cellID, indexPath)

    if (view := cellTest.targetView(cell)):
      cellTest.configHandler(view)
    
    pdbr.state(cell.contentView)
    return cell.ptr


class ButtonKind(Enum):
  buttonSystem = 'buttonSystem'
  buttonDetailDisclosure = 'buttonDetailDisclosure'
  buttonSystemAddContact = 'buttonSystemAddContact'
  buttonClose = 'buttonClose'
  buttonStyleGray = 'buttonStyleGray'
  buttonStyleTinted = 'buttonStyleTinted'
  buttonStyleFilled = 'buttonStyleFilled'
  buttonCornerStyle = 'buttonCornerStyle'
  buttonToggle = 'buttonToggle'
  buttonTitleColor = 'buttonTitleColor'
  buttonImage = 'buttonImage'
  buttonAttrText = 'buttonAttrText'
  buttonSymbol = 'buttonSymbol'
  buttonLargeSymbol = 'buttonLargeSymbol'
  buttonTextSymbol = 'buttonTextSymbol'
  buttonSymbolText = 'buttonSymbolText'
  buttonMultiTitle = 'buttonMultiTitle'
  buttonBackground = 'buttonBackground'
  addToCartButton = 'addToCartButton'
  buttonUpdateActivityHandler = 'buttonUpdateActivityHandler'
  buttonUpdateHandler = 'buttonUpdateHandler'
  buttonImageUpdateHandler = 'buttonImageUpdateHandler'


class ButtonViewController(BaseTableViewController):
  cartItemCount = objc_property(int)

  @objc_method
  def init(self):
    send_super(__class__, self, 'init')
    self.testCells = []
    self.cartItemCount = 0
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
    send_super(__class__, self, 'viewDidLoad')

    title = NSStringFromClass(__class__)
    self.navigationItem.title = title

    self.initPrototype()

    self.testCells.extend([
      # 0
      CaseElement(localizedString('DefaultTitle'),
                  ButtonKind.buttonSystem.value,
                  self.configureSystemTextButton_),

      # 1

      #CaseElement(localizedString('DetailDisclosureTitle'),ButtonKind.buttonDetailDisclosure.value,self.configureSystemDetailDisclosureButton_),
      # 2
      #CaseElement(localizedString('AddContactTitle'),ButtonKind.buttonSystemAddContact.value,self.configureSystemContactAddButton_),
      # 3
      #CaseElement(localizedString('CloseTitle'), ButtonKind.buttonClose.value,self.configureCloseButton_),
    ])

  # --- extension
  # 0
  @objc_method
  def configureSystemTextButton_(self, button):
    # todo: 冗長、差し替えを容易にしたい為
    title = localizedString('Button')
    state = UIControlState.normal
    button.setTitle_forState_(title, state)

    target = self
    action = SEL('buttonClicked:')
    controlEvents = UIControlEvents.touchUpInside
    button.addTarget_action_forControlEvents_(target, action, controlEvents)

  # 1
  @objc_method
  def configureSystemDetailDisclosureButton_(self, button):
    target = self
    action = SEL('buttonClicked:')
    controlEvents = UIControlEvents.touchUpInside
    button.addTarget_action_forControlEvents_(target, action, controlEvents)

  # 2
  @objc_method
  def configureSystemContactAddButton_(self, button):
    target = self
    action = SEL('buttonClicked:')
    controlEvents = UIControlEvents.touchUpInside
    button.addTarget_action_forControlEvents_(target, action, controlEvents)

  # 3
  @objc_method
  def configureCloseButton_(self, button):
    target = self
    action = SEL('buttonClicked:')
    controlEvents = UIControlEvents.touchUpInside
    button.addTarget_action_forControlEvents_(target, action, controlEvents)

  # MARK: - Button Actions
  @objc_method
  def buttonClicked_(self, sender):
    print(f'Button was clicked.{sender}')


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr
  bvc = ButtonViewController.new()

  #style = UIModalPresentationStyle.pageSheet
  style = UIModalPresentationStyle.fullScreen
  present_viewController(bvc, style)

