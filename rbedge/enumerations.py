from dataclasses import dataclass

# ref: [NSURLErrorNotConnectedToInternet | Apple Developer Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes/nsurlerrornotconnectedtointernet?language=objc)
NSURLErrorNotConnectedToInternet = -1009


# ref: [UIModalPresentationStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle)
@dataclass
class UIModalPresentationStyle:
  automatic: int = -2
  none: int = -1
  fullScreen: int = 0
  pageSheet: int = 1
  formSheet: int = 2
  currentContext: int = 3
  custom: int = 4
  overFullScreen: int = 5
  overCurrentContext: int = 6
  popover: int = 7
  blurOverFullScreen: int = 8


# ref: [UIRectEdge | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uirectedge?language=objc)
@dataclass
class UIRectEdge:
  none: int = 0
  top: int = 1 << 0
  left: int = 1 << 1
  bottom: int = 1 << 2
  right: int = 1 << 3
  all: int = top | left | bottom | right


# ref: [UIBarButtonSystemItem | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibarbuttonsystemitem?language=objc)
@dataclass
class UIBarButtonSystemItem:
  done: int = 0
  cancel: int = 1
  edit: int = 2
  add: int = 4
  flexibleSpace: int = 5
  fixedSpace: int = 6
  compose: int = 7
  reply: int = 8
  action: int = 9
  organize: int = 10
  bookmarks: int = 11
  search: int = 12
  refresh: int = 13
  stop: int = 14
  trash: int = 16
  play: int = 17
  pause: int = 18
  rewind: int = 19
  fastForward: int = 20
  undo: int = 21
  redo: int = 22
  pageCurl: int = 23  # Deprecated
  close: int = 24


# ref: [UIButtonType | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibuttontype?language=objc)
@dataclass
class UIButtonType:
  custom: int = 0
  system: int = 1
  detailDisclosure: int = 2
  infoLight: int = 3
  infoDark: int = 4
  contactAdd: int = 5
  plain: int = 6
  close: int = 7


# ref: [UIControlState | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicontrolstate?language=objc)
@dataclass
class UIControlState:
  normal: int = 0
  highlighted: int = 1 << 0
  disabled: int = 1 << 1
  selected: int = 1 << 2
  focused: int = 1 << 3
  application: int = 0x00FF0000
  reserved: int = 0xFF000000


# ref: [UIControlEvents | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicontrolevents?language=objc)
@dataclass
class UIControlEvents:
  touchDown: int = 1 << 0
  touchDownRepeat: int = 1 << 1
  touchDragInside: int = 1 << 2
  touchDragOutside: int = 1 << 3
  touchDragEnter: int = 1 << 4
  touchDragExit: int = 1 << 5
  touchUpInside: int = 1 << 6
  touchUpOutside: int = 1 << 7
  touchCancel: int = 1 << 8
  valueChanged: int = 1 << 12
  menuActionTriggered: int = 1 << 14
  primaryActionTriggered: int = 1 << 13
  editingDidBegin: int = 1 << 16
  editingChanged: int = 1 << 17
  editingDidEnd: int = 1 << 18
  editingDidEndOnExit: int = 1 << 19
  allTouchEvents: int = 0x00000FFF
  allEditingEvents: int = 0x000F0000
  applicationReserved: int = 0x0F000000
  systemReserved: int = 0xF0000000
  allEvents: int = 0xFFFFFFFF


# ref: [UIListContentTextAlignment | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uilistcontenttextalignment)
@dataclass
class UIListContentTextAlignment:
  # todo: `Enumeration Case` に値表記が無いので独自に調査
  natural: int = 0
  center: int = 1
  justified: int = 2


# ref: [UITableViewStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitableviewstyle?language=objc)
@dataclass
class UITableViewStyle:
  plain: int = 0
  grouped: int = 1
  insetGrouped: int = 2


# ref: [UIButtonConfigurationCornerStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibuttonconfigurationcornerstyle?language=objc)
@dataclass
class UIButtonConfigurationCornerStyle:
  # todo: `Enumeration Case` に値表記が無いので独自に調査
  dynamic: int = 0
  fixed: int = -1
  capsule: int = 4
  large: int = 3
  medium: int = 2
  small: int = 1


