'''
  note: Storyboard 未定義
'''

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super

from rbedge import pdbr

from pyLocalizedString import localizedString

UIViewController = ObjCClass('UIViewController')


print(localizedString('A Short Title is Best'))


class AlertControllerViewController(UIViewController):
  pass
  
if __name__ == '__main__':
  from rbedge.functions import NSStringFromClass
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  

  main_vc = AlertControllerViewController.new()
  _title = NSStringFromClass(AlertControllerViewController)
  main_vc.navigationItem.title = _title
  style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, style)

