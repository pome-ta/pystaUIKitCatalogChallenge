from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super

from rbedge.functions import NSStringFromClass

UIViewController = ObjCClass('UIViewController')
UIPageControl = ObjCClass('UIPageControl')


class PageControlViewController(UIViewController):

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    # --- Navigation
    title = NSStringFromClass(__class__)
    self.navigationItem.title = title
    pageControl = UIPageControl.alloc().init().autorelease()
    pdbr.state(pageControl)


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  pc_vc = PageControlViewController.new()
  style = UIModalPresentationStyle.fullScreen
  present_viewController(pc_vc, style)

