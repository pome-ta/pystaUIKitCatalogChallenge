import ctypes

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, SEL

from .lifeCycle import loop
from .enumerations import (
  UIRectEdge,
  UIBarButtonSystemItem,
)
#from .functions import NSStringFromClass
from . import pdbr

UINavigationController = ObjCClass('UINavigationController')
UIBarButtonItem = ObjCClass('UIBarButtonItem')


class RootNavigationController(UINavigationController):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    #print(f'- {NSStringFromClass(__class__)}: dealloc')
    loop.stop()

  @objc_method
  def loadView(self):
    send_super(__class__, self, 'loadView')
    #print(f'{NSStringFromClass(__class__)}: loadView')

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    #print(f'{NSStringFromClass(__class__)}: viewDidLoad')
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
    #print(f'{NSStringFromClass(__class__)}: viewWillAppear_')

  @objc_method
  def viewDidAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print(f'{NSStringFromClass(__class__)}: viewDidAppear_')
    #print('↓ ---')

  @objc_method
  def viewWillDisappear_(self, animated: bool):
    #print('↑ ---')
    send_super(__class__,
               self,
               'viewWillDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print(f'{NSStringFromClass(__class__)}: viewWillDisappear_')

  @objc_method
  def viewDidDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print(f'{NSStringFromClass(__class__)}: viewDidDisappear_')

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'{NSStringFromClass(__class__)}: didReceiveMemoryWarning')

  @objc_method
  def doneButtonTapped_(self, sender):
    #print('doneButtonTapped: start')
    '''
    @Block
    def completion() -> None:
      print('block: doneButtonTapped')
    '''

    #visibleViewController = self.visibleViewController
    #visibleViewController.dismissViewControllerAnimated_completion_(True, completion)
    #pdbr.state(self)
    #self.dismissViewControllerAnimated_completion_(True, completion)
    self.dismissViewControllerAnimated_completion_(True, None)
    #print('doneButtonTapped: end')

  @objc_method
  def navigationController_willShowViewController_animated_(
      self, navigationController, viewController, animated: bool):
    # xxx: layout 範囲の制限
    #extendedLayout = UIRectEdge.none
    #viewController.setEdgesForExtendedLayout_(extendedLayout)

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

