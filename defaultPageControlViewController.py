from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super
from pyrubicon.objc.types import CGRectMake

from rbedge.functions import NSStringFromClass

UIViewController = ObjCClass('UIViewController')
UIView = ObjCClass('UIView')
UIPageControl = ObjCClass('UIPageControl')
UIColor = ObjCClass('UIColor')

NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

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

    # xxx: あとで切り出す
    self.pageControl = UIPageControl.alloc().init().autorelease()

    self.colorView: UIView = UIView.new()

    self.setlayout()
    self.configurePageControl()

  @objc_method
  def setlayout(self):
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide
    # xxx: 仮置き
    self.pageControl.frame = CGRectMake(16.0, 639.5, 343.0, 27.5)
    self.colorView.frame = CGRectMake(0.0, 0.0, 375.0, 667.0)
    self.colorView.backgroundColor = UIColor.systemMintColor()

    self.view.addSubview_(self.pageControl)
    self.view.addSubview_(self.colorView)

    # --- layout
    self.pageControl.translatesAutoresizingMaskIntoConstraints = False

    NSLayoutConstraint.activateConstraints_([
      self.pageControl.trailingAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.trailingAnchor, -40),
      self.pageControl.leadingAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.leadingAnchor, 40),
      #self.pageControl.centerXAnchor.constraintEqualToAnchor_(safeAreaLayoutGuide.centerXAnchor),
      self.pageControl.bottomAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.bottomAnchor),
    ])

    self.colorView.translatesAutoresizingMaskIntoConstraints = False

    NSLayoutConstraint.activateConstraints_([
      #self.colorView.centerXAnchor.constraintEqualToAnchor_(safeAreaLayoutGuide.centerXAnchor),
      #self.colorView.centerXAnchor.constraintEqualToAnchor_(self.view.centerXAnchor),
      self.colorView.trailingAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.trailingAnchor, -40),
      self.colorView.leadingAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.leadingAnchor, 40),
      self.colorView.topAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.topAnchor, 35),
      self.colorView.bottomAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.bottomAnchor, -40),
    ])
    '''
    bottomAnchor",
    "centerXAnchor",
    "centerYAnchor",
    leadingAnchor
    topAnchor",
    "trailingAnchor",
    '''

    #key="frame" x="0.0" y="0.0" width="375" height="667"
    #pdbr.state(self.view, 1)
    #safeAreaLayoutGuide
    #safeAreaInsets
    #pdbr.state(self.view.safeAreaInsets)
    #print(self.view.safeAreaLayoutGuide)
    #pdbr.state(self.view.safeAreaLayoutGuide)
    #pdbr.state(self.pageControl.leadingAnchor)
    #pdbr.state(self.pageControl.layoutMargins,1)
    #print(type(self.pageControl.layoutMargins))

  @objc_method
  def configurePageControl(self):
    # todo: よしなに要素を配置したい
    #self.pageControl = UIPageControl.alloc().init().autorelease()
    self.pageControl.frame = CGRectMake(16, 639.5, 343, 27.5)

    self.pageControl.setNumberOfPages_(len(colors))
    self.pageControl.setCurrentPage_(2)
    self.pageControl.setPageIndicatorTintColor_(UIColor.systemGreenColor())
    self.pageControl.setCurrentPageIndicatorTintColor_(
      UIColor.systemPurpleColor())
    self.pageControl.setBackgroundColor_(UIColor.systemDarkRedColor())
    '''

    _max = self.pageControl.sizeForNumberOfPages_(len(colors))
    _size = self.pageControl.sizeThatFits_(_max)
    self.pageControl.size = _size
    '''

    #pdbr.state(self.pageControl, 0)
    #pdbr.state(pageControl.sizeForNumberOfPages_(len(colors)), 0)
    #print(pageControl.sizeForNumberOfPages_(len(colors)))
    #sizeForNumberOfPages
    #pdbr.state(UIColor)


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  pc_vc = PageControlViewController.new()
  style = UIModalPresentationStyle.fullScreen
  present_viewController(pc_vc, style)

