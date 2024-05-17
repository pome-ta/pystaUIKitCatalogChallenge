import sys
import pathlib

parent_level = 3
sys.path.append(str(pathlib.Path(__file__, '../' * parent_level).resolve()))

try:
  import ctypes

  from pyrubicon.objc.api import ObjCClass, ObjCProtocol, objc_method, objc_property
  from pyrubicon.objc.types import NSInteger, CGRectMake

  from rbedge.functions import NSStringFromClass
  from rbedge import present_viewController

except Exception as e:
  # xxx: `(ModuleNotFoundError, LookupError)`
  print(f'{e}: error')

# --- test modules
from storyboard.buttonViewController import prototypes

_test_p = prototypes
test_prototypes = _test_p if isinstance(_test_p, list) else [_test_p]

#ObjCClass.auto_rename = True
#ObjCProtocol.auto_rename = True # xxx: `__init__.py` にやるかも

UIColor = ObjCClass('UIColor')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UITableViewController = ObjCClass('UITableViewController')
UITableViewCell = ObjCClass('UITableViewCell')


class TableViewControllerTest(UITableViewController):

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

    for prototype in test_prototypes:
      cellClass = prototype['cellClass']
      identifier = prototype['identifier']
      self.tableView.registerClass_forCellReuseIdentifier_(
        cellClass, identifier)

  # --- UITableViewDataSource
  @objc_method
  def tableView_numberOfRowsInSection_(self, tableView,
                                       section: NSInteger) -> NSInteger:

    return len(test_prototypes)

  @objc_method
  def tableView_cellForRowAtIndexPath_(self, tableView,
                                       indexPath) -> ctypes.c_void_p:

    identifier = test_prototypes[indexPath.row]['identifier']

    cell = tableView.dequeueReusableCellWithIdentifier_forIndexPath_(
      identifier, indexPath)

    return cell.ptr


if __name__ == '__main__':
  from rbedge import pdbr
  vc = TableViewControllerTest.new()
  present_viewController(vc)

