"""
note: まずは参照してるのやりきってみる
ref: [Diffable DataSource 入門 #Swift - Qiita](https://qiita.com/maiyama18/items/28039293b4bbf886ce8e)
  - Diffable DataSource
"""

import ctypes

from pyrubicon.objc.api import ObjCClass, ObjCInstance, objc_method, Block
from pyrubicon.objc.runtime import send_super, objc_id
from pyrubicon.objc.types import CGRectMake, NSInteger

from rbedge.enumerations import UICollectionLayoutListAppearance
from rbedge.functions import NSStringFromClass

UIViewController = ObjCClass('UIViewController')
UICollectionView = ObjCClass('UICollectionView')
UICollectionViewCompositionalLayout = ObjCClass(
  'UICollectionViewCompositionalLayout')
UICollectionLayoutListConfiguration = ObjCClass(
  'UICollectionLayoutListConfiguration')
NSCollectionLayoutSection = ObjCClass('NSCollectionLayoutSection')

NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

CGRectZero = CGRectMake(0, 0, 0, 0)


class TodoListViewController(UIViewController):

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    # --- Navigation
    title = NSStringFromClass(__class__)
    self.navigationItem.title = title
    self.configureCollectionView()
    pdbr.state(self.collectionView)

  @objc_method
  def configureCollectionView(self):

    @Block
    def sectionProvider(sectionIndex: NSInteger,
                        layoutEnvironment: objc_id) -> ObjCInstance:
      _appearance = UICollectionLayoutListAppearance.plain
      configuration = UICollectionLayoutListConfiguration.alloc(
      ).initWithAppearance_(_appearance)
      return NSCollectionLayoutSection.sectionWithListConfiguration_layoutEnvironment_(
        configuration, layoutEnvironment)

    layout = UICollectionViewCompositionalLayout.alloc(
    ).initWithSectionProvider_(sectionProvider)
    self.collectionView = UICollectionView.alloc(
    ).initWithFrame_collectionViewLayout_(CGRectZero, layout)

    self.view.addSubview_(self.collectionView)
    # --- Layout
    self.collectionView.translatesAutoresizingMaskIntoConstraints = False

    NSLayoutConstraint.activateConstraints_([
      self.collectionView.leadingAnchor.constraintEqualToAnchor_(
        self.view.leadingAnchor),
      self.collectionView.trailingAnchor.constraintEqualToAnchor_(
        self.view.trailingAnchor),
      self.collectionView.topAnchor.constraintEqualToAnchor_(
        self.view.topAnchor),
      self.collectionView.bottomAnchor.constraintEqualToAnchor_(
        self.view.bottomAnchor),
    ])


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  todo_vc = TodoListViewController.new()
  style = UIModalPresentationStyle.fullScreen
  present_viewController(todo_vc, style)
  #print(CGRectZero)

