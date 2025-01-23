import ctypes

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, SEL

from .enumerations import (
  UIRectEdge,
  UIBarButtonSystemItem,
)
from . import pdbr

# --- UINavigationController
UINavigationController = ObjCClass('UINavigationController')
UINavigationBarAppearance = ObjCClass('UINavigationBarAppearance')
UIToolbarAppearance = ObjCClass('UIToolbarAppearance')
UIBarButtonItem = ObjCClass('UIBarButtonItem')


class RootNavigationController(UINavigationController):
  
  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    # print('\tdealloc')
    pass
  
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    # self.initNavigationBarAppearance()
    self.delegate = self
  
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
  
  @objc_method
  def initNavigationBarAppearance(self):
    navigationBarAppearance = UINavigationBarAppearance.new()
    navigationBarAppearance.configureWithDefaultBackground()
    
    navigationBar = self.navigationBar
    navigationBar.standardAppearance = navigationBarAppearance
    navigationBar.scrollEdgeAppearance = navigationBarAppearance
    navigationBar.compactAppearance = navigationBarAppearance
    navigationBar.compactScrollEdgeAppearance = navigationBarAppearance
  
  @objc_method
  def initToolbarAppearance(self):
    toolbarAppearance = UIToolbarAppearance.new()
    toolbarAppearance.configureWithDefaultBackground()
    # toolbarAppearance.configureWithOpaqueBackground()
    # toolbarAppearance.configureWithTransparentBackground()
    
    toolbar = self.toolbar
    toolbar.standardAppearance = toolbarAppearance
    toolbar.scrollEdgeAppearance = toolbarAppearance
    toolbar.compactAppearance = toolbarAppearance
    toolbar.compactScrollEdgeAppearance = toolbarAppearance
  
  @objc_method
  def doneButtonTapped_(self, sender):
    visibleViewController = self.visibleViewController
    visibleViewController.dismissViewControllerAnimated_completion_(True, None)
  
  @objc_method
  def navigationController_willShowViewController_animated_(
      self, navigationController, viewController, animated: bool):
    # xxx: layout 範囲の制限
    # extendedLayout = UIRectEdge.none
    # viewController.setEdgesForExtendedLayout_(extendedLayout)
    
    closeButtonItem = UIBarButtonItem.alloc().initWithBarButtonSystemItem(
      UIBarButtonSystemItem.close,
      target=navigationController,
      action=SEL('doneButtonTapped:'))
    # todo: view 遷移でのButton 重複を判別
    closeButtonItem.setTag_(UIBarButtonSystemItem.close)
    
    visibleViewController = navigationController.visibleViewController
    
    navigationItem = visibleViewController.navigationItem
    if (rightBarButtonItems := navigationItem.rightBarButtonItems):
      # todo: `UIViewController` で、`rightBarButtonItem` が存在していた場合、`closeButtonItem` を右端に
      setRightBarButtonItems = [
        closeButtonItem,
        *[
          item for item in rightBarButtonItems
          if item.tag != UIBarButtonSystemItem.close
        ],
      ]
      navigationItem.setRightBarButtonItems_animated_(setRightBarButtonItems,
                                                      True)
    else:
      navigationItem.rightBarButtonItem = closeButtonItem
