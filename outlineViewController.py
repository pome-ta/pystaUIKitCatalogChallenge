'''
  note: 
    - [【Swift】世界一わかりやすいTableViewのアコーディオンの実装方法 #Xode - Qiita](https://qiita.com/tosh_3/items/c254429f4f68c7eab39d)
    - `UICollectionView` 形式にもっていく
      - 階層をつける
      - tap 確認
'''

import ctypes

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method, objc_property, objc_const
from pyrubicon.objc.runtime import send_super, objc_id, load_library

from rbedge.enumerations import (
  UICollectionLayoutListAppearance,
  UICollectionLayoutListHeaderMode,
  UICellAccessoryOutlineDisclosureStyle,
  UIUserInterfaceSizeClass,
)
from rbedge.functions import NSStringFromClass
from rbedge import pdbr

UIKit = load_library('UIKit')  # todo: `objc_const` 用
UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')
UINavigationController = ObjCClass('UINavigationController')

# --- UICollectionView
UICollectionView = ObjCClass('UICollectionView')
UICollectionLayoutListConfiguration = ObjCClass(
  'UICollectionLayoutListConfiguration')
UICollectionViewCompositionalLayout = ObjCClass(
  'UICollectionViewCompositionalLayout')
UICollectionViewListCell = ObjCClass('UICollectionViewListCell')

UICellAccessoryDisclosureIndicator = ObjCClass(
  'UICellAccessoryDisclosureIndicator')
UICellAccessoryOutlineDisclosure = ObjCClass(
  'UICellAccessoryOutlineDisclosure')

# --- others
UIColor = ObjCClass('UIColor')
UIFont = ObjCClass('UIFont')
UITapGestureRecognizer = ObjCClass('UITapGestureRecognizer')
NSIndexSet = ObjCClass('NSIndexSet')
UIImage = ObjCClass('UIImage')
UILabel = ObjCClass('UILabel')

# --- Global Variable
UICollectionElementKindSectionHeader = objc_const(
  UIKit, 'UICollectionElementKindSectionHeader')
UIFontTextStyleHeadline = objc_const(UIKit, 'UIFontTextStyleHeadline')


class hogeViewController(UIViewController):

  @objc_method
  def viewDidLoad(self):
    title = NSStringFromClass(__class__)
    self.navigationItem.title = title
    # --- View
    self.view.backgroundColor = UIColor.systemDarkPurpleColor()

    self.label = UILabel.new()
    self.label.text = 'hoge'
    self.label.font = UIFont.systemFontOfSize_(26.0)
    self.label.sizeToFit()

    self.view.addSubview_(self.label)

    # --- Layout
    self.label.translatesAutoresizingMaskIntoConstraints = False
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide

    NSLayoutConstraint.activateConstraints_([
      self.label.centerXAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerXAnchor),
      self.label.centerYAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerYAnchor),
    ])


class OutlineItem:

  def __init__(self,
               title: str,
               imageName: str = None,
               storyboardName: str = None,
               subitems: list = []):
    self.title = title
    self.imageName = imageName
    self.storyboardName = storyboardName
    self.subitems = subitems


class SupplementaryItem:

  def __init__(self, outlineItems: OutlineItem):
    self.outlineItems = outlineItems
    self.title = outlineItems.title
    self.imageName = outlineItems.imageName
    self.storyboardName = outlineItems.storyboardName
    self.subitems = outlineItems.subitems

    self.children = []
    self._create_children()

  def _create_children(self):

    def append_loop(parent, n=1):
      for child in parent.subitems:
        child.indentationLevel = n
        self.children.append(child)
        if child.subitems:
          append_loop(child, n + 1)

    append_loop(self, 1)


buttonItems = [
  OutlineItem(title='ButtonsTitle',
              imageName='rectangle',
              storyboardName=hogeViewController),
  OutlineItem(title='MenuButtonsTitle',
              imageName='list.bullet.rectangle',
              storyboardName='MenuButtonViewController'),
]

controlsSubItems = [
  OutlineItem(title='ButtonsTitles',
              imageName='rectangle.on.rectangle',
              subitems=buttonItems),
  OutlineItem(title='PageControlTitle',
              imageName='photo.on.rectangle',
              subitems=[
                OutlineItem(title='DefaultPageControlTitle',
                            imageName=None,
                            storyboardName='DefaultPageControlViewController'),
                OutlineItem(title='CustomPageControlTitle',
                            imageName=None,
                            storyboardName='CustomPageControlViewController'),
              ]),
  OutlineItem(title='SearchBarsTitle',
              imageName='magnifyingglass',
              subitems=[
                OutlineItem(title='DefaultSearchBarTitle',
                            imageName=None,
                            storyboardName='DefaultSearchBarViewController'),
                OutlineItem(title='CustomSearchBarTitle',
                            imageName=None,
                            storyboardName='CustomSearchBarViewController'),
              ]),
  OutlineItem(title='SegmentedControlsTitle',
              imageName='square.split.3x1',
              storyboardName='SegmentedControlViewController'),
  OutlineItem(title='SlidersTitle',
              imageName=None,
              storyboardName='SliderViewController'),
  OutlineItem(title='SwitchesTitle',
              imageName=None,
              storyboardName='SwitchViewController'),
  OutlineItem(title='TextFieldsTitle',
              imageName=None,
              storyboardName='TextFieldViewController'),
]