# ref: [UIImageRenderingMode | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimagerenderingmode?language=objc)
@dataclass
class UIImageRenderingMode:
  automatic: int = 0
  alwaysOriginal: int = 1
  alwaysTemplate: int = 2


# ref: [NSUnderlineStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nsunderlinestyle?language=objc)
@dataclass
class NSUnderlineStyle:
  # ref: [NSAttributedString.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/NSAttributedString.rs.html#87)
  none: int = 0x00  # xxx: patternSolid ?
  single: int = 0x01
  thick: int = 0x02
  double: int = 0x09
  patternSolid: int = 0x0000  # xxx: none ?
  patternDot: int = 0x0100
  patternDash: int = 0x0200
  patternDashDot: int = 0x0300
  patternDashDotDot: int = 0x0400
  byWord: int = 0x8000


# ref: [UIImageSymbolScale | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimagesymbolscale?language=objc)
@dataclass
class UIImageSymbolScale:
  default: int = -1
  unspecified: int = 0
  small: int = 1
  medium: int = 2
  large: int = 3


# ref: [UIImageSymbolWeight | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimagesymbolweight?language=objc)
@dataclass
class UIImageSymbolWeight:
  unspecified: int = 0
  ultraLight: int = 1
  thin: int = 2
  light: int = 3
  regular: int = 4
  medium: int = 5
  semibold: int = 6
  bold: int = 7
  heavy: int = 8
  black: int = 9


# ref: [NSDirectionalRectEdge | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nsdirectionalrectedge?language=objc)
@dataclass
class NSDirectionalRectEdge:
  none: int = 0  # ref: [NSDirectionalRectEdgeNone | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nsdirectionalrectedge/nsdirectionalrectedgenone?language=objc)
  top: int = 1 << 0
  leading: int = 1 << 1
  bottom: int = 1 << 2
  trailing: int = 1 << 3
  all: int = top | leading | bottom | trailing


# ref: [UIButtonConfigurationSize | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibuttonconfigurationsize)
@dataclass
class UIButtonConfigurationSize:
  # todo: `Enumeration Case` に値表記が無いので独自に調査
  medium: int = 0
  small: int = 1
  mini: int = 2
  large: int = 3


# ref: [UIMenuElementState | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uimenuelementstate?language=objc)
@dataclass
class UIMenuElementState:
  off: int = 0
  on: int = 1
  mixed: int = 2


# ref: [UIMenuElementAttributes | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uimenuelementattributes)
@dataclass
class UIMenuElementAttributes:
  destructive: int = 1 << 1
  disabled: int = 1 << 0
  hidden: int = 1 << 2
  keepsMenuPresented: int = 1 << 3


# ref: [UIMenuOptions | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uimenuoptions?language=objc)
@dataclass
class UIMenuOptions:
  displayInline: int = 1 << 0
  destructive: int = 1 << 1
  singleSelection: int = 1 << 5
  displayAsPalette: int = 1 << 7


# ref: [UISplitViewControllerStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerstyle?language=objc)
@dataclass
class UISplitViewControllerStyle:
  doubleColumn: int = 1
  tripleColumn: int = 2


# ref: [UISplitViewControllerColumn | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uisplitviewcontrollercolumn?language=objc)
@dataclass
class UISplitViewControllerColumn:
  primary: int = 0
  supplementary: int = 1
  secondary: int = 2
  compact: int = 3


# ref: [UICollectionLayoutListAppearance | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistappearance?language=objc)
@dataclass
class UICollectionLayoutListAppearance:
  # ref: [UICollectionLayoutList.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UICollectionLayoutList.rs.html#16)
  plain: int = 0
  grouped: int = 1
  insetGrouped: int = 2
  sidebar: int = 3
  sidebarPlain: int = 4


# ref: [UICollectionLayoutListHeaderMode | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistheadermode)
@dataclass
class UICollectionLayoutListHeaderMode:
  # xxx: 独自調査 a.k.a: 勘
  # ref: [UICollectionLayoutList.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UICollectionLayoutList.rs.html)
  none: int = 0
  supplementary: int = 1
  firstItemInSection: int = 2


