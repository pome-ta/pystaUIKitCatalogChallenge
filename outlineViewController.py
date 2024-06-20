import ctypes

from pyrubicon.objc.api import ObjCClass, objc_method
from pyrubicon.objc.runtime import send_super
from pyrubicon.objc.types import NSInteger

from rbedge.enumerations import UISplitViewControllerStyle, UISplitViewControllerColumn, UICollectionLayoutListAppearance

#ObjCClass.auto_rename = True
UISplitViewController = ObjCClass('UISplitViewController')

UICollectionViewController = ObjCClass('UICollectionViewController')
#UICollectionViewLayout = ObjCClass('UICollectionViewLayout')
UICollectionViewCell = ObjCClass('UICollectionViewCell')
UICollectionViewListCell = ObjCClass('UICollectionViewListCell')

UICollectionViewCompositionalLayout = ObjCClass(
  'UICollectionViewCompositionalLayout')
UICollectionLayoutListConfiguration = ObjCClass(
  'UICollectionLayoutListConfiguration')

from rbedge.functions import NSStringFromClass

# --- UIViewController
UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UIView = ObjCClass('UIView')
UILabel = ObjCClass('UILabel')
UIFont = ObjCClass('UIFont')
UIColor = ObjCClass('UIColor')


class FirstViewController(UIViewController):

  @objc_method
  def viewDidLoad(self):
    # --- Navigation
    title = NSStringFromClass(__class__)
    self.navigationItem.title = title

    # --- View
    backgroundColor = UIColor.systemBlueColor()
    systemBlueColor

    self.view.backgroundColor = backgroundColor

    self.label = UILabel.new()
    self.label.text = title
    self.label.font = UIFont.systemFontOfSize_(26.0)
    self.label.sizeToFit()

    self.view.addSubview_(self.label)

    # --- Layout
    self.label.translatesAutoresizingMaskIntoConstraints = False

    NSLayoutConstraint.activateConstraints_([
      self.label.centerXAnchor.constraintEqualToAnchor_(
        self.view.centerXAnchor),
      self.label.centerYAnchor.constraintEqualToAnchor_(
        self.view.centerYAnchor),
    ])


class SecondViewController(UIViewController):

  @objc_method
  def viewDidLoad(self):
    # --- Navigation
    title = NSStringFromClass(__class__)
    self.navigationItem.title = title

    # --- View
    backgroundColor = UIColor.systemRedColor()
    self.view.backgroundColor = backgroundColor

    self.label = UILabel.new()
    self.label.text = title
    self.label.font = UIFont.systemFontOfSize_(26.0)
    self.label.sizeToFit()

    self.view.addSubview_(self.label)

    # --- Layout
    self.label.translatesAutoresizingMaskIntoConstraints = False

    NSLayoutConstraint.activateConstraints_([
      self.label.centerXAnchor.constraintEqualToAnchor_(
        self.view.centerXAnchor),
      self.label.centerYAnchor.constraintEqualToAnchor_(
        self.view.centerYAnchor),
    ])


class OutlineViewController(UISplitViewController):

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    '''
    self.setViewController_forColumn_(
      FirstViewController, UISplitViewControllerColumn.supplementary)
    '''
    view = self.view
    bg_view = UIView.new()
    bg_view.backgroundColor = UIColor.systemCyanColor()

    view.addSubview_(bg_view)

    bg_view.translatesAutoresizingMaskIntoConstraints = False
    NSLayoutConstraint.activateConstraints_([
      bg_view.centerXAnchor.constraintEqualToAnchor_(view.centerXAnchor),
      bg_view.centerYAnchor.constraintEqualToAnchor_(view.centerYAnchor),
      bg_view.widthAnchor.constraintEqualToAnchor_multiplier_(
        view.widthAnchor, 0.88),
      bg_view.heightAnchor.constraintEqualToAnchor_multiplier_(
        view.heightAnchor, 0.88),
    ])
    pdbr.state(UICollectionViewController)


# [UICollectionLayoutListConfigurationのheaderMode=.firstItemInSection観測隊](https://zenn.dev/samekard_dev/articles/2cbb0788915f01)
prefectures = [
  ['北海道', '北海道'],
  ['東北', '青森', '岩手', '秋田', '宮城', '山形', '福島'],
  ['関東', '茨城', '栃木', '群馬', '埼玉', '千葉', '東京', '神奈川'],
  ['甲信越', '新潟', '長野', '山梨'],
  ['北陸', '富山', '石川', '福井'],
  ['東海', '岐阜', '静岡', '愛知', '三重'],
  ['近畿', '滋賀', '京都', '奈良', '大阪', '和歌山', '兵庫'],
  ['中国', '鳥取', '島根', '岡山', '広島', '山口'],
  ['四国', '香川', '徳島', '愛媛', '高知'],
  ['九州', '福岡', '佐賀', '長崎', '大分', '熊本', '宮崎', '鹿児島'],
  ['沖縄', '沖縄'],
]


class CollectionViewController(UICollectionViewController):

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    self.identifier_str = 'customCell'
    self.collectionView.registerClass_forCellWithReuseIdentifier_(
      UICollectionViewListCell, self.identifier_str)

  @objc_method
  def numberOfSectionsInCollectionView_(self, collectionView) -> NSInteger:
    return len(prefectures)

  @objc_method
  def collectionView_numberOfItemsInSection_(self, collectionView,
                                             section: NSInteger) -> NSInteger:

    return len(prefectures[section])

  @objc_method
  def collectionView_cellForItemAtIndexPath_(self, collectionView,
                                             indexPath) -> ctypes.c_void_p:
    cell = collectionView.dequeueReusableCellWithReuseIdentifier_forIndexPath_(
      self.identifier_str, indexPath)

    
    cellConfiguration = cell.defaultContentConfiguration()
    cellConfiguration.text = prefectures[indexPath.section][indexPath.row]
    cell.contentConfiguration = cellConfiguration
    #cell.setBackgroundColor_(UIColor.systemRedColor())
    #pdbr.state(cell)
    #print(prefectures[indexPath.section][indexPath.row])
    return cell.ptr


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  listConfiguration = UICollectionLayoutListConfiguration.alloc(
  ).initWithAppearance_(1)
  layout = UICollectionViewCompositionalLayout.layoutWithListConfiguration_(
    listConfiguration)

  #main_vc = CollectionViewController.new()
  main_vc = CollectionViewController.alloc().initWithCollectionViewLayout_(
    layout)

  present_viewController(main_vc)
  #pdbr.state(main_vc)
  #layoutWithListConfiguration
  #listConfiguration = UICollectionLayoutListConfiguration.alloc().initWithAppearance_(0)
  #layout = UICollectionViewCompositionalLayout.layoutWithListConfiguration_(listConfiguration)

  #v = UICollectionViewController.alloc().initWithCollectionViewLayout_(layout)

  #pdbr.state(v.collectionView)
  #print(listConfiguration.appearance)
  #main_vc = CollectionViewController.alloc().initWithStyle_(UISplitViewControllerStyle.doubleColumn)
  #pdbr.state(main_vc)
  #print(main_vc.style)
  #pdbr.state(OutlineViewController.alloc())

  #style = UIModalPresentationStyle.fullScreen
  #style = UIModalPresentationStyle.pageSheet  # 1
  #present_viewController(main_vc, style, False)

