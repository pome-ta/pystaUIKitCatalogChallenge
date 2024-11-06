from enum import Enum
from pathlib import Path

from pyrubicon.objc.api import ObjCClass, ObjCInstance, Block
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import SEL, send_super, objc_id
#from pyrubicon.objc.types import CGSize, CGFloat, CGRectMake, CGSizeMake

from rbedge.enumerations import (
  UITableViewStyle,
  UIControlEvents,
  UIControlState,
  UIUserInterfaceIdiom,
  UIImageSymbolScale,
  UIImageSymbolWeight,
)
from rbedge.functions import NSStringFromClass

from caseElement import CaseElement
from pyLocalizedString import localizedString

from baseTableViewController import BaseTableViewController
from storyboard.sliderViewController import prototypes

UIScreen = ObjCClass('UIScreen')
NSURL = ObjCClass('NSURL')
NSData = ObjCClass('NSData')
UIImage = ObjCClass('UIImage')
UIImageSymbolConfiguration = ObjCClass('UIImageSymbolConfiguration')


# Cell identifier for each slider table view cell.
# スライダー テーブル ビューの各セルのセル識別子。
class SliderKind(Enum):
  sliderDefault = 'sliderDefault'
  sliderTinted = 'sliderTinted'
  sliderCustom = 'sliderCustom'
  sliderMaxMinImage = 'sliderMaxMinImage'


