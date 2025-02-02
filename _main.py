from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, objc_id

from rbedge.enumerations import (
  UISplitViewControllerStyle,
  UISplitViewControllerColumn,
  UISplitViewControllerDisplayMode,
  UIUserInterfaceSizeClass,
)
from rbedge.functions import NSStringFromClass
from rbedge import pdbr

from outlineViewController import OutlineViewController

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')
UINavigationController = ObjCClass('UINavigationController')  # todo: 型確認

# --- SplitView
UISplitViewController = ObjCClass('UISplitViewController')

# --- others
UIColor = ObjCClass('UIColor')
UILabel = ObjCClass('UILabel')
UIFont = ObjCClass('UIFont')

UIKitCatalog_title = 'UIKitCatalog'


class TopViewController(UIViewController):

  @objc_method
  def viewDidLoad(self):
    # --- View
    self.view.backgroundColor = UIColor.systemBackgroundColor()

    self.label = UILabel.new()
    self.label.text = UIKitCatalog_title
    self.label.font = UIFont.systemFontOfSize_(26.0)
    self.label.sizeToFit()

    self.view.addSubview_(self.label)

    # --- Layout
    self.label.translatesAutoresizingMaskIntoConstraints = False

    NSLayoutConstraint.activateConstraints_([
      self.label.centerXAnchor.constraintEqualToAnchor_(
        self.view.centerXAnchor),
      self.label.centerYAnchor.constraintEqualToAnchor_(
        self.view.centerYAnchor),
    ])


class SplitViewController(UISplitViewController):

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    self.delegate = self

    primary_vc = OutlineViewController.new()
    primary_vc.title = UIKitCatalog_title

    secondary_vc = TopViewController.new()

    primary = UISplitViewControllerColumn.primary
    secondary = UISplitViewControllerColumn.secondary

    self.setViewController_forColumn_(primary_vc, primary)
    self.setViewController_forColumn_(secondary_vc, secondary)

  # --- UISplitViewControllerDelegate
  @objc_method
  def splitViewController_topColumnForCollapsingToProposedTopColumn_(
      self, svc, proposedTopColumn: int) -> int:
    return UISplitViewControllerColumn.secondary

  @objc_method
  def splitViewController_displayModeForExpandingToProposedDisplayMode_(
      self, svc, proposedDisplayMode: int):

    if (navController :=
        svc.viewControllers[0]).isMemberOfClass_(UINavigationController):
      navController.popToRootViewControllerAnimated_(False)
    return UISplitViewControllerDisplayMode.automatic


class MainViewController(UIViewController):

  @objc_method
  def viewDidLoad(self):
    # --- Navigation
    send_super(__class__, self, 'viewDidLoad')
    title = NSStringFromClass(__class__)
    self.navigationItem.title = title

    # --- View
    split = SplitViewController.alloc().initWithStyle_(
      UISplitViewControllerStyle.doubleColumn)
    self.addChildViewController_(split)
    self.view.addSubview_(split.view)
    split.didMoveToParentViewController_(self)


if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import UIModalPresentationStyle

  vc = MainViewController.new()

  style = UIModalPresentationStyle.fullScreen
  #style = UIModalPresentationStyle.pageSheet

  app = App(vc)
  app.main_loop(style)

