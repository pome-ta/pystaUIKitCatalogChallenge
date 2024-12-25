from enum import Enum

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method, objc_id
from pyrubicon.objc.runtime import send_super
from pyrubicon.objc.types import NSInteger

from rbedge.enumerations import (
  UIActivityIndicatorViewStyle, )

from rbedge import pdbr

from caseElement import CaseElement
from pyLocalizedString import localizedString

from baseTableViewController import BaseTableViewController
from storyboard.activityIndicatorViewController import prototypes

UIColor = ObjCClass('UIColor')


class ActivityIndicatorKind(Enum):
  mediumIndicator = 'mediumIndicator'
  largeIndicator = 'largeIndicator'
  mediumTintedIndicator = 'mediumTintedIndicator'
  largeTintedIndicator = 'largeTintedIndicator'


class ActivityIndicatorViewController(BaseTableViewController):

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
    self.setupPrototypes_(prototypes)
    return self

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?

    self.navigationItem.title = localizedString('ActivityIndicatorsTitle') if (
      title := self.navigationItem.title) is None else title

    self.testCells.extend([
      CaseElement(localizedString('MediumIndicatorTitle'),
                  ActivityIndicatorKind.mediumIndicator.value,
                  self.configureMediumActivityIndicatorView_),
      CaseElement(localizedString('LargeIndicatorTitle'),
                  ActivityIndicatorKind.largeIndicator.value,
                  self.configureLargeActivityIndicatorView_),
    ])
    # if traitCollection.userInterfaceIdiom != .mac
    # Tinted activity indicators available only on iOS.
    self.testCells.extend([
      CaseElement(localizedString('MediumTintedIndicatorTitle'),
                  ActivityIndicatorKind.mediumTintedIndicator.value,
                  self.configureMediumTintedActivityIndicatorView_),
      CaseElement(localizedString('LargeTintedIndicatorTitle'),
                  ActivityIndicatorKind.largeTintedIndicator.value,
                  self.configureLargeTintedActivityIndicatorView_),
    ])

  # MARK: - Configuration
  @objc_method
  def configureMediumActivityIndicatorView_(self, activityIndicator):
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
  from rbedge.functions import NSStringFromClass
  from rbedge.enumerations import (
    UITableViewStyle,
    UIModalPresentationStyle,
  )
  from rbedge import present_viewController

  table_style = UITableViewStyle.grouped
  main_vc = ActivityIndicatorViewController.alloc().initWithStyle_(table_style)
  _title = NSStringFromClass(ActivityIndicatorViewController)
  main_vc.navigationItem.title = _title

  presentation_style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, presentation_style)

