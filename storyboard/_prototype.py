import ctypes

from pyrubicon.objc.api import ObjCClass, ObjCInstance, objc_method
from pyrubicon.objc.runtime import send_super
from pyrubicon.objc.types import NSInteger

UITableViewCell = ObjCClass('UITableViewCell')


class CustomTableViewCell(UITableViewCell):

  @objc_method
  def initWithStyle_reuseIdentifier_(self, style: NSInteger, reuseIdentifier):

    super_args = [
      style,
      reuseIdentifier,
    ]
    super_argtypes = [
      NSInteger,
      ctypes.c_void_p,
    ]

    self_ptr = send_super(__class__,
                          self,
                          'initWithStyle:reuseIdentifier:',
                          *super_args,
                          argtypes=super_argtypes)
    # todo: `self` に再定義しない
    #self = ObjCInstance(self_ptr)
    self.overrideCell()
    return ObjCInstance(self_ptr)

  @objc_method
  def overrideCell(self):
    pass

