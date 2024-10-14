"""
note: 案がないまま進める
"""

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method, objc_property, at
from pyrubicon.objc.runtime import send_super

from rbedge.enumerations import UICollectionLayoutListAppearance, UIViewAutoresizing

from rbedge.functions import NSStringFromClass

UIViewController = ObjCClass('UIViewController')
UICollectionView = ObjCClass('UICollectionView')
UICollectionViewLayout = ObjCClass('UICollectionViewLayout')
UICollectionLayoutListConfiguration = ObjCClass(
  'UICollectionLayoutListConfiguration')
UICollectionViewCompositionalLayout = ObjCClass(
  'UICollectionViewCompositionalLayout')


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

    pdbr.state(collectionView)

  @objc_method
  def generateLayout(self) -> ObjCInstance:
    listConfiguration = UICollectionLayoutListConfiguration.alloc(
    ).initWithAppearance_(UICollectionLayoutListAppearance.sidebar)

    layout = UICollectionViewCompositionalLayout.layoutWithListConfiguration_(
      listConfiguration)
    return layout


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  outline_vc = OutlineViewController.new()
  style = UIModalPresentationStyle.fullScreen
  present_viewController(outline_vc, style)
  #print(CGRectZero)

