"""
todo:
  Storyboard 未対応
  xcode だと再現できず？
"""

from pyrubicon.objc.api import ObjCClass, ObjCProtocol
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, objc_id
from pyrubicon.objc.types import CGRectMake

from pyLocalizedString import localizedString

from rbedge.functions import NSStringFromClass

UIViewController = ObjCClass('UIViewController')
UISearchBar = ObjCClass('UISearchBar')
UISearchBarDelegate = ObjCProtocol('UISearchBarDelegate')

NSLayoutConstraint = ObjCClass('NSLayoutConstraint')


class DefaultSearchBarViewController(UIViewController,
                                     protocols=[UISearchBarDelegate]):

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    # --- Navigation
    title = NSStringFromClass(__class__)
    self.navigationItem.title = title

    self.searchBar = UISearchBar.alloc().init().autorelease()
    self.setuptolayout()
    self.configureSearchBar()

  @objc_method
  def setuptolayout(self):
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide
    # xxx: 仮置き
    self.searchBar.frame = CGRectMake(0.0, 0.0, 375.0, 56.0)
    self.searchBar.delegate = self
    #pdbr.state(self.searchBar)
    #print(self.searchBar)
    pdbr.state(self)
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

    self.searchBar.scopeButtonTitles = [
      localizedString('Scope One'),
      localizedString('Scope Two'),
    ]
    #pdbr.state(self.searchBar)
    

  # MARK: - UISearchBarDelegate
  '''
  @objc_method
  def searchBar_selectedScopeButtonIndexDidChange_(self, searchBar,
                                                   selectedScope:int):
    pass
  '''
  
  

  @objc_method
  def searchBarSearchButtonClicked_(self, searchBar):
    print(
      f'The default search bar keyboard search button was tapped: {searchBar.text}.'
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

  sb_vc = DefaultSearchBarViewController.new()
  style = UIModalPresentationStyle.fullScreen
  present_viewController(sb_vc, style)

