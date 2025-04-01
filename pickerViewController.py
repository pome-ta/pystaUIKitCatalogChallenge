"""
  note: Storyboard 実装なし
"""
import ctypes
from enum import IntEnum, auto

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.runtime import send_super, objc_id
from pyrubicon.objc.types import NSInteger

from rbedge.globalVariables import NSAttributedStringKey

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

from pyLocalizedString import localizedString

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')
UIColor = ObjCClass('UIColor')
NSDictionary = ObjCClass('NSDictionary')

UIPickerView = ObjCClass('UIPickerView')
UIView = ObjCClass('UIView')
NSMutableAttributedString = ObjCClass('NSMutableAttributedString')


class RGB:
  max: float = 255.0
  min: float = 0.0
  offset: float = 5.0


class ColorComponent(IntEnum):
  red = 0
  green = auto()
  blue = auto()


class PickerViewController(UIViewController):

  colorSwatchPickerView: UIPickerView = objc_property()
  colorSwatchView: UIView = objc_property()
  numberOfColorValuesPerComponent: NSInteger = objc_property()
  redColor: float = objc_property()
  greenColor: float = objc_property()
  blueColor: float = objc_property()
  mutableAttributedString: NSMutableAttributedString = objc_property()

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t- {NSStringFromClass(__class__)}: dealloc')

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    #print(f'\t{NSStringFromClass(__class__)}: viewDidLoad')

    # --- Navigation
    self.navigationItem.title = localizedString('PickerViewTitle') if (
      title := self.navigationItem.title) is None else title
    self.view.backgroundColor = UIColor.systemBackgroundColor()

    # --- pickerView
    # todo: 変数名`pickerView` だと、関数名に干渉する
    colorSwatchPickerView = UIPickerView.new()
    colorSwatchPickerView.dataSource = self
    colorSwatchPickerView.delegate = self

    # --- colorSwatchView
    colorSwatchView = UIView.new()

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

    # todo: `pickerView_attributedTitleForRow_forComponent_` 内で定義すると落ちる
    self.mutableAttributedString = NSMutableAttributedString.alloc()

    self.configurePickerView()

  @objc_method
  def viewWillAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print(f'\t{NSStringFromClass(__class__)}: viewWillAppear_')

  @objc_method
  def viewDidAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print(f'\t{NSStringFromClass(__class__)}: viewDidAppear_')

  @objc_method
  def viewWillDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    # print(f'\t{NSStringFromClass(__class__)}: viewWillDisappear_')

  @objc_method
  def viewDidDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    print(f'\t{NSStringFromClass(__class__)}: viewDidDisappear_')

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'{__class__}: didReceiveMemoryWarning')

  @objc_method
  def updateColorSwatchViewBackgroundColor(self):
    self.colorSwatchView.backgroundColor = UIColor.colorWithRed_green_blue_alpha_(
      self.redColor.floatValue, self.greenColor.floatValue,
      self.blueColor.floatValue, 1.0)

  @objc_method
  def configurePickerView(self):
    # Set the default selected rows (the desired rows to initially select will vary from app to app).
    # デフォルトの選択行を設定します (最初に選択する行はアプリによって異なります)。
    selectedRows = {
      ColorComponent.red: 13,
      ColorComponent.green: 41,
      ColorComponent.blue: 24,
    }

    for colorComponent, selectedRow in selectedRows.items():
      """
      Note that the delegate method on `UIPickerViewDelegate` is not triggered
      when manually calling `selectRow(_:inComponent:animated:)`. To do
      this, we fire off delegate method manually.
      """
      """
      `selectRow(_:inComponent:animated:)` を手動で呼び出した場合、`UIPickerViewDelegate` のデリゲート メソッドはトリガーされないことに注意してください。これを行うには、デリゲート メソッドを手動で起動します。
      """
      self.colorSwatchPickerView.selectRow_inComponent_animated_(
        selectedRow, int(colorComponent), True)
      self.pickerView(self.colorSwatchPickerView,
                      didSelectRow=selectedRow,
                      inComponent=int(colorComponent))

  # MARK: - UIPickerViewDataSource
  @objc_method
  def numberOfComponentsInPickerView_(self, pickerView) -> NSInteger:
    return len(ColorComponent)

  @objc_method
  def pickerView_numberOfRowsInComponent_(self, component) -> NSInteger:
    return self.numberOfColorValuesPerComponent.intValue

  # MARK: - UIPickerViewDelegate

  @objc_method
  def pickerView_attributedTitleForRow_forComponent_(self, pickerView,
                                                     row: int, component: int):
    colorValue = row * RGB.offset
    # Set the initial colors for each picker segment.
    value = colorValue / RGB.max
    redColorComponent = RGB.min
    greenColorComponent = RGB.min
    blueColorComponent = RGB.min

    if component == ColorComponent.red:
      redColorComponent = value
    if component == ColorComponent.green:
      greenColorComponent = value
    if component == ColorComponent.blue:
      blueColorComponent = value

    if redColorComponent < 0.5:
      redColorComponent = 0.5
    if blueColorComponent < 0.5:
      blueColorComponent = 0.5
    if greenColorComponent < 0.5:
      greenColorComponent = 0.5

    foregroundColor = UIColor.colorWithRed_green_blue_alpha_(
      redColorComponent, greenColorComponent, blueColorComponent, 1.0)
    # Set the foreground color for the entire attributed string.
    attributes = NSDictionary.dictionaryWithObjects_forKeys_([
      foregroundColor,
    ], [
      NSAttributedStringKey.foregroundColor,
    ])

    title = self.mutableAttributedString.initWithString_attributes_(
      f'{int(colorValue)}', attributes)
    return title

  @objc_method
  def pickerView_didSelectRow_inComponent_(self, pickerView, row: int,
                                           component: int):
    colorComponentValue = RGB.offset * row / RGB.max
    if component == ColorComponent.red:
      self.redColor = colorComponentValue
    if component == ColorComponent.green:
      self.greenColor = colorComponentValue
    if component == ColorComponent.blue:
      self.blueColor = colorComponentValue
    self.updateColorSwatchViewBackgroundColor()

  # MARK: - UIPickerViewAccessibilityDelegate
  def pickerView_accessibilityLabelForComponent_(self, pickerView,
                                                 component: int) -> objc_id:
    if component == ColorComponent.red:
      return localizedString('Red color component value')
    if component == ColorComponent.green:
      return localizedString('Green color component value')
    if component == ColorComponent.blue:
      return localizedString('Blue color component value')


if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import UIModalPresentationStyle

  main_vc = PickerViewController.new()
  _title = NSStringFromClass(PickerViewController)
  main_vc.navigationItem.title = _title

  #presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

