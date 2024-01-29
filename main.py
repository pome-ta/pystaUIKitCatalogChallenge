from dataclasses import dataclass

from objc_util import ObjCClass, ObjCInstance, create_objc_class, on_main_thread
from objc_util import sel, CGRect

import pdbg


@dataclass
class UIModalPresentationStyle:
  # ref: [UIModalPresentationStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle)
  automatic: int = -2
  none: int = -1
  fullScreen: int = 0
  pageSheet: int = 1
  formSheet: int = 2
  currentContext: int = 3
  custom: int = 4
  overFullScreen: int = 5
  overCurrentContext: int = 6
  popover: int = 7
  blurOverFullScreen: int = 8


@on_main_thread
def present_objc(viewController):
  app = ObjCClass("UIApplication").sharedApplication()
  window = app.keyWindow() if app.keyWindow() else app.windows().firstObject()

  rootViewController = window.rootViewController()

  while rootViewController.presentedViewController():
    rootViewController = rootViewController.presentedViewController()

  fullScreen = UIModalPresentationStyle.fullScreen
  viewController.setModalPresentationStyle_(fullScreen)
  rootViewController.presentViewController_animated_completion_(
    viewController, True, None)


if __name__ == "__main__":
  pass

