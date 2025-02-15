import ctypes

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.api import NSString, NSMutableArray
from pyrubicon.objc.runtime import send_super, objc_id, send_message, SEL
from pyrubicon.objc.types import NSInteger

from rbedge.enumerations import UIListContentTextAlignment

from caseElement import CaseElement  # todo: 型呼び出し
from rbedge.functions import NSStringFromClass
from rbedge import pdbr

UITableViewController = ObjCClass('UITableViewController')
UITableViewHeaderFooterView = ObjCClass('UITableViewHeaderFooterView')
UIListContentConfiguration = ObjCClass('UIListContentConfiguration')


class BaseTableViewController(UITableViewController):

  #testCells: NSMutableArray = objc_property(weak=True)
  testCells: NSMutableArray = objc_property()
  headerFooterViewIdentifier: NSString = objc_property()

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
    self.testCells = NSMutableArray.new()
    #self.testCells = NSMutableArray.array()
    
    self.headerFooterViewIdentifier = NSString.stringWithString_('customHeaderFooterView')
    #self.tableView.delegate = self
    #self.tableView.dataSource = self
    return self

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    print(f'\t\t{NSStringFromClass(__class__)}: viewDidLoad')
    self.tableView.registerClass_forHeaderFooterViewReuseIdentifier_(
      UITableViewHeaderFooterView, self.headerFooterViewIdentifier)

  @objc_method
  def viewWillAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    print(f'\t{NSStringFromClass(__class__)}: viewWillAppear_')

  @objc_method
  def viewDidAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    print(f'\t{NSStringFromClass(__class__)}: viewDidAppear_')
    

  @objc_method
  def viewWillDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print(f'\t{NSStringFromClass(__class__)}: viewWillDisappear_')

  @objc_method
  def viewDidDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print(f'\t{NSStringFromClass(__class__)}: viewDidDisappear_')
    #self.testCells = None

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'\t{NSStringFromClass(__class__)}: didReceiveMemoryWarning')

  '''
  @objc_method
  def testCellsExtend_(self, addCells) -> None:
    """`@available(iOS 15.0, *)` で弾く用
    """
    for addCell in addCells:
      if not isinstance(addCell, CaseElement):
        continue
      if (cell := addCell).configHandlerName is None:
        continue
      self.testCells.addObject_(cell)
      #self.testCells.append(cell)
  '''
  '''
  @objc_method
  def centeredHeaderView_(self, title)->objc_id:
    headerView = self.tableView.dequeueReusableHeaderFooterViewWithIdentifier_(
      self.headerFooterViewIdentifier)

    content = UIListContentConfiguration.groupedHeaderConfiguration()
    content.text = title
    content.textProperties.alignment = UIListContentTextAlignment.center
    headerView.contentConfiguration = content

    return headerView
  '''

  # MARK: - UITableViewDataSource
  @objc_method
  def tableView_viewForHeaderInSection_(self, tableView,
                                        section: NSInteger) -> objc_id:

    #return self.centeredHeaderView_(self.testCells[section].title)
    headerView = self.tableView.dequeueReusableHeaderFooterViewWithIdentifier_(
      self.headerFooterViewIdentifier)

    content = UIListContentConfiguration.groupedHeaderConfiguration()
    content.text = self.testCells[section].title
    content.textProperties.alignment = UIListContentTextAlignment.center
    headerView.contentConfiguration = content

    return headerView

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
    
    print('▪︎ base')
    cellTest = self.testCells[indexPath.section]
    cell = tableView.dequeueReusableCellWithIdentifier_forIndexPath_(
      cellTest.cellID, indexPath)

    if (view := cellTest.targetView(cell)):
      #cellTest.configHandler(view)
      getattr(self, str(cellTest.configHandlerName))(view)
      #send_message(self, SEL(str(cellTest.configHandlerName)), view, restype=None, argtypes=[objc_id])

    return cell