# ref: [UIViewAutoresizing | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiviewautoresizing?language=objc)
@dataclass
class UIViewAutoresizing:
  none: int = 0  # ref: [UIViewAutoresizingNone | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiviewautoresizing/uiviewautoresizingnone?language=objc)
  flexibleLeftMargin: int = 1 << 0
  flexibleWidth: int = 1 << 1
  flexibleRightMargin: int = 1 << 2
  flexibleTopMargin: int = 1 << 3
  flexibleHeight: int = 1 << 4
  flexibleBottomMargin: int = 1 << 5


# ref: [UIViewContentMode | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiviewcontentmode?language=objc)
@dataclass
class UIViewContentMode:
  scaleToFill: int = 0
  scaleAspectFit: int = 1
  scaleAspectFill: int = 2
  redraw: int = 3
  center: int = 4
  top: int = 5
  bottom: int = 6
  left: int = 7
  right: int = 8
  topLeft: int = 9
  topRight: int = 10
  bottomLeft: int = 11
  bottomRight: int = 12


# ref: [UIControlContentHorizontalAlignment | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicontrolcontenthorizontalalignment?language=objc)
@dataclass
class UIControlContentHorizontalAlignment:
  center: int = 0
  left: int = 1
  right: int = 2
  fill: int = 3
  leading: int = 4
  trailing: int = 5


# ref: [UIControlContentVerticalAlignment | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicontrolcontentverticalalignment?language=objc)
@dataclass
class UIControlContentVerticalAlignment:
  center: int = 0
  top: int = 1
  bottom: int = 2
  fill: int = 3


# ref: [UIPageControlBackgroundStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uipagecontrolbackgroundstyle?language=objc)
@dataclass
class UIPageControlBackgroundStyle:
  automatic: int = 0
  prominent: int = 1
  minimal: int = 2


# ref: [UISearchBarIcon | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uisearchbaricon?language=objc)
@dataclass
class UISearchBarIcon:
  search: int = 0
  clear: int = 1
  bookmark: int = 2
  resultsList: int = 3


# ref: [UIUserInterfaceIdiom | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiuserinterfaceidiom?language=objc)
@dataclass
class UIUserInterfaceIdiom:
  unspecified: int = -1
  phone: int = 0
  pad: int = 1
  tv: int = 2
  carPlay: int = 3
  mac: int = 5
  vision: int = 6


# ref: [UIUserInterfaceStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiuserinterfacestyle?language=objc)
@dataclass
class UIUserInterfaceStyle:
  unspecified: int = 0
  light: int = 1
  dark: int = 2


# ref: [UIBarMetrics | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibarmetrics?language=objc)
@dataclass
class UIBarMetrics:
  default: int = 0  # xxx: '`' で囲まれてる
  compact: int = 1
  defaultPrompt: int = 101
  compactPrompt: int = 102
  landscapePhone: int = compact  # todo: Deprecated
  landscapePhonePrompt: int = compactPrompt  # todo: Deprecated


# ref: [UIBehavioralStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibehavioralstyle?language=objc)
@dataclass
class UIBehavioralStyle:
  automatic: int = 0
  pad: int = 1
  mac: int = 2


# ref: [UISwitchStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiswitchstyle?language=objc&language=objc)
@dataclass
class UISwitchStyle:
  automatic: int = 0
  checkbox: int = 1
  sliding: int = 2


# ref: [UITextBorderStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitextborderstyle?language=objc)
@dataclass
class UITextBorderStyle:
  none: int = 0
  line: int = 1
  bezel: int = 2
  roundedRect: int = 3


# ref: [UITextAutocorrectionType | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitextautocorrectiontype?language=objc)
@dataclass
class UITextAutocorrectionType:
  default: int = 0
  no: int = 1
  yes: int = 2


# ref: [UIReturnKeyType | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uireturnkeytype?language=objc)
@dataclass
class UIReturnKeyType:
  default: int = 0
  go: int = 1
  google: int = 2
  join: int = 3
  next: int = 4
  route: int = 5
  search: int = 6
  send: int = 7
  yahoo: int = 8
  done: int = 9
  emergencyCall: int = 10
  _continue: int = 11  # todo: 予約語のため


