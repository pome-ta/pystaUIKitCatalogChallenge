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


class CollectionViewController(UICollectionViewController):

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    self.identifier_str = 'customCell'
    self.collectionView.registerClass_forCellWithReuseIdentifier_(
      UICollectionViewCell, self.identifier_str)
    #pdbr.state(self.collectionView)

  @objc_method
  def collectionView_numberOfItemsInSection_(self, collectionView,
                                             section: NSInteger) -> NSInteger:
    return 10

  @objc_method
  def collectionView_cellForItemAtIndexPath_(self, collectionView,
                                             indexPath) -> ctypes.c_void_p:
    cell = collectionView.dequeueReusableCellWithReuseIdentifier_forIndexPath_(
      self.identifier_str, indexPath)
    cell.setBackgroundColor_(UIColor.systemRedColor())
    #pdbr.state(cell)
    return cell.ptr


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  listConfiguration = UICollectionLayoutListConfiguration.alloc(
  ).initWithAppearance_(0)
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

