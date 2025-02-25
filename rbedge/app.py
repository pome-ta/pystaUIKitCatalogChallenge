from pyrubicon.objc.api import ObjCClass

from .lifeCycle import loop
from .enumerations import (
  UISceneActivationState,
  UIModalPresentationStyle,
)
from .objcMainThread import onMainThread
from .rootNavigationController import RootNavigationController

UIApplication = ObjCClass('UIApplication')
UIViewController = ObjCClass('UIViewController')  # todo: アノテーション用


class App:

  sharedApplication = UIApplication.sharedApplication
  __objectEnumerator = sharedApplication.connectedScenes.objectEnumerator()
  while (__windowScene := __objectEnumerator.nextObject()):
    if __windowScene.activationState == 0:
      break
  rootViewController = __windowScene.keyWindow.rootViewController

  def __init__(self,
               viewController: UIViewController,
               modalPresentationStyle: UIModalPresentationStyle
               | int = UIModalPresentationStyle.pageSheet):
    self.viewController = viewController
    # xxx: style 指定を力技で確認
    _automatic = UIModalPresentationStyle.automatic  # -2
    _blurOverFullScreen = UIModalPresentationStyle.blurOverFullScreen  # 8
    _pageSheet = UIModalPresentationStyle.pageSheet  # 1

    self.modalPresentationStyle = modalPresentationStyle if isinstance(
      modalPresentationStyle, int
    ) and _automatic <= modalPresentationStyle <= _blurOverFullScreen else _pageSheet

  def present(self) -> None:

    @onMainThread
    def present_viewController(viewController: UIViewController,
                               style: int) -> None:

      presentViewController = RootNavigationController.alloc(
      ).initWithRootViewController_(viewController)

      presentViewController.setModalPresentationStyle_(style)

      self.rootViewController.presentViewController_animated_completion_(
        presentViewController, True, None)

    present_viewController(self.viewController, self.modalPresentationStyle)
    self.main_loop()

  def main_loop(self) -> None:
    loop.run_forever()
    loop.close()

