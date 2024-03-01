from dataclasses import dataclass


@dataclass
class UIRectEdge:
  # ref: [UIRectEdge | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uirectedge?language=objc)
  none: int = 0
  top: int = 1 << 0
  left: int = 1 << 1
  bottom: int = 1 << 2
  right: int = 1 << 3
  all: int = top | left | bottom | right


@dataclass
class UIView_ContentMode:
  # ref: [UIView.ContentMode | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiview/contentmode)
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


@dataclass
class UIModalPresentationStyle:
  # ref: [UIModalPresentationStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle)
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


@dataclass
class UITableViewCell_AccessoryType:
  # ref: [UITableViewCell.AccessoryType | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype)
  none: int = 0
  disclosureIndicator: int = 1
  detailDisclosureButton: int = 2
  checkmark: int = 3
  detailButton: int = 4


@dataclass
class UIBarButtonItem_SystemItem:
  # ref: [UIBarButtonSystemItem | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibarbuttonsystemitem?language=objc)
  done = 0
  cancel = 1
  edit = 2
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
  trash = 16
  play = 17
  pause = 18
  rewind = 19
  fastForward = 20
  undo = 21
  redo = 22
  pageCurl = 23  # Deprecated
  close = 24


@dataclass
class NSTextAlignment:
  # ref: [NSTextAlignment | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nstextalignment?language=objc)
  left = 0
  right = 2
  center = 1
  justified = 3
  natural = 4


@dataclass
class UIButton_ButtonType:
  custom = 0
  system = 1
  detailDisclosure = 2
  infoLight = 3
  infoDark = 4
  contactAdd = 5
  plain = 6
  close = 7


@dataclass
class UIControl_State:
  # ref: [UIControlState | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicontrolstate?language=objc)
  normal = 0
  highlighted = 1 << 0
  disabled = 1 << 1
  selected = 1 << 2
  focused = 1 << 3
  application = 0x00FF0000
  reserved = 0xFF000000


@dataclass
class UIControl_Event:
  # ref: [UIControlEvents | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uicontrolevents?language=objc)
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


@dataclass
class UIButton_Configuration_CornerStyle:
  # ref: [UIButtonConfigurationCornerStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibuttonconfigurationcornerstyle?language=objc)
  # todo: `Enumeration Case` に値表記が無いので独自に調査
  dynamic = 0
  fixed = -1
  capsule = 4
  large = 3
  medium = 2
  small = 1


@dataclass
class UIButton_Configuration_Size:
  # ref: [UIButtonConfigurationSize | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibuttonconfigurationsize?language=objc)
  # todo: `Enumeration Case` に値表記が無いので独自に調査
  medium = 0
  small = 1
  mini = 2
  large = 3


@dataclass
class NSUnderlineStyle:
  # ref: [NSUnderlineStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nsunderlinestyle?language=objc)
  none = 0x00  # ref: [NSUnderlineStyleNone | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nsunderlinestyle/nsunderlinestylenone?language=objc)
  single = 0x01
  thick = 0x02
  double = 0x09
  patternSolid = 0x0000  # xxx: ?
  patternDot = 0x0100
  patternDash = 0x0200
  patternDashDot = 0x0300
  patternDashDotDot = 0x0400
  byWord = 0x8000


@dataclass
class UIImage_SymbolScale:
  # ref: [UIImageSymbolScale | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimagesymbolscale?language=objc)
  default = -1
  unspecified = 0
  small = 1
  medium = 2
  large = 3


@dataclass
class NSDirectionalRectEdge:
  # ref: [NSDirectionalRectEdge | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nsdirectionalrectedge?language=objc)
  none = 0  # ref: [NSDirectionalRectEdgeNone | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nsdirectionalrectedge/nsdirectionalrectedgenone?language=objc)
  top = 1 << 0
  leading = 1 << 1
  bottom = 1 << 2
  trailing = 1 << 3
  all = top | leading | bottom | trailing


@dataclass
class UITableViewStyle:
  # ref: [UITableViewStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitableviewstyle?language=objc)
  plain = 0
  grouped = 1
  insetGrouped = 2


@dataclass
class UIListContentTextAlignment:
  # ref: [UIListContentTextAlignment | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uilistcontenttextalignment)
  # todo: `Enumeration Case` に値表記が無いので独自に調査
  natural = 0
  center = 1
  justified = 2

