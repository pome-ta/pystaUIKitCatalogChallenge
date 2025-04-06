"""
  note: Storyboard 実装なし
"""
import ctypes

from pyrubicon.objc.api import ObjCClass, ObjCInstance, Block
from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.runtime import send_super, SEL

from rbedge.enumerations import UIBarButtonSystemItem
from rbedge.globalVariables import NSAttributedStringKey

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
UIMenu = ObjCClass('UIMenu')
UIAction = ObjCClass('UIAction')


class DefaultToolbarViewController(UIViewController):

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
    # xxx: `setItems` 後だと、items 出てこない
    navigationContainer.setNavigationBarHidden_(True)
    navigationContainer.setToolbarHidden_animated_(False, True)

    self.addChildViewController_(navigationContainer)
    self.view.addSubview_(navigationContainer.view)
    navigationContainer.didMoveToParentViewController_(self)

    # xxx: 変数化してあげた方が、表示速度速い?
    self.toolbar = navigationContainer.toolbar
    self.navigationContainer = navigationContainer

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    # --- Navigation
    self.navigationItem.title = localizedString('DefaultToolBarTitle') if (
      title := self.navigationItem.title) is None else title

    self.view.backgroundColor = UIColor.systemBackgroundColor()

    # --- toolbarAppearance setup
    toolbarAppearance = UIToolbarAppearance.new()
    toolbarAppearance.configureWithDefaultBackground()
    #toolbarAppearance.configureWithOpaqueBackground()
    #toolbarAppearance.configureWithTransparentBackground()

    self.toolbar.standardAppearance = toolbarAppearance
    self.toolbar.scrollEdgeAppearance = toolbarAppearance
    self.toolbar.compactAppearance = toolbarAppearance
    self.toolbar.compactScrollEdgeAppearance = toolbarAppearance

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
    #print(f'\t{NSStringFromClass(__class__)}: viewWillDisappear_')
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
  from rbedge.app import App
  from rbedge.enumerations import UIModalPresentationStyle

  main_vc = DefaultToolbarViewController.new()
  _title = NSStringFromClass(DefaultToolbarViewController)
  main_vc.navigationItem.title = _title

  #presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

