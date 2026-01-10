from enum import IntEnum, IntFlag

# ref: [NSURLErrorNotConnectedToInternet | Apple Developer Documentation](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes/nsurlerrornotconnectedtointernet?language=objc)
NSURLErrorNotConnectedToInternet = -1009


# ref: [UIModalPresentationStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle)
class UIModalPresentationStyle(IntEnum):
  automatic = -2
  none = -1
  fullScreen = 0
  pageSheet = 1
  formSheet = 2
  currentContext = 3
  custom = 4
  overFullScreen = 5
  overCurrentContext = 6
  popover = 7
  blurOverFullScreen = 8


# ref: [UIRectEdge | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uirectedge?language=objc)
class UIRectEdge(IntEnum):
  none = 0
  top = 1 << 0
  left = 1 << 1
  bottom = 1 << 2
  right = 1 << 3
  all = top | left | bottom | right


# ref: [UIBarButtonSystemItem | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibarbuttonsystemitem?language=objc)
class UIBarButtonSystemItem(IntEnum):
  done = 0
  cancel = 1
  edit = 2
  save = 3
  add = 4
  flexibleSpace = 5
  fixedSpace = 6
  compose = 7
  reply = 8
  action = 9
  organize = 10
  bookmarks = 11
  search = 12
  refresh = 13
  stop = 14
  camera = 15
  trash = 16
  play = 17
  pause = 18
  rewind = 19
  fastForward = 20
  undo = 21
  redo = 22
  pageCurl = 23  # Deprecated
  close = 24
  writingTools = 25


# ref: [UIButtonType | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibuttontype?language=objc)
class UIButtonType(IntEnum):
  custom = 0
  system = 1
  detailDisclosure = 2
  infoLight = 3
  infoDark = 4
  contactAdd = 5
  plain = 6
  close = 7


# ref: [UIControlState | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicontrolstate?language=objc)
class UIControlState(IntFlag):
  normal = 0
  highlighted = 1 << 0
  disabled = 1 << 1
  selected = 1 << 2
  focused = 1 << 3
  application = 0x00FF0000
  reserved = 0xFF000000


# ref: [UIControlEvents | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicontrolevents?language=objc)
class UIControlEvents(IntFlag):
  touchDown = 1 << 0
  touchDownRepeat = 1 << 1
  touchDragInside = 1 << 2
  touchDragOutside = 1 << 3
  touchDragEnter = 1 << 4
  touchDragExit = 1 << 5
  touchUpInside = 1 << 6
  touchUpOutside = 1 << 7
  touchCancel = 1 << 8
  valueChanged = 1 << 12
  menuActionTriggered = 1 << 14
  primaryActionTriggered = 1 << 13
  editingDidBegin = 1 << 16
  editingChanged = 1 << 17
  editingDidEnd = 1 << 18
  editingDidEndOnExit = 1 << 19
  allTouchEvents = 0x00000FFF
  allEditingEvents = 0x000F0000
  applicationReserved = 0x0F000000
  systemReserved = 0xF0000000
  allEvents = 0xFFFFFFFF


# ref: [UIListContentTextAlignment | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uilistcontenttextalignment)
class UIListContentTextAlignment(IntEnum):
  # todo: `Enumeration Case` に値表記が無いので独自に調査
  natural = 0
  center = 1
  justified = 2


# ref: [UITableViewStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitableviewstyle?language=objc)
class UITableViewStyle(IntEnum):
  plain = 0
  grouped = 1
  insetGrouped = 2


# ref: [UIButtonConfigurationCornerStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibuttonconfigurationcornerstyle?language=objc)
class UIButtonConfigurationCornerStyle(IntEnum):
  # todo: `Enumeration Case` に値表記が無いので独自に調査
  dynamic = 0
  fixed = -1
  capsule = 4
  large = 3
  medium = 2
  small = 1


# ref: [UIImageRenderingMode | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimagerenderingmode?language=objc)
class UIImageRenderingMode(IntEnum):
  automatic = 0
  alwaysOriginal = 1
  alwaysTemplate = 2


