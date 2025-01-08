'''
  note: Storyboard 実装なし
'''
import ctypes

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method, objc_const
from pyrubicon.objc.runtime import send_super, objc_id, SEL

from rbedge.enumerations import (
  UIDatePickerMode,
  UIControlContentHorizontalAlignment,
  UIControlContentVerticalAlignment,
  UILayoutConstraintAxis,
  UIUserInterfaceSizeClass,
  UIDatePickerStyle,
  NSDateFormatterStyle,
  NSCalendarUnit,
  UIControlEvents,
  NSTextAlignment,
  NSLineBreakMode,
)

from rbedge import pdbr
from pyLocalizedString import localizedString

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')
UIColor = ObjCClass('UIColor')

UIPickerView = ObjCClass('UIPickerView')
UIView = ObjCClass('UIView')


class PickerViewController(UIViewController):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    #print('\tdealloc')
    pass

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    self.navigationItem.title = localizedString('PickerViewTitle') if (
      title := self.navigationItem.title) is None else title
    self.view.backgroundColor = UIColor.systemBackgroundColor()
    
    pickerView = UIPickerView.new()
    colorSwatchView = UIView.new()
    
        # --- Layout
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide
    layoutMarginsGuide = self.view.layoutMarginsGuide

    self.view.addSubview_(pickerView)
    pickerView.translatesAutoresizingMaskIntoConstraints = False
    self.view.addSubview_(colorSwatchView)
    colorSwatchView.translatesAutoresizingMaskIntoConstraints = False
    
    NSLayoutConstraint.activateConstraints_([
      pickerView.widthAnchor.constraintEqualToConstant_(375.0),
    ])

    NSLayoutConstraint.activateConstraints_([
      pickerButton.topAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.topAnchor, 24.0),
      colorView.centerXAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerXAnchor),
      pickerButton.leadingAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.leadingAnchor, 18.0),
      pickerWellView.topAnchor.constraintEqualToAnchor_constant_(
        pickerButton.bottomAnchor, 8.0),
      colorView.leadingAnchor.constraintGreaterThanOrEqualToAnchor_constant_(
        pickerButton.leadingAnchor, 8.0),
      pickerWellView.leadingAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.leadingAnchor, 18.0),
      colorView.topAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.topAnchor, 24.0),
    ])

    
  @objc_method
  def viewWillAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print('viewWillAppear')

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

  main_vc = PickerViewController.new()
  _title = NSStringFromClass(PickerViewController)
  main_vc.navigationItem.title = _title

  presentation_style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, presentation_style)

