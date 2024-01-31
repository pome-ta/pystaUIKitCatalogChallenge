from objc_util import ObjCClass
from ._classes import *
from ._view import _View


class ObjcView(_View):

  def __init__(self, *args, **kwargs):

    super().__init__(*args, **kwargs)
    self.instance = UIView.alloc()
    self.instance.initWithFrame_(self.CGRectZero)

