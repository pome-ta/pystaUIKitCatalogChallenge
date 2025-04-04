import ctypes
from enum import Enum

from pyrubicon.objc.api import ObjCClass, ObjCInstance, Block
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, objc_id, SEL
from pyrubicon.objc.types import NSInteger, CGSize, CGFloat, CGRectMake, CGSizeMake

from rbedge.functions import (
  NSStringFromClass,
  UIGraphicsBeginImageContextWithOptions,
  UIGraphicsGetImageFromCurrentImageContext,
  UIGraphicsEndImageContext,
)
from rbedge.enumerations import (
  UIControlEvents,
  UIUserInterfaceIdiom,
  UIUserInterfaceStyle,
  UIControlState,
  UIBarMetrics,
)
from rbedge.globalVariables import (
  UIFontTextStyle,
  NSAttributedStringKey,
)

from rbedge.pythonProcessUtils import (
  mainScreen_scale,
  dataWithContentsOfURL,
  get_srgb_named_style,
)

from rbedge import pdbr

from caseElement import CaseElement
from pyLocalizedString import localizedString

from baseTableViewController import BaseTableViewController
from storyboard.segmentedControlViewController import prototypes

UIImage = ObjCClass('UIImage')
UIAction = ObjCClass('UIAction')
UIColor = ObjCClass('UIColor')
UISegmentedControl = ObjCClass('UISegmentedControl')  # todo: 型呼び出し
UIFont = ObjCClass('UIFont')
UIFontDescriptor = ObjCClass('UIFontDescriptor')
NSAttributedString = ObjCClass('NSAttributedString')
NSDictionary = ObjCClass('NSDictionary')


# Cell identifier for each segmented control table view cell.
# セグメント化されたコントロールテーブルビューの各セルのセル識別子。
class SegmentKind(Enum):
  segmentDefault = 'segmentDefault'
  segmentTinted = 'segmentTinted'
  segmentCustom = 'segmentCustom'
  segmentCustomBackground = 'segmentCustomBackground'
  segmentAction = 'segmentAction'


