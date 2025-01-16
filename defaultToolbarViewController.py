'''
  note: Storyboard 実装なし
'''
import ctypes

from pyrubicon.objc.api import ObjCClass, ObjCInstance, Block
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, objc_id, SEL

from rbedge.enumerations import (
  UIBarButtonSystemItem, )

from rbedge import pdbr

from pyLocalizedString import localizedString

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')
UIColor = ObjCClass('UIColor')

UIToolbar = ObjCClass('UIToolbar')
UIToolbarAppearance = ObjCClass('UIToolbarAppearance')
UIBarButtonItem = ObjCClass('UIBarButtonItem')
UIImage = ObjCClass('UIImage')
UIMenu = ObjCClass('UIMenu')
UIAction = ObjCClass('UIAction')


class DefaultToolbarViewController(UIViewController):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    #print('\tdealloc')
    pass

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    self.navigationItem.title = localizedString('DefaultToolBarTitle') if (
      title := self.navigationItem.title) is None else title

    self.view.backgroundColor = UIColor.systemBackgroundColor()

    _navToolbar = self.navigationController.toolbar
    toolbar = UIToolbar.alloc().initWithFrame_(_navToolbar.frame)
    toolbar.setAutoresizingMask_(_navToolbar.autoresizingMask)

    toolbarAppearance = UIToolbarAppearance.new()
    toolbarAppearance.configureWithDefaultBackground()
    #toolbarAppearance.configureWithOpaqueBackground()
    #toolbarAppearance.configureWithTransparentBackground()

    toolbar.standardAppearance = toolbarAppearance
    toolbar.scrollEdgeAppearance = toolbarAppearance
    toolbar.compactAppearance = toolbarAppearance
    toolbar.compactScrollEdgeAppearance = toolbarAppearance

    self.navigationController.setToolbar_(toolbar)

    # MARK: - UIBarButtonItem Creation and Configuration
    trashBarButtonItem = UIBarButtonItem.alloc().initWithBarButtonSystemItem(
      UIBarButtonSystemItem.trash,
      target=self,
      action=SEL('barButtonItemClicked:'))

    flexibleSpaceBarButtonItem = UIBarButtonItem.alloc(
    ).initWithBarButtonSystemItem(UIBarButtonSystemItem.flexibleSpace,
                                  target=None,
                                  action=None)

    buttonMenu = UIMenu.menuWithTitle_children_('', [
      UIAction.actionWithTitle_image_identifier_handler_(
        f'Option {i + 1}', None, None,
        Block(self.menuHandler_, None, ctypes.c_void_p)) for i in range(5)
    ])
    customTitleBarButtonItem = UIBarButtonItem.alloc().initWithImage_menu_(
      UIImage.systemImageNamed('list.number'), buttonMenu)

    toolbarButtonItems = [
      trashBarButtonItem,
      flexibleSpaceBarButtonItem,
      customTitleBarButtonItem,
    ]
    self.setToolbarItems_animated_(toolbarButtonItems, True)
    self.navigationController.setToolbarHidden_animated_(False, True)

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

  @objc_method
  def menuHandler_(self, _action: ctypes.c_void_p) -> None:
    action = ObjCInstance(_action)
    print(f'Menu Action "{action.title}"')

  # MARK: - Actions
  @objc_method
  def barButtonItemClicked_(self, barButtonItem):
    print(
      f'A bar button item on the default toolbar was clicked: {barButtonItem}.'
    )


if __name__ == '__main__':
  from rbedge.functions import NSStringFromClass
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController

  main_vc = DefaultToolbarViewController.new()
  _title = NSStringFromClass(DefaultToolbarViewController)
  main_vc.navigationItem.title = _title

  presentation_style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, presentation_style)

