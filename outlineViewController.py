"""
note: まずは参照してるのやりきってみる
ref: [Diffable DataSource 入門 #Swift - Qiita](https://qiita.com/maiyama18/items/28039293b4bbf886ce8e)
  - Diffable DataSource
"""

import ctypes
from enum import IntEnum, auto

from pyrubicon.objc.api import ObjCClass, ObjCInstance, objc_method, objc_property, Block
from pyrubicon.objc.runtime import send_super, objc_id
from pyrubicon.objc.types import CGRectMake, NSInteger

from rbedge.enumerations import UICollectionLayoutListAppearance
from rbedge.functions import NSStringFromClass

# --- layout
UIViewController = ObjCClass('UIViewController')
UICollectionView = ObjCClass('UICollectionView')
UICollectionViewCompositionalLayout = ObjCClass(
  'UICollectionViewCompositionalLayout')
UICollectionLayoutListConfiguration = ObjCClass(
  'UICollectionLayoutListConfiguration')

# --- cell
UICollectionViewCellRegistration = ObjCClass(
  'UICollectionViewCellRegistration')
#UICollectionViewCell = ObjCClass('UICollectionViewCell')
UICollectionViewListCell = ObjCClass('UICollectionViewListCell')
UICellAccessoryCheckmark = ObjCClass('UICellAccessoryCheckmark')
NSIndexPath = ObjCClass('NSIndexPath')

# --- dataSource
UICollectionViewDiffableDataSource = ObjCClass(
  'UICollectionViewDiffableDataSource')

NSDiffableDataSourceSnapshot = ObjCClass('NSDiffableDataSourceSnapshot')

NSUUID = ObjCClass('NSUUID')
NSCollectionLayoutSection = ObjCClass('NSCollectionLayoutSection')

NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

CGRectZero = CGRectMake(0, 0, 0, 0)


class Todo:

  def __init__(self, id: NSUUID, title: str, done: bool):
    self.id = id
    self.title = title
    self.done = done

  @property
  def ID(self):
    return self.id


class Section(IntEnum):
  main = 0


class TodoRepository:

  def __init__(self):
    self.todos = [Todo(NSUUID.UUID(), f'Todo #{i}', False) for i in range(30)]
    self.todoIDs = [_todo.id for _todo in self.todos]

  def todo(self, id: Todo.ID) -> Todo:
    for _todo in self.todos:
      if id == _todo.id:
        return _todo


class TodoListViewController(UIViewController):

  @objc_method
  def viewDidLoad(self):
    #
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    # --- Navigation
    title = NSStringFromClass(__class__)
    self.navigationItem.title = title

    # xxx: 宣言する場所
    self.repository = TodoRepository()

    self.configureCollectionView()
    self.configureDataSource()
    self.applySnapshot()

  @objc_method
  def configureCollectionView(self):

    @Block
    def sectionProvider(sectionIndex: NSInteger,
                        layoutEnvironment: objc_id) -> objc_id:
      print('Block: sectionProvider')
      # xxx: `sectionIndex`, 'NSInteger' ? `objc_id` ? `int` ?
      _appearance = UICollectionLayoutListAppearance.plain
      configuration = UICollectionLayoutListConfiguration.alloc(
      ).initWithAppearance_(_appearance)

      layoutSection = NSCollectionLayoutSection.sectionWithListConfiguration_layoutEnvironment_(
        configuration, ObjCInstance(layoutEnvironment))
      #pdbr.state(layoutSection)
      return layoutSection

    layout = UICollectionViewCompositionalLayout.alloc(
    ).initWithSectionProvider_(ObjCInstance(sectionProvider))
    #pdbr.state(layout)
    

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

  @objc_method
  def configureDataSource(self):

    @Block
    def configurationHandler(cell: ObjCInstance, indexPath: ObjCInstance,
                             item: objc_id) -> None:
      print('Block: configurationHandler')
      configuration = cell.defaultContentConfiguration()
      configuration.setText_(item.title)
      cell.setContentConfiguration_(configuration)
      # xxx: UICellAccessoryCheckmark enum 確認
      cell.setAccessories_([
        UICellAccessoryCheckmark.alloc().init(),
      ])

    todoCellRegistration = UICollectionViewCellRegistration.registrationWithCellClass_configurationHandler_(
      UICollectionViewListCell, configurationHandler)

    @Block
    def cellProvider(collectionView: ObjCInstance, indexPath: ObjCInstance,
                     itemIdentifier: objc_id) -> ObjCInstance:
      print('Block: cellProvider')
      todo = self.repository.todo(itemIdentifier)
      return collectionView.dequeueConfiguredReusableCellWithRegistration_forIndexPath_item_(
        todoCellRegistration, indexPath, 'hoge')

    self.dataSource = UICollectionViewDiffableDataSource.alloc(
    ).initWithCollectionView_cellProvider_(self.collectionView, cellProvider)

  @objc_method
  def applySnapshot(self):
    snapshot = NSDiffableDataSourceSnapshot.alloc().init()
    snapshot.appendSectionsWithIdentifiers_([Section.main])
    #snapshot.appendItemsWithIdentifiers_intoSectionWithIdentifier_(['a'], Section.main)
    #snapshot.appendItemsWithIdentifiers_(self.repository.todoIDs)
    #pdbr.state(snapshot)
    self.dataSource.applySnapshot_animatingDifferences_(snapshot, True)

    #pdbr.state(self.dataSource)


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  todo_vc = TodoListViewController.new()
  style = UIModalPresentationStyle.fullScreen
  present_viewController(todo_vc, style)
  #print(CGRectZero)

