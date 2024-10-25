from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super
from pyrubicon.objc.types import CGRectMake

from rbedge.functions import NSStringFromClass

UIViewController = ObjCClass('UIViewController')
UIPageControl = ObjCClass('UIPageControl')
UIColor = ObjCClass('UIColor')

colors = [
  UIColor.blackColor,
  UIColor.systemGrayColor(),
  UIColor.systemRedColor(),
  UIColor.systemGreenColor(),
  UIColor.systemBlueColor(),
  UIColor.systemPinkColor(),
  UIColor.systemYellowColor(),
  UIColor.systemIndigoColor(),
  UIColor.systemOrangeColor(),
  UIColor.systemPurpleColor(),
]


class PageControlViewController(UIViewController):

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    # --- Navigation
    title = NSStringFromClass(__class__)
    self.navigationItem.title = title

    self.configurePageControl()

  @objc_method
  def configurePageControl(self):
    pageControl = UIPageControl.alloc().init().autorelease()
    pageControl.frame = CGRectMake(16, 639.5, 343, 27.5)

    pageControl.setNumberOfPages_(len(colors))
    pageControl.setCurrentPage_(2)
    pageControl.setPageIndicatorTintColor_(UIColor.systemGreenColor())
    pageControl.setCurrentPageIndicatorTintColor_(UIColor.systemPurpleColor())

    pageControl.setBackgroundColor_(UIColor.systemDarkRedColor())
    #pdbr.state(pageControl,1)
    #pdbr.state(UIColor)

    self.view.addSubview_(pageControl)


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  pc_vc = PageControlViewController.new()
  style = UIModalPresentationStyle.fullScreen
  present_viewController(pc_vc, style)