# ref: [UITextFieldViewMode | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitextfieldviewmode?language=objc)
@dataclass
class UITextFieldViewMode:
  never: int = 0
  whileEditing: int = 1
  unlessEditing: int = 2
  always: int = 3


# ref: [UIKeyboardType | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uikeyboardtype?language=objc)
@dataclass
class UIKeyboardType:
  default: int = 0
  asciiCapable: int = 1
  numbersAndPunctuation: int = 2
  URL: int = 3
  numberPad: int = 4
  phonePad: int = 5
  namePhonePad: int = 6
  emailAddress: int = 7
  decimalPad: int = 8
  twitter: int = 9
  webSearch: int = 10
  asciiCapableNumberPad: int = 11


# ref: [UISplitViewControllerDisplayMode | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdisplaymode?language=objc)
@dataclass
class UISplitViewControllerDisplayMode:
  automatic: int = 0
  secondaryOnly: int = 1
  oneBesideSecondary: int = 2
  oneOverSecondary: int = 3
  twoBesideSecondary: int = 4
  twoOverSecondary: int = 5
  twoDisplaceSecondary: int = 6


# ref: [UIUserInterfaceSizeClass | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiuserinterfacesizeclass?language=objc)
@dataclass
class UIUserInterfaceSizeClass:
  unspecified: int = 0
  compact: int = 1
  regular: int = 2


# ref: [UICellAccessoryOutlineDisclosureStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicellaccessoryoutlinedisclosurestyle?language=objc)
@dataclass
class UICellAccessoryOutlineDisclosureStyle:
  # ref: [UICellAccessory.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UICellAccessory.rs.html#467)
  automatic: int = 0
  header: int = 1
  cell: int = 2


# ref: [UITableViewRowAnimation | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitableview/rowanimation?language=objc)
@dataclass
class UITableViewRowAnimation:
  # ref: [UITableView.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UITableView.rs.html#59)
  fade: int = 0
  right: int = 1
  left: int = 2
  top: int = 3
  bottom: int = 4
  none: int = 5
  middle: int = 6
  automatic: int = 100


# ref: [UIActivityIndicatorViewStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/style-swift.enum?language=objc)
@dataclass
class UIActivityIndicatorViewStyle:
  # ref: [UIActivityIndicatorView.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIActivityIndicatorView.rs.html#14)
  large: int = 101
  medium: int = 100
  whiteLarge: int = 0  # todo: Deprecated
  white: int = 1  # todo: Deprecated
  gray: int = 2  # todo: Deprecated


# ref: [UIAlertControllerStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uialertcontroller/style?language=objc)
@dataclass
class UIAlertControllerStyle:
  # ref: [UIAlertController.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIAlertController.rs.html#31)
  actionSheet: int = 0
  alert: int = 1


# ref: [UIAlertActionStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uialertaction/style-swift.enum?language=objc)
@dataclass
class UIAlertActionStyle:
  # ref: [UIAlertController.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIAlertController.rs.html#11)
  default: int = 0
  cancel: int = 1
  destructive: int = 2


# ref: [NSLineBreakMode | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nslinebreakmode?language=objc)
@dataclass
class NSLineBreakMode:
  # ref: [NSParagraphStyle.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/NSParagraphStyle.rs.html#11)
  byWordWrapping: int = 0
  byCharWrapping: int = 1
  byClipping: int = 2
  byTruncatingHead: int = 3
  byTruncatingTail: int = 4
  byTruncatingMiddle: int = 5


# ref: [UIFontDescriptorSymbolicTraits | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits-swift.struct?language=objc)
@dataclass
class UIFontDescriptorSymbolicTraits:
  # ref: [UIFontDescriptor.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIFontDescriptor.rs.html#11)
  traitItalic: int = 1 << 0
  traitBold: int = 1 << 1
  traitExpanded: int = 1 << 5
  traitCondensed: int = 1 << 6
  traitMonoSpace: int = 1 << 10
  traitVertical: int = 1 << 11
  traitUIOptimized: int = 1 << 12
  traitTightLeading: int = 1 << 15
  traitLooseLeading: int = 1 << 16
  classMask: int = 0xF0000000
  classUnknown: int = 0 << 28  # xxx: ?
  classOldStyleSerifs: int = 1 << 28
  classTransitionalSerifs: int = 2 << 28
  classModernSerifs: int = 3 << 28
  classClarendonSerifs: int = 4 << 28
  classSlabSerifs: int = 5 << 28
  classFreeformSerifs: int = 7 << 28
  classSansSerif: int = 8 << 28
  classOrnamentals: int = 9 << 28
  classScripts: int = 10 << 28
  classSymbolic: int = 12 << 28


