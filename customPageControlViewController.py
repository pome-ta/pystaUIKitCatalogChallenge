"""
todo:
  Storyboard 未対応
  各 frame が仮
  `centerXAnchor` の挙動
"""

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, SEL
from pyrubicon.objc.types import CGRectMake

from rbedge.enumerations import UIControlEvents
from rbedge.functions import NSStringFromClass

UIViewController = ObjCClass('UIViewController')
UIView = ObjCClass('UIView')
UIPageControl = ObjCClass('UIPageControl')
UIColor = ObjCClass('UIColor')

NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

colors = [
  #UIColor.blackColor,
  UIColor.whiteColor,
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

    self.view.backgroundColor = UIColor.systemBackgroundColor()

    # xxx: あとで切り出す
    self.pageControl = UIPageControl.alloc().init().autorelease()
    self.colorView: UIView = UIView.new()

    self.setlayout()
    self.configurePageControl()
    self.pageControlValueDidChange()

  @objc_method
  def setlayout(self):
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide
    # xxx: 仮置き
    self.pageControl.frame = CGRectMake(16.0, 639.5, 343.0, 27.5)
    self.colorView.frame = CGRectMake(40.0, 79.0, 295.0, 548.0)
    #self.colorView.backgroundColor = UIColor.systemMintColor()

    self.view.addSubview_(self.pageControl)
    self.view.addSubview_(self.colorView)

    # --- layout
    self.pageControl.translatesAutoresizingMaskIntoConstraints = False
    NSLayoutConstraint.activateConstraints_([
      self.pageControl.trailingAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.trailingAnchor, -40),
      self.pageControl.leadingAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.leadingAnchor, 40),
      self.pageControl.bottomAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.bottomAnchor),
    ])

    self.colorView.translatesAutoresizingMaskIntoConstraints = False
    NSLayoutConstraint.activateConstraints_([
      self.colorView.trailingAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.trailingAnchor, -40),
      self.colorView.leadingAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.leadingAnchor, 40),
      self.colorView.topAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.topAnchor, 35),
      self.colorView.bottomAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.bottomAnchor, -40),
    ])

  @objc_method
  def configurePageControl(self):
    # wip: よしなに要素を配置したい

    self.pageControl.setNumberOfPages_(len(colors))
    self.pageControl.setCurrentPage_(2)
    self.pageControl.setPageIndicatorTintColor_(UIColor.systemGreenColor())
    self.pageControl.setCurrentPageIndicatorTintColor_(
      UIColor.systemPurpleColor())

    # xxx: 要素範囲確認用
    #self.pageControl.setBackgroundColor_(UIColor.systemDarkRedColor())

    self.pageControl.addTarget_action_forControlEvents_(
      self, SEL('pageControlValueDidChange'), UIControlEvents.valueChanged)

  # MARK: - Actions
  @objc_method
  def pageControlValueDidChange(self):
    # The total number of available pages is based on the number of available colors.
    # 利用可能なページの総数は、利用可能な色の数に基づいています。
    print(
      f'The page control changed its current page to {self.pageControl.currentPage}.'
    )
    self.colorView.backgroundColor = colors[self.pageControl.currentPage]


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  pc_vc = PageControlViewController.new()
  style = UIModalPresentationStyle.fullScreen
  present_viewController(pc_vc, style)

