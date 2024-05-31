__version__ = '0.0.0'
from pathlib import Path

from pyrubicon.objc.api import ObjCClass

from .enumerations import UIModalPresentationStyle
from .objcMainThread import onMainThread


def get_absolutepath(path_str: str) -> str:
  # xxx: かなり意味ないので、要検討
  _path = Path(path_str)
  if (_path.exists()):
    return str(_path.absolute())
  else:
    print('画像が見つかりません')
    raise


def get_dataWithContentsOfURL(path_str: str) -> NSData:
  _nsurl = nsurl(get_absolutepath(path_str))
  return NSData.dataWithContentsOfURL_(_nsurl)


ObjCClass.auto_rename = True

UIViewController = ObjCClass('UIViewController')  # todo: アノテーション用


@onMainThread
def present_viewController(viewController: UIViewController,
                           modalPresentationStyle: UIModalPresentationStyle
                           | int = UIModalPresentationStyle.fullScreen,
                           navigationController_enabled: bool = True):
  sharedApplication = ObjCClass('UIApplication').sharedApplication
  keyWindow = sharedApplication.keyWindow if sharedApplication.keyWindow else sharedApplication.windows[
    0]
  rootViewController = keyWindow.rootViewController

  while _presentedViewController := rootViewController.presentedViewController:
    rootViewController = _presentedViewController

  if navigationController_enabled:
    from .rootNavigationController import RootNavigationController

    presentViewController = RootNavigationController.alloc(
    ).initWithRootViewController_(viewController)
  else:
    presentViewController = viewController

  # xxx: style 指定を力技で確認
  automatic = UIModalPresentationStyle.automatic  # -2
  blurOverFullScreen = UIModalPresentationStyle.blurOverFullScreen  # 8
  pageSheet = UIModalPresentationStyle.pageSheet  # 1

  style = modalPresentationStyle if isinstance(
    modalPresentationStyle, int
  ) and automatic <= modalPresentationStyle <= blurOverFullScreen else pageSheet

  presentViewController.setModalPresentationStyle_(style)

  rootViewController.presentViewController_animated_completion_(
    presentViewController, True, None)