# ref: [NSUnderlineStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nsunderlinestyle?language=objc)
class NSUnderlineStyle(IntFlag):
  # ref: [NSAttributedString.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/NSAttributedString.rs.html#87)
  none = 0x00  # xxx: patternSolid ?
  single = 0x01
  thick = 0x02
  double = 0x09
  patternSolid = 0x0000  # xxx: none ?
  patternDot = 0x0100
  patternDash = 0x0200
  patternDashDot = 0x0300
  patternDashDotDot = 0x0400
  byWord = 0x8000


# ref: [UIImageSymbolScale | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimagesymbolscale?language=objc)
class UIImageSymbolScale(IntEnum):
  default = -1
  unspecified = 0
  small = 1
  medium = 2
  large = 3


# ref: [UIImageSymbolWeight | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimagesymbolweight?language=objc)
class UIImageSymbolWeight(IntEnum):
  unspecified = 0
  ultraLight = 1
  thin = 2
  light = 3
  regular = 4
  medium = 5
  semibold = 6
  bold = 7
  heavy = 8
  black = 9


# ref: [NSDirectionalRectEdge | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nsdirectionalrectedge?language=objc)
class NSDirectionalRectEdge(IntFlag):
  none = 0  # ref: [NSDirectionalRectEdgeNone | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nsdirectionalrectedge/nsdirectionalrectedgenone?language=objc)
  top = 1 << 0
  leading = 1 << 1
  bottom = 1 << 2
  trailing = 1 << 3
  all = top | leading | bottom | trailing


# ref: [UIButtonConfigurationSize | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibuttonconfigurationsize)
class UIButtonConfigurationSize(IntEnum):
  # todo: `Enumeration Case` に値表記が無いので独自に調査
  medium = 0
  small = 1
  mini = 2
  large = 3


# ref: [UIMenuElementState | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uimenuelementstate?language=objc)
class UIMenuElementState(IntEnum):
  off = 0
  on = 1
  mixed = 2


# ref: [UIMenuElementAttributes | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uimenuelementattributes)
class UIMenuElementAttributes(IntFlag):
  destructive = 1 << 1
  disabled = 1 << 0
  hidden = 1 << 2
  keepsMenuPresented = 1 << 3


# ref: [UIMenuOptions | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uimenuoptions?language=objc)
class UIMenuOptions(IntFlag):
  displayInline = 1 << 0
  destructive = 1 << 1
  singleSelection = 1 << 5
  displayAsPalette = 1 << 7


# ref: [UISplitViewControllerStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerstyle?language=objc)
class UISplitViewControllerStyle(IntEnum):
  doubleColumn = 1
  tripleColumn = 2


# ref: [UISplitViewControllerColumn | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uisplitviewcontrollercolumn?language=objc)
class UISplitViewControllerColumn(IntEnum):
  primary = 0
  supplementary = 1
  secondary = 2
  compact = 3


# ref: [UICollectionLayoutListAppearance | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistappearance?language=objc)
class UICollectionLayoutListAppearance(IntEnum):
  # ref: [UICollectionLayoutList.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UICollectionLayoutList.rs.html#16)
  plain = 0
  grouped = 1
  insetGrouped = 2
  sidebar = 3
  sidebarPlain = 4


# ref: [UICollectionLayoutListHeaderMode | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistheadermode)
class UICollectionLayoutListHeaderMode(IntEnum):
  # xxx: 独自調査 a.k.a: 勘
  # ref: [UICollectionLayoutList.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UICollectionLayoutList.rs.html)
  none = 0
  supplementary = 1
  firstItemInSection = 2


# ref: [UIViewAutoresizing | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiviewautoresizing?language=objc)
class UIViewAutoresizing(IntFlag):
  none = 0  # ref: [UIViewAutoresizingNone | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiviewautoresizing/uiviewautoresizingnone?language=objc)
  flexibleLeftMargin = 1 << 0
  flexibleWidth = 1 << 1
  flexibleRightMargin = 1 << 2
  flexibleTopMargin = 1 << 3
  flexibleHeight = 1 << 4
  flexibleBottomMargin = 1 << 5


# ref: [UIViewContentMode | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiviewcontentmode?language=objc)
class UIViewContentMode(IntEnum):
  scaleToFill = 0
  scaleAspectFit = 1
  scaleAspectFill = 2
  redraw = 3
  center = 4
  top = 5
  bottom = 6
  left = 7
  right = 8
  topLeft = 9
  topRight = 10
  bottomLeft = 11
  bottomRight = 12