# ref: [NSLayoutAttribute | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nslayoutconstraint/attribute?language=objc)
@dataclass
class NSLayoutAttribute:
  # ref [NSLayoutConstraint.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/NSLayoutConstraint.rs.html#49)
  left: int = 1
  right: int = 2
  top: int = 3
  bottom: int = 4
  leading: int = 5
  trailing: int = 6
  width: int = 7
  height: int = 8
  centerX: int = 9
  centerY: int = 10
  lastBaseline: int = 11
  firstBaseline: int = 12
  leftMargin: int = 13
  rightMargin: int = 14
  topMargin: int = 15
  bottomMargin: int = 16
  leadingMargin: int = 17
  trailingMargin: int = 18
  centerXWithinMargins: int = 19
  centerYWithinMargins: int = 20
  notAnAttribute: int = 0


# ref: [NSLayoutRelation | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nslayoutconstraint/relation-swift.enum?language=objc)
@dataclass
class NSLayoutRelation:
  # ref: [NSLayoutConstraint.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/NSLayoutConstraint.rs.html#28)
  lessThanOrEqual: int = -1
  equal: int = 0
  greaterThanOrEqual: int = 1


# ref: [UIViewAnimationCurve | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiview/animationcurve?language=objc)
@dataclass
class UIViewAnimationCurve:
  # ref: [UIView.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIView.rs.html#14)
  easeInOut: int = 0
  easeIn: int = 1
  easeOut: int = 2
  linear: int = 3


# ref: [UIProgressViewStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiprogressview/style?language=objc)
@dataclass
class UIProgressViewStyle:
  default: int = 0
  bar: int = 1


# ref: [NSKeyValueObservingOptions | Apple Developer Documentation](https://developer.apple.com/documentation/foundation/nskeyvalueobservingoptions?language=objc)
@dataclass
class NSKeyValueObservingOptions:
  new: int = 0x01
  old: int = 0x02
  initial: int = 0x04
  prior: int = 0x08


# ref: [UILayoutConstraintAxis | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nslayoutconstraint/axis?language=objc)
@dataclass
class UILayoutConstraintAxis:
  # ref: [UIView.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIView.rs.html#1002)
  horizontal: int = 0
  vertical: int = 1


# wip: [text.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/text.rs.html#8)
'''
(!TARGET_CPU_X86_64 || (TARGET_OS_IPHONE && !TARGET_OS_MACCATALYST))
<https://github.com/xamarin/xamarin-macios/issues/12111>
TODO: Make this work with mac catalyst
const TARGET_ABI_USES_IOS_VALUES: bool =
    !cfg!(any(target_arch = "x86", target_arch = "x86_64")) || cfg!(not(target_os = "macos"));
'''


# ref: [NSTextAlignment | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nstextalignment?language=objc)
@dataclass
class NSTextAlignment:
  # ref: [text.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/text.rs.html#26)
  left: int = 0
  right: int = 2  # wip: `TARGET_ABI_USES_IOS_VALUES`
  center: int = 1  # wip: `TARGET_ABI_USES_IOS_VALUES`
  justified: int = 3
  natural: int = 4


# ref: [UIControlContentVerticalAlignment | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicontrol/contentverticalalignment-swift.enum?language=objc)
@dataclass
class UIControlContentVerticalAlignment:
  # ref: [UIControl.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIControl.rs.html#52)
  center: int = 0
  top: int = 1
  bottom: int = 2
  fill: int = 3


# ref: [UIControlContentHorizontalAlignment | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicontrol/contenthorizontalalignment-swift.enum?language=objc)
@dataclass
class UIControlContentHorizontalAlignment:
  # ref: [UIControl.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIControl.rs.html#75)
  center: int = 0
  left: int = 1
  right: int = 2
  fill: int = 3
  leading: int = 4
  trailing: int = 5


