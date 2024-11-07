from dataclasses import dataclass


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
  # xxx: 独自調査 a.k.a: 勘
  plain: int = 0
  grouped: int = 1
  insetGrouped: int = 2
  sidebar: int = 3
  sidebarPlain: int = 4


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
  default: int = 0  # xxx: '`' で囲まれてる
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

