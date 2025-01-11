'''
  note: Storyboard 実装なし
'''
import ctypes
from enum import IntEnum, auto

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method, objc_const
from pyrubicon.objc.runtime import send_super, objc_id, load_library, SEL

from rbedge.enumerations import (
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

UIKit = load_library('UIKit')  # todo: `objc_const` 用
UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')
UIColor = ObjCClass('UIColor')
NSDictionary = ObjCClass('NSDictionary')

UIPickerView = ObjCClass('UIPickerView')
UIView = ObjCClass('UIView')
NSMutableAttributedString = ObjCClass('NSMutableAttributedString')

# --- Global Variables
NSForegroundColorAttributeName = objc_const(UIKit,
                                            'NSForegroundColorAttributeName')


class RGB:
  max: float = 255.0
  min: float = 0.0
  offset: float = 5.0


class ColorComponent(IntEnum):
  red = 0
  green = auto()
  blue = auto()


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

    # todo: 変数名`pickerView` だと、関数名に干渉する
    colorSwatchPickerView = UIPickerView.new()
    colorSwatchPickerView.dataSource = self
    #colorSwatchPickerView.delegate = self

    

    colorSwatchPickerView.backgroundColor = UIColor.systemDarkGreenColor()
    #pdbr.state(pickerView.dataSource)

    colorSwatchView = UIView.new()
    
    
    colorValue = 128
    foregroundColor = UIColor.colorWithRed_green_blue_alpha_(
      0.8, 0.5, 0.2, 1.0)

    # Set the foreground color for the entire attributed string.
    attributes = NSDictionary.dictionaryWithObject(
      foregroundColor, forKey=NSForegroundColorAttributeName)

    title = NSMutableAttributedString.alloc().initWithString_attributes_(
      f'{int(colorValue)}', attributes)

    
    #pdbr.state(title)
    #colorSwatchView.addSubview_(title)
    UILabel = ObjCClass('UILabel')
    testLabel = UILabel.new()
    testLabel.attributedText = title
    #pdbr.state(testLabel)
    colorSwatchView.addSubview_(testLabel)
    
    testLabel.translatesAutoresizingMaskIntoConstraints = False
    NSLayoutConstraint.activateConstraints_([
      testLabel.heightAnchor.constraintEqualToConstant_(161.0),
      testLabel.widthAnchor.constraintEqualToConstant_(183.0),
      testLabel.heightAnchor.constraintEqualToConstant_(32.0),
      testLabel.widthAnchor.constraintEqualToConstant_(32.0),
    ])
    
    colorSwatchView.backgroundColor = UIColor.systemDarkBlueColor()
    
    

    # --- Layout
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide
    layoutMarginsGuide = self.view.layoutMarginsGuide

    self.view.addSubview_(colorSwatchPickerView)
    colorSwatchPickerView.translatesAutoresizingMaskIntoConstraints = False
    self.view.addSubview_(colorSwatchView)
    colorSwatchView.translatesAutoresizingMaskIntoConstraints = False

    NSLayoutConstraint.activateConstraints_([
      colorSwatchPickerView.widthAnchor.constraintEqualToConstant_(375.0),
    ])

    NSLayoutConstraint.activateConstraints_([
      colorSwatchView.trailingAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.trailingAnchor, -20.0),
      colorSwatchView.topAnchor.constraintEqualToAnchor_constant_(
        colorSwatchPickerView.bottomAnchor, 8.0),
      colorSwatchView.bottomAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.bottomAnchor, -20.0),
      colorSwatchPickerView.centerXAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerXAnchor),
      colorSwatchPickerView.topAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.topAnchor, 13.0),
      colorSwatchView.leadingAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.leadingAnchor, 20.0),
    ])

    self.colorSwatchPickerView = colorSwatchPickerView
    self.colorSwatchView = colorSwatchView

    self.numberOfColorValuesPerComponent = int(RGB.max / RGB.offset) + 1

    self.redColor = RGB.min
    self.greenColor = RGB.min
    self.blueColor = RGB.min

    self.configurePickerView()

  @objc_method
  def updateColorSwatchViewBackgroundColor(self):
    self.colorSwatchView.backgroundColor = UIColor.colorWithRed_green_blue_alpha_(
      self.redColor, self.greenColor, self.blueColor, 1.0)

  @objc_method
  def configurePickerView(self):
    # Set the default selected rows (the desired rows to initially select will vary from app to app).
    # デフォルトの選択行を設定します (最初に選択する行はアプリによって異なります)。
    selectedRows = {
      ColorComponent.red: 13,
      ColorComponent.green: 41,
      ColorComponent.blue: 24,
    }
    
    pdbr.state(self.colorSwatchPickerView)

    for colorComponent, selectedRow in selectedRows.items():
      """
      Note that the delegate method on `UIPickerViewDelegate` is not triggered
      when manually calling `selectRow(_:inComponent:animated:)`. To do
      this, we fire off delegate method manually.
      """
      """
      `selectRow(_:inComponent:animated:)` を手動で呼び出した場合、`UIPickerViewDelegate` のデリゲート メソッドはトリガーされないことに注意してください。これを行うには、デリゲート メソッドを手動で起動します。
      """
      #print(colorComponent, ':', selectedRow)
      pass
      #selectRow_inComponent_animated_

  # MARK: - UIPickerViewDataSource
  @objc_method
  def numberOfComponentsInPickerView_(self, pickerView) -> int:
    return len(ColorComponent)

  @objc_method
  def pickerView_numberOfRowsInComponent_(self, component) -> int:
    return self.numberOfColorValuesPerComponent

  # MARK: - UIPickerViewDelegate
  @objc_method
  def pickerView_attributedTitleForRow_forComponent_(self, pickerView,
                                                     row: int, component: int)->ObjCInstance:
    #colorValue = row * RGB.offset
    colorValue = 128
    foregroundColor = UIColor.colorWithRed_green_blue_alpha_(
      0.8, 0.5, 0.2, 1.0)

    # Set the foreground color for the entire attributed string.
    attributes = NSDictionary.dictionaryWithObject(
      foregroundColor, forKey=NSForegroundColorAttributeName)

    title = NSMutableAttributedString.alloc().initWithString_attributes_(
      f'{int(colorValue)}', attributes)

    return title
    
  @objc_method
  def pickerView_didSelectRow_inComponent_(self, pickerView, row:int,component:int):
    print(component)

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

