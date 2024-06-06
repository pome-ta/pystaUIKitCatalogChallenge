import ctypes
from enum import Enum

from pyrubicon.objc.api import ObjCClass, objc_method, objc_property, objc_const
from pyrubicon.objc.runtime import SEL, send_super, load_library
from pyrubicon.objc.types import NSInteger

from rbedge.enumerations import (
  UIControlState,
  UIControlEvents,
  UIListContentTextAlignment,
  UITableViewStyle,
  UIButtonConfigurationCornerStyle,
  UIImageRenderingMode,
  NSUnderlineStyle,
  UIImageSymbolScale,
  NSDirectionalRectEdge,
  UIButtonConfigurationSize,
)
from rbedge.functions import NSStringFromClass

from caseElement import CaseElement
from pyLocalizedString import localizedString

from storyboard.buttonViewController import prototypes

UITableViewController = ObjCClass('UITableViewController')
UITableViewHeaderFooterView = ObjCClass('UITableViewHeaderFooterView')
UIListContentConfiguration = ObjCClass('UIListContentConfiguration')

# todo: extension
from pyrubicon.objc.api import Block, ObjCInstance
from pyrubicon.objc.runtime import objc_id
from pyrubicon.objc.types import CGPoint

UIKit = load_library('UIKit')
UIButtonConfiguration = ObjCClass('UIButtonConfiguration')
UIColor = ObjCClass('UIColor')
UIImage = ObjCClass('UIImage')
NSAttributedString = ObjCClass('NSAttributedString')
UIImageSymbolConfiguration = ObjCClass('UIImageSymbolConfiguration')
UIFont = ObjCClass('UIFont')
UIScreen = ObjCClass('UIScreen')
NSURL = ObjCClass('NSURL')
NSData = ObjCClass('NSData')
UIImage = ObjCClass('UIImage')
UIToolTipConfiguration = ObjCClass('UIToolTipConfiguration')
UIAction = ObjCClass('UIAction')


class BaseTableViewController(UITableViewController):

  testCells: list[CaseElement] = []

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要？
    self.tableView.registerClass_forHeaderFooterViewReuseIdentifier_(
      UITableViewHeaderFooterView, 'customHeaderFooterView')

  @objc_method
  def centeredHeaderView_(self, title):
    # todo: let headerView: UITableViewHeaderFooterView = UITableViewHeaderFooterView()
    headerView = self.tableView.dequeueReusableHeaderFooterViewWithIdentifier_(
      'customHeaderFooterView')

    content = UIListContentConfiguration.groupedHeaderConfiguration()
    content.text = title
    content.textProperties.alignment = UIListContentTextAlignment.center
    headerView.contentConfiguration = content

    return headerView

  # MARK: - UITableViewDataSource
  @objc_method
  def tableView_viewForHeaderInSection_(self, tableView,
                                        section: NSInteger) -> ctypes.c_void_p:
    return self.centeredHeaderView_(self.testCells[section].title).ptr

  @objc_method
  def tableView_titleForHeaderInSection_(self, tableView, section: NSInteger):
    return self.testCells[section].title

  @objc_method
  def tableView_numberOfRowsInSection_(self, tableView,
                                       section: NSInteger) -> NSInteger:
    return 1

  @objc_method
  def numberOfSectionsInTableView_(self, tableView) -> NSInteger:
    return len(self.testCells)

  @objc_method
  def tableView_cellForRowAtIndexPath_(self, tableView,
                                       indexPath) -> ctypes.c_void_p:
    cellTest = self.testCells[indexPath.section]
    cell = tableView.dequeueReusableCellWithIdentifier_forIndexPath_(
      cellTest.cellID, indexPath)

    if (view := cellTest.targetView(cell)):
      cellTest.configHandler(view)

    return cell.ptr


