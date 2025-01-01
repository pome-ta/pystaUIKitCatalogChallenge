'''
  note: Storyboard 実装なし
'''
import ctypes
from pathlib import Path

from pyrubicon.objc.api import ObjCClass, ObjCInstance, Block, NSData
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, objc_id, SEL

from rbedge.enumerations import (
  UIBarStyle,
  UIBarButtonSystemItem,
)

from rbedge import pdbr

from pyLocalizedString import localizedString

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')
UIColor = ObjCClass('UIColor')

UIBarButtonItem = ObjCClass('UIBarButtonItem')
NSURL = ObjCClass('NSURL')
UIImage = ObjCClass('UIImage')
UIScreen = ObjCClass('UIScreen')


class CustomToolbarViewController(UIViewController):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    #print('\tdealloc')
    pass

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    self.navigationItem.title = localizedString('CustomToolbarBarTitle') if (
      title := self.navigationItem.title) is None else title

    self.view.backgroundColor = UIColor.systemBackgroundColor()

    scale = int(UIScreen.mainScreen.scale)
    #initWithData_scale_
    # xxx: `lambda` の使い方が悪い
    dataWithContentsOfURL = lambda path_str: NSData.dataWithContentsOfURL_(
      NSURL.fileURLWithPath_(str(Path(path_str).absolute())))

    image_path = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/toolbar_background.imageset/toolbar_background_{scale}x.png'

    toolbarBackgroundImage = UIImage.alloc().initWithData_scale_(
      dataWithContentsOfURL(image_path), scale)
    pdbr.state(self.navigationController.toolbar)
    #setBackgroundImage_forToolbarPosition_barMetrics_
    
    '''
    image_path = './UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/Flowers_1.imageset/Flowers_1.png'
    self.navigationController.toolbar.setBarStyle_(UIBarStyle.black)
    self.navigationController.toolbar.setTranslucent_(False)
    self.navigationController.toolbar.setTintColor_(UIColor.systemGreenColor())
    self.navigationController.toolbar.setBackgroundColor_(
      UIColor.systemBlueColor())

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
    self.setToolbarItems_animated_(toolbarButtonItems, True)
    '''
    self.navigationController.setToolbarHidden_(False)

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

  # MARK: - Actions
  @objc_method
  def barButtonItemClicked_(self, barButtonItem):
    print(
      f'A bar button item on the tinted toolbar was clicked: {barButtonItem}.')

  @objc_method
  def actionBarButtonItemClicked_(self, barButtonItem):
    # xxx: `lambda` の使い方が悪い
    dataWithContentsOfURL = lambda path_str: NSData.dataWithContentsOfURL_(
      NSURL.fileURLWithPath_(str(Path(path_str).absolute())))

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
  from rbedge.functions import NSStringFromClass
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController

  main_vc = CustomToolbarViewController.new()
  _title = NSStringFromClass(CustomToolbarViewController)
  main_vc.navigationItem.title = _title

  presentation_style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, presentation_style)

