__version__ = '0.0.0'
import ctypes
from pathlib import Path
from objc_util import c, ObjCInstance, on_main_thread, nsurl

from ._classes import *
from .constants import *


# ref: [Picker wheel for lists (not just dates) | omz:forum](https://forum.omz-software.com/topic/4592/picker-wheel-for-lists-not-just-dates/2)
# [Pythonista/_2017/picker-wheel-for-lists.py at 3e082d53b6b9b501a3c8cf3251a8ad4c8be9c2ad · tdamdouni/Pythonista · GitHub](https://github.com/tdamdouni/Pythonista/blob/3e082d53b6b9b501a3c8cf3251a8ad4c8be9c2ad/_2017/picker-wheel-for-lists.py#L24)
def globalVariable(name: str):
  return ObjCInstance(ctypes.c_void_p.in_dll(c, name))


def get_absolutepath(path):
  # xxx: かなり意味ないので、要検討
  _path = Path(path)
  if (_path.exists()):
    return str(_path.absolute())
  else:
    print('画像が見つかりません')
    raise


def get_dataWithContentsOfURL(path: str) -> NSData:
  _nsurl = nsurl(get_absolutepath(path))
  return NSData.dataWithContentsOfURL_(_nsurl)


@on_main_thread
def run_controller(view_controller,
                   modalPresentationStyle: UIModalPresentationStyle
                   | int = UIModalPresentationStyle.fullScreen):
  app = ObjCClass("UIApplication").sharedApplication()
  window = app.keyWindow() if app.keyWindow() else app.windows().firstObject()

  root_view_controller = window.rootViewController()

  while root_view_controller.presentedViewController():
    root_view_controller = root_view_controller.presentedViewController()

  # xxx: style 指定を力技で確認
  automatic = UIModalPresentationStyle.automatic  # -2
  blurOverFullScreen = UIModalPresentationStyle.blurOverFullScreen  # 8
  pageSheet = UIModalPresentationStyle.pageSheet  # 1

  style = modalPresentationStyle if isinstance(
    modalPresentationStyle, int
  ) and automatic <= modalPresentationStyle <= blurOverFullScreen else pageSheet
  view_controller.setModalPresentationStyle_(style)
  root_view_controller.presentViewController_animated_completion_(
    view_controller, True, None)

