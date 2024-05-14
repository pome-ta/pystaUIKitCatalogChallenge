from pyrubicon.objc.api import ObjCClass, ObjCProtocol, objc_method
from pyrubicon.objc.runtime import SEL

from .enumerations import UIRectEdge, UIBarButtonSystemItem

#ObjCClass.auto_rename = True

# --- UINavigationController
UINavigationController = ObjCClass('UINavigationController')
UINavigationControllerDelegate = ObjCProtocol('UINavigationControllerDelegate')
UINavigationBarAppearance = ObjCClass('UINavigationBarAppearance')
UIBarButtonItem = ObjCClass('UIBarButtonItem')


class RootNavigationController(UINavigationController,
                               protocols=[UINavigationControllerDelegate]):

  @objc_method
  def viewDidLoad(self):
    appearance = UINavigationBarAppearance.new()
    appearance.configureWithDefaultBackground()

    navigationBar = self.navigationBar
    navigationBar.standardAppearance = appearance
    navigationBar.scrollEdgeAppearance = appearance
    navigationBar.compactAppearance = appearance
    navigationBar.compactScrollEdgeAppearance = appearance

    self.delegate = self

  @objc_method
  def doneButtonTapped_(self, sender):
    visibleViewController = self.visibleViewController
    visibleViewController.dismissViewControllerAnimated_completion_(True, None)

  @objc_method
  def navigationController_willShowViewController_animated_(
      self, navigationController, viewController, animated: bool):
    extendedLayout = UIRectEdge.none
    viewController.setEdgesForExtendedLayout_(extendedLayout)

    barButtonSystemItem = UIBarButtonSystemItem.done
    doneButton = UIBarButtonItem.alloc(
    ).initWithBarButtonSystemItem_target_action_(barButtonSystemItem,
                                                 navigationController,
                                                 SEL('doneButtonTapped:'))
    visibleViewController = navigationController.visibleViewController

    navigationItem = visibleViewController.navigationItem
    navigationItem.rightBarButtonItem = doneButton

