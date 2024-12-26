'''
  note: Storyboard 実装なし
'''
import ctypes

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method, objc_const
from pyrubicon.objc.runtime import send_super, objc_id, load_library
from pyrubicon.objc.types import CGRectMake

from rbedge.enumerations import (
  UILayoutConstraintAxis,
  NSTextAlignment,
)

from rbedge import pdbr

UIKit = load_library('UIKit')
UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UIStackView = ObjCClass('UIStackView')

UILabel = ObjCClass('UILabel')
UIFont = ObjCClass('UIFont')

UIColor = ObjCClass('UIColor')

# --- Global Variables
UIFontTextStyleHeadline = objc_const(UIKit, 'UIFontTextStyleHeadline')


class StackViewController(UIViewController):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    #print('\tdealloc')
    pass

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    self.navigationItem.title = localizedString('StackViewsTitle') if (
      title := self.navigationItem.title) is None else title

    #self.view.backgroundColor = UIColor.systemBackgroundColor()
    self.view.backgroundColor = UIColor.systemIndigoColor()

    #Add/remove
    #addRemoveExampleStackView
    # xxx: あとで、`setup` 的なのを作る
    # --- showingHidingExampleStackView
    showingHidingExampleStackView = UIStackView.alloc().initWithFrame_(
      CGRectMake(16.0, 52.0, 343.0, 134.5))
    # todo: 確認用
    showingHidingExampleStackView.backgroundColor = UIColor.systemGreenColor()
    showingHidingExampleStackView.axis = UILayoutConstraintAxis.vertical
    showingHidingExampleStackView.spacing = 10.0

    labelShowingHiding = UILabel.new()
    labelShowingHiding.text = 'Showing/hiding views'
    labelShowingHiding.textAlignment = NSTextAlignment.center
    labelShowingHiding.setFont_(
      UIFont.preferredFontForTextStyle_(UIFontTextStyleHeadline))

    # --- subShowingHidingStackView
    subShowingHidingStackView = UIStackView.alloc().initWithFrame_(
      CGRectMake(0.0, 30.5, 343.0, 34.0))
    subShowingHidingStackView.spacing = 10.0
    showingHidingExampleStackView.addArrangedSubview_(labelShowingHiding)

    self.view.addSubview_(showingHidingExampleStackView)

  @objc_method
  def viewDidAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print('viewDidAppear')

  @objc_method
  def viewDidDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print('viewDidDisappear')

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'{__class__}: didReceiveMemoryWarning')


if __name__ == '__main__':
  from rbedge.functions import NSStringFromClass
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController

  main_vc = StackViewController.new()
  _title = NSStringFromClass(StackViewController)
  main_vc.navigationItem.title = _title

  presentation_style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, presentation_style)

