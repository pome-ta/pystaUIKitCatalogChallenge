"""
  note: Storyboard 実装なし
"""
import ctypes

from pyrubicon.objc.api import ObjCClass, ObjCInstance, Block
from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.runtime import send_super, objc_id, SEL
from pyrubicon.objc.types import CGRectMake

from rbedge.enumerations import (
  UIButtonType,
  UIControlState,
  UIControlEvents,
  UIUserInterfaceSizeClass,
  UIUserInterfaceIdiom,
  UIModalPresentationStyle,
  UIBarButtonItemStyle,
)
from rbedge.functions import NSStringFromClass

from rbedge import pdbr
from pyLocalizedString import localizedString

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')
UIColor = ObjCClass('UIColor')

UIColorPickerViewController = ObjCClass('UIColorPickerViewController')
UIColorWell = ObjCClass('UIColorWell')
UIView = ObjCClass('UIView')
UIAction = ObjCClass('UIAction')
UIBarButtonItem = ObjCClass('UIBarButtonItem')
UIButton = ObjCClass('UIButton')


class ColorPickerViewController(UIViewController):

  pickerWellView: UIView = objc_property()
  colorView: UIView = objc_property()
  colorPicker: UIColorPickerViewController = objc_property()

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t- {NSStringFromClass(__class__)}: dealloc')

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    
    # --- Navigation
    self.navigationItem.title = localizedString('ColorPickerTitle') if (
      title := self.navigationItem.title) is None else title
    self.view.backgroundColor = UIColor.systemBackgroundColor()

    # --- pickerBarButton
    pickerBarButton = UIBarButtonItem.alloc().initWithTitle(
      'Picker',
      style=UIBarButtonItemStyle.plain,
      target=self,
      action=SEL('presentColorPickerByBarButton:'))
    self.navigationItem.rightBarButtonItem = pickerBarButton

    # --- pickerButton
    pickerButton = UIButton.buttonWithType_(UIButtonType.system)
    pickerButton.setTitle_forState_('Picker', UIControlState.normal)
    pickerButton.addTarget_action_forControlEvents_(
      self, SEL('presentColorPickerByButton:'), UIControlEvents.touchUpInside)

    # --- pickerWellView
    pickerWellView = UIView.new()
    pickerWellView.backgroundColor = UIColor.systemBackgroundColor()

    # --- colorView
    colorView = UIView.new()
    colorView.backgroundColor = UIColor.systemBackgroundColor()

    # --- Layout
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide
    layoutMarginsGuide = self.view.layoutMarginsGuide

    self.view.addSubview_(colorView)
    colorView.translatesAutoresizingMaskIntoConstraints = False
    self.view.addSubview_(pickerButton)
    pickerButton.translatesAutoresizingMaskIntoConstraints = False
    self.view.addSubview_(pickerWellView)
    pickerWellView.translatesAutoresizingMaskIntoConstraints = False

    NSLayoutConstraint.activateConstraints_([
      colorView.heightAnchor.constraintEqualToConstant_(161.0),
      colorView.widthAnchor.constraintEqualToConstant_(183.0),
      pickerWellView.heightAnchor.constraintEqualToConstant_(32.0),
      pickerWellView.widthAnchor.constraintEqualToConstant_(32.0),
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

    self.pickerWellView = pickerWellView
    self.colorView = colorView
    self.configureColorPicker()
    self.configureColorWell()

    # For iOS, the picker button in the main view is not used, the color picker is presented from the navigation bar.
    if self.navigationController.traitCollection.userInterfaceIdiom != UIUserInterfaceIdiom.mac:
      pickerButton.setHidden_(True)

  @objc_method
  def viewWillAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    # print('viewWillAppear')

  @objc_method
  def viewDidAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    # print('viewDidAppear')

  @objc_method
  def viewWillDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    # print('viewWillDisappear')

  @objc_method
  def viewDidDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    # print('viewDidDisappear')

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'{__class__}: didReceiveMemoryWarning')

  # MARK: - UIColorWell
  # Update the color view from the color well chosen action.
  @objc_method
  def colorWellHandler_(self, _action: ctypes.c_void_p) -> None:
    action = ObjCInstance(_action)
    if (colorWell := action.sender).isKindOfClass_(UIColorWell):
      self.colorView.backgroundColor = colorWell.selectedColor

  @objc_method
  def configureColorWell(self):
    """
    Note: Both color well and picker buttons achieve the same thing, presenting the color picker.
          But one presents it with a color well control, the other by a bar button item.
    """
    """
    注: カラー ウェルとピッカー ボタンは両方とも同じことを実現し、カラー ピッカーを表示します。
    ただし、1 つはカラー ウェル コントロールで表示され、もう 1 つはバー ボタン項目で表示されます。
    """
    colorWellAction = UIAction.actionWithHandler_(
      Block(self.colorWellHandler_, None, ctypes.c_void_p))
    colorWell = UIColorWell.alloc().initWithFrame_primaryAction_(
      CGRectMake(0.0, 0.0, 32.0, 32.0), colorWellAction)

    # For Mac Catalyst, the UIColorWell is placed in the main view.
    if self.navigationController.traitCollection.userInterfaceIdiom == UIUserInterfaceIdiom.mac:
      self.pickerWellView.addSubview_(colorWell)
    else:
      # For iOS, the UIColorWell is placed inside the navigation bar as a UIBarButtonItem.
      colorWellBarItem = UIBarButtonItem.alloc().initWithCustomView_(colorWell)
      fixedBarItem = UIBarButtonItem.fixedSpaceItemOfWidth_(20.0)

      rightBarButtonItems = self.navigationItem.rightBarButtonItems
      self.navigationItem.setRightBarButtonItems_animated_([
        *rightBarButtonItems,
        fixedBarItem,
        colorWellBarItem,
      ], True)

  # MARK: - UIColorPickerViewController
  @objc_method
  def configureColorPicker(self):
    colorPicker = UIColorPickerViewController.new()
    colorPicker.supportsAlpha = True
    colorPicker.selectedColor = UIColor.blueColor
    colorPicker.delegate = self

    self.colorPicker = colorPicker

  # Present the color picker from the UIBarButtonItem, iOS only.
  # This will present it as a popover (preferred), or for compact mode as a modal sheet.
  @objc_method
  def presentColorPickerByBarButton_(self, sender):
    self.colorPicker.modalPresentationStyle = UIModalPresentationStyle.popover  # will display as popover for iPad or sheet for compact screens.
    popover = self.colorPicker.popoverPresentationController()
    popover.barButtonItem = sender

    self.presentViewController(self.colorPicker,
                               animated=True,
                               completion=None)

  # Present the color picker from the UIButton, Mac Catalyst only.
  # This will present it as a popover (preferred), or for compact mode as a modal sheet.
  @objc_method
  def presentColorPickerByButton_(self, sender):
    self.colorPicker.modalPresentationStyle = UIModalPresentationStyle.popover
    if (popover := self.colorPicker.popoverPresentationController()):
      popover.sourceView = sender
      self.presentViewController(self.colorPicker,
                                 animated=True,
                                 completion=None)

  # MARK: - UIColorPickerViewControllerDelegate
  # Color returned from the color picker via UIBarButtonItem - iOS 15.0
  # UIBarButtonItem 経由でカラーピッカーから返される色 - iOS 15.0
  # @available(iOS 15.0, *)
  @objc_method
  def colorPickerViewController_didSelectColor_continuously_(
      self, viewController, color, continuously: ctypes.c_bool):
    # User has chosen a color.
    chosenColor = viewController.selectedColor
    self.colorView.backgroundColor = chosenColor

    # Dismiss the color picker if the conditions are right:
    # 1) User is not doing a continous pick (tap and drag across multiple colors).
    # 2) Picker is presented on a non-compact device.
    #
    # Use the following check to determine how the color picker was presented (modal or popover).
    # For popover, we want to dismiss it when a color is locked.
    # For modal, the picker has a close button.
    """
    条件が正しい場合は、カラーピッカーを閉じます。
    1) ユーザーが連続的な選択 (複数の色をタップしてドラッグすること) を行っていない。
    2) ピッカーは非コンパクトなデバイス上で表示されます。
    
    次のチェックを使用して、カラー ピッカーがどのように表示されたか (モーダルまたはポップオーバー) を判断します。
    ポップオーバーの場合、色がロックされているときにポップオーバーを解除したいと考えています。
    モーダルの場合、ピッカーには閉じるボタンがあります。
    """
    if not continuously:
      if self.traitCollection.horizontalSizeClass != UIUserInterfaceSizeClass.compact:
        viewController.dismissViewControllerAnimated_completion_(
          True, Block(lambda: print(f'{chosenColor}'), None))

  # Color returned from the color picker - iOS 14.x and earlier.
  # カラー ピッカーから返された色 - iOS 14.x 以前。
  @objc_method
  def colorPickerViewControllerDidSelectColor_(self, viewController):
    # xxx: `colorPickerViewController_didSelectColor_continuously_` が実行されたら、呼ばれない（よきこと？）
    # User has chosen a color.
    # chosenColor = viewController.selectedColor
    # self.colorView.backgroundColor = chosenColor
    # Use the following check to determine how the color picker was presented (modal or popover).
    # For popover, we want to dismiss it when a color is locked.
    # For modal, the picker has a close button.
    """
    次のチェックを使用して、カラー ピッカーがどのように表示されたか (モーダルまたはポップオーバー) を判断します。
    ポップオーバーの場合、色がロックされているときにポップオーバーを解除したいと考えています。
    モーダルの場合、ピッカーには閉じるボタンがあります。
    """
    if self.traitCollection.horizontalSizeClass != UIUserInterfaceSizeClass.compact:
      viewController.dismissViewControllerAnimated_completion_(
        True, Block(lambda: print(f'{chosenColor}'), None))

  @objc_method
  def colorPickerViewControllerDidFinish_(self, viewController):
    """
    In presentations (except popovers) the color picker shows a close button. If the close button is tapped,
    the view controller is dismissed and `colorPickerViewControllerDidFinish:` is called. Can be used to
    animate alongside the dismissal.
    """
    """
    プレゼンテーション (ポップオーバーを除く) では、カラー ピッカーに閉じるボタンが表示されます。
    閉じるボタンがタップされると、ビュー コントローラーが閉じられ、`colorPickerViewControllerDidFinish:` が呼び出されます。
    解雇と同時にアニメーション化するために使用できます。
    """
    pass


if __name__ == '__main__':
  from rbedge.app import App

  from rbedge.enumerations import UIModalPresentationStyle

  main_vc = ColorPickerViewController.new()
  _title = NSStringFromClass(ColorPickerViewController)
  main_vc.navigationItem.title = _title

  #presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc)
  app.main_loop(presentation_style)

