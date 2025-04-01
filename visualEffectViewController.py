"""
  note: Storyboard 実装なし
"""
import ctypes

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, objc_id

from rbedge.enumerations import (
  UIBlurEffectStyle,
  UIFontDescriptorSymbolicTraits,
  UILayoutConstraintAxis,
)
from rbedge.globalVariables import UIFontTextStyle
from rbedge.pythonProcessUtils import dataWithContentsOfURL

from pyLocalizedString import localizedString

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')
UIColor = ObjCClass('UIColor')

UIImageView = ObjCClass('UIImageView')
UIImage = ObjCClass('UIImage')
UIToolTipInteraction = ObjCClass('UIToolTipInteraction')

UIVisualEffectView = ObjCClass('UIVisualEffectView')
UIBlurEffect = ObjCClass('UIBlurEffect')
UITextView = ObjCClass('UITextView')
UIFont = ObjCClass('UIFont')
UIFontDescriptor = ObjCClass('UIFontDescriptor')


class VisualEffectViewController(UIViewController):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def loadView(self):
    send_super(__class__, self, 'loadView')
    #print(f'\t{NSStringFromClass(__class__)}: loadView')

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    #print(f'\t{NSStringFromClass(__class__)}: viewDidLoad')
    
    # --- Navigation
    self.navigationItem.title = localizedString('VisualEffectTitle') if (
      title := self.navigationItem.title) is None else title
    self.view.backgroundColor = UIColor.systemBackgroundColor()

    image_path = './UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/Flowers_2.imageset/Flowers_2.png'

    imageReference = UIImage.alloc().initWithData_(
      dataWithContentsOfURL(image_path))
    imageView = UIImageView.alloc().initWithImage_(imageReference)
    imageView.setContentHuggingPriority_forAxis_(
      251.0, UILayoutConstraintAxis.horizontal)
    imageView.setContentHuggingPriority_forAxis_(
      251.0, UILayoutConstraintAxis.vertical)

    # xxx: 関数で返すと落ちるので
    visualEffect = UIVisualEffectView.alloc().initWithEffect_(
      UIBlurEffect.effectWithStyle_(UIBlurEffectStyle.regular))
    visualEffect.translatesAutoresizingMaskIntoConstraints = False

    # xxx: 関数で返すと落ちるので
    textView = UITextView.new()
    textView.setFont_(UIFont.systemFontOfSize_(14.0))
    textView.setText_(localizedString('VisualEffectTextContent'))
    textView.translatesAutoresizingMaskIntoConstraints = False
    textView.backgroundColor = UIColor.clearColor
    if (fontDescriptor :=
        UIFontDescriptor.preferredFontDescriptorWithTextStyle_(
          UIFontTextStyle.body).fontDescriptorWithSymbolicTraits_(
            UIFontDescriptorSymbolicTraits.traitLooseLeading)):
      looseLeadingFont = UIFont.fontWithDescriptor_size_(fontDescriptor, 0.0)
      textView.setFont_(looseLeadingFont)

    # --- Layout
    layoutMarginsGuide = self.view.layoutMarginsGuide
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide

    self.view.addSubview_(imageView)
    imageView.translatesAutoresizingMaskIntoConstraints = False
    NSLayoutConstraint.activateConstraints_([
      imageView.heightAnchor.constraintEqualToConstant_(215.0),
      imageView.widthAnchor.constraintEqualToConstant_(343.0),
      imageView.centerXAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerXAnchor),
      imageView.centerYAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerYAnchor),
    ])

    self.view.addSubview_(visualEffect)
    visualEffect.translatesAutoresizingMaskIntoConstraints = False
    NSLayoutConstraint.activateConstraints_([
      visualEffect.topAnchor.constraintEqualToAnchor_(imageView.topAnchor),
      visualEffect.leadingAnchor.constraintEqualToAnchor_(
        imageView.leadingAnchor),
      visualEffect.trailingAnchor.constraintEqualToAnchor_(
        imageView.trailingAnchor),
      visualEffect.bottomAnchor.constraintEqualToAnchor_(
        imageView.bottomAnchor),
    ])

    self.view.addSubview_(textView)
    textView.translatesAutoresizingMaskIntoConstraints = False
    NSLayoutConstraint.activateConstraints_([
      textView.topAnchor.constraintEqualToAnchor_(
        visualEffect.safeAreaLayoutGuide.topAnchor),
      textView.leadingAnchor.constraintEqualToAnchor_(
        visualEffect.safeAreaLayoutGuide.leadingAnchor),
      textView.trailingAnchor.constraintEqualToAnchor_(
        visualEffect.safeAreaLayoutGuide.trailingAnchor),
      textView.bottomAnchor.constraintEqualToAnchor_(
        visualEffect.safeAreaLayoutGuide.bottomAnchor),
    ])

    if True:  # wip: `available(iOS 15, *)`
      # Use UIToolTipInteraction which is available on iOS 15 or later, add it to the image view.
      toolTipString = localizedString('VisualEffectToolTipTitle')
      interaction = UIToolTipInteraction.alloc().initWithDefaultToolTip_(
        toolTipString)
      imageView.addInteraction_(interaction)

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
    print(f'\t{NSStringFromClass(__class__)}: didReceiveMemoryWarning')


if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import UIModalPresentationStyle

  main_vc = VisualEffectViewController.new()
  _title = NSStringFromClass(VisualEffectViewController)
  main_vc.navigationItem.title = _title

  #presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

