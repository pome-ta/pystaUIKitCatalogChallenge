'''
  note: Storyboard 実装なし
'''
import ctypes

from pyrubicon.objc.api import ObjCClass, ObjCInstance, Block
from pyrubicon.objc.api import objc_method, objc_const
from pyrubicon.objc.runtime import send_super, objc_id, SEL
from pyrubicon.objc.types import CGRectMake

from rbedge.enumerations import (
  UIButtonType,
  UIControlState,
  UILayoutConstraintAxis,
  NSTextAlignment,
  NSLineBreakMode,
)

from rbedge import pdbr
from pyLocalizedString import localizedString

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')
UIColor = ObjCClass('UIColor')

UIFontPickerViewController = ObjCClass('UIFontPickerViewController')
UITextFormattingCoordinator = ObjCClass('UITextFormattingCoordinator')

UIButton = ObjCClass('UIButton')
UILabel = ObjCClass('UILabel')
UIFont = ObjCClass('UIFont')


class FontPickerViewController(UIViewController):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    #print('\tdealloc')
    pass

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    self.navigationItem.title = localizedString('FontPickerTitle') if (
      title := self.navigationItem.title) is None else title
    self.view.backgroundColor = UIColor.systemBackgroundColor()

    # --- fontPickerButton
    fontPickerButton = UIButton.buttonWithType_(UIButtonType.system)
    fontPickerButton.setTitle('UIFontPickerViewController',
                              forState=UIControlState.normal)

    # --- textFormatterButton
    textFormatterButton = UIButton.buttonWithType_(UIButtonType.system)
    textFormatterButton.setTitle('UITextFormattingCoordinator',
                                 forState=UIControlState.normal)

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
    # todo: 確認用
    fontLabel.backgroundColor = UIColor.systemDarkPurpleColor()

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

  main_vc = FontPickerViewController.new()
  _title = NSStringFromClass(FontPickerViewController)
  main_vc.navigationItem.title = _title

  presentation_style = UIModalPresentationStyle.fullScreen
  #presentation_style = UIModalPresentationStyle.pageSheet
  present_viewController(main_vc, presentation_style)

