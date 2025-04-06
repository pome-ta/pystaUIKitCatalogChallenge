"""
  note: Storyboard 実装なし
"""
import ctypes

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.runtime import send_super, SEL

from rbedge.enumerations import (
  UIBarStyle,
  UIBarButtonSystemItem,
  UIBarPosition,
  UIBarMetrics,
  UIBarButtonItemStyle,
  UIControlState,
)
from rbedge.globalVariables import NSAttributedStringKey
from rbedge.pythonProcessUtils import (
  mainScreen_scale,
  dataWithContentsOfURL,
)

from pyLocalizedString import localizedString

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')
UIColor = ObjCClass('UIColor')

UINavigationController = ObjCClass('UINavigationController')

UIToolbar = ObjCClass('UIToolbar')  # todo: 型
UIToolbarAppearance = ObjCClass('UIToolbarAppearance')
UIBarButtonItem = ObjCClass('UIBarButtonItem')
UIImage = ObjCClass('UIImage')
NSDictionary = ObjCClass('NSDictionary')


class CustomToolbarViewController(UIViewController):

  toolbar: UIToolbar = objc_property()
  navigationContainer: UINavigationController = objc_property()

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def loadView(self):
    send_super(__class__, self, 'loadView')
    #print(f'\t{NSStringFromClass(__class__)}: loadView')

    # --- navigationContainer
    navigationContainer = UINavigationController.alloc(
    ).initWithNavigationBarClass_toolbarClass_(None, None)
    # todo: `setToolbarHidden` は先に指定
    # xxx: `setItems` 後だと、items 出てこない
    navigationContainer.setNavigationBarHidden_(True)
    navigationContainer.setToolbarHidden_animated_(False, True)

    scale = int(mainScreen_scale)

    image_path = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/toolbar_background.imageset/toolbar_background_{scale}x.png'

    toolbarBackgroundImage = UIImage.alloc().initWithData_scale_(
      dataWithContentsOfURL(image_path), scale)

    # --- toolbarAppearance setup
    toolbarAppearance = UIToolbarAppearance.new()
    toolbarAppearance.configureWithDefaultBackground()
    #toolbarAppearance.configureWithOpaqueBackground()
    #toolbarAppearance.configureWithTransparentBackground()

    toolbarAppearance.setBackgroundImage_(toolbarBackgroundImage)

    # xxx: 変数化してあげた方が、表示速度速い?
    toolbar = navigationContainer.toolbar

    toolbar.standardAppearance = toolbarAppearance
    toolbar.scrollEdgeAppearance = toolbarAppearance
    toolbar.compactAppearance = toolbarAppearance
    toolbar.compactScrollEdgeAppearance = toolbarAppearance

    self.addChildViewController_(navigationContainer)
    self.view.addSubview_(navigationContainer.view)
    navigationContainer.didMoveToParentViewController_(self)

    self.toolbar = toolbar
    self.navigationContainer = navigationContainer

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    #print(f'\t{NSStringFromClass(__class__)}: viewDidLoad')

    # --- Navigation
    self.navigationItem.title = localizedString('CustomToolbarBarTitle') if (
      title := self.navigationItem.title) is None else title

    self.view.backgroundColor = UIColor.systemBackgroundColor()

    # xxx: ? `toolbar` からは変化が確認できない
    # toolbar.setShadowImage_forToolbarPosition_(toolbarBackgroundImage, UIBarPosition.any)
    # toolbar.setBackgroundImage_forToolbarPosition_barMetrics_(toolbarBackgroundImage, UIBarPosition.bottom, UIBarMetrics.default)

    # MARK: - `UIBarButtonItem` Creation and Configuration
    customBarButtonItemImage = UIImage.systemImageNamed_(
      'exclamationmark.triangle')
    customImageBarButtonItem = UIBarButtonItem.alloc().initWithImage(
      customBarButtonItemImage,
      style=UIBarButtonItemStyle.plain,
      target=self,
      action=SEL('barButtonItemClicked:'))
    customImageBarButtonItem.tintColor = UIColor.systemPurpleColor()

    # Note that there's no target/action since this represents empty space.
    flexibleSpaceBarButtonItem = UIBarButtonItem.alloc(
    ).initWithBarButtonSystemItem(UIBarButtonSystemItem.flexibleSpace,
                                  target=None,
                                  action=None)

    customBarButtonItem = UIBarButtonItem.alloc().initWithTitle(
      localizedString('Button'),
      style=UIBarButtonItemStyle.plain,
      target=self,
      action=SEL('barButtonItemClicked:'))
    attributes = NSDictionary.dictionaryWithObject(
      UIColor.systemPurpleColor(),
      forKey=NSAttributedStringKey.foregroundColor)
    customBarButtonItem.setTitleTextAttributes_forState_(
      attributes, UIControlState.normal)

    toolbarButtonItems = [
      customImageBarButtonItem,
      flexibleSpaceBarButtonItem,
      customBarButtonItem,
    ]
    self.toolbar.setItems_animated_(toolbarButtonItems, True)

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
    self.navigationContainer.setToolbarHidden_animated_(True, True)

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

  # MARK: - Actions
  @objc_method
  def barButtonItemClicked_(self, barButtonItem):
    print(
      f'A bar button item on the tinted toolbar was clicked: {barButtonItem}.')


if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import UIModalPresentationStyle

  main_vc = CustomToolbarViewController.new()
  _title = NSStringFromClass(CustomToolbarViewController)
  main_vc.navigationItem.title = _title

  #presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

