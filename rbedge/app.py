from pyrubicon.objc.api import ObjCClass

from .lifeCycle import loop
from .enumerations import UIModalPresentationStyle
from .objcMainThread import onMainThread

UIApplication = ObjCClass('UIApplication')
UIViewController = ObjCClass('UIViewController')  # todo: アノテーション用


class App:

  def __init__(self, viewController):
    self.viewController = viewController

  def main_loop(self, modalPresentationStyle: int = 0):

    @onMainThread
    def present_viewController(viewController: UIViewController,
                               _style: int) -> None:
      sharedApplication = UIApplication.sharedApplication
      keyWindow = sharedApplication.windows.firstObject()
      rootViewController = keyWindow.rootViewController

      while _presentedViewController := rootViewController.presentedViewController:
        rootViewController = _presentedViewController

      from .rootNavigationController import RootNavigationController

      presentViewController = RootNavigationController.alloc(
      ).initWithRootViewController_(viewController)

      # xxx: style 指定を力技で確認
      automatic = UIModalPresentationStyle.automatic  # -2
      blurOverFullScreen = UIModalPresentationStyle.blurOverFullScreen  # 8
      pageSheet = UIModalPresentationStyle.pageSheet  # 1

      style = _style if isinstance(
        _style,
        int) and automatic <= _style <= blurOverFullScreen else pageSheet

      presentViewController.setModalPresentationStyle_(style)

      rootViewController.presentViewController_animated_completion_(
        presentViewController, True, None)

    present_viewController(self.viewController, modalPresentationStyle)
    loop.run_forever()
    #print('--- run_forever: close')
    loop.close()

