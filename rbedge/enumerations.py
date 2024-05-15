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

