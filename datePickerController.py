'''
  note: Storyboard 実装なし
'''
import ctypes

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method, objc_const
from pyrubicon.objc.runtime import send_super, objc_id

from rbedge.enumerations import (
  UIDatePickerMode,
  UIControlContentHorizontalAlignment,
  UIControlContentVerticalAlignment,
  UIUserInterfaceSizeClass,
  UIDatePickerStyle,
  NSDateFormatterStyle,
  NSCalendarUnit,
)

from rbedge import pdbr
from pyLocalizedString import localizedString

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')
UIColor = ObjCClass('UIColor')

UIDatePicker = ObjCClass('UIDatePicker')
NSDate = ObjCClass('NSDate')
NSDateFormatter = ObjCClass('NSDateFormatter')
NSDateComponents = ObjCClass('NSDateComponents')
NSCalendar = ObjCClass('NSCalendar')


class DatePickerController(UIViewController):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    #print('\tdealloc')
    pass

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    self.navigationItem.title = localizedString('DatePickerTitle') if (
      title := self.navigationItem.title) is None else title
    self.view.backgroundColor = UIColor.systemBackgroundColor()

    datePicker = UIDatePicker.new()
    # todo: Default
    datePicker.setDatePickerMode_(UIDatePickerMode.dateAndTime)
    datePicker.setMinuteInterval_(1)
    datePicker.setContentHorizontalAlignment_(
      UIControlContentHorizontalAlignment.center)
    datePicker.setContentVerticalAlignment_(
      UIControlContentVerticalAlignment.center)

    # todo: 確認用
    datePicker.setBackgroundColor_(UIColor.systemDarkPurpleColor())

    # --- Layout
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide

    self.view.addSubview_(datePicker)
    datePicker.translatesAutoresizingMaskIntoConstraints = False
    NSLayoutConstraint.activateConstraints_([
      datePicker.centerXAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerXAnchor),
      datePicker.centerYAnchor.constraintEqualToAnchor_(
        self.view.centerYAnchor),
    ])

    self.datePicker = datePicker
    self.configureDatePicker()

  # MARK: - Configuration
  @objc_method
  def configureDatePicker(self):
    self.datePicker.datePickerMode = UIDatePickerMode.dateAndTime

    # Set min/max date for the date picker. As an example we will limit the date between now and 7 days from now.
    # 日付ピッカーの最小/最大日付を設定します。例として、日付を現在から 7 日後までに制限します。
    now = NSDate.now()  # todo: `new()` 、`alloc().init()` と同義
    self.datePicker.minimumDate = now
    # Decide the best date picker style based on the trait collection's vertical size.
    # 特性コレクションの垂直サイズに基づいて、最適な日付ピッカー スタイルを決定します。
    self.datePicker.preferredDatePickerStyle = UIDatePickerStyle.compact if self.traitCollection.verticalSizeClass == UIUserInterfaceSizeClass.compact else UIDatePickerStyle.inline

    # A date formatter to format the `date` property of `datePicker`.
    # xxx: 関数化すると落ちるので、ここに展開
    dateFormatter = NSDateFormatter.new()
    dateFormatter.setDateStyle_(NSDateFormatterStyle.medium)
    dateFormatter.setTimeStyle_(NSDateFormatterStyle.short)
    
    dateComponents = NSDateComponents.new()
    dateComponents.day = 7
    
    #pdbr.state(NSCalendar.currentCalendar)
    sevenDaysFromNow = NSCalendar.currentCalendar.dateByAddingUnit_value_toDate_options_(NSCalendarUnit.day, 7, now, None)
    #pdbr.state(sevenDaysFromNow)
    
    

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

  main_vc = DatePickerController.new()
  _title = NSStringFromClass(DatePickerController)
  main_vc.navigationItem.title = _title

  presentation_style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, presentation_style)

