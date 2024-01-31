from objc_util import ObjCClass, ObjCInstance, create_objc_class, on_main_thread

from ._controller import _Controller

UINavigationController = ObjCClass('UINavigationController')
UIViewController = ObjCClass('UIViewController')


class ObjcNavigationController(_Controller):

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