# ref: [UIStackViewAlignment | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uistackview/alignment-swift.enum?language=objc)
@dataclass
class UIStackViewAlignment:
  # ref: [UIStackView.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIStackView.rs.html#39)
  fill: int = 0
  leading: int = 1
  top: int = 1  # xxx: [UIStackViewAlignment Enum (UIKit) | Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/api/uikit.uistackviewalignment?view=xamarin-ios-sdk-12)
  firstBaseline: int = 2
  center: int = 3
  trailing: int = 4
  bottom: int = 4  # xxx: [UIStackViewAlignment Enum (UIKit) | Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/api/uikit.uistackviewalignment?view=xamarin-ios-sdk-12)
  lastBaseline: int = 5


# ref: [UIBarStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibarstyle?language=objc)
@dataclass
class UIBarStyle:
  # ref: [UIInterface.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIInterface.rs.html#12)
  default: int = 0
  black: int = 1
  blackOpaque: int = 1  # xxx: deprecated
  blackTranslucent: int = 2  # xxx: deprecated


# ref: [UIBarPosition | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibarposition?language=objc)
@dataclass
class UIBarPosition:
  # ref: [UIBarCommon.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIBarCommon.rs.html#40)
  any: int = 0
  bottom: int = 1
  top: int = 2
  topAttached: int = 3


# ref: [UIBarMetrics | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibarmetrics?language=objc)
@dataclass
class UIBarMetrics:
  # ref: [UIBarCommon.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIBarCommon.rs.html#11)
  default: int = 0
  compact: int = 1
  defaultPrompt: int = 101
  compactPrompt: int = 102
  landscapePhone: int = default  # xxx: deprecated
  landscapePhonePrompt: int = default  # xxx: deprecated


# ref: [UIBlurEffectStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiblureffect/style?language=objc)
@dataclass
class UIBlurEffectStyle:
  # ref: [UIBlurEffect.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIBlurEffect.rs.html#12)
  extraLight: int = 0
  light: int = 1
  dark: int = 2
  extraDark: int = 3
  regular: int = 4
  prominent: int = 5
  systemUltraThinMaterial: int = 6
  systemThinMaterial: int = 7
  systemMaterial: int = 8
  systemThickMaterial: int = 9
  systemChromeMaterial: int = 10
  systemUltraThinMaterialLight: int = 11
  systemThinMaterialLight: int = 12
  systemMaterialLight: int = 13
  systemThickMaterialLight: int = 14
  systemChromeMaterialLight: int = 15
  systemUltraThinMaterialDark: int = 16
  systemThinMaterialDark: int = 17
  systemMaterialDark: int = 18
  systemThickMaterialDark: int = 19
  systemChromeMaterialDark: int = 20


# ref: [UIDatePickerMode | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uidatepicker/mode?language=objc)
@dataclass
class UIDatePickerMode:
  # ref: [UIDatePicker.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIDatePicker.rs.html#15)
  time: int = 0
  date: int = 1
  dateAndTime: int = 2
  countDownTimer: int = 3
  yearAndMonth: int = 4


# ref: [UIDatePickerStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uidatepickerstyle?language=objc)
@dataclass
class UIDatePickerStyle:
  # ref: [UIDatePicker.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIDatePicker.rs.html#40)
  automatic: int = 0
  wheels: int = 1
  compact: int = 2
  inline: int = 3


# ref: [NSDateFormatterStyle | Apple Developer Documentation](https://developer.apple.com/documentation/foundation/nsdateformatterstyle?language=objc)
@dataclass
class NSDateFormatterStyle:
  none: int = 0
  short: int = 1
  medium: int = 2
  long: int = 3
  full: int = 4


