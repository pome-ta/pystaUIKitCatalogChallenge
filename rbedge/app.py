from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.runtime import objc_id, send_message

from .lifeCycle import loop
from .enumerations import UIModalPresentationStyle
from .objcMainThread import onMainThread

UIApplication = ObjCClass('UIApplication')
UIViewController = ObjCClass('UIViewController')  # todo: アノテーション用


class App:

  def __init__(self, viewController):
    print('App: __init__')
    self.viewController = viewController
  '''
  def __del__(self):
    print('App: __del__')
    try:
      print('try')
      send_message(self, 'autorelease', restype=objc_id, argtypes=[])
    except (NameError, TypeError):
      print('except')
      # Handle interpreter shutdown gracefully where send_message might be deleted
      # (NameError) or set to None (TypeError).
      pass
  '''

  def main_loop(self, modalPresentationStyle: int = 0):
    print('App: main_loop')

    @onMainThread
    def present_viewController(viewController: UIViewController,
                               _style: int) -> None:
      print(f'\t# present_viewController')
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
    loop.close()

