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