# ref: [NSCalendarUnit | Apple Developer Documentation](https://developer.apple.com/documentation/foundation/nscalendarunit)
@dataclass
class NSCalendarUnit:
  # ref: [NSCalendar.rs - source](https://docs.rs/objc2-foundation/0.2.2/aarch64-apple-ios/src/objc2_foundation/generated/NSCalendar.rs.html#94)
  era: int = 2
  year: int = 4
  month: int = 8
  day: int = 16
  hour: int = 32
  minute: int = 64
  second: int = 128
  weekday: int = 512
  weekdayOrdinal: int = 1024
  quarter: int = 2048
  weekOfMonth: int = 4096
  weekOfYear: int = 8192
  yearForWeekOfYear: int = 16384
  nanosecond: int = 32768
  calendar: int = 1048576
  timeZone: int = 2097152
  # deprecated ---
  NSEraCalendarUnit: int = 2
  NSYearCalendarUnit: int = 4
  NSMonthCalendarUnit: int = 8
  NSDayCalendarUnit: int = 16
  NSHourCalendarUnit: int = 32
  NSMinuteCalendarUnit: int = 64
  NSSecondCalendarUnit: int = 128
  # `NSCalendarUnitWeekOfMonth` or `NSCalendarUnitWeekOfYear` , depending on which you mean
  NSWeekCalendarUnit: int = 256
  NSWeekdayCalendarUnit: int = 512
  NSWeekdayOrdinalCalendarUnit: int = 1024
  NSQuarterCalendarUnit: int = 2048
  NSWeekOfMonthCalendarUnit: int = 4096
  NSWeekOfYearCalendarUnit: int = 8192
  NSYearForWeekOfYearCalendarUnit: int = 16384
  NSCalendarCalendarUnit: int = 1048576
  NSTimeZoneCalendarUnit: int = 2097152
  # --- deprecated


# ref: [UIBarButtonItemStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibarbuttonitem/style-swift.enum?language=objc)
@dataclass
class UIBarButtonItemStyle:
  # ref: [UIBarButtonItem.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIBarButtonItem.rs.html#14)
  plain: int = 0
  bordered: int = 1  # Deprecated
  done: int = 2


# ref: [UIFontDescriptorSymbolicTraits | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits-swift.struct?language=objc)
@dataclass
class UIFontDescriptorSymbolicTraits:
  # ref: [UIFontDescriptor.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIFontDescriptor.rs.html#11)
  traitItalic: int = 1 << 0
  traitBold: int = 1 << 1
  traitExpanded: int = 1 << 5
  traitCondensed: int = 1 << 6
  traitMonoSpace: int = 1 << 10
  traitVertical: int = 1 << 11
  traitUIOptimized: int = 1 << 12
  traitTightLeading: int = 1 << 15
  traitLooseLeading: int = 1 << 16
  classMask: int = 0xF0000000
  UIFontDescriptorClassUnknown: int = 0 << 28  # xxx: Swift ?
  classOldStyleSerifs: int = 1 << 28
  classTransitionalSerifs: int = 2 << 28
  classModernSerifs: int = 3 << 28
  classClarendonSerifs: int = 4 << 28
  classSlabSerifs: int = 5 << 28
  classFreeformSerifs: int = 7 << 28
  classSansSerif: int = 8 << 28
  classOrnamentals: int = 9 << 28
  classScripts: int = 10 << 28
  classSymbolic: int = 12 << 28


# ref: [UIImagePickerControllerSourceType | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/sourcetype-swift.enum?language=objc)
@dataclass
class UIImagePickerControllerSourceType:
  # ref: [UIImagePickerController.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIImagePickerController.rs.html#12)
  photoLibrary: int = 0  # todo: deprecated
  camera: int = 1
  savedPhotosAlbum: int = 2  # todo: deprecated


# ref: [NSURLRequestCachePolicy | Apple Developer Documentation](https://developer.apple.com/documentation/foundation/nsurlrequestcachepolicy)
@dataclass
class NSURLRequestCachePolicy:
  useProtocolCachePolicy: int = 0
  reloadIgnoringLocalCacheData: int = 1
  reloadIgnoringLocalAndRemoteCacheData: int = 4
  reloadIgnoringCacheData: int = reloadIgnoringLocalCacheData
  returnCacheDataElseLoad: int = 2
  returnCacheDataDontLoad: int = 3
  reloadRevalidatingCacheData: int = 5


# ref: [WKNavigationActionPolicy | Apple Developer Documentation](https://developer.apple.com/documentation/webkit/wknavigationactionpolicy?language=objc)
@dataclass
class WKNavigationActionPolicy:
  cancel: int = 0
  allow: int = 1
  download: int = 2

