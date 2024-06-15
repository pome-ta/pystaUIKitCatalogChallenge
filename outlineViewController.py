from pyrubicon.objc.api import ObjCClass, objc_method
from pyrubicon.objc.runtime import send_super



#ObjCClass.auto_rename = True
UISplitViewController = ObjCClass('UISplitViewController')


class OutlineViewController(UISplitViewController):

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  main_vc = OutlineViewController.new()
  style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, style,False)

