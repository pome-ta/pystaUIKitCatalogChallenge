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
)
from rbedge.pythonProcessUtils import dataWithContentsOfURL

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
UIActivityViewController = ObjCClass('UIActivityViewController')


class TintedToolbarViewController(UIViewController):

  toolbar: UIToolbar = objc_property()
  navigationContainer: UINavigationController = objc_property()

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t- {NSStringFromClass(__class__)}: dealloc')
    #self.navigationController.setToolbarHidden_animated_(True, True)

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

    # --- toolbarAppearance setup
    toolbarAppearance = UIToolbarAppearance.new()
    toolbarAppearance.configureWithDefaultBackground()
    #toolbarAppearance.configureWithOpaqueBackground()
    #toolbarAppearance.configureWithTransparentBackground()
    toolbarAppearance.setBackgroundColor_(UIColor.systemBlueColor())

    # xxx: 変数化してあげた方が、表示速度速い?
    toolbar = navigationContainer.toolbar

    toolbar.standardAppearance = toolbarAppearance
    toolbar.scrollEdgeAppearance = toolbarAppearance
    toolbar.compactAppearance = toolbarAppearance
    toolbar.compactScrollEdgeAppearance = toolbarAppearance

    toolbar.setTintColor_(UIColor.systemGreenColor())
    #toolbar.setBackgroundColor_(UIColor.systemBlueColor())

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
    self.navigationItem.title = localizedString('TintedToolbarTitle') if (
      title := self.navigationItem.title) is None else title

    self.view.backgroundColor = UIColor.systemBackgroundColor()

    # See the `UIBarStyle` enum for more styles, including `.Default`.
    self.toolbar.setBarStyle_(UIBarStyle.black)
    self.toolbar.setTranslucent_(False)

    # MARK: - `UIBarButtonItem` Creation and Configuration
    refreshBarButtonItem = UIBarButtonItem.alloc().initWithBarButtonSystemItem(
      UIBarButtonSystemItem.refresh,
      target=self,
      action=SEL('barButtonItemClicked:'))

    # Note that there's no target/action since this represents empty space.
    flexibleSpaceBarButtonItem = UIBarButtonItem.alloc(
    ).initWithBarButtonSystemItem(UIBarButtonSystemItem.flexibleSpace,
                                  target=None,
                                  action=None)

    actionBarButtonItem = UIBarButtonItem.alloc().initWithBarButtonSystemItem(
      UIBarButtonSystemItem.action,
      target=self,
      action=SEL('actionBarButtonItemClicked:'))

    toolbarButtonItems = [
      refreshBarButtonItem,
      flexibleSpaceBarButtonItem,
      actionBarButtonItem,
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

  @objc_method
  def actionBarButtonItemClicked_(self, barButtonItem):
    image_path = './UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/Flowers_1.imageset/Flowers_1.png'
    if (image :=
        UIImage.alloc().initWithData_(dataWithContentsOfURL(image_path))):
      activityItems = [
        'Shared piece of text',
        image,
      ]
      activityViewController = UIActivityViewController.alloc(
      ).initWithActivityItems_applicationActivities_(activityItems, None)
      if (popoverPresentationController :=
          activityViewController.popoverPresentationController()) is not None:
        # xxx: 挙動未確認
        popoverPresentationController.barButtonItem = barButtonItem
      self.presentViewController(activityViewController,
                                 animated=True,
                                 completion=None)


if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import UIModalPresentationStyle

  main_vc = TintedToolbarViewController.new()
  _title = NSStringFromClass(TintedToolbarViewController)
  main_vc.navigationItem.title = _title

  #presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

