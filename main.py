from objc_util import ObjCClass, ObjCInstance, create_objc_class, on_main_thread
from objc_util import sel, CGRect


from objcista import *
from objcista.constants import UIRectEdge, UIModalPresentationStyle
from objcista.objcNavigationController import ObjcNavigationController

import pdbg


@on_main_thread
def run_controller(view_controller):
  app = ObjCClass("UIApplication").sharedApplication()
  window = app.keyWindow() if app.keyWindow() else app.windows().firstObject()

  root_view_controller = window.rootViewController()

  while root_view_controller.presentedViewController():
    root_view_controller = root_view_controller.presentedViewController()

  full_screen = UIModalPresentationStyle.fullScreen
  view_controller.setModalPresentationStyle_(full_screen)
  root_view_controller.presentViewController_animated_completion_(
    view_controller, True, None)





class PlainNavigationController(ObjcNavigationController):

  def willShowViewController(self,
                             navigationController: UINavigationController,
                             viewController: UIViewController, animated: bool):
    # --- appearance
    appearance = UINavigationBarAppearance.alloc()
    appearance.configureWithDefaultBackground()

    # --- navigationBar
    navigationBar = navigationController.navigationBar()

    navigationBar.standardAppearance = appearance
    navigationBar.scrollEdgeAppearance = appearance
    navigationBar.compactAppearance = appearance
    navigationBar.compactScrollEdgeAppearance = appearance

    viewController.setEdgesForExtendedLayout_(0)


if __name__ == "__main__":
  nav = PlainNavigationController()

