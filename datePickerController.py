"""
  note: Storyboard 実装なし
"""
import ctypes

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method, objc_property
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
from rbedge.functions import NSStringFromClass
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

UILabel = ObjCClass('UILabel')
UIFont = ObjCClass('UIFont')


class DatePickerController(UIViewController):

  dateFormatter: NSDateFormatter = objc_property()
  datePicker: UIDatePicker = objc_property()
  dateLabel: UILabel = objc_property()

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t- {NSStringFromClass(__class__)}: dealloc')

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    self.navigationItem.title = localizedString('DatePickerTitle') if (
      title := self.navigationItem.title) is None else title
    self.view.backgroundColor = UIColor.systemBackgroundColor()

    # A date formatter to format the `date` property of `datePicker`.
    # xxx: 関数化すると落ちる(かも?な)ので、ここに展開
    dateFormatter = NSDateFormatter.new()
    dateFormatter.setDateStyle_(NSDateFormatterStyle.medium)
    dateFormatter.setTimeStyle_(NSDateFormatterStyle.short)

    datePicker = UIDatePicker.new()
    # todo: Default
    datePicker.setDatePickerMode_(UIDatePickerMode.dateAndTime)
    datePicker.setMinuteInterval_(1)
    datePicker.setContentHorizontalAlignment_(
      UIControlContentHorizontalAlignment.center)
    datePicker.setContentVerticalAlignment_(
      UIControlContentVerticalAlignment.center)

    dateLabel = UILabel.new()
    dateLabel.setContentHuggingPriority_forAxis_(
      251.0, UILayoutConstraintAxis.horizontal)
    dateLabel.setContentHuggingPriority_forAxis_(
      251.0, UILayoutConstraintAxis.vertical)
    dateLabel.text = 'Label'
    dateLabel.textAlignment = NSTextAlignment.center
    dateLabel.lineBreakMode = NSLineBreakMode.byTruncatingTail
    dateLabel.font = UIFont.systemFontOfSize_(17.0)
    dateLabel.textColor = UIColor.secondaryLabelColor()

    if True:  # wip: `available(iOS 15, *)`
      # In case the label's content is too large to fit inside the label (causing truncation),
      # use this to reveal the label's full text drawn as a tool tip.
      dateLabel.showsExpansionTextWhenTruncated = True

    # --- Layout
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide
    layoutMarginsGuide = self.view.layoutMarginsGuide

    self.view.addSubview_(datePicker)
    datePicker.translatesAutoresizingMaskIntoConstraints = False
    # xxx: `datePicker.centerYAnchor` が画面全体を取ってる模様で中心ではないが、表記の通りに実装
    NSLayoutConstraint.activateConstraints_([
      datePicker.centerYAnchor.constraintEqualToAnchor_(
        self.view.centerYAnchor),
      datePicker.centerXAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerXAnchor),
    ])

    self.view.addSubview_(dateLabel)
    dateLabel.translatesAutoresizingMaskIntoConstraints = False
    NSLayoutConstraint.activateConstraints_([
      dateLabel.topAnchor.constraintEqualToAnchor_constant_(
        datePicker.bottomAnchor, 19.0),
      dateLabel.leadingAnchor.constraintEqualToAnchor_(
        layoutMarginsGuide.leadingAnchor),
      dateLabel.trailingAnchor.constraintEqualToAnchor_(
        layoutMarginsGuide.trailingAnchor),
    ])

    self.dateFormatter = dateFormatter
    self.datePicker = datePicker
    self.dateLabel = dateLabel

    self.configureDatePicker()

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

    # xxx: `dateComponents` 使わない、、、？
    dateComponents = NSDateComponents.new()
    dateComponents.day = 7

    sevenDaysFromNow = NSCalendar.currentCalendar.dateByAddingUnit(
      NSCalendarUnit.day, value=7, toDate=now, options=0)
    self.datePicker.maximumDate = sevenDaysFromNow
    self.datePicker.minuteInterval = 2

    self.datePicker.addTarget(self,
                              action=SEL('updateDatePickerLabel'),
                              forControlEvents=UIControlEvents.valueChanged)
    self.updateDatePickerLabel()

  @objc_method  # override
  def traitCollectionDidChange_(self, previousTraitCollection):
    # xxx: iOS 17 からはDeprecated
    # note: [iOS 17 からの画面サイズ変化への対応方法](https://zenn.dev/matsuei/articles/a9143244622d01)
    # ref: [traitCollectionDidChange: | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitraitenvironment/traitcollectiondidchange(_:)?language=objc)
    # ref: [registerForTraitChanges:withHandler: | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitraitchangeobservable-7qoet/registerfortraitchanges:withhandler:?language=objc)
    send_super(__class__,
               self,
               'traitCollectionDidChange:',
               previousTraitCollection,
               argtypes=[
                 objc_id,
               ])
    # Adjust the date picker style due to the trait collection's vertical size.
    self.datePicker.preferredDatePickerStyle = UIDatePickerStyle.compact if self.traitCollection.verticalSizeClass == UIUserInterfaceSizeClass.compact else UIDatePickerStyle.inline

  # MARK: - Actions
  @objc_method
  def updateDatePickerLabel(self):
    # todo: `print` でも呼び出すので、変数化
    _date_text = self.dateFormatter.stringFromDate_(self.datePicker.date)
    self.dateLabel.text = _date_text

    print(f'Chosen date: {_date_text}')


if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import UIModalPresentationStyle

  main_vc = DatePickerController.new()
  _title = NSStringFromClass(DatePickerController)
  main_vc.navigationItem.title = _title

  #presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

