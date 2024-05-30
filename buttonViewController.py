import ctypes
from enum import Enum

from pyrubicon.objc.api import ObjCClass, ObjCInstance, objc_method, objc_property, objc_const
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
)
from rbedge.functions import NSStringFromClass

from caseElement import CaseElement
from pyLocalizedString import localizedString

from storyboard.buttonViewController import prototypes

UITableViewController = ObjCClass('UITableViewController')
UITableViewHeaderFooterView = ObjCClass('UITableViewHeaderFooterView')
UIListContentConfiguration = ObjCClass('UIListContentConfiguration')

# todo: extension
UIKit = load_library('UIKit')
UIButtonConfiguration = ObjCClass('UIButtonConfiguration')
UIColor = ObjCClass('UIColor')
UIImage = ObjCClass('UIImage')
NSAttributedString = ObjCClass('NSAttributedString')
UIImageSymbolConfiguration = ObjCClass('UIImageSymbolConfiguration')
UIFont = ObjCClass('UIFont')


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
      # 12
      CaseElement(localizedString('StringSymbolTitle'),
                  ButtonKind.buttonTextSymbol.value,
                  self.configureTextSymbolButton_),
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

  # MARK: - Button Actions
  @objc_method
  def buttonClicked_(self, sender):
    print(f'Button was clicked.{sender}')


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  bvc = ButtonViewController.new()

  #style = UIModalPresentationStyle.pageSheet
  style = UIModalPresentationStyle.fullScreen
  present_viewController(bvc, style)