class SliderViewController(BaseTableViewController):

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
                  SliderKind.sliderDefault.value,
                  self.configureDefaultSlider_),
    ])
    # todo: `@available(iOS 15.0, *)`
    self.testCells.extend([
      CaseElement(localizedString('CustomTitle'),
                  SliderKind.sliderCustom.value, self.configureCustomSlider_),
      CaseElement(localizedString('MinMaxImagesTitle'),
                  SliderKind.sliderMaxMinImage.value,
                  self.configureMinMaxImageSlider_),
      CaseElement(localizedString('TintedTitle'),
                  SliderKind.sliderTinted.value,
                  self.configureTintedSlider_),
    ])

  # MARK: - Configuration
  @objc_method
  def configureDefaultSlider_(self, slider):
    slider.minimumValue = 0
    slider.maximumValue = 100
    slider.value = 42
    slider.isContinuous = True

    slider.addTarget_action_forControlEvents_(self,
                                              SEL('sliderValueDidChange:'),
                                              UIControlEvents.valueChanged)

  # todo: `@available(iOS 15.0, *)`
  @objc_method
  def configureTintedSlider_(self, slider):
    '''
    To keep the look the same betwen iOS and macOS:
    For minimumTrackTintColor, maximumTrackTintColor to work in Mac Catalyst, use UIBehavioralStyle as ".pad",
    Available in macOS 12 or later (Mac Catalyst 15.0 or later).
    Use this for controls that need to look the same between iOS and macOS.
    '''
    '''
    iOS と macOS で見た目を同じにするには:
    minimumTrackTintColor、maximumTrackTintColor を Mac Catalyst で機能させるには、UIBehavioralStyle を「.pad」として使用します。
    macOS 12以降(Mac Catalyst 15.0以降)で利用可能です。
    iOS と macOS の間で同じように見える必要があるコントロールにこれを使用します。
    '''
    pass
  # todo: `@available(iOS 15.0, *)`
  @objc_method
  def configureCustomSlider_(self, slider):
    '''
    To keep the look the same betwen iOS and macOS:
    For setMinimumTrackImage, setMaximumTrackImage, setThumbImage to work in Mac Catalyst, use UIBehavioralStyle as ".pad",
    Available in macOS 12 or later (Mac Catalyst 15.0 or later).
    Use this for controls that need to look the same between iOS and macOS.
    '''
    '''
    iOS と macOS で見た目を同じにするには:
    setMinimumTrackImage、setMinimumTrackImage、setThumbImage を Mac Catalyst で動作させるには、UIBehavioralStyle を「.pad」として使用します。
    macOS 12以降(Mac Catalyst 15.0以降)で利用可能です。
    iOS と macOS の間で同じように見える必要があるコントロールにこれを使用します。
    '''
    # To keep the look the same betwen iOS and macOS:
    #   For setMinimumTrackImage, setMaximumTrackImage, setThumbImage to work in Mac Catalyst, use UIBehavioralStyle as ".pad",
    #   Available in macOS 12 or later (Mac Catalyst 15.0 or later).
    #   Use this for controls that need to look the same between iOS and macOS.
    # iOSとmacOSで見た目を同じにするため:
    #  setMinimumTrackImage、setMaximumTrackImage、setThumbImageをMac Catalystで動作させるには、UIBehavioralStyleを".pad "として使用します。
    #  iOSとmacOSで同じ外観にする必要があるコントロールに使用します。

    scale = int(UIScreen.mainScreen.scale)
    leftTrack_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/slider_blue_track.imageset/slider_blue_track_{scale}x.png'
    rightTrack_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/slider_green_track.imageset/slider_green_track_{scale}x.png'

    # xxx: `lambda` の使い方が悪い
    dataWithContentsOfURL = lambda path_str: NSData.dataWithContentsOfURL_(
      NSURL.fileURLWithPath_(str(Path(path_str).absolute())))

    leftTrackImage = UIImage.alloc().initWithData_scale_(
      dataWithContentsOfURL(leftTrack_str), scale)
    rightTrackImage = UIImage.alloc().initWithData_scale_(
      dataWithContentsOfURL(rightTrack_str), scale)

    slider.setMinimumTrackImage_forState_(leftTrackImage,
                                          UIControlState.normal)
    slider.setMaximumTrackImage_forState_(rightTrackImage,
                                          UIControlState.normal)

    # Set the sliding thumb image (normal and highlighted).
    # スライドサム画像(通常およびハイライト)を設定します。
    # For fun, choose a different image symbol configuraton for the thumb's image between macOS and iOS.
    # お楽しみとして、macOS と iOS の間でサムの画像に異なる画像シンボル構成を選択してください。
    thumbImageConfig: 'UIImage.SymbolConfiguration'
    if slider.traitCollection.userInterfaceIdiom == UIUserInterfaceIdiom.mac:
      thumbImageConfig = UIImageSymbolConfiguration.configurationWithScale_(
        UIImageSymbolScale.large)
    else:
      thumbImageConfig = UIImageSymbolConfiguration.configurationWithPointSize_weight_scale_(
        30.0, UIImageSymbolWeight.heavy, UIImageSymbolScale.large)
    thumbImage = UIImage.systemImageNamed_withConfiguration_(
      'circle.fill', thumbImageConfig)
    thumbImageHighlighted = UIImage.systemImageNamed_withConfiguration_(
      'circle', thumbImageConfig)

    slider.setThumbImage_forState_(thumbImage, UIControlState.normal)

    slider.setThumbImage_forState_(thumbImageHighlighted,
                                   UIControlState.highlighted)

    slider.minimumValue = 0
    slider.maximumValue = 100
    slider.isContinuous = False
    slider.value = 84

    slider.addTarget_action_forControlEvents_(self,
                                              SEL('sliderValueDidChange:'),
                                              UIControlEvents.valueChanged)

  @objc_method
  def configureMinMaxImageSlider_(self, slider):
    '''
    To keep the look the same betwen iOS and macOS:
    For setMinimumValueImage, setMaximumValueImage to work in Mac Catalyst, use UIBehavioralStyle as ".pad",
    Available in macOS 12 or later (Mac Catalyst 15.0 or later).
    Use this for controls that need to look the same between iOS and macOS.
    '''
    '''
    iOSとmacOSで見た目を同じにするためです:
    Mac CatalystでsetMinimumValueImage、setMaximumValueImageを動作させるには、UIBehavioralStyleを".pad "として使用してください、
    macOS 12以降(Mac Catalyst 15.0以降)で使用できます。
    iOSとmacOSで同じ外観にする必要があるコントロールに使用します。
    '''
    # xxx: あとで調整
    if True:  # xxx: `#available(iOS 15, *)`
      if True:  # xxx: `traitCollection.userInterfaceIdiom != .mac`
        pass

    slider.minimumValueImage = UIImage.systemImageNamed_('tortoise')
    slider.maximumValueImage = UIImage.systemImageNamed_('hare')

    slider.addTarget_action_forControlEvents_(self,
                                              SEL('sliderValueDidChange:'),
                                              UIControlEvents.valueChanged)

  # MARK: - Actions
  @objc_method
  def sliderValueDidChange_(self, slider):
    formattedValue = f'{slider.value:.2f}'
    print(f'Slider changed its value: {formattedValue}')


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  main_vc = SliderViewController.new()
  #style = UIModalPresentationStyle.pageSheet
  style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, style)

