import sys
import pathlib

parent_level = 3
sys.path.append(str(pathlib.Path(__file__, '../' * parent_level).resolve()))

try:
  import ctypes
  from pyrubicon.objc.api import ObjCClass, ObjCProtocol, objc_method, objc_property
  #from pyrubicon.objc.runtime import send_super
  from pyrubicon.objc.types import NSInteger, CGRectMake

  from rbedge.functions import NSStringFromClass
  #from rbedge.enumerations import UITableViewStyle
  from rbedge import present_viewController
  from rbedge import pdbr
except Exception as e:
  # xxx: `(ModuleNotFoundError, LookupError)`
  print(f'{e}: error')

# --- test modules
from storyboard.buttonViewController import prototypes

#ObjCClass.auto_rename = True
#ObjCProtocol.auto_rename = True # xxx: `__init__.py` にやるかも

UIColor = ObjCClass('UIColor')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UITableViewController = ObjCClass('UITableViewController')
UITableViewCell = ObjCClass('UITableViewCell')


class TableViewControllerTest(UITableViewController):

  '''
  @objc_method
  def init(self):
    self.cell_identifier = 'customCell'
    return self
  '''

  @objc_method
  def viewDidLoad(self):
    # --- Navigation
    title = NSStringFromClass(__class__)
    self.navigationItem.title = title

    # --- View
    self.view.backgroundColor = UIColor.systemGreenColor()
    self.tableSetup()

  @objc_method
  def tableSetup(self):

    for prototype in prototypes:
      cellClass = prototype['cellClass']
      identifier = prototype['identifier']
      self.tableView.registerClass_forCellReuseIdentifier_(
        cellClass, identifier)

    #self.tableView.registerClass_forCellReuseIdentifier_(prototypes[0]['cellClass'], self.cell_identifier)

  # --- UITableViewDataSource
  @objc_method
  def tableView_numberOfRowsInSection_(self, tableView,
                                       section: NSInteger) -> NSInteger:

    return len(prototypes)
    #return 1

  @objc_method
  def tableView_cellForRowAtIndexPath_(self, tableView,
                                       indexPath) -> ctypes.c_void_p:

    identifier = prototypes[indexPath.row]['identifier']
    #print(indexPath.row)

    cell = tableView.dequeueReusableCellWithIdentifier_forIndexPath_(
      identifier, indexPath)

    #cell = tableView.dequeueReusableCellWithIdentifier_forIndexPath_(self.cell_identifier, indexPath)

    content = cell.defaultContentConfiguration()
    #print('h')
    #content.text = 'symbol_name'
    #content.textProperties.numberOfLines = 1

    #cell.contentConfiguration = content
    return cell.ptr


if __name__ == '__main__':
  vc = TableViewControllerTest.new()
  present_viewController(vc)

