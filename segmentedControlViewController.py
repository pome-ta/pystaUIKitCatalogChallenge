import ctypes
from enum import Enum
from pathlib import Path
import json

from pyrubicon.objc.api import ObjCClass, ObjCInstance, Block
from pyrubicon.objc.api import objc_method, objc_const
from pyrubicon.objc.runtime import SEL, send_super, objc_id, load_library
from pyrubicon.objc.types import CGSize, CGFloat, CGRectMake

from rbedge.enumerations import UITableViewStyle
from rbedge.functions import NSStringFromClass

from caseElement import CaseElement
from pyLocalizedString import localizedString
from baseTableViewController import BaseTableViewController
from storyboard.segmentedControlViewController import prototypes

from rbedge.enumerations import (
  UIControlEvents,
  UIUserInterfaceIdiom,
  UIUserInterfaceStyle,
  UIControlState,
  UIBarMetrics,
)

UIKit = load_library('UIKit')
UIImage = ObjCClass('UIImage')
UIAction = ObjCClass('UIAction')
UIScreen = ObjCClass('UIScreen')
NSURL = ObjCClass('NSURL')
NSData = ObjCClass('NSData')
UIImage = ObjCClass('UIImage')
UIColor = ObjCClass('UIColor')
UISegmentedControl = ObjCClass('UISegmentedControl')  # todo: 型呼び出し
UIFont = ObjCClass('UIFont')
UIFontDescriptor = ObjCClass('UIFontDescriptor')
NSAttributedString = ObjCClass('NSAttributedString')


def UIGraphicsBeginImageContextWithOptions(size: CGSize, opaque: bool,
                                           scale: CGFloat) -> ObjCInstance:
  _fnc = UIKit.UIGraphicsBeginImageContextWithOptions
  _fnc.restype = ctypes.c_void_p
  _fnc.argtypes = [
    CGSize,
    ctypes.c_bool,
    CGFloat,
  ]
  return ObjCInstance(_fnc(size, opaque, scale))


def UIGraphicsGetImageFromCurrentImageContext() -> ObjCInstance:
  _fnc = UIKit.UIGraphicsGetImageFromCurrentImageContext
  _fnc.restype = objc_id
  _fnc.argtypes = []
  return ObjCInstance(_fnc())


def UIGraphicsEndImageContext():
  _fnc = UIKit.UIGraphicsEndImageContext
  _fnc.restype = ctypes.c_void_p
  _fnc.argtypes = []
  _fnc()


