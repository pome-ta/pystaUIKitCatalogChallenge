import ctypes
from enum import Enum

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, objc_id, objc_block,SEL
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
  def loadView(self):
    send_super(__class__, self, 'loadView')
    print(f'\t{NSStringFromClass(__class__)}: loadView')

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
    print(f'\t{NSStringFromClass(__class__)}: initWithStyle_')
    self.setupPrototypes_(prototypes)
    return self

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    print(f'\t{NSStringFromClass(__class__)}: viewDidLoad')

    self.navigationItem.title = localizedString('ActivityIndicatorsTitle') if (
      title := self.navigationItem.title) is None else title

    #pdbr.state(self.configureMediumActivityIndicatorView_)
    #print(dir(self.configureMediumActivityIndicatorView_))
    #print(self.configureMediumActivityIndicatorView_)

    #c = CaseElement.alloc().initWithTitle_cellID_configHandler_(localizedString('MediumIndicatorTitle'),ActivityIndicatorKind.mediumIndicator.value, self.configureMediumActivityIndicatorView_)
    
    #c = CaseElement.alloc().initWithTitle_cellID_configHandler_(localizedString('MediumIndicatorTitle'),ActivityIndicatorKind.mediumIndicator.value, ctypes.c_void_p(self.configureMediumActivityIndicatorView_))
    
    
    #c = CaseElement.alloc().initWithTitle_cellID_configHandler_(localizedString('MediumIndicatorTitle'),ActivityIndicatorKind.mediumIndicator.value)
    
    c = CaseElement.alloc().initWithTitle_cellID_(localizedString('MediumIndicatorTitle'),ActivityIndicatorKind.mediumIndicator.value)
    c.setConfigHandler_(self.configureMediumActivityIndicatorView_)
    pdbr.state(c)
    
    '''
    self.testCellsExtend_([
      CaseElement.alloc().initWithTitle_cellID_configHandler_(
        localizedString('MediumIndicatorTitle'),
        ActivityIndicatorKind.mediumIndicator.value,
        self.configureMediumActivityIndicatorView_)
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

  # MARK: - Configuration
  @objc_method
  def configureMediumActivityIndicatorView_(self, activityIndicator:objc_id)->None:
    activityIndicator.style = UIActivityIndicatorViewStyle.medium
    activityIndicator.hidesWhenStopped = True

    activityIndicator.startAnimating()
    # When the activity is done, be sure to use UIActivityIndicatorView.stopAnimating().

  @objc_method
  def configureLargeActivityIndicatorView_(self, activityIndicator):
    activityIndicator.style = UIActivityIndicatorViewStyle.large
    activityIndicator.hidesWhenStopped = True

    activityIndicator.startAnimating()
    # When the activity is done, be sure to use UIActivityIndicatorView.stopAnimating().
  @objc_method
  def configureMediumTintedActivityIndicatorView_(self, activityIndicator):
    activityIndicator.style = UIActivityIndicatorViewStyle.medium
    activityIndicator.hidesWhenStopped = True
    activityIndicator.color = UIColor.systemPurpleColor()

    activityIndicator.startAnimating()
    # When the activity is done, be sure to use UIActivityIndicatorView.stopAnimating().

  @objc_method
  def configureLargeTintedActivityIndicatorView_(self, activityIndicator):
    activityIndicator.style = UIActivityIndicatorViewStyle.large
    activityIndicator.hidesWhenStopped = True
    activityIndicator.color = UIColor.systemPurpleColor()

    activityIndicator.startAnimating()
    # When the activity is done, be sure to use UIActivityIndicatorView.stopAnimating().


if __name__ == '__main__':
  from rbedge.app import App

  from rbedge.enumerations import (
    UITableViewStyle,
    UIModalPresentationStyle,
  )

  table_style = UITableViewStyle.grouped
  main_vc = ActivityIndicatorViewController.alloc().initWithStyle_(table_style)
  _title = NSStringFromClass(ActivityIndicatorViewController)
  main_vc.navigationItem.title = _title

  presentation_style = UIModalPresentationStyle.fullScreen
  app = App(main_vc)
  app.main_loop(presentation_style)

