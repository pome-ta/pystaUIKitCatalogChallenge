from dataclasses import dataclass

from objc_util import ObjCClass, ObjCInstance, create_objc_class, on_main_thread
from objc_util import sel, CGRect

import pdbg


@dataclass
class UIRectEdge:
  # ref: [UIRectEdge | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uirectedge?language=objc)
  none: int = 0
  top: int = 1 << 0
  left: int = 1 << 1
  bottom: int = 1 << 2
  right: int = 1 << 3
  all: int = top | left | bottom | right


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


UIViewController = ObjCClass('UIViewController')
UINavigationController = ObjCClass("UINavigationController")
UINavigationBarAppearance = ObjCClass("UINavigationBarAppearance")


# --- navigation
class ObjcNavigationController(ObjcController):

  def _override_controller(self):
    # --- `UINavigationController` Methods

    # --- `UINavigationController` set up
    _methods = []
    if self._msgs: _methods.extend(self._msgs)

    create_kwargs = {
      'name': '_nv',
      'superclass': UINavigationController,
      'methods': _methods,
    }
    _nv = create_objc_class(**create_kwargs)
    self.controller_instance = _nv

  def willShowViewController(self,
                             navigationController: UINavigationController,
                             viewController: UIViewController, animated: bool):

    pass

  def create_navigationControllerDelegate(self):
    # --- `UINavigationControllerDelegate` Methods
    def navigationController_willShowViewController_animated_(
        _self, _cmd, _navigationController, _viewController, _animated):

      navigationController = ObjCInstance(_navigationController)
      viewController = ObjCInstance(_viewController)
      self.willShowViewController(navigationController, viewController,
                                  _animated)

    # --- `UINavigationControllerDelegate` set up
    _methods = [
      navigationController_willShowViewController_animated_,
    ]
    _protocols = [
      'UINavigationControllerDelegate',
    ]

    create_kwargs = {
      'name': '_nvDelegate',
      'methods': _methods,
      'protocols': _protocols,
    }
    _nvDelegate = create_objc_class(**create_kwargs)
    return _nvDelegate.new()

  def _init_controller(self,
                       vc: UIViewController,
                       is_main_thread: bool = False):

    def __initialize():
      self._override_controller()
      _delegate = self.create_navigationControllerDelegate()
      nv = self.controller_instance.alloc()
      nv.initWithRootViewController_(vc).autorelease()
      nv.setDelegate_(_delegate)
      return nv

    if is_main_thread:

      @on_main_thread
      def __run():
        return __initialize()
    else:

      def __run():
        return __initialize()

    return __run()

  @classmethod
  def new(cls,
          viewController: UIViewController,
          is_main_thread: bool = False) -> ObjCInstance:
    _cls = cls()
    return _cls._init_controller(viewController, is_main_thread)


class ObjcViewController(ObjcController):

  def didLoad(self, this: UIViewController):
    pass

  def willAppear(self, this: UIViewController, animated: bool):
    pass

  def willLayoutSubviews(self, this: UIViewController):
    pass

  def didLayoutSubviews(self, this: UIViewController):
    pass

  def didAppear(self, this: UIViewController, animated: bool):
    pass

  def willDisappear(self, this: UIViewController, animated: bool):
    pass

  def didDisappear(self, this: UIViewController, animated: bool):
    pass

  def _override_controller(self):
    # --- `UIViewController` Methods
    def viewDidLoad(_self, _cmd):
      this = ObjCInstance(_self)
      self.didLoad(this)

    def viewWillAppear_(_self, _cmd, animated):
      this = ObjCInstance(_self)
      self.willAppear(this, animated)

    def viewWillLayoutSubviews(_self, _cmd):
      this = ObjCInstance(_self)
      self.willLayoutSubviews(this)

    def viewDidLayoutSubviews(_self, _cmd):
      this = ObjCInstance(_self)
      self.didLayoutSubviews(this)

    def viewDidAppear_(_self, _cmd, animated):
      this = ObjCInstance(_self)
      self.didAppear(this, animated)

    def viewWillDisappear_(_self, _cmd, animated):
      this = ObjCInstance(_self)
      self.willDisappear(this, animated)

    def viewDidDisappear_(_self, _cmd, animated):
      this = ObjCInstance(_self)
      self.didDisappear(this, animated)

    # --- `UIViewController` set up
    _methods = [
      viewDidLoad,
      viewWillAppear_,
      viewWillLayoutSubviews,
      viewDidLayoutSubviews,
      viewDidAppear_,
      viewWillDisappear_,
      viewDidDisappear_,
    ]

    if self._msgs: _methods.extend(self._msgs)

    create_kwargs = {
      'name': '_vc',
      'superclass': UIViewController,
      'methods': _methods,
    }
    _vc = create_objc_class(**create_kwargs)
    self.controller_instance = _vc

  def _init_controller(self):
    self._override_controller()
    vc = self.controller_instance.new().autorelease()
    return vc

  @classmethod
  def new(cls, *args, **kwargs) -> ObjCInstance:
    _cls = cls(*args, **kwargs)
    return _cls._init_controller()


class PlainNavigationController(ObjcNavigationController):

  def willShowViewController(self,
                             navigationController: UINavigationController,
                             viewController: UIViewController, animated: bool):
    # --- appearance
    appearance = UINavigationBarAppearance.alloc()
    appearance.configureWithDefaultBackground()

    # --- navigationBar
    navigationBar = navigationController.navigationBar()

    navigationBar.standardAppearance = appearance
    navigationBar.scrollEdgeAppearance = appearance
    navigationBar.compactAppearance = appearance
    navigationBar.compactScrollEdgeAppearance = appearance

    viewController.setEdgesForExtendedLayout_(0)


if __name__ == "__main__":
  pass