def get_srgb_named_style(named: str,
                         userInterfaceStyle: UIUserInterfaceStyle) -> list:
  # todo: 本来`UIColor.colorNamed:` で呼び出す。asset(bundle) の取り込みが難しそうなので、独自に直で呼び出し
  _path = Path(
    f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/{named}.colorset/Contents.json'
  )
  _str = _path.read_text()
  _dict = json.loads(_str)

  def _pick_color(colors: list[dict], style: str | None = None) -> list:
    components: dict
    for color in colors:
      if color.get('idiom') != 'universal':
        continue
      appearance, *_ = appearances if (
        appearances := color.get('appearances')) is not None else [None]
      if style is None and appearance is None:
        components = color.get('color').get('components')
        break
      if appearance is not None and style == appearance.get('value'):
        components = color.get('color').get('components')
        break

    red, green, blue, alpha = (float(components.get(clr))
                               for clr in ('red', 'green', 'blue', 'alpha'))
    # wip: エラーハンドリング
    return [red, green, blue, alpha]

  color_dicts = _dict.get('colors')
  if userInterfaceStyle == UIUserInterfaceStyle.light:
    return _pick_color(color_dicts, 'light')
  elif userInterfaceStyle == UIUserInterfaceStyle.dark:
    return _pick_color(color_dicts, 'dark')
  else:
    return _pick_color(color_dicts)


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
  def init(self):
    send_super(__class__, self, 'init')  # xxx: 不要?
    tableViewStyle = UITableViewStyle.grouped
    self.initWithStyle_(tableViewStyle)

    self.testCells = []
    self.initPrototype()

    return self

  @objc_method
  def initPrototype(self):
    [
      self.tableView.registerClass_forCellReuseIdentifier_(
        prototype['cellClass'], prototype['identifier'])
      for prototype in prototypes
    ]

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?

    title = NSStringFromClass(__class__)
    self.navigationItem.title = title

    self.testCells.extend([
      CaseElement(localizedString('DefaultTitle'),
                  SegmentKind.segmentDefault.value,
                  self.configureDefaultSegmentedControl_),
      CaseElement(localizedString('CustomSegmentsTitle'),
                  SegmentKind.segmentCustom.value,
                  self.configureCustomSegmentsSegmentedControl_),
      CaseElement(localizedString('CustomBackgroundTitle'),
                  SegmentKind.segmentCustomBackground.value,
                  self.configureCustomBackgroundSegmentedControl_),
      CaseElement(localizedString('ActionBasedTitle'),
                  SegmentKind.segmentAction.value,
                  self.configureActionBasedSegmentedControl_),
    ])
    if self.traitCollection.userInterfaceIdiom != UIUserInterfaceIdiom.mac:
      # Tinted segmented control is only available on iOS.
      # ティント・セグメンテッド・コントロールはiOSでのみ利用可能。
      self.testCells.extend([
        CaseElement(localizedString('Tinted'), SegmentKind.segmentTinted.value,
                    self.configureTintedSegmentedControl_),
      ])
    '''
    self.testCells.extend([
      CaseElement(localizedString('DefaultTitle'),
                  SegmentKind.segmentDefault.value,
                  self.configureDefaultSegmentedControl_),
    ])
    

    self.testCells.extend([
      CaseElement(localizedString('CustomBackgroundTitle'),
                  SegmentKind.segmentCustomBackground.value,
                  self.configureCustomBackgroundSegmentedControl_),
    ])
    '''

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
    # ダイナミックな色合いの "グリーン "を使用する(ライト・アピアランス用とダーク・アピアランス用に分ける)。
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
    ]).autorelease()
    customBackgroundSegmentedControl.selectedSegmentIndex = 2

    # Place this custom segmented control within the placeholder view.
    # このカスタムのセグメント化されたコントロールをプレースホルダー ビュー内に配置します。

    customBackgroundSegmentedControl.frame.size.width = placeHolderView.frame.size.width
    customBackgroundSegmentedControl.frame.origin.y = (
      placeHolderView.bounds.size.height -
      customBackgroundSegmentedControl.bounds.size.height) / 2

    placeHolderView.addSubview_(customBackgroundSegmentedControl)

    scale = int(UIScreen.mainScreen.scale)
    normal_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/background.imageset/stepper_and_segment_background_{scale}x.png'
    highlighted_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/background_highlighted.imageset/stepper_and_segment_background_highlighted_{scale}x.png'
    disabled_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/background_disabled.imageset/stepper_and_segment_background_disabled_{scale}x.png'

    # xxx: あとで取り回し考える
    from pathlib import Path

    # xxx: `lambda` の使い方が悪い
    dataWithContentsOfURL = lambda path_str: NSData.dataWithContentsOfURL_(
      NSURL.fileURLWithPath_(str(Path(path_str).absolute())))

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
        objc_const(UIKit, 'UIFontTextStyleBody')), 0.0)

    normalTextAttributes = {
      str(objc_const(UIKit, 'NSForegroundColorAttributeName')):
      UIColor.systemPurpleColor(),
      str(objc_const(UIKit, 'NSFontAttributeName')):
      font,
    }
    customBackgroundSegmentedControl.setTitleTextAttributes_forState_(
      normalTextAttributes, UIControlState.normal)

    highlightedTextAttributes = {
      str(objc_const(UIKit, 'NSForegroundColorAttributeName')):
      UIColor.systemGreenColor(),
      str(objc_const(UIKit, 'NSFontAttributeName')):
      font,
    }
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
  # todo: override
  @objc_method
  def tableView_cellForRowAtIndexPath_(self, tableView, indexPath) -> objc_id:
    cellTest = self.testCells[indexPath.section]
    cell = tableView.dequeueReusableCellWithIdentifier_forIndexPath_(
      cellTest.cellID, indexPath)
    # The only non-segmented control cell has a placeholder UIView (for adding one as a subview).
    # 唯一の非セグメント化コントロール セルには、プレースホルダー UIView (サブビューとして追加するため) があります。
    # xxx: Python 上では、同じ処理

    if cellTest.targetView(cell).isMemberOfClass_(UISegmentedControl):

      if (segementedControl := cellTest.targetView(cell)):
        cellTest.configHandler(segementedControl)
    else:
      if (placeHolderView := cellTest.targetView(cell)):
        cellTest.configHandler(placeHolderView)

    return cell


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  main_vc = SegmentedControlViewController.new()
  #style = UIModalPresentationStyle.pageSheet
  style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, style)

