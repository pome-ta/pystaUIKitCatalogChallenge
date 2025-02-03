import ctypes

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, objc_id
from pyrubicon.objc.types import NSInteger

from rbedge.enumerations import UIListContentTextAlignment

from caseElement import CaseElement  # todo: 型呼び出し
from rbedge.functions import NSStringFromClass

UITableViewController = ObjCClass('UITableViewController')
UITableViewHeaderFooterView = ObjCClass('UITableViewHeaderFooterView')
UIListContentConfiguration = ObjCClass('UIListContentConfiguration')


class BaseTableViewController(UITableViewController):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`

    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def loadView(self):
    send_super(__class__, self, 'loadView')
    print(f'\t\t{NSStringFromClass(__class__)}: loadView')

  @objc_method
  def initWithStyle_(self, style: NSInteger) -> ObjCInstance:
    send_super(__class__,
               self,
               'initWithStyle:',
               style,
               restype=objc_id,
               argtypes=[
                 NSInteger,
               ])

    print(f'\t\t{NSStringFromClass(__class__)}: initWithStyle_')
    self.testCells: list[CaseElement] = []
    self.headerFooterView_identifier = 'customHeaderFooterView'
    return self

  @objc_method
  def setupPrototypes_(self, prototypes) -> None:
    [
      self.tableView.registerClass_forCellReuseIdentifier_(
        prototype['cellClass'], prototype['identifier'])
      for prototype in prototypes
    ]

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    print(f'\t\t{NSStringFromClass(__class__)}: viewDidLoad')
    self.tableView.registerClass_forHeaderFooterViewReuseIdentifier_(
      UITableViewHeaderFooterView, self.headerFooterView_identifier)

  @objc_method
  def viewDidDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    # todo: `dealloc` 呼び出す為、インスタンス変数を初期化
    #self.testCells = None
    #self.headerFooterView_identifier = None

  @objc_method
  def testCells_extend(self, testCells: ctypes.py_object):
    """`@available(iOS 15.0, *)` で弾く用
    """
    for testCell in testCells:
      if not isinstance(testCell, CaseElement):
        continue
      if (cell := testCell).configHandler is None:
        continue
      self.testCells.append(cell)

  @objc_method
  def centeredHeaderView_(self, title):
    headerView = self.tableView.dequeueReusableHeaderFooterViewWithIdentifier_(
      self.headerFooterView_identifier)

    content = UIListContentConfiguration.groupedHeaderConfiguration()
    content.text = title
    content.textProperties.alignment = UIListContentTextAlignment.center
    headerView.contentConfiguration = content

    return headerView

  # MARK: - UITableViewDataSource
  @objc_method
  def tableView_viewForHeaderInSection_(self, tableView,
                                        section: NSInteger) -> objc_id:
    return self.centeredHeaderView_(self.testCells[section].title)

  @objc_method
  def tableView_titleForHeaderInSection_(self, tableView, section: NSInteger):
    return self.testCells[section].title

  @objc_method
  def tableView_numberOfRowsInSection_(self, tableView,
                                       section: NSInteger) -> NSInteger:
    return 1

  @objc_method
  def numberOfSectionsInTableView_(self, tableView) -> NSInteger:
    return len(self.testCells)

  @objc_method
  def tableView_cellForRowAtIndexPath_(self, tableView, indexPath) -> objc_id:
    cellTest = self.testCells[indexPath.section]
    cell = tableView.dequeueReusableCellWithIdentifier_forIndexPath_(
      cellTest.cellID, indexPath)

    if (view := cellTest.targetView(cell)):
      cellTest.configHandler(view)

    return cell

