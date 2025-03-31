"""
  note: Storyboard 未定義
"""
import ctypes

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.runtime import send_super
from pyrubicon.objc.types import CGRect

from rbedge.enumerations import (
  UIViewAutoresizing,
  UIViewContentMode,
)
from rbedge.pythonProcessUtils import dataWithContentsOfURL

from pyLocalizedString import localizedString

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UIImageView = ObjCClass('UIImageView')
UIImage = ObjCClass('UIImage')
NSURL = ObjCClass('NSURL')
UIToolTipInteraction = ObjCClass('UIToolTipInteraction')

UIColor = ObjCClass('UIColor')


class ImageViewController(UIViewController):

  imageView: UIImage = objc_property()

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t - {NSStringFromClass(__class__)}: dealloc')
    #pass

  @objc_method
  def loadView(self):
    send_super(__class__, self, 'loadView')
    #print(f'\t{NSStringFromClass(__class__)}: loadView')

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    #print(f'\t{NSStringFromClass(__class__)}: viewDidLoad')
    self.navigationItem.title = localizedString('ImageViewTitle') if (
      title := self.navigationItem.title) is None else title

    self.view.backgroundColor = UIColor.systemBackgroundColor()

    imageView = UIImageView.alloc().init()

    # --- Layout
    self.view.addSubview_(imageView)
    imageView.translatesAutoresizingMaskIntoConstraints = False
    #areaLayoutGuide = self.view.safeAreaLayoutGuide
    areaLayoutGuide = self.view
    NSLayoutConstraint.activateConstraints_([
      imageView.centerXAnchor.constraintEqualToAnchor_(
        areaLayoutGuide.centerXAnchor),
      imageView.centerYAnchor.constraintEqualToAnchor_(
        areaLayoutGuide.centerYAnchor),
      imageView.widthAnchor.constraintEqualToAnchor_multiplier_(
        areaLayoutGuide.widthAnchor, 1.0),
      imageView.heightAnchor.constraintEqualToAnchor_multiplier_(
        areaLayoutGuide.heightAnchor, 1.0),
    ])

    self.imageView = imageView
    self.configureImageView()

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
  def configureImageView(self):
    # The root view of the view controller is set in Interface Builder and is an UIImageView.
    # ビュー コントローラーのルート ビューは Interface Builder で設定され、UIImageView です。
    # todo: 上記コメントと実装方法が違う。`self.imageView` は`self.view` で`addSubview_` してる。
    if (imageView := self.imageView).isKindOfClass_(UIImageView):
      # xxx: `lambda` の使い方が悪い
      flowers_str = lambda index: f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/Flowers_{index}.imageset/Flowers_{index}.png'

      # Fetch the images (each image is of the format Flowers_number).
      self.imageView.animationImages = [
        UIImage.alloc().initWithData_scale_(
          dataWithContentsOfURL(flowers_str(i)), 1) for i in range(1, 3)
      ]
      # We want the image to be scaled to the correct aspect ratio within imageView's bounds.
      self.imageView.contentMode = UIViewContentMode.scaleAspectFit

      self.imageView.animationDuration = 5
      self.imageView.startAnimating()

      self.imageView.isAccessibilityElement = True
      self.imageView.accessibilityLabel = localizedString('Animated')

      if True:  # wip: `available(iOS 15, *)`
        interaction = UIToolTipInteraction.alloc().initWithDefaultToolTip_(
          localizedString('ImageToolTipTitle'))
        self.imageView.addInteraction_(interaction)


if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import UIModalPresentationStyle

  main_vc = ImageViewController.new()
  _title = NSStringFromClass(ImageViewController)
  main_vc.navigationItem.title = _title

  #presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