controlsOutlineItem = OutlineItem(title='Controls',
                                  imageName='slider.horizontal.3',
                                  subitems=controlsSubItems)

pickerSubItems = [
  OutlineItem(title='DatePickerTitle',
              imageName=None,
              storyboardName='DatePickerController'),
  OutlineItem(title='ColorPickerTitle',
              imageName=None,
              storyboardName='ColorPickerViewController'),
  OutlineItem(title='FontPickerTitle',
              imageName=None,
              storyboardName='FontPickerViewController'),
  OutlineItem(title='ImagePickerTitle',
              imageName=None,
              storyboardName='ImagePickerViewController'),
]

pickersOutlineItem = OutlineItem(title='Pickers',
                                 imageName='list.bullet',
                                 subitems=pickerSubItems)

viewsOutlineItem = OutlineItem(
  title='Views',
  imageName='rectangle.stack.person.crop',
  subitems=[
    OutlineItem(title='ActivityIndicatorsTitle',
                imageName=None,
                storyboardName='ActivityIndicatorViewController'),
    OutlineItem(title='AlertControllersTitle',
                imageName=None,
                storyboardName='AlertControllerViewController'),
    OutlineItem(title='TextViewTitle',
                imageName=None,
                storyboardName='TextViewController'),
    OutlineItem(title='ImagesTitle',
                imageName='photo',
                subitems=[
                  OutlineItem(title='ImageViewTitle',
                              imageName=None,
                              storyboardName='ImageViewController'),
                  OutlineItem(title='SymbolsTitle',
                              imageName=None,
                              storyboardName='SymbolViewController'),
                ]),
    OutlineItem(title='ProgressViewsTitle',
                imageName=None,
                storyboardName='ProgressViewController'),
    OutlineItem(title='StackViewsTitle',
                imageName=None,
                storyboardName='StackViewController'),
    OutlineItem(title='ToolbarsTitle',
                imageName='hammer',
                subitems=[
                  OutlineItem(title='DefaultToolBarTitle',
                              imageName=None,
                              storyboardName='DefaultToolbarViewController'),
                  OutlineItem(title='TintedToolbarTitle',
                              imageName=None,
                              storyboardName='TintedToolbarViewController'),
                  OutlineItem(title='CustomToolbarBarTitle',
                              imageName=None,
                              storyboardName='CustomToolbarViewController'),
                ]),
    OutlineItem(title='VisualEffectTitle',
                imageName=None,
                storyboardName='VisualEffectViewController'),
    OutlineItem(title='WebViewTitle',
                imageName=None,
                storyboardName='WebViewController'),
  ])

menuItems = [
  SupplementaryItem(controlsOutlineItem),
  SupplementaryItem(viewsOutlineItem),
  SupplementaryItem(pickersOutlineItem),
]


