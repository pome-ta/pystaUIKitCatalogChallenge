from objc_util import ObjCInstance
from objc_util import CGRect


class _View:

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