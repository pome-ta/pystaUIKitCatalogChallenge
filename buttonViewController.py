import ctypes
from enum import Enum

from pyrubicon.objc.api import ObjCClass, ObjCInstance, Block
from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.runtime import send_super, objc_id, SEL
from pyrubicon.objc.types import NSInteger, CGPoint

from rbedge.enumerations import (
  UIUserInterfaceIdiom,
  UIControlState,
  UIControlEvents,
  UIButtonConfigurationCornerStyle,
  UIImageRenderingMode,
  NSUnderlineStyle,
  UIImageSymbolScale,
  NSDirectionalRectEdge,
  UIButtonConfigurationSize,
)
from rbedge.globalVariables import (
  NSAttributedStringKey,
  UIFontTextStyle,
)

from rbedge.pythonProcessUtils import (
  mainScreen_scale,
  dataWithContentsOfURL,
)
from rbedge.functions import NSStringFromClass
from rbedge import pdbr

from caseElement import CaseElement
from pyLocalizedString import localizedString

from baseTableViewController import BaseTableViewController
from storyboard.buttonViewController import prototypes

UIButtonConfiguration = ObjCClass('UIButtonConfiguration')
UIColor = ObjCClass('UIColor')
NSAttributedString = ObjCClass('NSAttributedString')
UIImageSymbolConfiguration = ObjCClass('UIImageSymbolConfiguration')
UIFont = ObjCClass('UIFont')
UIImage = ObjCClass('UIImage')
NSDictionary = ObjCClass('NSDictionary')
UIToolTipConfiguration = ObjCClass('UIToolTipConfiguration')
UIAction = ObjCClass('UIAction')
UIButton = ObjCClass('UIButton')  # todo: 型確認用


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

  cartItemCount: NSInteger = objc_property()

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
    self.cartItemCount = 0

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    #print(f'\t{NSStringFromClass(__class__)}: viewDidLoad')
    
    # --- Navigation
    self.navigationItem.title = localizedString('ButtonsTitle') if (
      title := self.navigationItem.title) is None else title

    self.testCellsAppendContentsOf_([
      # 00
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('DefaultTitle'), ButtonKind.buttonSystem.value,
        'configureSystemTextButton:'),
      # 01
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('DetailDisclosureTitle'),
        ButtonKind.buttonDetailDisclosure.value,
        'configureSystemDetailDisclosureButton:'),
      # 02
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('AddContactTitle'),
        ButtonKind.buttonSystemAddContact.value,
        'configureSystemContactAddButton:'),
      # 03
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('CloseTitle'), ButtonKind.buttonClose.value,
        'configureCloseButton:'),
    ])

    if True:  # xxx: `#available(iOS 15, *)`
      # These button styles are available on iOS 15 or later.
      self.testCellsAppendContentsOf_([
        # 04
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('GrayTitle'), ButtonKind.buttonStyleGray.value,
          'configureStyleGrayButton:'),
        # 05
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('TintedTitle'), ButtonKind.buttonStyleTinted.value,
          'configureStyleTintedButton:'),
        # 06
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('FilledTitle'), ButtonKind.buttonStyleFilled.value,
          'configureStyleFilledButton:'),
        # 07
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('CornerStyleTitle'),
          ButtonKind.buttonCornerStyle.value, 'configureCornerStyleButton:'),
        # 15
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('ToggleTitle'), ButtonKind.buttonToggle.value,
          'configureToggleButton:'),
      ])

    if True:  # xxx: `traitCollection.userInterfaceIdiom != .mac`
      self.testCellsAppendContentsOf_([
        # 16
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('ButtonColorTitle'),
          ButtonKind.buttonTitleColor.value, 'configureTitleTextButton:'),
      ])

    self.testCellsAppendContentsOf_([
      # 08
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('ImageTitle'), ButtonKind.buttonImage.value,
        'configureImageButton:'),
      # 09
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('AttributedStringTitle'),
        ButtonKind.buttonAttrText.value,
        'configureAttributedTextSystemButton:'),
      # 10
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('SymbolTitle'), ButtonKind.buttonSymbol.value,
        'configureSymbolButton:'),
    ])

    if True:  # xxx: `#available(iOS 15, *)`
      if self.traitCollection.userInterfaceIdiom != UIUserInterfaceIdiom.mac:
        self.testCellsAppendContentsOf_([
          # 11
          CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
            localizedString('LargeSymbolTitle'),
            ButtonKind.buttonLargeSymbol.value, 'configureLargeSymbolButton:'),
        ])

    if True:  # xxx: `#available(iOS 15, *)`
      self.testCellsAppendContentsOf_([
        # 12
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('SymbolStringTitle'),
          ButtonKind.buttonSymbolText.value, 'configureSymbolTextButton:'),
        # 13
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('StringSymbolTitle'),
          ButtonKind.buttonTextSymbol.value, 'configureTextSymbolButton:'),
        # 17
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('BackgroundTitle'),
          ButtonKind.buttonBackground.value, 'configureBackgroundButton:'),
        # 14
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('MultiTitleTitle'),
          ButtonKind.buttonMultiTitle.value, 'configureMultiTitleButton:'),
        # 21
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('AddToCartTitle'), ButtonKind.addToCartButton.value,
          'configureAddToCartButton:'),

        # 18
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('UpdateActivityHandlerTitle'),
          ButtonKind.buttonUpdateActivityHandler.value,
          'configureUpdateActivityHandlerButton:'),
        # 19
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('UpdateHandlerTitle'),
          ButtonKind.buttonUpdateHandler.value,
          'configureUpdateHandlerButton:'),
        # 20
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('UpdateImageHandlerTitle'),
          ButtonKind.buttonImageUpdateHandler.value,
          'configureUpdateImageHandlerButton:'),
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
    normalTitleAttributes = NSDictionary.dictionaryWithObjects_forKeys_([
      NSUnderlineStyle.single,
    ], [
      NSAttributedStringKey.strikethroughStyle,
    ])

    normalAttributedTitle = NSAttributedString.alloc(
    ).initWithString_attributes_(buttonTitle, normalTitleAttributes)

    normal = UIControlState.normal
    button.setAttributedTitle_forState_(normalAttributedTitle, normal)

    # Set the button's title for highlighted state (note this is not supported in Mac Catalyst).
    # > ボタンのタイトルを強調表示状態に設定します (これは Mac Catalyst ではサポートされていないことに注意してください)。
    highlightedTitleAttributes = NSDictionary.dictionaryWithObjects_forKeys_([
      UIColor.systemGreenColor(),
      NSUnderlineStyle.thick,
    ], [
      NSAttributedStringKey.foregroundColor,
      NSAttributedStringKey.strikethroughStyle
    ])

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
      UIFontTextStyle.body, UIImageSymbolScale.large)

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
        UIFontTextStyle.largeTitle)

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
        UIFontTextStyle.body)

      buttonConfig.image = buttonImage
      button.configuration = buttonConfig

    else:
      button.setImage_forState_(buttonImage, UIControlState.normal)
      config = UIImageSymbolConfiguration.configurationWithTextStyle_scale_(
        UIFontTextStyle.body, UIImageSymbolScale.small)
      button.setPreferredSymbolConfiguration_forImageInState_(
        config, UIControlState.normal)

    button.setTitle_forState_(localizedString('Person'), UIControlState.normal)

    button.titleLabel.font = UIFont.preferredFontForTextStyle_(
      UIFontTextStyle.body)

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
        UIFontTextStyle.body)

      buttonConfig.image = buttonImage

      # if traitCollection.userInterfaceIdiom == .mac
      #  button.preferredBehavioralStyle = .pad
      buttonConfig.imagePlacement = NSDirectionalRectEdge.trailing
      button.configuration = buttonConfig

    button.setTitle_forState_(localizedString('Person'), UIControlState.normal)

    button.titleLabel.font = UIFont.preferredFontForTextStyle_(
      UIFontTextStyle.body)

    button.addTarget_action_forControlEvents_(self, SEL('buttonClicked:'),
                                              UIControlEvents.touchUpInside)

  # 14
  @objc_method
  def configureMultiTitleButton_(self, button):
    # if traitCollection.userInterfaceIdiom == .mac
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
      # if traitCollection.userInterfaceIdiom == .mac
      #  button.preferredBehavioralStyle = .pad
      pass
    scale = int(mainScreen_scale)

    normal_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/background.imageset/stepper_and_segment_background_{scale}x.png'
    highlighted_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/background_highlighted.imageset/stepper_and_segment_background_highlighted_{scale}x.png'
    disabled_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/background_disabled.imageset/stepper_and_segment_background_disabled_{scale}x.png'

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
      UIFontTextStyle.body)

    button.configuration = buttonConfig

    button.setTitle_forState_(localizedString('Button'), UIControlState.normal)

    button.titleLabel.font = UIFont.preferredFontForTextStyle_(
      UIFontTextStyle.body)

    button.changesSelectionAsPrimaryAction = True
    button.configurationUpdateHandler = activityUpdateHandler

    # if traitCollection.userInterfaceIdiom == .mac
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

    # if traitCollection.userInterfaceIdiom == .mac
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
        UIFontTextStyle.largeTitle)
      _button.configuration = buttonConfig

      # xxx: `toolTip` 挙動未確認
      _button.toolTip = localizedString(
        'CartFilledButtonToolTipTitle') if _button.isSelected(
        ) else localizedString('CartEmptyButtonToolTipTitle')

    buttonConfig = UIButtonConfiguration.plainButtonConfiguration()
    buttonConfig.image = UIImage.systemImageNamed('cart')
    buttonConfig.preferredSymbolConfigurationForImage = UIImageSymbolConfiguration.configurationWithTextStyle_(
      UIFontTextStyle.largeTitle)

    button.configuration = buttonConfig

    button.changesSelectionAsPrimaryAction = True
    button.configurationUpdateHandler = colorUpdateHandler

    # if traitCollection.userInterfaceIdiom == .mac
    #  button.preferredBehavioralStyle = .pad

    button.setTitle_forState_(
      '', UIControlState.normal)  # No title, just an image.
    # button.isSelected = True
    button.setSelected_(False)

    button.addTarget_action_forControlEvents_(self,
                                              SEL('toggleButtonClicked:'),
                                              UIControlEvents.touchUpInside)

  # MARK: - Add To Cart Button
  # xxx: wip
  @objc_method
  def toolTipInteraction_configurationAtPoint_(
      self, interaction, point: CGPoint) -> ctypes.c_void_p:
    return UIToolTipConfiguration.configurationWithToolTip_('hoge').ptr

  @objc_method
  def addToCart_(self, _action: ctypes.c_void_p) -> None:
    action = ObjCInstance(_action)

    self.cartItemCount = 0 if self.cartItemCount.intValue > 0 else 12

    if action.sender.isKindOfClass_(UIButton):
      button = action.sender
      button.setNeedsUpdateConfiguration()

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
    # xxx: wip
    # button.toolTipInteraction.delegate = self
    button.addAction_forControlEvents_(
      UIAction.actionWithHandler_(Block(self.addToCart_, None,
                                        ctypes.c_void_p)),
      UIControlEvents.touchUpInside)

    button.changesSelectionAsPrimaryAction = True

    @Block
    def _handler(button_id: objc_id) -> None:
      _button = ObjCInstance(button_id)

      # Start with the current button's configuration.
      # > 現在のボタンの設定から始めます。
      # newConfig = _button.configuration
      newConfig = UIButtonConfiguration.filledButtonConfiguration()
      newConfig.buttonSize = UIButtonConfigurationSize.large
      newConfig.title = 'Add to Cart'
      newConfig.cornerStyle = UIButtonConfigurationCornerStyle.capsule
      newConfig.baseBackgroundColor = UIColor.systemTealColor()

      if _button.isSelected():
        # xxx: これだと`0` の時、取れない？
        newConfig.image = UIImage.systemImageNamed(
          'cart.fill.badge.plus'
        ) if self.cartItemCount.intValue > 0 else UIImage.systemImageNamed(
          'cart.badge.plus')
        # xxx: 力技
        newConfig.subtitle = f'{self.cartItemCount.intValue}items'
      else:
        # As the button is highlighted (pressed), apply a temporary image and subtitle.
        # > ボタンがハイライト表示される(押される)と、一時的な画像と字幕が適用されます。
        newConfig.image = UIImage.systemImageNamed('cart.fill')
        newConfig.subtitle = ' '  # xxx: 文字パディング

      newConfig.imagePadding = 8
      _button.configuration = newConfig

    # This handler is called when this button needs updating.
    # > このハンドラーは、このボタンを更新する必要がある場合に呼び出されます。
    button.configurationUpdateHandler = _handler

  # MARK: - Button Actions
  @objc_method
  def buttonClicked_(self, sender):
    print(f'Button was clicked.{sender}')

  @objc_method
  def toggleButtonClicked_(self, sender):
    print(f'Toggle action: {sender}')


if __name__ == '__main__':
  from rbedge.app import App

  from rbedge.enumerations import (
    UITableViewStyle,
    UIModalPresentationStyle,
  )

  table_style = UITableViewStyle.grouped
  main_vc = ButtonViewController.alloc().initWithStyle_(table_style)
  _title = NSStringFromClass(ButtonViewController)
  main_vc.navigationItem.title = _title

  # presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

