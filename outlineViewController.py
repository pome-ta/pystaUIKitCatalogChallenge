import ctypes

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.runtime import send_super

from rbedge.enumerations import (
  UITableViewStyle,
  UICollectionLayoutListAppearance,
  UICollectionLayoutListHeaderMode,
  UICellAccessoryOutlineDisclosureStyle,
  UIUserInterfaceIdiom,
  UIUserInterfaceSizeClass,
)
from rbedge.globalVariables import (
  UIFontTextStyle,
  UICollectionElementKindSectionHeader,
)

from pyLocalizedString import localizedString

from rbedge.rootNavigationController import RootNavigationController  # todo: 型確認
from baseTableViewController import BaseTableViewController  # todo: 型確認

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

# --- UIKitCatalog ViewControllers
# --- --- controlsOutlineItem
from buttonViewController import ButtonViewController
from menuButtonViewController import MenuButtonViewController
from defaultPageControlViewController import PageControlViewController
from customPageControlViewController import CustomPageControlViewController
from defaultSearchBarViewController import DefaultSearchBarViewController
from customSearchBarViewController import CustomSearchBarViewController
from segmentedControlViewController import SegmentedControlViewController
from sliderViewController import SliderViewController
from switchViewController import SwitchViewController
from textFieldViewController import TextFieldViewController
from stepperViewController import StepperViewController
# --- --- viewsOutlineItem
from activityIndicatorViewController import ActivityIndicatorViewController
from alertControllerViewController import AlertControllerViewController
from textViewController import TextViewController
from imageViewController import ImageViewController
from symbolViewController import SymbolViewController
from progressViewController import ProgressViewController
from stackViewController import StackViewController
from defaultToolbarViewController import DefaultToolbarViewController
from tintedToolbarViewController import TintedToolbarViewController
from customToolbarViewController import CustomToolbarViewController
from visualEffectViewController import VisualEffectViewController
from webViewController import WebViewController
# --- --- pickersOutlineItem
from datePickerController import DatePickerController
from colorPickerViewController import ColorPickerViewController
from fontPickerViewController import FontPickerViewController
from imagePickerViewController import ImagePickerViewController
from pickerViewController import PickerViewController

# --- /

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
UIImage = ObjCClass('UIImage')


class OutlineItem:

  def __init__(self,
               title: str,
               imageName: str | None = None,
               storyboardName: UIViewController | None = None,
               subitems: list = []):
    self.title = localizedString(title)
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
              storyboardName=ButtonViewController),
  OutlineItem(title='MenuButtonsTitle',
              imageName='list.bullet.rectangle',
              storyboardName=MenuButtonViewController),
]

controlsSubItems = [
  OutlineItem(title='ButtonsTitle',
              imageName='rectangle.on.rectangle',
              subitems=buttonItems),
  OutlineItem(title='PageControlTitle',
              imageName='photo.on.rectangle',
              subitems=[
                OutlineItem(title='DefaultPageControlTitle',
                            imageName=None,
                            storyboardName=PageControlViewController),
                OutlineItem(title='CustomPageControlTitle',
                            imageName=None,
                            storyboardName=CustomPageControlViewController),
              ]),
  OutlineItem(title='SearchBarsTitle',
              imageName='magnifyingglass',
              subitems=[
                OutlineItem(title='DefaultSearchBarTitle',
                            imageName=None,
                            storyboardName=DefaultSearchBarViewController),
                OutlineItem(title='CustomSearchBarTitle',
                            imageName=None,
                            storyboardName=CustomSearchBarViewController),
              ]),
  OutlineItem(title='SegmentedControlsTitle',
              imageName='square.split.3x1',
              storyboardName=SegmentedControlViewController),
  OutlineItem(title='SlidersTitle',
              imageName=None,
              storyboardName=SliderViewController),
  OutlineItem(title='SwitchesTitle',
              imageName=None,
              storyboardName=SwitchViewController),
  OutlineItem(title='TextFieldsTitle',
              imageName=None,
              storyboardName=TextFieldViewController),
]

# todo: traitCollection.userInterfaceIdiom != .mac
# xxx: `self` の実態で呼べない
if True:
  stepperItem = OutlineItem(title='SteppersTitle',
                            imageName=None,
                            storyboardName=StepperViewController)
  controlsSubItems.append(stepperItem)

controlsOutlineItem = OutlineItem(title='Controls',
                                  imageName='slider.horizontal.3',
                                  subitems=controlsSubItems)

pickerSubItems = [
  OutlineItem(title='DatePickerTitle',
              imageName=None,
              storyboardName=DatePickerController),
  OutlineItem(title='ColorPickerTitle',
              imageName=None,
              storyboardName=ColorPickerViewController),
  OutlineItem(title='FontPickerTitle',
              imageName=None,
              storyboardName=FontPickerViewController),
  OutlineItem(title='ImagePickerTitle',
              imageName=None,
              storyboardName=ImagePickerViewController),
]

# todo: traitCollection.userInterfaceIdiom != .mac
if True:
  pickerViewItem = OutlineItem(title='PickerViewTitle',
                               imageName=None,
                               storyboardName=PickerViewController)
  pickerSubItems.append(pickerViewItem)

pickersOutlineItem = OutlineItem(title='Pickers',
                                 imageName='list.bullet',
                                 subitems=pickerSubItems)

