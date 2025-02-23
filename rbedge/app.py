from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.runtime import objc_id, send_message

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

  def __init__(self, viewController):
    print('App: __init__')
    self.viewController = viewController
    self.rootViewController = None

  def main_loop(self, modalPresentationStyle: int = 0):
    #print('App: main_loop')

    sharedApplication = UIApplication.sharedApplication
    connectedScenes = sharedApplication.connectedScenes
    objectEnumerator = connectedScenes.objectEnumerator()
    while (windowScene := objectEnumerator.nextObject()):
      if windowScene.activationState == UISceneActivationState.foregroundActive:
        break
    keyWindow = windowScene.keyWindow
    self.rootViewController = keyWindow.rootViewController

    @onMainThread
    def present_viewController(viewController: UIViewController,
                               _style: int) -> None:
      #from .rootNavigationController import RootNavigationController

      presentViewController = RootNavigationController.alloc(
      ).initWithRootViewController_(viewController)

      presentViewController.setModalPresentationStyle_(style)

      self.rootViewController.presentViewController_animated_completion_(
        presentViewController, True, None)


    # xxx: style 指定を力技で確認
    _automatic = UIModalPresentationStyle.automatic  # -2
    _blurOverFullScreen = UIModalPresentationStyle.blurOverFullScreen  # 8
    _pageSheet = UIModalPresentationStyle.pageSheet  # 1

    style = modalPresentationStyle if isinstance(modalPresentationStyle, int) and _automatic <= modalPresentationStyle <= _blurOverFullScreen else _pageSheet

    present_viewController(self.viewController, style)
    loop.run_forever()
    loop.close()

