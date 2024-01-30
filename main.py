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


class ObjcController:

  def __init__(self, *args, **kwargs):
    self._msgs: list['def'] = []  # xxx: 型名ちゃんとやる
    self.controller_instance: ObjCInstance

  def override(self):
    # todo: objc で独自にmethod 生やしたいときなど
    # todo: この関数内に関数を作り`@self.add_msg`
    pass

  def add_msg(self, msg):
    if not (hasattr(self, '_msgs')):
      self._msgs: list['def'] = []
    self._msgs.append(msg)

  def _override_controller(self):
    # todo: 既存method と独自追加method をシュッと持ちたい
    # if self._msgs: _methods.extend(self._msgs)
    pass

  def _init_controller(self):
    pass

  @classmethod
  def new(cls) -> ObjCInstance | None:
    return None


class ObjcMetaView:

  def __init__(self, *args, **kwargs):
    self.instance: ObjCInstance
    self.CGRectZero = CGRect((0.0, 0.0), (0.0, 0.0))

    self.IS_LAYOUT_DEBUG = True if kwargs.get('LAYOUT_DEBUG') else False

  def _init(self):
    if self.IS_LAYOUT_DEBUG:
      from objc_util import ObjCClass
      color = ObjCClass('UIColor').systemRedColor()
      self.instance.layer().setBorderWidth_(1.0)
      self.instance.layer().setBorderColor_(color.cgColor())
    self.instance.setTranslatesAutoresizingMaskIntoConstraints_(False)

    return self.instance

  @classmethod
  def new(cls, *args, **kwargs) -> ObjCInstance:
    _cls = cls(*args, **kwargs)
    return _cls._init()


# --- navigation
UINavigationController = ObjCClass("UINavigationController")
UINavigationBarAppearance = ObjCClass("UINavigationBarAppearance")

if __name__ == "__main__":
  pass

