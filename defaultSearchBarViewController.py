"""
todo:
  Storyboard 未対応
  xcode だと再現できず？
"""

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super
from pyrubicon.objc.types import CGRectMake

from rbedge.functions import NSStringFromClass

UIViewController = ObjCClass('UIViewController')

NSLayoutConstraint = ObjCClass('NSLayoutConstraint')


class DefaultSearchBarViewController(UIViewController):

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    # --- Navigation
    title = NSStringFromClass(__class__)
    self.navigationItem.title = title


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  sb_vc = DefaultSearchBarViewController.new()
  style = UIModalPresentationStyle.fullScreen
  present_viewController(sb_vc, style)

