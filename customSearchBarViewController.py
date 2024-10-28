"""
todo:
  Storyboard 未対応
  xcode だと再現できず?
  `searchBar_selectedScopeButtonIndexDidChange_` は`searchBar` とバッティングする(?)ので、`objc_property` で宣言
    `TypeError: Don't know how to convert a pyrubicon.objc.api.ObjCBoundMethod to a Foundation object`
    こんなエラーになる
    `searchBar` という変数を別にすれば、解決するが、`objc_property` 宣言の方が正規ぽいので、そうする
"""

from pyrubicon.objc.api import ObjCClass, ObjCProtocol
from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.runtime import send_super, objc_id
from pyrubicon.objc.types import CGRectMake

from pyLocalizedString import localizedString
from rbedge.enumerations import UIControlState, UISearchBarIcon

from rbedge.functions import NSStringFromClass

UIViewController = ObjCClass('UIViewController')
UISearchBar = ObjCClass('UISearchBar')
UISearchBarDelegate = ObjCProtocol('UISearchBarDelegate')

UIColor = ObjCClass('UIColor')
UIImage = ObjCClass('UIImage')

NSLayoutConstraint = ObjCClass('NSLayoutConstraint')


class CustomSearchBarViewController(UIViewController,
                                    protocols=[UISearchBarDelegate]):

  searchBar = objc_property()

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    # --- Navigation
    title = NSStringFromClass(__class__)
    self.navigationItem.title = title

    self.searchBar = UISearchBar.alloc().init().autorelease()
    self.setlayout()
    self.configureSearchBar()

  @objc_method
  def setlayout(self):
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide
    # xxx: 仮置き
    self.searchBar.frame = CGRectMake(0.0, 0.0, 375.0, 56.0)
    self.searchBar.delegate = self
    self.view.addSubview_(self.searchBar)

    self.searchBar.translatesAutoresizingMaskIntoConstraints = False
    NSLayoutConstraint.activateConstraints_([
      self.searchBar.trailingAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.trailingAnchor),
      self.searchBar.topAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.topAnchor),
      self.searchBar.leadingAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.leadingAnchor),
    ])

  # MARK: - Configuration
  @objc_method
  def configureSearchBar(self):
    self.searchBar.showsCancelButton = True
    self.searchBar.showsScopeBar = True
    self.searchBar.setTintColor_(UIColor.systemPurpleColor())
    self.searchBar.backgroundImage = UIImage.systemImageNamed_(
      'search_bar_background')

    # Set the bookmark image for both normal and highlighted states.
    # しおり画像を通常状態とハイライト状態の両方に設定する。
    #setImage_forSearchBarIcon_state_

    bookImage = UIImage.systemImageNamed_('bookmark')
    self.searchBar.setImage_forSearchBarIcon_state_(bookImage,
                                                    UISearchBarIcon.bookmark,
                                                    UIControlState.normal)

    bookFillImage = UIImage.systemImageNamed_('bookmark.fill')
    self.searchBar.setImage_forSearchBarIcon_state_(bookFillImage,
                                                    UISearchBarIcon.bookmark,
                                                    UIControlState.highlighted)


  # MARK: - UISearchBarDelegate

  @objc_method
  def searchBarSearchButtonClicked_(self, searchBar):
    print(
      'The custom search bar keyboard "Search" button was tapped.'
    )
    searchBar.resignFirstResponder()

  @objc_method
  def searchBarCancelButtonClicked_(self, searchBar):
    print('The default search bar cancel button was tapped.')
    searchBar.resignFirstResponder()


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  sb_vc = CustomSearchBarViewController.new()
  style = UIModalPresentationStyle.fullScreen
  present_viewController(sb_vc, style)

