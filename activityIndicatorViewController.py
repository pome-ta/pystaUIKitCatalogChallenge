from enum import Enum

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super

from rbedge.enumerations import (
  UITableViewStyle,
  UIActivityIndicatorViewStyle,
)

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
  def init(self):
    send_super(__class__, self, 'init')  # xxx: 不要?
    tableViewStyle = UITableViewStyle.grouped
    self.initWithStyle_(tableViewStyle)

    self.testCells = []
    self.initPrototype()

    return self

  @objc_method
  def initPrototype(self):
    [
      self.tableView.registerClass_forCellReuseIdentifier_(
        prototype['cellClass'], prototype['identifier'])
      for prototype in prototypes
    ]

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    self.navigationItem.title = localizedString('ActivityIndicatorsTitle')

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
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController

  main_vc = ActivityIndicatorViewController.new()
  _title = NSStringFromClass(ActivityIndicatorViewController)
  main_vc.navigationItem.title = _title

  #style = UIModalPresentationStyle.pageSheet
  style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, style)