class SegmentedControlViewController(BaseTableViewController):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def initWithStyle_(self, style: NSInteger) -> ObjCInstance:
    send_super(__class__,
               self,
               'initWithStyle:',
               style,
               restype=objc_id,
               argtypes=[
                 NSInteger,
               ])
    #print(f'\t{NSStringFromClass(__class__)}: initWithStyle_')
    return self

  @objc_method
  def loadView(self):
    send_super(__class__, self, 'loadView')
    #print(f'\t{NSStringFromClass(__class__)}: loadView')
    [
      self.tableView.registerClass_forCellReuseIdentifier_(
        prototype['cellClass'], prototype['identifier'])
      for prototype in prototypes
    ]

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    #print(f'\t{NSStringFromClass(__class__)}: viewDidLoad')
    
    # --- Navigation
    self.navigationItem.title = localizedString('SegmentedControlsTitle') if (
      title := self.navigationItem.title) is None else title

    self.testCellsAppendContentsOf_([
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('DefaultTitle'), SegmentKind.segmentDefault.value,
        'configureDefaultSegmentedControl:'),
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('CustomSegmentsTitle'),
        SegmentKind.segmentCustom.value,
        'configureCustomSegmentsSegmentedControl:'),
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('CustomBackgroundTitle'),
        SegmentKind.segmentCustomBackground.value,
        'configureCustomBackgroundSegmentedControl:'),
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('ActionBasedTitle'), SegmentKind.segmentAction.value,
        'configureActionBasedSegmentedControl:'),
    ])

    if self.traitCollection.userInterfaceIdiom != UIUserInterfaceIdiom.mac:
      # Tinted segmented control is only available on iOS.
      # ティント・セグメンテッド・コントロールはiOSでのみ利用可能。
      self.testCellsAppendContentsOf_([
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('Tinted'), SegmentKind.segmentTinted.value,
          'configureTintedSegmentedControl:'),
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

  # MARK: - Configuration
  @objc_method
  def configureDefaultSegmentedControl_(self, segmentedControl):
    # As a demonstration, disable the first segment.
    # デモとして、最初のセグメントを無効にします。
    segmentedControl.setEnabled_forSegmentAtIndex_(False, 0)
    segmentedControl.addTarget_action_forControlEvents_(
      self, SEL('selectedSegmentDidChange:'), UIControlEvents.valueChanged)

  @objc_method
  def configureTintedSegmentedControl_(self, segmentedControl):
    # Use a dynamic tinted "green" color (separate one for Light Appearance and separate one for Dark Appearance).
    # ダイナミックな色合いの "グリーン"を使用する(ライト・アピアランス用とダーク・アピアランス用に分ける)。
    _style = self.traitCollection.userInterfaceStyle
    _srgb = get_srgb_named_style('tinted_segmented_control', _style)

    color_named = UIColor.colorWithRed_green_blue_alpha_(*_srgb)

    segmentedControl.selectedSegmentTintColor = color_named
    segmentedControl.selectedSegmentIndex = 1

    segmentedControl.addTarget_action_forControlEvents_(
      self, SEL('selectedSegmentDidChange:'), UIControlEvents.valueChanged)

  @objc_method
  def configureCustomSegmentsSegmentedControl_(self, segmentedControl):
    airplaneImage = UIImage.systemImageNamed_('airplane')
    airplaneImage.accessibilityLabel = localizedString('Airplane')
    segmentedControl.setImage_forSegmentAtIndex_(airplaneImage, 0)

    giftImage = UIImage.systemImageNamed_('gift')
    giftImage.accessibilityLabel = localizedString('Gift')
    segmentedControl.setImage_forSegmentAtIndex_(giftImage, 1)

    burstImage = UIImage.systemImageNamed_('burst')
    burstImage.accessibilityLabel = localizedString('Burst')
    segmentedControl.setImage_forSegmentAtIndex_(burstImage, 2)

    segmentedControl.selectedSegmentIndex = 0

    segmentedControl.addTarget_action_forControlEvents_(
      self, SEL('selectedSegmentDidChange:'), UIControlEvents.valueChanged)

  # Utility function to resize an image to a particular size.
  # 画像を特定のサイズに変更するユーティリティ関数。
  @objc_method
  def scaledImage_scaledToSize_(self, image, newSize: CGSize):
    UIGraphicsBeginImageContextWithOptions(newSize, False, 0.0)
    image.drawInRect_(CGRectMake(0.0, 0.0, newSize.width, newSize.height))
    newImage = UIGraphicsGetImageFromCurrentImageContext()
    UIGraphicsEndImageContext()

    return newImage

  # Configure the segmented control with a background image, dividers, and custom font.
  # セグメント化されたコントロールに、背景画像、仕切り、カスタム・フォントを設定する。
  # The background image first needs to be sized to match the control's size.
  # 背景画像は、まずコントロールのサイズに合わせた大きさにする必要があります。
  @objc_method
  def configureCustomBackgroundSegmentedControl_(self, placeHolderView):
    customBackgroundSegmentedControl = UISegmentedControl.alloc(
    ).initWithItems_([
      localizedString('CheckTitle'),
      localizedString('SearchTitle'),
      localizedString('ToolsTitle'),
    ])

    customBackgroundSegmentedControl.selectedSegmentIndex = 2

    # Place this custom segmented control within the placeholder view.
    # このカスタムのセグメント化されたコントロールをプレースホルダー ビュー内に配置します。
    _width = placeHolderView.frame.size.width
    _height = customBackgroundSegmentedControl.frame.size.height
    # todo: `=` では、反映されないので`setSize_` してる
    # customBackgroundSegmentedControl.frame.size.width = placeHolderView.frame.size.width
    customBackgroundSegmentedControl.setSize_(CGSizeMake(_width, _height))

    # xxx: ここもか？
    customBackgroundSegmentedControl.frame.origin.y = (
      placeHolderView.bounds.size.height -
      customBackgroundSegmentedControl.bounds.size.height) / 2

    placeHolderView.addSubview_(customBackgroundSegmentedControl)

    scale = int(mainScreen_scale)
    normal_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/background.imageset/stepper_and_segment_background_{scale}x.png'
    highlighted_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/background_highlighted.imageset/stepper_and_segment_background_highlighted_{scale}x.png'
    disabled_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/background_disabled.imageset/stepper_and_segment_background_disabled_{scale}x.png'

    # Set the background images for each control state.
    # 制御状態ごとに背景画像を設定します。
    normalSegmentBackgroundImage = UIImage.alloc().initWithData_scale_(
      dataWithContentsOfURL(normal_str), scale)
    # Size the background image to match the bounds of the segmented control.
    # セグメント化されたコントロールの境界に一致するように背景画像のサイズを設定します。
    backgroundImageSize = customBackgroundSegmentedControl.bounds.size

    newBackgroundImageSize = self.scaledImage_scaledToSize_(
      normalSegmentBackgroundImage, backgroundImageSize)
    customBackgroundSegmentedControl.setBackgroundImage_forState_barMetrics_(
      newBackgroundImageSize, UIControlState.normal, UIBarMetrics.default)

    disabledSegmentBackgroundImage = UIImage.alloc().initWithData_scale_(
      dataWithContentsOfURL(disabled_str), scale)
    customBackgroundSegmentedControl.setBackgroundImage_forState_barMetrics_(
      disabledSegmentBackgroundImage, UIControlState.disabled,
      UIBarMetrics.default)

    highlightedSegmentBackgroundImage = UIImage.alloc().initWithData_scale_(
      dataWithContentsOfURL(highlighted_str), scale)
    customBackgroundSegmentedControl.setBackgroundImage_forState_barMetrics_(
      highlightedSegmentBackgroundImage, UIControlState.highlighted,
      UIBarMetrics.default)

    # xxx: `x1`,`x2` と`x3` だと、ファイル名が違う
    divider_scale = 'stepper_and_segment_divider_' if scale == 3 else 'stepper_and_segment_segment_divider_'
    divider_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/stepper_and_segment_divider.imageset/{divider_scale}{scale}x.png'

    # Set the divider image.
    # 分割画像を設定します。
    segmentDividerImage = UIImage.alloc().initWithData_scale_(
      dataWithContentsOfURL(divider_str), scale)
    customBackgroundSegmentedControl.setDividerImage_forLeftSegmentState_rightSegmentState_barMetrics_(
      segmentDividerImage, UIControlState.normal, UIControlState.normal,
      UIBarMetrics.default)

    # Create a font to use for the attributed title, for both normal and highlighted states.
    # 通常状態と強調表示状態の両方で、属性付きタイトルに使用するフォントを作成します。
    font = UIFont.fontWithDescriptor_size_(
      UIFontDescriptor.preferredFontDescriptorWithTextStyle_(
        UIFontTextStyle.body), 0.0)

    normalTextAttributes = NSDictionary.dictionaryWithObjects_forKeys_([
      UIColor.systemPurpleColor(),
      font,
    ], [
      NSAttributedStringKey.foregroundColor,
      NSAttributedStringKey.font,
    ])

    customBackgroundSegmentedControl.setTitleTextAttributes_forState_(
      normalTextAttributes, UIControlState.normal)

    highlightedTextAttributes = NSDictionary.dictionaryWithObjects_forKeys_([
      UIColor.systemGreenColor(),
      font,
    ], [
      NSAttributedStringKey.foregroundColor,
      NSAttributedStringKey.font,
    ])

    customBackgroundSegmentedControl.setTitleTextAttributes_forState_(
      highlightedTextAttributes, UIControlState.highlighted)

    customBackgroundSegmentedControl.addTarget_action_forControlEvents_(
      self, SEL('selectedSegmentDidChange:'), UIControlEvents.valueChanged)

  @objc_method
  def configureActionBasedSegmentedControl_(self, segmentedControl):
    segmentedControl.selectedSegmentIndex = 0

    @Block
    def actionHandler_(_action: objc_id) -> None:
      action = ObjCInstance(_action)
      print(f'Segment Action "{action.title}"')

    firstAction = UIAction.actionWithHandler_(actionHandler_)
    firstAction.setTitle_(localizedString('CheckTitle'))
    segmentedControl.setAction_forSegmentAtIndex_(firstAction, 0)

    secondAction = UIAction.actionWithHandler_(actionHandler_)
    secondAction.setTitle_(localizedString('SearchTitle'))
    segmentedControl.setAction_forSegmentAtIndex_(secondAction, 1)

    thirdAction = UIAction.actionWithHandler_(actionHandler_)
    thirdAction.setTitle_(localizedString('ToolsTitle'))
    segmentedControl.setAction_forSegmentAtIndex_(thirdAction, 2)

  # MARK: - Actions
  @objc_method
  def selectedSegmentDidChange_(self, segmentedControl):
    print(f'The selected segment: {segmentedControl.selectedSegmentIndex}')

  # MARK: - UITableViewDataSource
  @objc_method  # todo: override
  def tableView_cellForRowAtIndexPath_(self, tableView,
                                       indexPath) -> ObjCInstance:

    cellTest = self.testCells[indexPath.section]
    cell = tableView.dequeueReusableCellWithIdentifier_forIndexPath_(
      cellTest.cellID, indexPath)

    if cellTest.targetView(cell).isMemberOfClass_(UISegmentedControl):
      if (segementedControl := cellTest.targetView(cell)):
        configHandlerName = str(cellTest.configHandlerName)

        self.performSelector_withObject_(SEL(configHandlerName),
                                         segementedControl)
    else:
      if (placeHolderView := cellTest.targetView(cell)):
        # The only non-segmented control cell has a placeholder UIView (for adding one as a subview).
        # 唯一の非セグメント化コントロール セルには、プレースホルダー UIView (サブビューとして追加するため) があります。
        # xxx: Python 上では、同じ処理
        configHandlerName = str(cellTest.configHandlerName)

        self.performSelector_withObject_(SEL(configHandlerName),
                                         placeHolderView)

    return cell


if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import (
    UITableViewStyle,
    UIModalPresentationStyle,
  )

  table_style = UITableViewStyle.grouped
  main_vc = SegmentedControlViewController.alloc().initWithStyle_(table_style)
  _title = NSStringFromClass(SegmentedControlViewController)
  main_vc.navigationItem.title = _title

  # presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