# ref: [UIControlContentHorizontalAlignment | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicontrolcontenthorizontalalignment?language=objc)
class UIControlContentHorizontalAlignment(IntEnum):
  center = 0
  left = 1
  right = 2
  fill = 3
  leading = 4
  trailing = 5


# ref: [UIControlContentVerticalAlignment | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicontrolcontentverticalalignment?language=objc)
class UIControlContentVerticalAlignment(IntEnum):
  center = 0
  top = 1
  bottom = 2
  fill = 3


# ref: [UIPageControlBackgroundStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uipagecontrolbackgroundstyle?language=objc)
class UIPageControlBackgroundStyle(IntEnum):
  automatic = 0
  prominent = 1
  minimal = 2


# ref: [UISearchBarIcon | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uisearchbaricon?language=objc)
class UISearchBarIcon(IntEnum):
  search = 0
  clear = 1
  bookmark = 2
  resultsList = 3


# ref: [UIUserInterfaceIdiom | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiuserinterfaceidiom?language=objc)
class UIUserInterfaceIdiom(IntEnum):
  unspecified = -1
  phone = 0
  pad = 1
  tv = 2
  carPlay = 3
  mac = 5
  vision = 6


# ref: [UIUserInterfaceStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiuserinterfacestyle?language=objc)
class UIUserInterfaceStyle(IntEnum):
  unspecified = 0
  light = 1
  dark = 2


# ref: [UIBarMetrics | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibarmetrics?language=objc)
class UIBarMetrics(IntFlag):
  default = 0  # xxx: '`' で囲まれてる
  compact = 1
  defaultPrompt = 101
  compactPrompt = 102
  landscapePhone = compact  # todo: Deprecated
  landscapePhonePrompt = compactPrompt  # todo: Deprecated


# ref: [UIBehavioralStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibehavioralstyle?language=objc)
class UIBehavioralStyle(IntEnum):
  automatic = 0
  pad = 1
  mac = 2


# ref: [UISwitchStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiswitchstyle?language=objc&language=objc)
class UISwitchStyle(IntEnum):
  automatic = 0
  checkbox = 1
  sliding = 2


# ref: [UITextBorderStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitextborderstyle?language=objc)
class UITextBorderStyle(IntEnum):
  none = 0
  line = 1
  bezel = 2
  roundedRect = 3


# ref: [UITextAutocorrectionType | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitextautocorrectiontype?language=objc)
class UITextAutocorrectionType(IntEnum):
  default = 0
  no = 1
  yes = 2


# ref: [UIReturnKeyType | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uireturnkeytype?language=objc)
class UIReturnKeyType(IntEnum):
  default = 0
  go = 1
  google = 2
  join = 3
  next = 4
  route = 5
  search = 6
  send = 7
  yahoo = 8
  done = 9
  emergencyCall = 10
  _continue = 11  # todo: 予約語のため


# ref: [UITextFieldViewMode | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitextfieldviewmode?language=objc)
class UITextFieldViewMode(IntEnum):
  never = 0
  whileEditing = 1
  unlessEditing = 2
  always = 3


# ref: [UIKeyboardType | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uikeyboardtype?language=objc)
class UIKeyboardType(IntEnum):
  default = 0
  asciiCapable = 1
  numbersAndPunctuation = 2
  URL = 3
  numberPad = 4
  phonePad = 5
  namePhonePad = 6
  emailAddress = 7
  decimalPad = 8
  twitter = 9
  webSearch = 10
  asciiCapableNumberPad = 11


# ref: [UISplitViewControllerDisplayMode | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdisplaymode?language=objc)
class UISplitViewControllerDisplayMode(IntEnum):
  automatic = 0
  secondaryOnly = 1
  oneBesideSecondary = 2
  oneOverSecondary = 3
  twoBesideSecondary = 4
  twoOverSecondary = 5
  twoDisplaceSecondary = 6


# ref: [UIUserInterfaceSizeClass | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiuserinterfacesizeclass?language=objc)
class UIUserInterfaceSizeClass(IntEnum):
  unspecified = 0
  compact = 1
  regular = 2


