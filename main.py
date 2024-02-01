from objc_util import ObjCClass, ObjCInstance, create_objc_class, on_main_thread
from objc_util import sel, CGRect

from objcista import *
from objcista.constants import UIRectEdge, UIModalPresentationStyle
from objcista.objcNavigationController import ObjcNavigationController

import pdbg


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

    edge = UIRectEdge.none

    viewController.setEdgesForExtendedLayout_(edge)


if __name__ == "__main__":
  nav = PlainNavigationController()