viewsOutlineItem = OutlineItem(
  title='Views',
  imageName='rectangle.stack.person.crop',
  subitems=[
    OutlineItem(title='ActivityIndicatorsTitle',
                imageName=None,
                storyboardName=ActivityIndicatorViewController),
    OutlineItem(title='AlertControllersTitle',
                imageName=None,
                storyboardName=AlertControllerViewController),
    OutlineItem(title='TextViewTitle',
                imageName=None,
                storyboardName=TextViewController),
    OutlineItem(title='ImagesTitle',
                imageName='photo',
                subitems=[
                  OutlineItem(title='ImageViewTitle',
                              imageName=None,
                              storyboardName=ImageViewController),
                  OutlineItem(title='SymbolsTitle',
                              imageName=None,
                              storyboardName=SymbolViewController),
                ]),
    OutlineItem(title='ProgressViewsTitle',
                imageName=None,
                storyboardName=ProgressViewController),
    OutlineItem(title='StackViewsTitle',
                imageName=None,
                storyboardName=StackViewController),
    OutlineItem(title='ToolbarsTitle',
                imageName='hammer',
                subitems=[
                  OutlineItem(title='DefaultToolBarTitle',
                              imageName=None,
                              storyboardName=DefaultToolbarViewController),
                  OutlineItem(title='TintedToolbarTitle',
                              imageName=None,
                              storyboardName=TintedToolbarViewController),
                  OutlineItem(title='CustomToolbarBarTitle',
                              imageName=None,
                              storyboardName=CustomToolbarViewController),
                ]),
    OutlineItem(title='VisualEffectTitle',
                imageName=None,
                storyboardName=VisualEffectViewController),
    OutlineItem(title='WebViewTitle',
                imageName=None,
                storyboardName=WebViewController),
  ])

menuItems = [
  SupplementaryItem(controlsOutlineItem),
  SupplementaryItem(viewsOutlineItem),
  SupplementaryItem(pickersOutlineItem),
]


class OutlineViewController(UIViewController):

  listCell_identifier: str = objc_property()
  header_identifier: str = objc_property()

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def loadView(self):
    send_super(__class__, self, 'loadView')
    #print(f'\t{NSStringFromClass(__class__)}: loadView')
    self.listCell_identifier = 'customListCell'
    self.header_identifier = 'customHeader'

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    #print(f'\t{NSStringFromClass(__class__)}: viewDidLoad')

    # --- Navigation
    self.navigationItem.title = NSStringFromClass(__class__) if (
      title := self.navigationItem.title) is None else title

    self.view.backgroundColor = UIColor.systemBackgroundColor()
    # --- collection set
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
    layoutMarginsGuide = self.view.layoutMarginsGuide
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide
    NSLayoutConstraint.activateConstraints_([
      collectionView.centerXAnchor.constraintEqualToAnchor_(
        layoutMarginsGuide.centerXAnchor),
      collectionView.centerYAnchor.constraintEqualToAnchor_(
        layoutMarginsGuide.centerYAnchor),
      collectionView.widthAnchor.constraintEqualToAnchor_multiplier_(
        layoutMarginsGuide.widthAnchor, 1.0),
      collectionView.heightAnchor.constraintEqualToAnchor_multiplier_(
        layoutMarginsGuide.heightAnchor, 1.0),
    ])

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
                                             indexPath) -> ObjCInstance:
    cell = collectionView.dequeueReusableCellWithReuseIdentifier_forIndexPath_(
      self.listCell_identifier, indexPath)
    target_item = menuItems[indexPath.section].children[indexPath.row]

    contentConfiguration = cell.defaultContentConfiguration()
    contentConfiguration.text = target_item.title
    if (image := target_item.imageName) is not None:
      contentConfiguration.image = UIImage.systemImageNamed_(image)

    if target_item.subitems:  # containerCellRegistration
      contentConfiguration.textProperties.font = UIFont.preferredFontForTextStyle_(
        UIFontTextStyle.headline)
      disclosureOptions = UICellAccessoryOutlineDisclosureStyle.header

      outlineDisclosure = UICellAccessoryOutlineDisclosure.new()
      outlineDisclosure.setStyle_(disclosureOptions)
      cell.accessories = [
        outlineDisclosure,
      ]

    else:  # cellRegistration
      disclosureIndicator = UICellAccessoryDisclosureIndicator.new()
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
    menuItem = menuItems[indexPath.section].children[indexPath.row]
    try:
      if (storyboardName :=
          menuItem.storyboardName).isSubclassOfClass_(BaseTableViewController):
        viewController = storyboardName.alloc().initWithStyle_(
          UITableViewStyle.grouped)
      else:
        viewController = storyboardName.new()
      self.pushOrPresentViewController_(viewController)
    except Exception as e:
      print(f'{e}')

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
    # _appearance = UICollectionLayoutListAppearance.plain
    _appearance = UICollectionLayoutListAppearance.sidebar
    listConfiguration = UICollectionLayoutListConfiguration.alloc(
    ).initWithAppearance_(_appearance)
    # _headerMode = UICollectionLayoutListHeaderMode.firstItemInSection
    _headerMode = UICollectionLayoutListHeaderMode.supplementary
    listConfiguration.headerMode = _headerMode

    layout = UICollectionViewCompositionalLayout.layoutWithListConfiguration_(
      listConfiguration)
    return layout


if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import UIModalPresentationStyle

  main_vc = OutlineViewController.new()
  _title = NSStringFromClass(OutlineViewController)
  main_vc.navigationItem.title = _title

  #presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