# ref: [UICellAccessoryOutlineDisclosureStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicellaccessoryoutlinedisclosurestyle?language=objc)
class UICellAccessoryOutlineDisclosureStyle(IntEnum):
  # ref: [UICellAccessory.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UICellAccessory.rs.html#467)
  automatic = 0
  header = 1
  cell = 2


# ref: [UITableViewRowAnimation | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitableview/rowanimation?language=objc)
class UITableViewRowAnimation(IntEnum):
  # ref: [UITableView.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UITableView.rs.html#59)
  fade = 0
  right = 1
  left = 2
  top = 3
  bottom = 4
  none = 5
  middle = 6
  automatic = 100


# ref: [UIActivityIndicatorViewStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/style-swift.enum?language=objc)
class UIActivityIndicatorViewStyle(IntEnum):
  # ref: [UIActivityIndicatorView.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIActivityIndicatorView.rs.html#14)
  large = 101
  medium = 100
  whiteLarge = 0  # todo: Deprecated
  white = 1  # todo: Deprecated
  gray = 2  # todo: Deprecated


# ref: [UIAlertControllerStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uialertcontroller/style?language=objc)
class UIAlertControllerStyle(IntEnum):
  # ref: [UIAlertController.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIAlertController.rs.html#31)
  actionSheet = 0
  alert = 1


# ref: [UIAlertActionStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uialertaction/style-swift.enum?language=objc)
class UIAlertActionStyle(IntEnum):
  # ref: [UIAlertController.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIAlertController.rs.html#11)
  default = 0
  cancel = 1
  destructive = 2


# ref: [NSLineBreakMode | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nslinebreakmode?language=objc)
class NSLineBreakMode(IntEnum):
  # ref: [NSParagraphStyle.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/NSParagraphStyle.rs.html#11)
  byWordWrapping = 0
  byCharWrapping = 1
  byClipping = 2
  byTruncatingHead = 3
  byTruncatingTail = 4
  byTruncatingMiddle = 5


# ref: [NSLayoutAttribute | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nslayoutconstraint/attribute?language=objc)
class NSLayoutAttribute(IntEnum):
  # ref [NSLayoutConstraint.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/NSLayoutConstraint.rs.html#49)
  left = 1
  right = 2
  top = 3
  bottom = 4
  leading = 5
  trailing = 6
  width = 7
  height = 8
  centerX = 9
  centerY = 10
  lastBaseline = 11
  firstBaseline = 12
  leftMargin = 13
  rightMargin = 14
  topMargin = 15
  bottomMargin = 16
  leadingMargin = 17
  trailingMargin = 18
  centerXWithinMargins = 19
  centerYWithinMargins = 20
  notAnAttribute = 0


# ref: [NSLayoutRelation | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nslayoutconstraint/relation-swift.enum?language=objc)
class NSLayoutRelation(IntEnum):
  # ref: [NSLayoutConstraint.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/NSLayoutConstraint.rs.html#28)
  lessThanOrEqual = -1
  equal = 0
  greaterThanOrEqual = 1


# ref: [UIViewAnimationCurve | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiview/animationcurve?language=objc)
class UIViewAnimationCurve(IntEnum):
  # ref: [UIView.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIView.rs.html#14)
  easeInOut = 0
  easeIn = 1
  easeOut = 2
  linear = 3


# ref: [UIProgressViewStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiprogressview/style?language=objc)
class UIProgressViewStyle(IntEnum):
  default = 0
  bar = 1


# ref: [NSKeyValueObservingOptions | Apple Developer Documentation](https://developer.apple.com/documentation/foundation/nskeyvalueobservingoptions?language=objc)
class NSKeyValueObservingOptions(IntFlag):
  new = 0x01
  old = 0x02
  initial = 0x04
  prior = 0x08


# ref: [UILayoutConstraintAxis | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nslayoutconstraint/axis?language=objc)
class UILayoutConstraintAxis(IntEnum):
  # ref: [UIView.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIView.rs.html#1002)
  horizontal = 0
  vertical = 1


