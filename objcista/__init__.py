__version__ = '0.0.0'

from objc_util import on_main_thread

from ._classes import *
from .constants import *


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

