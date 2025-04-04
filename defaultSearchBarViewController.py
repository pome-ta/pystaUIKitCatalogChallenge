"""
  note: Storyboard 実装なし
"""
import ctypes

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.runtime import send_super, objc_id

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

from pyLocalizedString import localizedString

UIViewController = ObjCClass('UIViewController')
UIColor = ObjCClass('UIColor')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UISearchBar = ObjCClass('UISearchBar')


class DefaultSearchBarViewController(UIViewController):

  searchBarView: UISearchBar = objc_property()

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    #print(f'\t{NSStringFromClass(__class__)}: viewDidLoad')
    
    # --- Navigation
    self.navigationItem.title = localizedString('DefaultSearchBarTitle') if (
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

  # MARK: - Configuration
  @objc_method
  def configureSearchBar(self):
    self.searchBarView.showsCancelButton = True
    self.searchBarView.showsScopeBar = True

    self.searchBarView.scopeButtonTitles = [
      localizedString('Scope One'),
      localizedString('Scope Two'),
    ]

  # MARK: - UISearchBarDelegate
  @objc_method
  def searchBar_selectedScopeButtonIndexDidChange_(self, searchBar,
                                                   selectedScope: int):
    print(
      f'The default search selected scope button index changed to {selectedScope}.'
    )

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
  from rbedge.app import App
  from rbedge.enumerations import UIModalPresentationStyle

  main_vc = DefaultSearchBarViewController.new()
  _title = NSStringFromClass(DefaultSearchBarViewController)
  main_vc.navigationItem.title = _title

  #presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

