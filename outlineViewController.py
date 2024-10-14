"""
note: 案がないまま進める
"""

from pyrubicon.objc.api import ObjCClass, ObjCInstance, Block
from pyrubicon.objc.api import objc_method, objc_property, at
from pyrubicon.objc.runtime import send_super, objc_id

from rbedge.enumerations import UICollectionLayoutListAppearance, UIViewAutoresizing

from rbedge.functions import NSStringFromClass

UIViewController = ObjCClass('UIViewController')
UICollectionView = ObjCClass('UICollectionView')
UICollectionViewLayout = ObjCClass('UICollectionViewLayout')
UICollectionLayoutListConfiguration = ObjCClass(
  'UICollectionLayoutListConfiguration')
UICollectionViewCompositionalLayout = ObjCClass(
  'UICollectionViewCompositionalLayout')
UICollectionViewCellRegistration = ObjCClass(
  'UICollectionViewCellRegistration')
UICollectionViewListCell = ObjCClass('UICollectionViewListCell')

NSDiffableDataSourceSectionSnapshot = ObjCClass(
  'NSDiffableDataSourceSectionSnapshot')


class OutlineViewController(UIViewController):
  # xxx: `objc_property` 宣言って必要？
  outlineCollectionView: UICollectionView = objc_property()

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    # --- Navigation
    title = NSStringFromClass(__class__)
    self.navigationItem.title = title

    self.configureCollectionView()
    self.configureDataSource()

  @objc_method
  def viewDidAppear_(self, animated: bool):
    # xxx: 引数不要?
    send_super(__class__, self, 'viewDidAppear:')
    # todo: 実行確認用
    #print('viewDidAppear')

  # MARK: - UICollectionViewDiffableDataSource
  @objc_method
  def configureCollectionView(self):
    view = self.view
    collectionView = UICollectionView.alloc(
    ).initWithFrame_collectionViewLayout_(view.bounds, self.generateLayout())
    view.addSubview_(collectionView)
    collectionView.autoresizingMask = UIViewAutoresizing.flexibleHeight | UIViewAutoresizing.flexibleWidth
    self.outlineCollectionView = collectionView

    # xxx: `UICollectionViewDelegate` 後回し

  @objc_method
  def configureDataSource(self):

    @Block
    def containerCellRegistrationHandler(_cell: objc_id, _indexPath: objc_id,
                                         _menuItem: objc_id) -> None:
      print(f'containerCellRegistrationHandler')
      cell = ObjCInstance(_cell)
      indexPath = ObjCInstance(_indexPath)
      menuItem = ObjCInstance(_menuItem)
      # xxx: 処理は後で書く
      contentConfiguration = cell.defaultContentConfiguration()
      contentConfiguration.text = 'hoge'

    @Block
    def cellRegistrationHandler(_cell: objc_id, _indexPath: objc_id,
                                _menuItem: objc_id) -> None:
      print(f'cellRegistrationHandler')
      cell = ObjCInstance(_cell)
      indexPath = ObjCInstance(_indexPath)
      menuItem = ObjCInstance(_menuItem)
      # xxx: 処理は後で書く
      contentConfiguration = cell.defaultContentConfiguration()
      contentConfiguration.text = 'fuga'

    containerCellRegistration = UICollectionViewCellRegistration.registrationWithCellClass_configurationHandler_(
      UICollectionViewListCell, containerCellRegistrationHandler)

    cellRegistration = UICollectionViewCellRegistration.registrationWithCellClass_configurationHandler_(
      UICollectionViewListCell, cellRegistrationHandler)

    #pdbr.state(containerCellRegistration)
    #snapshot = self.initialSnapshot()
    self.initialSnapshot()
    #pdbr.state(snapshot)

  @objc_method
  def generateLayout(self) -> ObjCInstance:
    listConfiguration = UICollectionLayoutListConfiguration.alloc(
    ).initWithAppearance_(UICollectionLayoutListAppearance.sidebar)

    layout = UICollectionViewCompositionalLayout.layoutWithListConfiguration_(
      listConfiguration)
    return layout

  @objc_method
  def initialSnapshot(self):
    snapshot = NSDiffableDataSourceSectionSnapshot.alloc().init()
    snapshot.appendItems_(at([]))
    pdbr.state(snapshot)
    return  #snapshot


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  outline_vc = OutlineViewController.new()
  style = UIModalPresentationStyle.fullScreen
  present_viewController(outline_vc, style)
  #print(CGRectZero)

