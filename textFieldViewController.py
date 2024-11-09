from enum import Enum

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.runtime import SEL, send_super, objc_id
from pyrubicon.objc.types import CGFloat


#UITextField = ObjCClass('UITextField')
# Custom text field for controlling input text placement.
# 入力テキストの配置を制御するためのカスタム テキスト フィールド。
class CustomTextField(ObjCClass('UITextField')):
  leftMarginPadding = objc_property(CGFloat)
  rightMarginPadding = objc_property(CGFloat)

  @objc_method
  def init(self):
    send_super(__class__, self, 'init')  # xxx: 不要?
    print('CustomTextField: init')
    self.leftMarginPadding = 12.0
    self.rightMarginPadding = 36.0
    return self


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

