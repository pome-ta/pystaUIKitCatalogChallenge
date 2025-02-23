from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, objc_id
from pyrubicon.objc.types import NSInteger

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

UITableViewCell = ObjCClass('UITableViewCell')


class CustomTableViewCell(UITableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def initWithStyle_reuseIdentifier_(self, style: NSInteger, reuseIdentifier):
    #print(f'\t\t\t{NSStringFromClass(__class__)}: initWithStyle:reuseIdentifier:')
    super_args = [
      style,
      reuseIdentifier,
    ]
    super_argtypes = [
      NSInteger,
      objc_id,
    ]

    send_super(__class__,
               self,
               'initWithStyle:reuseIdentifier:',
               *super_args,
               argtypes=super_argtypes)

    self.overrideCell()
    return self

  @objc_method
  def overrideCell(self):
    #print(f'\t\t\t{NSStringFromClass(__class__)}: prototype.overrideCell')
    pass

