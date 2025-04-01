"""
  note: Storyboard 実装なし
"""
import ctypes

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.runtime import send_super, SEL

from rbedge.enumerations import (
  UIButtonType,
  UIControlState,
  UIControlEvents,
  UILayoutConstraintAxis,
  NSTextAlignment,
  NSLineBreakMode,
  UIUserInterfaceIdiom,
  UIFontDescriptorSymbolicTraits,
  UIModalPresentationStyle,
)

from rbedge.globalVariables import NSAttributedStringKey
from rbedge.functions import NSStringFromClass
from rbedge import pdbr

from pyLocalizedString import localizedString

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')
UIColor = ObjCClass('UIColor')

UIFontPickerViewController = ObjCClass('UIFontPickerViewController')
UIFontPickerViewControllerConfiguration = ObjCClass(
  'UIFontPickerViewControllerConfiguration')
UITextFormattingCoordinator = ObjCClass('UITextFormattingCoordinator')

UIButton = ObjCClass('UIButton')
UILabel = ObjCClass('UILabel')
NSDictionary = ObjCClass('NSDictionary')
UIFont = ObjCClass('UIFont')


class FontPickerViewController(UIViewController):

  fontLabel: UILabel = objc_property()
  textFormatter: UITextFormattingCoordinator = objc_property()
  fontPicker: UIFontPickerViewController = objc_property()

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
    self.navigationItem.title = localizedString('FontPickerTitle') if (
      title := self.navigationItem.title) is None else title
    self.view.backgroundColor = UIColor.systemBackgroundColor()

    # --- fontPickerButton
    fontPickerButton = UIButton.buttonWithType_(UIButtonType.system)
    fontPickerButton.setTitle('UIFontPickerViewController',
                              forState=UIControlState.normal)
    fontPickerButton.addTarget_action_forControlEvents_(
      self, SEL('presentFontPicker:'), UIControlEvents.touchUpInside)

    # --- textFormatterButton
    textFormatterButton = UIButton.buttonWithType_(UIButtonType.system)
    textFormatterButton.setTitle('UITextFormattingCoordinator',
                                 forState=UIControlState.normal)
    textFormatterButton.addTarget_action_forControlEvents_(
      self, SEL('presentTextFormattingCoordinator:'),
      UIControlEvents.touchUpInside)

    # --- fontLabel
    fontLabel = UILabel.new()
    fontLabel.setContentHuggingPriority_forAxis_(
      251.0, UILayoutConstraintAxis.horizontal)
    fontLabel.setContentHuggingPriority_forAxis_(
      251.0, UILayoutConstraintAxis.vertical)
    fontLabel.textAlignment = NSTextAlignment.center
    fontLabel.lineBreakMode = NSLineBreakMode.byTruncatingTail
    fontLabel.font = UIFont.systemFontOfSize_(28.0)

    fontLabel.text = localizedString('SampleFontTitle')

    self.view.addSubview_(fontPickerButton)
    fontPickerButton.translatesAutoresizingMaskIntoConstraints = False
    self.view.addSubview_(textFormatterButton)
    textFormatterButton.translatesAutoresizingMaskIntoConstraints = False
    self.view.addSubview_(fontLabel)
    fontLabel.translatesAutoresizingMaskIntoConstraints = False

    # --- Layout
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide
    layoutMarginsGuide = self.view.layoutMarginsGuide

    NSLayoutConstraint.activateConstraints_([
      fontLabel.heightAnchor.constraintEqualToConstant_(62.0),
    ])

    NSLayoutConstraint.activateConstraints_([
      textFormatterButton.centerXAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerXAnchor),
      fontPickerButton.centerXAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerXAnchor),
      textFormatterButton.topAnchor.constraintEqualToAnchor_constant_(
        fontPickerButton.bottomAnchor, 8.0),
      fontLabel.leadingAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.leadingAnchor, 16.0),
      fontPickerButton.topAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.topAnchor, 17.0),
      fontLabel.trailingAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.trailingAnchor, -16.0),
      fontLabel.topAnchor.constraintEqualToAnchor_constant_(
        textFormatterButton.bottomAnchor, 20.0),
    ])

    self.fontLabel = fontLabel
    self.configureFontPicker()

    if self.navigationController.traitCollection.userInterfaceIdiom != UIUserInterfaceIdiom.mac:
      # UITextFormattingCoordinator's toggleFontPanel is available only for macOS.
      textFormatterButton.setHidden_(True)

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
  def configureFontPicker(self):
    configuration = UIFontPickerViewControllerConfiguration.new()
    configuration.includeFaces = True
    configuration.displayUsingSystemFont = False
    """
      xxx: 以下がピックアップされてる？
        - UIFontDescriptorClassOldStyleSerifs
        - UIFontDescriptorClassTransitionalSerifs
        - UIFontDescriptorClassModernSerifs
        - UIFontDescriptorClassSlabSerifs
        - UIFontDescriptorClassFreeformSerifs
        - UIFontDescriptorClassOrnamentals
        - UIFontDescriptorClassScripts
    """
    configuration.filteredTraits = UIFontDescriptorSymbolicTraits.classModernSerifs

    fontPicker = UIFontPickerViewController.alloc().initWithConfiguration_(
      configuration)
    fontPicker.delegate = self
    fontPicker.modalPresentationStyle = UIModalPresentationStyle.popover

    self.fontPicker = fontPicker

  @objc_method
  def configureTextFormatter(self):
    # xxx: `UITextFormattingCoordinator` 検証不可のため、未確認
    if self.textFormatter is None:
      if (scene := self.view.window().windowScene) is None:
        return
      attributes = NSDictionary.dictionaryWithObject(
        self.fontLabel.font, forKey=NSAttributedStringKey.font)

      textFormatter = UITextFormattingCoordinator.alloc().initWithWindowScene_(
        scene)
      textFormatter.delegate = self
      textFormatter.setSelectedAttributes_isMultiple_(attributes, True)

      self.textFormatter = textFormatter

  @objc_method
  def presentFontPicker_(self, sender):
    if (button := sender).isKindOfClass_(UIButton):
      popover = self.fontPicker.popoverPresentationController()
      popover.sourceView = button
      self.presentViewController(self.fontPicker,
                                 animated=True,
                                 completion=None)

  @objc_method
  def presentTextFormattingCoordinator_(self, sender):
    # xxx: `UITextFormattingCoordinator` 検証不可のため、未確認
    if not UITextFormattingCoordinator.isFontPanelVisible():
      UITextFormattingCoordinator.toggleFontPanel_(sender)

  # MARK: - UIFontPickerViewControllerDelegate
  @objc_method
  def fontPickerViewControllerDidCancel_(self, viewController):
    pass

  @objc_method
  def fontPickerViewControllerDidPickFont_(self, viewController):
    if (fontDescriptor := viewController.selectedFontDescriptor) is None:
      return
    else:
      font = UIFont.fontWithDescriptor_size_(fontDescriptor, 28.0)
      self.fontLabel.font = font

  # MARK: - UITextFormattingCoordinatorDelegate
  @objc_method
  def updateTextAttributesWithConversionHandler_(self, conversionHandler):
    # xxx: `UITextFormattingCoordinator` 検証不可のため、未確認
    print(conversionHandler)


if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import UIModalPresentationStyle

  main_vc = FontPickerViewController.new()
  _title = NSStringFromClass(FontPickerViewController)
  main_vc.navigationItem.title = _title

  #presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

