from enum import Enum

import ctypes
from objc_util import ObjCInstance, sel, create_objc_class, ns

from objcista import *
#from objcista._controller import _Controller


from caseElement import CaseElement
from storyboard_ButtonViewController import prototypes
from pyLocalizedString import pylocalizedString

import pdbg


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


# todo: まずはここで作りつつ、モジュール化するケアも考慮
#UITableViewController
class ObjcTableViewController:

  def __init__(self, *args, **kwargs):
    self._msgs: list['Callable'] = []  # xxx: 型名ちゃんとやる
    self.controller_instance: ObjCInstance
    self.prototypes = prototypes
    self.testCells = []

  def set_prototypes(self, view: UITableView):
    for proto in self.prototypes:
      cellClass = proto.this()
      identifier = proto.reuseIdentifier_name()
      view.registerClass_forCellReuseIdentifier_(cellClass, identifier)

  def _override_controller(self):
    # todo: 既存method と独自追加method をシュッと持ちたい
    def viewDidLoad(_self, _cmd):
      this = ObjCInstance(_self)

      _view = this.view()
      style = UITableViewStyle.grouped

      view = _view.initWithFrame_style_(_view.frame(), style)
      this.setView_(view)
      self.set_prototypes(view)

      self.testCells.extend([
        # 0
        CaseElement(pylocalizedString('DefaultTitle'),
                    ButtonKind.buttonSystem.value,
                    this.configureSystemTextButton_),

        # 1
        CaseElement(pylocalizedString('DetailDisclosureTitle'),
                    ButtonKind.buttonDetailDisclosure.value,
                    this.configureSystemDetailDisclosureButton_),

        # 2
        CaseElement(pylocalizedString('AddContactTitle'),
                    ButtonKind.buttonSystemAddContact.value,
                    this.configureSystemContactAddButton_),

        # 3
        CaseElement(pylocalizedString('CloseTitle'),
                    ButtonKind.buttonClose.value, this.configureCloseButton_),
      ])

      # xxx: 'if #available(iOS 15, *)'
      # These button styles are available on iOS 15 or later.
      self.testCells.extend([
        # 4
        CaseElement(pylocalizedString('GrayTitle'),
                    ButtonKind.buttonStyleGray.value,
                    this.configureStyleGrayButton_),

        #5
        CaseElement(pylocalizedString('TintedTitle'),
                    ButtonKind.buttonStyleTinted.value,
                    this.configureStyleTintedButton_),

        # 6
        CaseElement(pylocalizedString('FilledTitle'),
                    ButtonKind.buttonStyleFilled.value,
                    this.configureStyleFilledButton_),

        # 7
        CaseElement(pylocalizedString('CornerStyleTitle'),
                    ButtonKind.buttonCornerStyle.value,
                    this.configureCornerStyleButton_),

        # 8
        CaseElement(pylocalizedString('ToggleTitle'),
                    ButtonKind.buttonToggle.value,
                    this.configureToggleButton_),
      ])

      # xxx: `if traitCollection.userInterfaceIdiom != .mac`
      # Colored button titles only on iOS.
      self.testCells.extend([
        # 9
        CaseElement(pylocalizedString('ButtonColorTitle'),
                    ButtonKind.buttonTitleColor.value,
                    this.configureTitleTextButton_),
      ])

      self.testCells.extend([
        # 10
        CaseElement(pylocalizedString('ImageTitle'),
                    ButtonKind.buttonImage.value, this.configureImageButton_),

        # 11
        CaseElement(pylocalizedString('AttributedStringTitle'),
                    ButtonKind.buttonAttrText.value,
                    this.configureAttributedTextSystemButton_),

        # 12
        CaseElement(pylocalizedString('SymbolTitle'),
                    ButtonKind.buttonSymbol.value,
                    this.configureSymbolButton_),
      ])

      # xxx: `if #available(iOS 15, *)`
      # This case uses UIButtonConfiguration which is available on iOS 15 or later.
      # xxx: `if traitCollection.userInterfaceIdiom != .mac`
      # UIButtonConfiguration for large images available only on iOS.
      self.testCells.extend([
        # 13
        CaseElement(pylocalizedString('LargeSymbolTitle'),
                    ButtonKind.buttonLargeSymbol.value,
                    this.configureLargeSymbolButton_),
      ])

      # xxx: `if #available(iOS 15, *)`
      self.testCells.extend([
        # 14
        CaseElement(pylocalizedString('StringSymbolTitle'),
                    ButtonKind.buttonTextSymbol.value,
                    this.configureTextSymbolButton_),

        # 15
        CaseElement(pylocalizedString('SymbolStringTitle'),
                    ButtonKind.buttonSymbolText.value,
                    this.configureSymbolTextButton_),

        # 16
        CaseElement(pylocalizedString('BackgroundTitle'),
                    ButtonKind.buttonBackground.value,
                    this.configureBackgroundButton_),

        # Multi-title button: title for normal and highlight state, setTitle(.highlighted) is for iOS 15 and later.
        # 17
        CaseElement(pylocalizedString('MultiTitleTitle'),
                    ButtonKind.buttonMultiTitle.value,
                    this.configureMultiTitleButton_),

        # Various button effects done to the addToCartButton are available only on iOS 15 or later.

        # 18
        CaseElement(pylocalizedString('AddToCartTitle'),
                    ButtonKind.addToCartButton.value,
                    this.configureAddToCartButton_),

        # UIButtonConfiguration with updateHandlers is available only on iOS 15 or later.
        # 19
        CaseElement(pylocalizedString('UpdateActivityHandlerTitle'),
                    ButtonKind.buttonUpdateActivityHandler.value,
                    this.configureUpdateActivityHandlerButton_),

        # 20
        CaseElement(pylocalizedString('UpdateHandlerTitle'),
                    ButtonKind.buttonUpdateHandler.value,
                    this.configureUpdateHandlerButton_),

        # 21
        CaseElement(pylocalizedString('UpdateImageHandlerTitle'),
                    ButtonKind.buttonImageUpdateHandler.value,
                    this.configureUpdateImageHandlerButton_),
      ])

    # --- UITableViewDelegate

    # xxx: `return` ができないので、`tableView_viewForHeaderInSection_` で処理
    '''
    def centeredHeaderView_(_self, _cmd, _title):
      title = ObjCInstance(_title)
      alignment = UIListContentTextAlignment.center

      headerView = UITableViewHeaderFooterView.new()
      content = UIListContentConfiguration.groupedHeaderConfiguration()
      content.setText_(title)
      content.textProperties().setAlignment_(alignment)
      headerView.setContentConfiguration_(content)
      return headerView.ptr
    '''

    # MARK: - UITableViewDataSource
    def tableView_viewForHeaderInSection_(_self, _cmd, _tableView, _section):
      title = self.testCells[_section].title
      alignment = UIListContentTextAlignment.center

      headerView = UITableViewHeaderFooterView.new()
      content = UIListContentConfiguration.groupedHeaderConfiguration()
      content.setText_(title)
      content.textProperties().setAlignment_(alignment)
      headerView.setContentConfiguration_(content)

      # xxx: `return` ができないので、`tableView_viewForHeaderInSection_` で処理
      #return ObjCInstance(_self).centeredHeaderView_(self.testCells[_section].title)

      return headerView.ptr

    def tableView_titleForHeaderInSection_(_self, _cmd, _tableView, _section):
      return ns(self.testCells[_section].title).ptr

    def tableView_numberOfRowsInSection_(_self, _cmd, _tableView, _section):
      return 1

    def numberOfSectionsInTableView_(_self, _cmd, _tableView):
      return len(self.testCells)

    def tableView_cellForRowAtIndexPath_(_self, _cmd, _tableView, _indexPath):
      tableView = ObjCInstance(_tableView)
      indexPath = ObjCInstance(_indexPath)

      cellTest = self.testCells[indexPath.section()]

      cell = tableView.dequeueReusableCellWithIdentifier(
        cellTest.cellID, forIndexPath=indexPath)

      if (view := cellTest.targetView(cell)):
        cellTest.configHandler(view)
      return cell.ptr

    _methods = [
      viewDidLoad,
      #centeredHeaderView_,
      tableView_viewForHeaderInSection_,
      tableView_titleForHeaderInSection_,
      tableView_numberOfRowsInSection_,
      numberOfSectionsInTableView_,
      tableView_cellForRowAtIndexPath_,
    ]

    self.add_extensions()
    if self._msgs: _methods.extend(self._msgs)

    create_kwargs = {
      'name': '_vc',
      'superclass': UITableViewController,
      'methods': _methods,
    }
    _vc = create_objc_class(**create_kwargs)
    self.controller_instance = _vc

  def add_extensions(self):
    # todo: objc で独自にmethod 生やしたいときなど
    # todo: この関数内に関数を作り`@self.extension`

    @self.extension
    def configureSystemTextButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      state = UIControl_State.normal
      button.setTitle_forState_('Button', state)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureSystemDetailDisclosureButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureSystemContactAddButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureCloseButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    # todo: `@available(iOS 15.0, *)`
    # xxx: あとでやる
    def configureStyleGrayButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      config = UIButtonConfiguration.grayButtonConfiguration()
      button.setConfiguration_(config)
      state = UIControl_State.normal
      button.setTitle_forState_('Button', state)
      button.setToolTip_('GrayStyleButtonToolTipTitle')

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    # todo: `@available(iOS 15.0, *)`
    def configureStyleTintedButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      config = UIButtonConfiguration.tintedButtonConfiguration()
      # todo: `if traitCollection.userInterfaceIdiom == .mac`
      # xxx: あとでやる
      systemRed = UIColor.systemRedColor()
      config.setBaseBackgroundColor_(systemRed)
      config.setBaseForegroundColor_(systemRed)

      state = UIControl_State.normal
      button.setTitle_forState_('Button', state)
      button.setToolTip_('TintedStyleButtonToolTipTitle')
      button.setConfiguration_(config)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    # todo: `@available(iOS 15.0, *)`
    def configureStyleFilledButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      config = UIButtonConfiguration.filledButtonConfiguration()

      # todo: `if traitCollection.userInterfaceIdiom == .mac`
      # xxx: あとでやる
      systemRed = UIColor.systemRedColor()
      config.background().setBackgroundColor_(systemRed)
      button.setConfiguration_(config)

      state = UIControl_State.normal
      button.setTitle_forState_('Button', state)
      button.setToolTip_('FilledStyleButtonToolTipTitle')

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    # todo: `@available(iOS 15.0, *)`
    def configureCornerStyleButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      # todo: `if traitCollection.userInterfaceIdiom == .mac`
      config = UIButtonConfiguration.grayButtonConfiguration()
      cornerStyle = UIButton_Configuration_CornerStyle.capsule
      config.setCornerStyle_(cornerStyle)

      button.setConfiguration_(config)

      state = UIControl_State.normal
      button.setTitle_forState_('Button', state)
      button.setToolTip_('CapsuleStyleButtonToolTipTitle')

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureImageButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      image = UIImage.systemImageNamed('xmark')

      systemPurple = UIColor.systemPurpleColor()
      renderingMode = UIImageRenderingMode.alwaysOriginal
      # ref: [swift - iOS 13 `withTintColor` not obeying the color I assign - Stack Overflow](https://stackoverflow.com/questions/58867627/ios-13-withtintcolor-not-obeying-the-color-i-assign)
      imageButtonNormalImage = image.imageWithTintColor_(
        systemPurple).imageWithRenderingMode_(renderingMode)

      state = UIControl_State.normal
      button.setImage_forState_(imageButtonNormalImage, state)

      # todo: `if traitCollection.userInterfaceIdiom == .mac`

      button.setToolTip_('XButtonToolTipTitle')

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureAttributedTextSystemButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      buttonTitle = 'Buttonnn'
      NSStrikethroughStyleAttributeName = globalVariable(
        'NSStrikethroughStyleAttributeName')

      normalTitleAttributes = {
        NSStrikethroughStyleAttributeName: NSUnderlineStyle.single,
      }

      normalAttributedTitle = NSAttributedString.alloc(
      ).initWithString_attributes_(buttonTitle, normalTitleAttributes)

      state = UIControl_State.normal
      button.setAttributedTitle_forState_(normalAttributedTitle, state)

      NSForegroundColorAttributeName = globalVariable(
        'NSForegroundColorAttributeName')
      NSStrikethroughStyleAttributeName = globalVariable(
        'NSStrikethroughStyleAttributeName')

      highlightedTitleAttributes = {
        NSForegroundColorAttributeName: UIColor.systemGreenColor(),
        NSStrikethroughStyleAttributeName: NSUnderlineStyle.thick,
      }

      highlightedAttributedTitle = NSAttributedString.alloc(
      ).initWithString_attributes_(buttonTitle, highlightedTitleAttributes)

      state = UIControl_State.highlighted
      button.setAttributedTitle_forState_(highlightedAttributedTitle, state)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureSymbolButton_(_self, _cmd, _button):
      # xxx: 合ってる説ある？
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      buttonImage = UIImage.systemImageNamed('person')
      state = UIControl_State.normal
      if True:  # xxx: `available(iOS 15, *)`
        buttonConfig = UIButtonConfiguration.plainButtonConfiguration()
        buttonConfig.setImage_(buttonImage)
        button.setConfiguration_(buttonConfig)
        button.setToolTip_('PersonButtonToolTipTitle')
      else:
        button.setImage_forState_(buttonImage, state)

      UIFontTextStyleBody = globalVariable('UIFontTextStyleBody')
      scale = UIImage_SymbolScale.large

      config = UIImageSymbolConfiguration.configurationWithTextStyle_scale_(
        UIFontTextStyleBody, scale)

      button.setPreferredSymbolConfiguration_forImageInState_(config, state)

      # todo: `button.accessibilityLabel = NSLocalizedString("Person", comment: "")`

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureLargeSymbolButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)
      buttonImage = UIImage.systemImageNamed('person')
      if True:  # xxx: `available(iOS 15, *)`
        buttonConfig = UIButtonConfiguration.plainButtonConfiguration()

        UIFontTextStyleLargeTitle = globalVariable('UIFontTextStyleLargeTitle')

        _symbolConfiguration = UIImageSymbolConfiguration.configurationWithTextStyle_(
          UIFontTextStyleLargeTitle)

        buttonConfig.setPreferredSymbolConfigurationForImage_(
          _symbolConfiguration)
        buttonConfig.setImage_(buttonImage)
        button.setConfiguration_(buttonConfig)
      else:
        state = UIControl_State.normal
        button.setImage_forState_(buttonImage, state)

        UIFontTextStyleBody = globalVariable('UIFontTextStyleBody')
        scale = UIImage_SymbolScale.small

        config = UIImageSymbolConfiguration.configurationWithTextStyle_scale_(
          UIFontTextStyleBody, scale)
        button.setPreferredSymbolConfiguration_forImageInState_(config, state)

      # todo: `button.accessibilityLabel = NSLocalizedString("Person", comment: "")`

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureSymbolTextButton_(_self, _cmd, _button):
      # Button with image to the left of the title.
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      buttonImage = UIImage.systemImageNamed('person')
      if True:  # xxx: `available(iOS 15, *)`
        buttonConfig = UIButtonConfiguration.plainButtonConfiguration()
        UIFontTextStyleBody = globalVariable('UIFontTextStyleBody')
        _symbolConfiguration = UIImageSymbolConfiguration.configurationWithTextStyle_(
          UIFontTextStyleBody)

        buttonConfig.setPreferredSymbolConfigurationForImage_(
          _symbolConfiguration)
        buttonConfig.setImage_(buttonImage)
        button.setConfiguration_(buttonConfig)
      else:
        state = UIControl_State.normal
        button.setImage_forState_(buttonImage, state)

      state = UIControl_State.normal
      button.setTitle_forState_('Person', state)

      # xxx: 正解かは不明
      UIFontTextStyleBody = globalVariable('UIFontTextStyleBody')
      preferredFont = UIFont.preferredFontForTextStyle_(UIFontTextStyleBody)

      button.titleLabel().setFont_(preferredFont)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureTextSymbolButton_(_self, _cmd, _button):
      # Button with image to the right of the title.
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      buttonImage = UIImage.systemImageNamed('person')
      if True:  # xxx: `available(iOS 15, *)`
        buttonConfig = UIButtonConfiguration.plainButtonConfiguration()

        UIFontTextStyleBody = globalVariable('UIFontTextStyleBody')
        _symbolConfiguration = UIImageSymbolConfiguration.configurationWithTextStyle_(
          UIFontTextStyleBody)

        buttonConfig.setImage_(buttonImage)
        # todo: `if traitCollection.userInterfaceIdiom == .mac`
        imagePlacement = NSDirectionalRectEdge.trailing
        buttonConfig.setImagePlacement_(imagePlacement)
        button.setConfiguration_(buttonConfig)

      state = UIControl_State.normal
      button.setTitle_forState_('Person', state)

      # xxx: 正解かは不明
      UIFontTextStyleBody = globalVariable('UIFontTextStyleBody')
      preferredFont = UIFont.preferredFontForTextStyle_(UIFontTextStyleBody)

      button.titleLabel().setFont_(preferredFont)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureMultiTitleButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      # todo: `,if traitCollection.userInterfaceIdiom == .mac`
      normal = UIControl_State.normal
      highlighted = UIControl_State.highlighted

      button.setTitle_forState_('Button', normal)
      button.setTitle_forState_('Person', highlighted)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureToggleButton_(_self, _cmd, _button):
      # This makes the button style a "toggle button".
      #this = ObjCInstance(_self)
      button = ObjCInstance(_button)
      button.setChangesSelectionAsPrimaryAction_(True)

    @self.extension
    def configureTitleTextButton_(_self, _cmd, _button):
      # Note: Only for iOS the title's color can be changed.
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      normal = UIControl_State.normal
      highlighted = UIControl_State.highlighted
      systemGreen = UIColor.systemGreenColor()
      systemRed = UIColor.systemRedColor()

      button.setTitleColor_forState_(systemGreen, normal)
      button.setTitleColor_forState_(systemRed, highlighted)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureBackgroundButton_(_self, _cmd, _button):
      # Note: Only for iOS the title's color can be changed.
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      # ref: [iphone - Retina display and [UIImage initWithData] - Stack Overflow](https://stackoverflow.com/questions/3289286/retina-display-and-uiimage-initwithdata)
      # xxx: scale 指定これでいいのかな？
      scale = int(UIScreen.mainScreen().scale())

      normal_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/background.imageset/stepper_and_segment_background_{scale}x.png'
      highlighted_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/background_highlighted.imageset/stepper_and_segment_background_highlighted_{scale}x.png'
      disabled_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/background_disabled.imageset/stepper_and_segment_background_disabled_{scale}x.png'

      normal_data = get_dataWithContentsOfURL(normal_str)
      highlighted_data = get_dataWithContentsOfURL(highlighted_str)
      disabled_data = get_dataWithContentsOfURL(disabled_str)

      normal_img = UIImage.alloc().initWithData_scale_(normal_data, scale)
      highlighted_img = UIImage.alloc().initWithData_scale_(
        highlighted_data, scale)
      disabled_img = UIImage.alloc().initWithData_scale_(disabled_data, scale)

      normal = UIControl_State.normal
      highlighted = UIControl_State.highlighted
      disabled = UIControl_State.disabled

      button.setBackgroundImage_forState_(normal_img, normal)
      button.setBackgroundImage_forState_(highlighted_img, highlighted)
      button.setBackgroundImage_forState_(disabled_img, disabled)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureUpdateActivityHandlerButton_(_self, _cmd, _button):
      # xxx: wip 後ほど実装
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      def activityUpdateHandler_(_cmd, _button):
        print(_button)
        print('____ e')

      buttonConfig = UIButtonConfiguration.plainButtonConfiguration()
      buttonConfig.setImage_(UIImage.systemImageNamed('tray'))

      UIFontTextStyleBody = globalVariable('UIFontTextStyleBody')
      _symbolConfiguration = UIImageSymbolConfiguration.configurationWithTextStyle_(
        UIFontTextStyleBody)
      buttonConfig.setPreferredSymbolConfigurationForImage_(
        _symbolConfiguration)

      button.setConfiguration_(buttonConfig)

      state = UIControl_State.normal
      button.setTitle_forState_('Button', state)

      # xxx: 正解かは不明
      UIFontTextStyleBody = globalVariable('UIFontTextStyleBody')
      preferredFont = UIFont.preferredFontForTextStyle_(UIFontTextStyleBody)

      button.titleLabel().setFont_(preferredFont)
      # This turns on the toggle behavior.
      button.setChangesSelectionAsPrimaryAction_(True)

      #handler_block = ObjCBlock(activityUpdateHandler_, restype=ctypes.c_void_p,argtypes=[ctypes.c_void_p,ctypes.c_void_p])
      #button.setConfigurationUpdateHandler_(handler_block)

      selector = sel('toggleButtonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureUpdateHandlerButton_(_self, _cmd, _button):
      # xxx: wip 後ほど実装
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      def colorUpdateHandler_(_cmd, _button):
        print(_button)
        print('____ e')

      buttonConfig = UIButtonConfiguration.filledButtonConfiguration()
      button.setConfiguration_(buttonConfig)

      button.setChangesSelectionAsPrimaryAction_(True)

      #handler_block = ObjCBlock(colorUpdateHandler_, restype=ctypes.c_void_p,argtypes=[ctypes.c_void_p,ctypes.c_void_p])
      #button.setConfigurationUpdateHandler_(handler_block)

      selector = sel('toggleButtonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureUpdateImageHandlerButton_(_self, _cmd, _button):
      # xxx: wip 後ほど実装
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      def colorUpdateHandler_(_cmd, _button):
        print(_button)
        print('____ e')

      buttonConfig = UIButtonConfiguration.plainButtonConfiguration()
      buttonConfig.setImage_(UIImage.systemImageNamed('cart'))

      UIFontTextStyleLargeTitle = globalVariable('UIFontTextStyleLargeTitle')
      _symbolConfiguration = UIImageSymbolConfiguration.configurationWithTextStyle_(
        UIFontTextStyleLargeTitle)
      buttonConfig.setPreferredSymbolConfigurationForImage_(
        _symbolConfiguration)

      button.setConfiguration_(buttonConfig)

      #handler_block = ObjCBlock(colorUpdateHandler_, restype=ctypes.c_void_p,argtypes=[ctypes.c_void_p,ctypes.c_void_p])
      #button.setConfigurationUpdateHandler_(handler_block)

      button.setChangesSelectionAsPrimaryAction_(True)

      normal = UIControl_State.normal
      button.setTitle_forState_('', normal)
      button.setSelected_(False)

      selector = sel('toggleButtonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    # MARK: - Add To Cart Button
    @self.extension
    def configureAddToCartButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      config = UIButtonConfiguration.filledButtonConfiguration()

      _size = UIButton_Configuration_Size.large
      config.setButtonSize_(_size)
      config.setImage_(UIImage.systemImageNamed('cart.fill'))
      config.setTitle_('Add to Cart')
      _cornerStyle = UIButton_Configuration_CornerStyle.capsule
      config.setCornerStyle_(_cornerStyle)
      _color = UIColor.systemTealColor()
      config.setBaseBackgroundColor_(_color)
      button.setConfiguration_(config)

      button.setChangesSelectionAsPrimaryAction_(True)

    @self.extension
    def buttonClicked_(_self, _cmd, _sender):
      print('Button was clicked.')

    @self.extension
    def toggleButtonClicked_(_self, _cmd, _sender):
      sender = ObjCInstance(_sender)
      print(f'Toggle action: {sender}')

  def extension(self, msg):
    if not (hasattr(self, '_msgs')):
      self._msgs: list['Callable'] = []
    self._msgs.append(msg)

  def _init_controller(self):
    self._override_controller()
    vc = self.controller_instance.new().autorelease()
    return vc

  @classmethod
  def new(cls, *args, **kwargs) -> ObjCInstance:
    _cls = cls(*args, **kwargs)
    return _cls._init_controller()


if __name__ == "__main__":
  from objcista.objcNavigationController import PlainNavigationController

  class TopNavigationController(PlainNavigationController):

    def __init__(self):
      self.add_extensions()

    def add_extensions(self):

      @self.extension
      def doneButtonTapped_(_self, _cmd, _sender):
        this = ObjCInstance(_self)
        visibleViewController = this.visibleViewController()
        visibleViewController.dismissViewControllerAnimated_completion_(
          True, None)

    def willShowViewController(self,
                               navigationController: UINavigationController,
                               viewController: UIViewController,
                               animated: bool):

      super().willShowViewController(navigationController, viewController,
                                     animated)

      systemItem = UIBarButtonItem_SystemItem.done
      done_btn = UIBarButtonItem.alloc(
      ).initWithBarButtonSystemItem_target_action_(systemItem,
                                                   navigationController,
                                                   sel('doneButtonTapped:'))

      visibleViewController = navigationController.visibleViewController()

      # --- navigationItem
      navigationItem = visibleViewController.navigationItem()
      navigationItem.rightBarButtonItem = done_btn

  LAYOUT_DEBUG = True

  #LAYOUT_DEBUG = False
  #vc = ButtonViewController.new()
  #buttonSystemAddContact
  vc = ObjcTableViewController.new()
  nv = TopNavigationController.new(vc, True)
  style = UIModalPresentationStyle.pageSheet
  #style = UIModalPresentationStyle.fullScreen

  run_controller(nv, style)