class ViewController(UIViewController):

  collectionView: UICollectionView = objc_property()

  @objc_method
  def viewDidLoad(self):
    # --- Navigation
    send_super(__class__, self, 'viewDidLoad')
    title = NSStringFromClass(__class__)
    self.navigationItem.title = title

    # --- View
    self.view.backgroundColor = UIColor.systemBrownColor()  # todo: 確認用

    # --- collection set
    self.listCell_identifier = 'customListCell'
    self.header_identifier = 'customHeader'

    collectionView = UICollectionView.alloc(
    ).initWithFrame_collectionViewLayout_(self.view.bounds,
                                          self.generateLayout())
    collectionView.registerClass_forCellWithReuseIdentifier_(
      UICollectionViewListCell, self.listCell_identifier)

    collectionView.registerClass_forSupplementaryViewOfKind_withReuseIdentifier_(
      UICollectionViewListCell, UICollectionElementKindSectionHeader,
      self.header_identifier)

    collectionView.delegate = self
    collectionView.dataSource = self

    # --- Layout
    self.view.addSubview_(collectionView)
    collectionView.translatesAutoresizingMaskIntoConstraints = False
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide
    NSLayoutConstraint.activateConstraints_([
      collectionView.centerXAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerXAnchor),
      collectionView.centerYAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerYAnchor),
      collectionView.widthAnchor.constraintEqualToAnchor_multiplier_(
        safeAreaLayoutGuide.widthAnchor, 1.0),
      collectionView.heightAnchor.constraintEqualToAnchor_multiplier_(
        safeAreaLayoutGuide.heightAnchor, 1.0),
    ])
    self.collectionView = collectionView

  @objc_method
  def viewDidAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #pdbr.state(self.collectionView)

  # --- UICollectionViewDataSource
  @objc_method
  def numberOfSectionsInCollectionView_(self, collectionView) -> int:
    return len(menuItems)

  @objc_method
  def collectionView_numberOfItemsInSection_(self, collectionView,
                                             section: int) -> int:
    return len(menuItems[section].children)

  @objc_method
  def collectionView_cellForItemAtIndexPath_(self, collectionView,
                                             indexPath) -> objc_id:
    cell = collectionView.dequeueReusableCellWithReuseIdentifier_forIndexPath_(
      self.listCell_identifier, indexPath)
    target_item = menuItems[indexPath.section].children[indexPath.row]

    contentConfiguration = cell.defaultContentConfiguration()
    contentConfiguration.text = target_item.title
    if (image := target_item.imageName) is not None:
      contentConfiguration.image = UIImage.systemImageNamed_(image)

    if target_item.subitems:  # containerCellRegistration
      contentConfiguration.textProperties.font = UIFont.preferredFontForTextStyle_(
        UIFontTextStyleHeadline)
      disclosureOptions = UICellAccessoryOutlineDisclosureStyle.header

      outlineDisclosure = UICellAccessoryOutlineDisclosure.new()
      outlineDisclosure.setStyle_(disclosureOptions)
      cell.accessories = [
        outlineDisclosure,
      ]

    else:  # cellRegistration
      disclosureIndicator = UICellAccessoryDisclosureIndicator.alloc().init()
      cell.accessories = [
        disclosureIndicator,
      ]

    cell.indentationLevel = target_item.indentationLevel
    cell.contentConfiguration = contentConfiguration
    return cell

  @objc_method
  def collectionView_viewForSupplementaryElementOfKind_atIndexPath_(
      self, collectionView, kind, indexPath) -> ObjCInstance:
    headerView = collectionView.dequeueReusableSupplementaryViewOfKind_withReuseIdentifier_forIndexPath_(
      UICollectionElementKindSectionHeader, self.header_identifier, indexPath)

    target_item = menuItems[indexPath.section]

    contentConfiguration = headerView.defaultContentConfiguration()
    contentConfiguration.text = target_item.title

    if (image := target_item.imageName) is not None:
      contentConfiguration.image = UIImage.systemImageNamed_(image)

    disclosureOptions = UICellAccessoryOutlineDisclosureStyle.header
    outlineDisclosure = UICellAccessoryOutlineDisclosure.new()
    outlineDisclosure.setStyle_(disclosureOptions)

    headerView.accessories = [
      outlineDisclosure,
    ]

    headerView.contentConfiguration = contentConfiguration
    return headerView

  # --- UICollectionViewDelegate
  @objc_method
  def collectionView_didSelectItemAtIndexPath_(self, collectionView,
                                               indexPath):
    # xxx: `section` は検知しないから、判断なくてもいい?
    #print(indexPath)
    #pdbr.state(self.collectionView)
    #pdbr.state(collectionView)
    menuItem = menuItems[indexPath.section].children[indexPath.row]
    menuItem_vc = menuItem.storyboardName.new()
    self.pushOrPresentViewController_(menuItem_vc)
    #print(menuItem)

  # --- private
  @objc_method
  def splitViewWantsToShowDetail(self) -> bool:
    if (splitViewController := self.splitViewController) is not None:
      return splitViewController.traitCollection.horizontalSizeClass == UIUserInterfaceSizeClass.regular
    else:
      return False

  # --- private
  @objc_method
  def pushOrPresentViewController_(self, viewController):
    if self.splitViewWantsToShowDetail():
      navVC = UINavigationController.alloc().initWithRootViewController_(
        viewController)

      self.splitViewController.showDetailViewController_sender_(navVC, navVC)
    else:
      self.navigationController.pushViewController_animated_(
        viewController, True)

  # --- private
  @objc_method
  def generateLayout(self) -> ObjCInstance:
    #_appearance = UICollectionLayoutListAppearance.plain
    _appearance = UICollectionLayoutListAppearance.sidebar
    listConfiguration = UICollectionLayoutListConfiguration.alloc(
    ).initWithAppearance_(_appearance)
    #_headerMode = UICollectionLayoutListHeaderMode.firstItemInSection
    _headerMode = UICollectionLayoutListHeaderMode.supplementary
    listConfiguration.headerMode = _headerMode

    layout = UICollectionViewCompositionalLayout.layoutWithListConfiguration_(
      listConfiguration)
    return layout


if __name__ == '__main__':
  from rbedge import present_viewController
  from rbedge.enumerations import UIModalPresentationStyle

  vc = ViewController.new()

  style = UIModalPresentationStyle.fullScreen
  #style = UIModalPresentationStyle.pageSheet
  present_viewController(vc, style)