class ButtonKind(Enum):
  buttonSystem = 'buttonSystem'
  buttonDetailDisclosure = 'buttonDetailDisclosure'
  buttonSystemAddContact = 'buttonSystemAddContact'
  buttonClose = 'buttonClose'
  buttonStyleGray = 'buttonStyleGray'
  buttonStyleTinted = 'buttonStyleTinted'
  buttonStyleFilled = 'buttonStyleFilled'
  buttonCornerStyle = 'buttonCornerStyle'
  buttonToggle = 'buttonToggle'
  buttonTitleColor = 'buttonTitleColor'
  buttonImage = 'buttonImage'
  buttonAttrText = 'buttonAttrText'
  buttonSymbol = 'buttonSymbol'
  buttonLargeSymbol = 'buttonLargeSymbol'
  buttonTextSymbol = 'buttonTextSymbol'
  buttonSymbolText = 'buttonSymbolText'
  buttonMultiTitle = 'buttonMultiTitle'
  buttonBackground = 'buttonBackground'
  addToCartButton = 'addToCartButton'
  buttonUpdateActivityHandler = 'buttonUpdateActivityHandler'
  buttonUpdateHandler = 'buttonUpdateHandler'
  buttonImageUpdateHandler = 'buttonImageUpdateHandler'


class ButtonViewController(BaseTableViewController):
  cartItemCount = objc_property(int)

  @objc_method
  def init(self):
    send_super(__class__, self, 'init')  # xxx: 不要？
    tableViewStyle = UITableViewStyle.grouped
    self.initWithStyle_(tableViewStyle)

    self.testCells = []
    self.cartItemCount = 0

    return self

  @objc_method
  def initPrototype(self):
    [
      self.tableView.registerClass_forCellReuseIdentifier_(
        prototype['cellClass'], prototype['identifier'])
      for prototype in prototypes
    ]

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要？

    title = NSStringFromClass(__class__)
    self.navigationItem.title = title

    self.initPrototype()
    # --- test
    self.testCells.extend([
      # 20
      CaseElement(localizedString('AddToCartTitle'),
                  ButtonKind.addToCartButton.value,
                  self.configureAddToCartButton_),
    ])
    '''
    self.testCells.extend([
      # 00
      CaseElement(localizedString('DefaultTitle'),
                  ButtonKind.buttonSystem.value,
                  self.configureSystemTextButton_),
      # 01
      CaseElement(localizedString('DetailDisclosureTitle'),
                  ButtonKind.buttonDetailDisclosure.value,
                  self.configureSystemDetailDisclosureButton_),
      # 02
      CaseElement(localizedString('AddContactTitle'),
                  ButtonKind.buttonSystemAddContact.value,
                  self.configureSystemContactAddButton_),
      # 03
      CaseElement(localizedString('CloseTitle'), ButtonKind.buttonClose.value,
                  self.configureCloseButton_),
    ])
    # xxx: 'if #available(iOS 15, *)'
    # These button styles are available on iOS 15 or later.
    self.testCells.extend([
      # 04
      CaseElement(localizedString('GrayTitle'),
                  ButtonKind.buttonStyleGray.value,
                  self.configureStyleGrayButton_),
      # 05
      CaseElement(localizedString('TintedTitle'),
                  ButtonKind.buttonStyleTinted.value,
                  self.configureStyleTintedButton_),
      # 06
      CaseElement(localizedString('FilledTitle'),
                  ButtonKind.buttonStyleFilled.value,
                  self.configureStyleFilledButton_),
      # 07
      CaseElement(localizedString('CornerStyleTitle'),
                  ButtonKind.buttonCornerStyle.value,
                  self.configureCornerStyleButton_),
    ])

    self.testCells.extend([
      # 0
      CaseElement(localizedString('ImageTitle'), ButtonKind.buttonImage.value,
                  self.configureImageButton_),
      # 9
      CaseElement(localizedString('AttributedStringTitle'),
                  ButtonKind.buttonAttrText.value,
                  self.configureAttributedTextSystemButton_),
      # 10
      CaseElement(localizedString('SymbolTitle'),
                  ButtonKind.buttonSymbol.value, self.configureSymbolButton_),
    ])
    
    if True:  # xxx: `#available(iOS 15, *)`
      self.testCells.extend([
        # 11
        CaseElement(localizedString('LargeSymbolTitle'),
                    ButtonKind.buttonLargeSymbol.value,
                    self.configureLargeSymbolButton_),
      ])
      
    # xxx: あとで並べる
    # 12
      CaseElement(localizedString('SymbolStringTitle'),
                  ButtonKind.buttonSymbolText.value,
                  self.configureSymbolTextButton_),
    
    # 13
      CaseElement(localizedString('StringSymbolTitle'),
                  ButtonKind.buttonTextSymbol.value,
                  self.configureTextSymbolButton_),
    
    # 14
      CaseElement(localizedString('MultiTitleTitle'),
                  ButtonKind.buttonMultiTitle.value,
                  self.configureMultiTitleButton_),
    # 15
      CaseElement(localizedString('ToggleTitle'),
                  ButtonKind.buttonToggle.value,
                  self.configureToggleButton_),
      # 16
      CaseElement(localizedString('ButtonColorTitle'),
                  ButtonKind.buttonTitleColor.value,
                  self.configureTitleTextButton_),
    # 17
      CaseElement(localizedString('BackgroundTitle'),
                  ButtonKind.buttonBackground.value,
                  self.configureBackgroundButton_),
    
    # 18
      CaseElement(localizedString('UpdateActivityHandlerTitle'),
                  ButtonKind.buttonUpdateActivityHandler.value,
                  self.configureUpdateActivityHandlerButton_),
      # 19
      CaseElement(localizedString('UpdateHandlerTitle'),
                  ButtonKind.buttonUpdateHandler.value,
                  self.configureUpdateHandlerButton_),
      # 20
      CaseElement(localizedString('UpdateImageHandlerTitle'),
                  ButtonKind.buttonImageUpdateHandler.value,
                  self.configureUpdateImageHandlerButton_),
          
    
    '''

  @objc_method
  def viewDidDisappear_(self, animated: bool):
    send_super(__class__, self, 'viewDidDisappear:')

  # --- extension
  # xxx: extension 別にしたい
  # 00
  @objc_method
  def configureSystemTextButton_(self, button):
    # Nothing particular to set here, it's all been done in the storyboard.
    # > ここでは特に設定するものはなく、すべてストーリーボードで行われます。
    # todo: 冗長、差し替えを容易にしたい為
    title = localizedString('Button')
    state = UIControlState.normal
    button.setTitle_forState_(title, state)

    button.addTarget_action_forControlEvents_(self, SEL('buttonClicked:'),
                                              UIControlEvents.touchUpInside)

  # 01
  @objc_method
  def configureSystemDetailDisclosureButton_(self, button):
    button.addTarget_action_forControlEvents_(self, SEL('buttonClicked:'),
                                              UIControlEvents.touchUpInside)

  # 02
  @objc_method
  def configureSystemContactAddButton_(self, button):
    button.addTarget_action_forControlEvents_(self, SEL('buttonClicked:'),
                                              UIControlEvents.touchUpInside)

  # 03
  @objc_method
  def configureCloseButton_(self, button):
    button.addTarget_action_forControlEvents_(self, SEL('buttonClicked:'),
                                              UIControlEvents.touchUpInside)

  # 04
  # todo: `@available(iOS 15.0, *)`
  # xxx: あとでやる
  @objc_method
  def configureStyleGrayButton_(self, button):
    config = UIButtonConfiguration.grayButtonConfiguration()
    button.configuration = config

    title = localizedString('Button')
    state = UIControlState.normal
    button.setTitle_forState_(title, state)

    # xxx: `toolTip` 挙動未確認
    button.toolTip = localizedString('GrayStyleButtonToolTipTitle')

    button.addTarget_action_forControlEvents_(self, SEL('buttonClicked:'),
                                              UIControlEvents.touchUpInside)

  # 05
  # todo: `@available(iOS 15.0, *)`
  @objc_method
  def configureStyleTintedButton_(self, button):
    config = UIButtonConfiguration.tintedButtonConfiguration()
    # todo: `if traitCollection.userInterfaceIdiom == .mac`
    # xxx: あとでやる
    systemRed = UIColor.systemRedColor()
    config.baseBackgroundColor = systemRed
    config.baseForegroundColor = systemRed

    button.configuration = config

    title = localizedString('Button')
    state = UIControlState.normal
    button.setTitle_forState_(title, state)

    button.toolTip = localizedString('TintedStyleButtonToolTipTitle')

    button.addTarget_action_forControlEvents_(self, SEL('buttonClicked:'),
                                              UIControlEvents.touchUpInside)

  # 06
  # todo: `@available(iOS 15.0, *)`
  @objc_method
  def configureStyleFilledButton_(self, button):
    config = UIButtonConfiguration.filledButtonConfiguration()

    systemRed = UIColor.systemRedColor()
    config.background.backgroundColor = systemRed

    button.configuration = config

    title = localizedString('Button')
    state = UIControlState.normal
    button.setTitle_forState_(title, state)

    button.toolTip = localizedString('FilledStyleButtonToolTipTitle')

    button.addTarget_action_forControlEvents_(self, SEL('buttonClicked:'),
                                              UIControlEvents.touchUpInside)

  # 07
  # todo: `@available(iOS 15.0, *)`
  @objc_method
  def configureCornerStyleButton_(self, button):
    # To keep the look the same betwen iOS and macOS:
    # For cornerStyle to work in Mac Catalyst, use UIBehavioralStyle as ".pad", Available in macOS 12 or later (Mac Catalyst 15.0 or later). Use this for controls that need to look the same between iOS and macOS.
    # > iOS と macOS の間で外観を同じにするには: CornerStyle を Mac Catalyst で機能させるには、UIBehavioralStyle を「.pad」として使用します。macOS 12 以降 (Mac Catalyst 15.0 以降) で使用できます。 iOS と macOS の間で同じように見える必要があるコントロールにこれを使用します。

    config = UIButtonConfiguration.grayButtonConfiguration()

    # todo: `if traitCollection.userInterfaceIdiom == .mac`
    # xxx: あとでやる
    cornerStyle = UIButtonConfigurationCornerStyle.capsule
    config.cornerStyle = cornerStyle

    button.configuration = config

    title = localizedString('Button')
    state = UIControlState.normal
    button.setTitle_forState_(title, state)

    button.toolTip = localizedString('CapsuleStyleButtonToolTipTitle')

    button.addTarget_action_forControlEvents_(self, SEL('buttonClicked:'),
                                              UIControlEvents.touchUpInside)

  # 08
  @objc_method
  def configureImageButton_(self, button):
    _systemImageNamed = UIImage.systemImageNamed('xmark')

    systemPurple = UIColor.systemPurpleColor()
    renderingMode = UIImageRenderingMode.alwaysOriginal
    # ref: [swift - iOS 13 `withTintColor` not obeying the color I assign - Stack Overflow](https://stackoverflow.com/questions/58867627/ios-13-withtintcolor-not-obeying-the-color-i-assign)

    image = _systemImageNamed.imageWithTintColor_(
      systemPurple).imageWithRenderingMode_(renderingMode)
    button.accessibilityLabel = localizedString('X')

    state = UIControlState.normal
    button.setImage_forState_(image, state)

    # todo: `@available(iOS 15.0, *)`
    button.toolTip = localizedString('XButtonToolTipTitle')

    button.addTarget_action_forControlEvents_(self, SEL('buttonClicked:'),
                                              UIControlEvents.touchUpInside)

  # 09
  # todo: `@available(iOS 15.0, *)`
  @objc_method
  def configureAttributedTextSystemButton_(self, button):
    buttonTitle = localizedString('Button')

    # Set the button's title for normal state.
    # > 通常状態のボタンのタイトルを設定します。
    normalTitleAttributes = {
      str(objc_const(UIKit, 'NSStrikethroughStyleAttributeName')):
      NSUnderlineStyle.single,
    }
    normalAttributedTitle = NSAttributedString.alloc(
    ).initWithString_attributes_(buttonTitle, normalTitleAttributes)

    normal = UIControlState.normal
    button.setAttributedTitle_forState_(normalAttributedTitle, normal)

    # Set the button's title for highlighted state (note this is not supported in Mac Catalyst).
    # > ボタンのタイトルを強調表示状態に設定します (これは Mac Catalyst ではサポートされていないことに注意してください)。
    highlightedTitleAttributes = {
      str(objc_const(UIKit, 'NSForegroundColorAttributeName')):
      UIColor.systemGreenColor(),
      str(objc_const(UIKit, 'NSStrikethroughStyleAttributeName')):
      NSUnderlineStyle.thick,
    }
    highlightedAttributedTitle = NSAttributedString.alloc(
    ).initWithString_attributes_(buttonTitle, highlightedTitleAttributes)

    highlighted = UIControlState.highlighted
    button.setAttributedTitle_forState_(highlightedAttributedTitle,
                                        highlighted)
    button.addTarget_action_forControlEvents_(self, SEL('buttonClicked:'),
                                              UIControlEvents.touchUpInside)

  # 10
  @objc_method
  def configureSymbolButton_(self, button):
    buttonImage = UIImage.systemImageNamed('person')

    if True:  # xxx: `available(iOS 15, *)`
      # For iOS 15 use the UIButtonConfiguration to set the image.
      # iOS 15 の場合は、UIButtonConfiguration を使用して画像を設定します。
      buttonConfig = UIButtonConfiguration.plainButtonConfiguration()
      buttonConfig.image = buttonImage
      button.configuration = buttonConfig
      button.toolTip = localizedString('PersonButtonToolTipTitle')
    else:
      button.setImage_forState_(buttonImage, UIControlState.normal)

    config = UIImageSymbolConfiguration.configurationWithTextStyle_scale_(
      str(objc_const(UIKit, 'UIFontTextStyleBody')), UIImageSymbolScale.large)

    button.setPreferredSymbolConfiguration_forImageInState_(
      config, UIControlState.normal)

    button.accessibilityLabel = localizedString('Person')

    button.addTarget_action_forControlEvents_(self, SEL('buttonClicked:'),
                                              UIControlEvents.touchUpInside)

  # 11
  @objc_method
  def configureLargeSymbolButton_(self, button):
    buttonImage = UIImage.systemImageNamed('person')

    if True:  # xxx: `available(iOS 15, *)`
      # For iOS 15 use the UIButtonConfiguration to set the image.
      # iOS 15 の場合は、UIButtonConfiguration を使用して画像を設定します。
      buttonConfig = UIButtonConfiguration.plainButtonConfiguration()

      buttonConfig.preferredSymbolConfigurationForImage = UIImageSymbolConfiguration.configurationWithTextStyle_(
        str(objc_const(UIKit, 'UIFontTextStyleLargeTitle')))

      buttonConfig.image = buttonImage
      button.configuration = buttonConfig

    else:
      button.setImage_forState_(buttonImage, UIControlState.normal)

    button.accessibilityLabel = localizedString('Person')

    button.addTarget_action_forControlEvents_(self, SEL('buttonClicked:'),
                                              UIControlEvents.touchUpInside)

  # 12
  @objc_method
  def configureSymbolTextButton_(self, button):
    # Button with image to the left of the title.
    # > タイトルの左側にある画像付きのボタン。
    buttonImage = UIImage.systemImageNamed('person')

    if True:  # xxx: `available(iOS 15, *)`
      # For iOS 15 use the UIButtonConfiguration to set the image.
      # iOS 15 の場合は、UIButtonConfiguration を使用して画像を設定します。
      buttonConfig = UIButtonConfiguration.plainButtonConfiguration()

      buttonConfig.preferredSymbolConfigurationForImage = UIImageSymbolConfiguration.configurationWithTextStyle_(
        str(objc_const(UIKit, 'UIFontTextStyleBody')))

      buttonConfig.image = buttonImage
      button.configuration = buttonConfig

    else:
      button.setImage_forState_(buttonImage, UIControlState.normal)
      config = UIImageSymbolConfiguration.configurationWithTextStyle_scale_(
        str(objc_const(UIKit, 'UIFontTextStyleBody')),
        UIImageSymbolScale.small)
      button.setPreferredSymbolConfiguration_forImageInState_(
        config, UIControlState.normal)

    button.setTitle_forState_(localizedString('Person'), UIControlState.normal)

    button.titleLabel.font = UIFont.preferredFontForTextStyle_(
      str(objc_const(UIKit, 'UIFontTextStyleBody')))

    button.addTarget_action_forControlEvents_(self, SEL('buttonClicked:'),
                                              UIControlEvents.touchUpInside)

  # 13
  @objc_method
  def configureTextSymbolButton_(self, button):
    # Button with image to the right of the title.
    # > タイトルの右側にある画像付きのボタン。
    buttonImage = UIImage.systemImageNamed('person')

    if True:  # xxx: `available(iOS 15, *)`
      buttonConfig = UIButtonConfiguration.plainButtonConfiguration()

      buttonConfig.preferredSymbolConfigurationForImage = UIImageSymbolConfiguration.configurationWithTextStyle_(
        str(objc_const(UIKit, 'UIFontTextStyleBody')))

      buttonConfig.image = buttonImage

      #if traitCollection.userInterfaceIdiom == .mac
      #  button.preferredBehavioralStyle = .pad
      buttonConfig.imagePlacement = NSDirectionalRectEdge.trailing
      button.configuration = buttonConfig

    button.setTitle_forState_(localizedString('Person'), UIControlState.normal)

    button.titleLabel.font = UIFont.preferredFontForTextStyle_(
      str(objc_const(UIKit, 'UIFontTextStyleBody')))

    button.addTarget_action_forControlEvents_(self, SEL('buttonClicked:'),
                                              UIControlEvents.touchUpInside)

  # 14
  @objc_method
  def configureMultiTitleButton_(self, button):
    #if traitCollection.userInterfaceIdiom == .mac
    #  button.preferredBehavioralStyle = .pad
    button.setTitle_forState_(localizedString('Button'), UIControlState.normal)
    button.setTitle_forState_(localizedString('Person'),
                              UIControlState.highlighted)

    button.addTarget_action_forControlEvents_(self, SEL('buttonClicked:'),
                                              UIControlEvents.touchUpInside)

  # 15
  @objc_method
  def configureToggleButton_(self, button):
    button.changesSelectionAsPrimaryAction = True

  # 16
  @objc_method
  def configureTitleTextButton_(self, button):
    # Note: Only for iOS the title's color can be changed.
    # 注: タイトルの色を変更できるのは iOS の場合のみです。
    button.setTitleColor_forState_(UIColor.systemGreenColor(),
                                   UIControlState.normal)
    button.setTitleColor_forState_(UIColor.systemRedColor(),
                                   UIControlState.highlighted)

    button.addTarget_action_forControlEvents_(self, SEL('buttonClicked:'),
                                              UIControlEvents.touchUpInside)

  # 17
  @objc_method
  def configureBackgroundButton_(self, button):
    if True:  # xxx: `available(iOS 15, *)`
      #if traitCollection.userInterfaceIdiom == .mac
      #  button.preferredBehavioralStyle = .pad
      pass
    # ref: [iphone - Retina display and [UIImage initWithData] - Stack Overflow](https://stackoverflow.com/questions/3289286/retina-display-and-uiimage-initwithdata)
    # xxx: scale 指定これでいいのかな?
    scale = int(UIScreen.mainScreen.scale)
    normal_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/background.imageset/stepper_and_segment_background_{scale}x.png'
    highlighted_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/background_highlighted.imageset/stepper_and_segment_background_highlighted_{scale}x.png'
    disabled_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/background_disabled.imageset/stepper_and_segment_background_disabled_{scale}x.png'

    # xxx: あとで取り回し考える
    from pathlib import Path

    # xxx: `lambda` の使い方が悪い
    dataWithContentsOfURL = lambda path_str: NSData.dataWithContentsOfURL_(
      NSURL.fileURLWithPath_(str(Path(path_str).absolute())))

    background = UIImage.alloc().initWithData_scale_(
      dataWithContentsOfURL(normal_str), scale)

    background_highlighted = UIImage.alloc().initWithData_scale_(
      dataWithContentsOfURL(highlighted_str), scale)

    background_disabled = UIImage.alloc().initWithData_scale_(
      dataWithContentsOfURL(disabled_str), scale)

    button.setBackgroundImage_forState_(background, UIControlState.normal)
    button.setBackgroundImage_forState_(background_highlighted,
                                        UIControlState.highlighted)

    button.setBackgroundImage_forState_(background_disabled,
                                        UIControlState.disabled)

    button.addTarget_action_forControlEvents_(self, SEL('buttonClicked:'),
                                              UIControlEvents.touchUpInside)

  # 18
  # This handler is called when this button needs updating.
  # このハンドラーは、このボタンを更新する必要がある場合に呼び出されます。
  @objc_method
  def configureUpdateActivityHandlerButton_(self, button):

    @Block
    def activityUpdateHandler(button_id: objc_id) -> None:
      _button = ObjCInstance(button_id)

      config = _button.configuration
      config.showsActivityIndicator = False if _button.isSelected() else True
      _button.configuration = config

    buttonConfig = UIButtonConfiguration.plainButtonConfiguration()
    buttonConfig.image = UIImage.systemImageNamed('tray')
    buttonConfig.preferredSymbolConfigurationForImage = UIImageSymbolConfiguration.configurationWithTextStyle_(
      str(objc_const(UIKit, 'UIFontTextStyleBody')))

    button.configuration = buttonConfig

    button.setTitle_forState_(localizedString('Button'), UIControlState.normal)

    button.titleLabel.font = UIFont.preferredFontForTextStyle_(
      str(objc_const(UIKit, 'UIFontTextStyleBody')))

    button.changesSelectionAsPrimaryAction = True
    button.configurationUpdateHandler = activityUpdateHandler

    #if traitCollection.userInterfaceIdiom == .mac
    #  button.preferredBehavioralStyle = .pad

    button.addTarget_action_forControlEvents_(self,
                                              SEL('toggleButtonClicked:'),
                                              UIControlEvents.touchUpInside)

  # 19
  @objc_method
  def configureUpdateHandlerButton_(self, button):
    # This is called when a button needs an update.
    # > これは、ボタンを更新する必要がある場合に呼び出されます。

    @Block
    def colorUpdateHandler(button_id: objc_id) -> None:
      _button = ObjCInstance(button_id)
      _title = _button.configuration.title

      _systemPinkColor = UIColor.systemPinkColor()

      baseBackgroundColor = _systemPinkColor.colorWithAlphaComponent_(
        0.4) if _button.isSelected() else _systemPinkColor

      # xxx: `button.configuration?.baseBackgroundColor` を直接呼んでも変化しないので再定義している
      buttonConfig = UIButtonConfiguration.filledButtonConfiguration()
      buttonConfig.title = _title
      buttonConfig.baseBackgroundColor = baseBackgroundColor
      _button.configuration = buttonConfig

    buttonConfig = UIButtonConfiguration.filledButtonConfiguration()
    button.configuration = buttonConfig

    button.changesSelectionAsPrimaryAction = True
    button.configurationUpdateHandler = colorUpdateHandler

    #if traitCollection.userInterfaceIdiom == .mac
    #  button.preferredBehavioralStyle = .pad

    button.addTarget_action_forControlEvents_(self,
                                              SEL('toggleButtonClicked:'),
                                              UIControlEvents.touchUpInside)

  # 20
  @objc_method
  def configureUpdateImageHandlerButton_(self, button):
    # This is called when a button needs an update.
    # > これは、ボタンを更新する必要がある場合に呼び出されます。

    @Block
    def colorUpdateHandler(button_id: objc_id) -> None:
      _button = ObjCInstance(button_id)

      image = UIImage.systemImageNamed('cart.fill') if _button.isSelected(
      ) else UIImage.systemImageNamed('cart')
      # xxx: `button.configuration?.image` を直接呼んでも変化しないので再定義している
      buttonConfig = UIButtonConfiguration.plainButtonConfiguration()
      buttonConfig.image = image
      buttonConfig.preferredSymbolConfigurationForImage = UIImageSymbolConfiguration.configurationWithTextStyle_(
        str(objc_const(UIKit, 'UIFontTextStyleLargeTitle')))
      _button.configuration = buttonConfig

      # xxx: `toolTip` 挙動未確認
      _button.toolTip = localizedString(
        'CartFilledButtonToolTipTitle') if _button.isSelected(
        ) else localizedString('CartEmptyButtonToolTipTitle')

    buttonConfig = UIButtonConfiguration.plainButtonConfiguration()
    buttonConfig.image = UIImage.systemImageNamed('cart')
    buttonConfig.preferredSymbolConfigurationForImage = UIImageSymbolConfiguration.configurationWithTextStyle_(
      str(objc_const(UIKit, 'UIFontTextStyleLargeTitle')))

    button.configuration = buttonConfig

    button.changesSelectionAsPrimaryAction = True
    button.configurationUpdateHandler = colorUpdateHandler

    #if traitCollection.userInterfaceIdiom == .mac
    #  button.preferredBehavioralStyle = .pad

    button.setTitle_forState_(
      '', UIControlState.normal)  # No title, just an image.
    #button.isSelected = True
    button.setSelected_(False)

    button.addTarget_action_forControlEvents_(self,
                                              SEL('toggleButtonClicked:'),
                                              UIControlEvents.touchUpInside)

  # MARK: - Add To Cart Button
  @objc_method
  def toolTipInteraction_configurationAtPoint_(self, interaction,
                                               point) -> None:
    #return UIToolTipConfiguration.configurationWithToolTip_('hoge')
    return None

  @objc_method
  def addToCart_(self, _action: ctypes.c_void_p) -> None:
    action = ObjCInstance(_action)
    pdbr.state(action)

  # 21
  @objc_method
  def configureAddToCartButton_(self, button):
    config = UIButtonConfiguration.filledButtonConfiguration()
    config.buttonSize = UIButtonConfigurationSize.large
    config.image = UIImage.systemImageNamed('cart.fill')
    config.title = 'Add to Cart'
    config.cornerStyle = UIButtonConfigurationCornerStyle.capsule
    config.baseBackgroundColor = UIColor.systemTealColor()
    button.configuration = config

    button.toolTip = ''  # The value will be determined in its delegate. > 値はデリゲート内で決定されます。
    #button.toolTipInteraction.delegate = self
    button.addAction_forControlEvents_(
      UIAction.actionWithHandler_(Block(self.addToCart_, None,
                                        ctypes.c_void_p)),
      UIControlEvents.touchUpInside)

  # MARK: - Button Actions
  @objc_method
  def buttonClicked_(self, sender):
    print(f'Button was clicked.{sender}')

  @objc_method
  def toggleButtonClicked_(self, sender):
    #print(f'Toggle action: {sender}')
    print(f'Toggle action: ')


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  bvc = ButtonViewController.new()

  #style = UIModalPresentationStyle.pageSheet
  style = UIModalPresentationStyle.fullScreen
  present_viewController(bvc, style)

