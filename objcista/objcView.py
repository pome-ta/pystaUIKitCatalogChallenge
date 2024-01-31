from objc_util import ObjCClass
from ._view import _View

UIView = ObjCClass('UIView')


class ObjcView(_View):

  def __init__(self, *args, **kwargs):

    super().__init__(*args, **kwargs)
    self.instance = UIView.alloc()
    self.instance.initWithFrame_(self.CGRectZero)