# wip: [text.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/text.rs.html#8)
'''
(!TARGET_CPU_X86_64 || (TARGET_OS_IPHONE && !TARGET_OS_MACCATALYST))
<https://github.com/xamarin/xamarin-macios/issues/12111>
TODO: Make this work with mac catalyst
const TARGET_ABI_USES_IOS_VALUES: bool =
    !cfg!(any(target_arch = "x86", target_arch = "x86_64")) || cfg!(not(target_os = "macos"));
'''


# ref: [NSTextAlignment | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nstextalignment?language=objc)
class NSTextAlignment(IntEnum):
  # ref: [text.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/text.rs.html#26)
  left = 0
  right = 2  # wip: `TARGET_ABI_USES_IOS_VALUES`
  center = 1  # wip: `TARGET_ABI_USES_IOS_VALUES`
  justified = 3
  natural = 4


# ref: [UIStackViewAlignment | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uistackview/alignment-swift.enum?language=objc)
class UIStackViewAlignment(IntEnum):
  # ref: [UIStackView.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIStackView.rs.html#39)
  fill = 0
  leading = 1
  top = 1  # xxx: [UIStackViewAlignment Enum (UIKit) | Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/api/uikit.uistackviewalignment?view=xamarin-ios-sdk-12)
  firstBaseline = 2
  center = 3
  trailing = 4
  bottom = 4  # xxx: [UIStackViewAlignment Enum (UIKit) | Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/api/uikit.uistackviewalignment?view=xamarin-ios-sdk-12)
  lastBaseline = 5


# ref: [UIBarStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibarstyle?language=objc)
class UIBarStyle(IntEnum):
  # ref: [UIInterface.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIInterface.rs.html#12)
  default = 0
  black = 1
  blackOpaque = 1  # xxx: deprecated
  blackTranslucent = 2  # xxx: deprecated


# ref: [UIBarPosition | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibarposition?language=objc)
class UIBarPosition(IntEnum):
  # ref: [UIBarCommon.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIBarCommon.rs.html#40)
  any = 0
  bottom = 1
  top = 2
  topAttached = 3


# ref: [UIBlurEffectStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiblureffect/style?language=objc)
class UIBlurEffectStyle(IntEnum):
  # ref: [UIBlurEffect.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIBlurEffect.rs.html#12)
  extraLight = 0
  light = 1
  dark = 2
  extraDark = 3
  regular = 4
  prominent = 5
  systemUltraThinMaterial = 6
  systemThinMaterial = 7
  systemMaterial = 8
  systemThickMaterial = 9
  systemChromeMaterial = 10
  systemUltraThinMaterialLight = 11
  systemThinMaterialLight = 12
  systemMaterialLight = 13
  systemThickMaterialLight = 14
  systemChromeMaterialLight = 15
  systemUltraThinMaterialDark = 16
  systemThinMaterialDark = 17
  systemMaterialDark = 18
  systemThickMaterialDark = 19
  systemChromeMaterialDark = 20


# ref: [UIDatePickerMode | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uidatepicker/mode?language=objc)
class UIDatePickerMode(IntEnum):
  # ref: [UIDatePicker.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIDatePicker.rs.html#15)
  time = 0
  date = 1
  dateAndTime = 2
  countDownTimer = 3
  yearAndMonth = 4


# ref: [UIDatePickerStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uidatepickerstyle?language=objc)
class UIDatePickerStyle(IntEnum):
  # ref: [UIDatePicker.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIDatePicker.rs.html#40)
  automatic = 0
  wheels = 1
  compact = 2
  inline = 3


# ref: [NSDateFormatterStyle | Apple Developer Documentation](https://developer.apple.com/documentation/foundation/nsdateformatterstyle?language=objc)
class NSDateFormatterStyle(IntEnum):
  none = 0
  short = 1
  medium = 2
  long = 3
  full = 4


