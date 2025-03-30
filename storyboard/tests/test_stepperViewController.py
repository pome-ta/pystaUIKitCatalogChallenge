import sys
import pathlib

parent_level = 3
sys.path.append(str(pathlib.Path(__file__, '../' * parent_level).resolve()))

import ctypes
try:
  from pyrubicon.objc.api import ObjCClass, ObjCInstance
  from pyrubicon.objc.api import objc_method, objc_id
  from pyrubicon.objc.runtime import send_super
  from pyrubicon.objc.types import NSInteger

  from rbedge.functions import NSStringFromClass
  from rbedge import pdbr

except Exception as e:
  # xxx: `(ModuleNotFoundError, LookupError)`
  print(f'{e}: error')

# --- test module
from storyboard.stepperViewController import prototypes

test_prototypes = prototypes if isinstance(prototypes, list) else [prototypes]

UIColor = ObjCClass('UIColor')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UITableViewController = ObjCClass('UITableViewController')
UITableViewCell = ObjCClass('UITableViewCell')


class StepperViewControllerTest(UITableViewController):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def loadView(self):
    send_super(__class__, self, 'loadView')
    #print(f'\t{NSStringFromClass(__class__)}: loadView')
    [
      self.tableView.registerClass_forCellReuseIdentifier_(
        prototype['cellClass'], prototype['identifier'])
      for prototype in test_prototypes
    ]

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
    #print(f'\t{NSStringFromClass(__class__)}: initWithStyle_')
    return self

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    # --- Navigation
    self.navigationItem.title = NSStringFromClass(__class__) if (
      title := self.navigationItem.title) is None else title
    # --- View
    self.view.backgroundColor = UIColor.systemDarkGreenColor()

  @objc_method
  def viewWillAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print(f'\t{NSStringFromClass(__class__)}: viewWillAppear_')

  @objc_method
  def viewDidAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print(f'\t{NSStringFromClass(__class__)}: viewDidAppear_')

  @objc_method
  def viewWillDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    # print(f'\t{NSStringFromClass(__class__)}: viewWillDisappear_')

  @objc_method
  def viewDidDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    print(f'\t{NSStringFromClass(__class__)}: viewDidDisappear_')

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'\t{NSStringFromClass(__class__)}: didReceiveMemoryWarning')

  # --- UITableViewDataSource
  @objc_method
  def tableView_numberOfRowsInSection_(self, tableView,
                                       section: NSInteger) -> NSInteger:

    return len(test_prototypes)

  @objc_method
  def tableView_cellForRowAtIndexPath_(self, tableView,
                                       indexPath) -> ObjCInstance:

    identifier = test_prototypes[indexPath.row]['identifier']

    cell = tableView.dequeueReusableCellWithIdentifier_forIndexPath_(
      identifier, indexPath)

    return cell


if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import (
    UITableViewStyle,
    UIModalPresentationStyle,
  )

  table_style = UITableViewStyle.grouped
  main_vc = StepperViewControllerTest.alloc().initWithStyle_(table_style)
  _title = NSStringFromClass(StepperViewControllerTest)
  main_vc.navigationItem.title = _title

  # presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

