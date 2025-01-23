"""
  note: Storyboard 実装なし
"""
import ctypes

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, objc_id

from rbedge.enumerations import (
  UIControlState,
  UISearchBarIcon,
)
from rbedge.pythonProcessUtils import (
  mainScreen_scale,
  dataWithContentsOfURL,
)

from rbedge import pdbr

from pyLocalizedString import localizedString

UIViewController = ObjCClass('UIViewController')
UIColor = ObjCClass('UIColor')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UISearchBar = ObjCClass('UISearchBar')
UIScreen = ObjCClass('UIScreen')
UIImage = ObjCClass('UIImage')


class CustomSearchBarViewController(UIViewController):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    #print('\tdealloc')
    pass

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    # --- Navigation
    self.navigationItem.title = localizedString('CustomSearchBarTitle') if (
      title := self.navigationItem.title) is None else title
    self.view.backgroundColor = UIColor.systemBackgroundColor()

    searchBarView = UISearchBar.new()
    searchBarView.delegate = self

    # --- Layout
    searchBarView.translatesAutoresizingMaskIntoConstraints = False
    self.view.addSubview_(searchBarView)

    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide
    NSLayoutConstraint.activateConstraints_([
      searchBarView.trailingAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.trailingAnchor),
      searchBarView.topAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.topAnchor),
      searchBarView.leadingAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.leadingAnchor),
    ])

    self.searchBarView = searchBarView
    self.configureSearchBar()

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
  def viewWillDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print('viewWillDisappear')

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

  # MARK: - Configuration
  @objc_method
  def configureSearchBar(self):
    self.searchBarView.showsCancelButton = True
    self.searchBarView.showsBookmarkButton = True
    self.searchBarView.setTintColor_(UIColor.systemPurpleColor())

    scale = int(mainScreen_scale)

    search_bar_background_str = './UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/search_bar_background.imageset/search_bar_background_3x.png'

    self.searchBarView.backgroundImage = UIImage.alloc().initWithData_scale_(
      dataWithContentsOfURL(search_bar_background_str), scale)

    # Set the bookmark image for both normal and highlighted states.
    # しおり画像を通常状態とハイライト状態の両方に設定する。
    #setImage_forSearchBarIcon_state_

    bookImage = UIImage.systemImageNamed_('bookmark')
    self.searchBarView.setImage_forSearchBarIcon_state_(
      bookImage, UISearchBarIcon.bookmark, UIControlState.normal)

    bookFillImage = UIImage.systemImageNamed_('bookmark.fill')
    self.searchBarView.setImage_forSearchBarIcon_state_(
      bookFillImage, UISearchBarIcon.bookmark, UIControlState.highlighted)

  # MARK: - UISearchBarDelegate

  @objc_method
  def searchBarSearchButtonClicked_(self, searchBar):
    print('The custom search bar keyboard "Search" button was tapped.')
    searchBar.resignFirstResponder()

  @objc_method
  def searchBarCancelButtonClicked_(self, searchBar):
    print('The custom search bar "Cancel" button was tapped.')
    searchBar.resignFirstResponder()

  @objc_method
  def searchBarBookmarkButtonClicked_(self, searchBar):
    print('The custom "bookmark button" inside the search bar was tapped.')


if __name__ == '__main__':
  from rbedge.functions import NSStringFromClass
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController

  main_vc = CustomSearchBarViewController.new()
  _title = NSStringFromClass(CustomSearchBarViewController)
  main_vc.navigationItem.title = _title

  presentation_style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, presentation_style)