# ref: [NSCalendarUnit | Apple Developer Documentation](https://developer.apple.com/documentation/foundation/nscalendarunit)
class NSCalendarUnit(IntEnum):
  # ref: [NSCalendar.rs - source](https://docs.rs/objc2-foundation/0.2.2/aarch64-apple-ios/src/objc2_foundation/generated/NSCalendar.rs.html#94)
  era = 2
  year = 4
  month = 8
  day = 16
  hour = 32
  minute = 64
  second = 128
  weekday = 512
  weekdayOrdinal = 1024
  quarter = 2048
  weekOfMonth = 4096
  weekOfYear = 8192
  yearForWeekOfYear = 16384
  nanosecond = 32768
  calendar = 1048576
  timeZone = 2097152
  # deprecated ---
  NSEraCalendarUnit = 2
  NSYearCalendarUnit = 4
  NSMonthCalendarUnit = 8
  NSDayCalendarUnit = 16
  NSHourCalendarUnit = 32
  NSMinuteCalendarUnit = 64
  NSSecondCalendarUnit = 128
  # `NSCalendarUnitWeekOfMonth` or `NSCalendarUnitWeekOfYear` , depending on which you mean
  NSWeekCalendarUnit = 256
  NSWeekdayCalendarUnit = 512
  NSWeekdayOrdinalCalendarUnit = 1024
  NSQuarterCalendarUnit = 2048
  NSWeekOfMonthCalendarUnit = 4096
  NSWeekOfYearCalendarUnit = 8192
  NSYearForWeekOfYearCalendarUnit = 16384
  NSCalendarCalendarUnit = 1048576
  NSTimeZoneCalendarUnit = 2097152
  # --- deprecated


# ref: [UIBarButtonItemStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibarbuttonitem/style-swift.enum?language=objc)
class UIBarButtonItemStyle(IntEnum):
  # ref: [UIBarButtonItem.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIBarButtonItem.rs.html#14)
  plain = 0
  bordered = 1  # Deprecated
  done = 2


# ref: [UIFontDescriptorSymbolicTraits | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits-swift.struct?language=objc)
class UIFontDescriptorSymbolicTraits(IntFlag):
  # ref: [UIFontDescriptor.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIFontDescriptor.rs.html#11)
  traitItalic = 1 << 0
  traitBold = 1 << 1
  traitExpanded = 1 << 5
  traitCondensed = 1 << 6
  traitMonoSpace = 1 << 10
  traitVertical = 1 << 11
  traitUIOptimized = 1 << 12
  traitTightLeading = 1 << 15
  traitLooseLeading = 1 << 16
  classMask = 0xF0000000
  UIFontDescriptorClassUnknown = 0 << 28  # xxx: Swift ?
  classOldStyleSerifs = 1 << 28
  classTransitionalSerifs = 2 << 28
  classModernSerifs = 3 << 28
  classClarendonSerifs = 4 << 28
  classSlabSerifs = 5 << 28
  classFreeformSerifs = 7 << 28
  classSansSerif = 8 << 28
  classOrnamentals = 9 << 28
  classScripts = 10 << 28
  classSymbolic = 12 << 28


# ref: [UIImagePickerControllerSourceType | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/sourcetype-swift.enum?language=objc)
class UIImagePickerControllerSourceType(IntEnum):
  # ref: [UIImagePickerController.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UIImagePickerController.rs.html#12)
  photoLibrary = 0  # todo: deprecated
  camera = 1
  savedPhotosAlbum = 2  # todo: deprecated


# ref: [NSURLRequestCachePolicy | Apple Developer Documentation](https://developer.apple.com/documentation/foundation/nsurlrequestcachepolicy)
class NSURLRequestCachePolicy(IntFlag):
  useProtocolCachePolicy = 0
  reloadIgnoringLocalCacheData = 1
  reloadIgnoringLocalAndRemoteCacheData = 4
  reloadIgnoringCacheData = reloadIgnoringLocalCacheData
  returnCacheDataElseLoad = 2
  returnCacheDataDontLoad = 3
  reloadRevalidatingCacheData = 5


# ref: [WKNavigationActionPolicy | Apple Developer Documentation](https://developer.apple.com/documentation/webkit/wknavigationactionpolicy?language=objc)
class WKNavigationActionPolicy(IntEnum):
  cancel = 0
  allow = 1
  download = 2


# ref: [UISceneActivationState | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiscene/activationstate-swift.enum?language=objc)
class UISceneActivationState(IntEnum):
  # ref: [UISceneDefinitions.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/generated/UISceneDefinitions.rs.html#12)
  unattached = -1
  foregroundActive = 0
  foregroundInactive = 1
  background = 2
