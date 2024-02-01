__version__ = '0.0.0'

from objc_util import on_main_thread
from ._classes import *
from .constants import *


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

