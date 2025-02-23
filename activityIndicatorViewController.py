import ctypes
from enum import Enum

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method, at
from pyrubicon.objc.runtime import send_super, objc_id, objc_block, SEL, Class, objc_super
from pyrubicon.objc.types import NSInteger

from rbedge.enumerations import UIActivityIndicatorViewStyle

from caseElement import CaseElement
from pyLocalizedString import localizedString

from baseTableViewController import BaseTableViewController
from storyboard.activityIndicatorViewController import prototypes

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

UIColor = ObjCClass('UIColor')


class ActivityIndicatorKind(Enum):
  mediumIndicator = 'mediumIndicator'
  largeIndicator = 'largeIndicator'
  mediumTintedIndicator = 'mediumTintedIndicator'
  largeTintedIndicator = 'largeTintedIndicator'


class ActivityIndicatorViewController(BaseTableViewController):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t- {NSStringFromClass(__class__)}: dealloc')

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
  def loadView(self):
    send_super(__class__, self, 'loadView')
    #print(f'\t{NSStringFromClass(__class__)}: loadView')
    [
      self.tableView.registerClass_forCellReuseIdentifier_(
        prototype['cellClass'], prototype['identifier'])
      for prototype in prototypes
    ]

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    #print(f'\t{NSStringFromClass(__class__)}: viewDidLoad')

    self.navigationItem.title = localizedString('ActivityIndicatorsTitle') if (
      title := self.navigationItem.title) is None else title

    #c1 = CaseElement.alloc().initWithTitle_cellID_configHandlerName_(localizedString('MediumIndicatorTitle'),ActivityIndicatorKind.mediumIndicator.value,'configureMediumActivityIndicatorView:')

    #c2 = CaseElement.alloc().initWithTitle_cellID_configHandlerName_(localizedString('LargeIndicatorTitle'), ActivityIndicatorKind.largeIndicator.value, 'configureLargeActivityIndicatorView:')
    #c1 = CaseElement(localizedString('MediumIndicatorTitle'), ActivityIndicatorKind.mediumIndicator.value, 'configureMediumActivityIndicatorView:')

    self.testCellsAppendContentsOf_([
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('MediumIndicatorTitle'),
        ActivityIndicatorKind.mediumIndicator.value,
        'configureMediumActivityIndicatorView:'),
    ])

    #self.testCells.addObject_(c1)
    '''
    self.testCellsExtend_([
      CaseElement.alloc().initWithTitle_cellID_targetSelf_configHandlerName_(localizedString('MediumIndicatorTitle'),ActivityIndicatorKind.mediumIndicator.value, self, 'configureMediumActivityIndicatorView:')
    ])
    '''
    '''

    self.testCellsExtend_([
      CaseElement(localizedString('MediumIndicatorTitle'),
                  ActivityIndicatorKind.mediumIndicator.value,
                  self.configureMediumActivityIndicatorView_),
      CaseElement(localizedString('LargeIndicatorTitle'),
                  ActivityIndicatorKind.largeIndicator.value,
                  self.configureLargeActivityIndicatorView_),
    ])
    '''
    '''
    # if traitCollection.userInterfaceIdiom != .mac
    # Tinted activity indicators available only on iOS.
    self.testCells_extend([
      CaseElement(localizedString('MediumTintedIndicatorTitle'),
                  ActivityIndicatorKind.mediumTintedIndicator.value,
                  self.configureMediumTintedActivityIndicatorView_),
      CaseElement(localizedString('LargeTintedIndicatorTitle'),
                  ActivityIndicatorKind.largeTintedIndicator.value,
                  self.configureLargeTintedActivityIndicatorView_),
    ])
    '''

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
    #self.tableView.reloadData()

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
    # print('\t↑ ---')
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
    # xxx: a-shell で動くけど、Pythonista3 の2回目の`dealloc` が呼ばれない
    #self.testCells = None
    #prototypes = None
    #pdbr.state(self.tableView)

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'\t{NSStringFromClass(__class__)}: didReceiveMemoryWarning')

  # MARK: - Configuration
  @objc_method
  def configureMediumActivityIndicatorView_(self, activityIndicator):
    #pdbr.state(activityIndicator)

    #activityIndicator.style = UIActivityIndicatorViewStyle.medium
    activityIndicator.setStyle_(UIActivityIndicatorViewStyle.large)
    #initWithActivityIndicatorStyle_

    activityIndicator.hidesWhenStopped = True

    activityIndicator.color = UIColor.systemRedColor()
    #pdbr.state(activityIndicator)

    activityIndicator.startAnimating()

    # When the activity is done, be sure to use UIActivityIndicatorView.stopAnimating().

  @objc_method
  def configureLargeActivityIndicatorView_(self, activityIndicator):
    activityIndicator.style = UIActivityIndicatorViewStyle.large
    activityIndicator.hidesWhenStopped = True

    #activityIndicator.startAnimating()
    # When the activity is done, be sure to use UIActivityIndicatorView.stopAnimating().

  @objc_method
  def configureMediumTintedActivityIndicatorView_(self, activityIndicator):
    activityIndicator.style = UIActivityIndicatorViewStyle.medium
    activityIndicator.hidesWhenStopped = True
    activityIndicator.color = UIColor.systemPurpleColor()

    #activityIndicator.startAnimating()
    # When the activity is done, be sure to use UIActivityIndicatorView.stopAnimating().

  @objc_method
  def configureLargeTintedActivityIndicatorView_(self, activityIndicator):
    activityIndicator.style = UIActivityIndicatorViewStyle.large
    activityIndicator.hidesWhenStopped = True
    activityIndicator.color = UIColor.systemPurpleColor()

    #activityIndicator.startAnimating()
    # When the activity is done, be sure to use UIActivityIndicatorView.stopAnimating().

  '''
  @objc_method
  def tableView_cellForRowAtIndexPath_(self, tableView,
                                       indexPath) -> ObjCInstance:

    cellTest = self.testCells[indexPath.section]
    cell = tableView.dequeueReusableCellWithIdentifier_forIndexPath_(
      cellTest.cellID, indexPath)

    if (view := cellTest.targetView(cell)):
      #getattr(self, SEL('configureMediumActivityIndicatorView_'))(view)

      self.performSelector_withObject_(SEL(str(cellTest.configHandlerName)), view)
      #self.configureMediumActivityIndicatorView_(view)
      #pdbr.state(self, 1)
      #pass

    return cell
  '''


if __name__ == '__main__':
  from rbedge.app import App

  from rbedge.enumerations import (
    UITableViewStyle,
    UIModalPresentationStyle,
  )

  print('__name__')

  table_style = UITableViewStyle.grouped
  main_vc = ActivityIndicatorViewController.alloc().initWithStyle_(table_style)
  _title = NSStringFromClass(ActivityIndicatorViewController)
  main_vc.navigationItem.title = _title

  # presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc)
  print('---')
  #print(app)
  # pdbr.state(main_vc, 1)
  app.main_loop(presentation_style)
  print('--- end ---\n')

