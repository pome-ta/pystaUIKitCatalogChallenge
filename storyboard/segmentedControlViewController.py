from pyrubicon.objc.api import ObjCClass, objc_method
from pyrubicon.objc.types import CGRectMake

from ._prototype import CustomTableViewCell
from rbedge import pdbr

UISegmentedControl = ObjCClass('UISegmentedControl')
UIView = ObjCClass('UIView')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')


def add_prototype(identifier: str):

  def _create_reuse_dict(cellClass: CustomTableViewCell):
    prototypes.append({
      'cellClass': cellClass,
      'identifier': identifier,
    })

  return _create_reuse_dict


prototypes: list[dict[CustomTableViewCell, str]] = []

segments = [
  'Check',
  'Search',
  'Tools',
]


@add_prototype('segmentDefault')
class SegmentDefault(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    segmentedControl = UISegmentedControl.alloc().initWithItems_(
      segments)#.autorelease()
    # xxx: ベタ打ち
    segmentedControl.frame = CGRectMake(47.5, 6.5, 280.0, 32.0)
    segmentedControl.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(segmentedControl)

    NSLayoutConstraint.activateConstraints_([
      segmentedControl.widthAnchor.constraintGreaterThanOrEqualToConstant_(
        280.0),
      segmentedControl.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      segmentedControl.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('segmentTinted')
class SegmentTinted(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    segmentedControl = UISegmentedControl.alloc().initWithItems_(
      segments)#.autorelease()
    # xxx: ベタ打ち
    segmentedControl.frame = CGRectMake(47.5, 6.5, 280.0, 32.0)
    segmentedControl.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(segmentedControl)

    NSLayoutConstraint.activateConstraints_([
      segmentedControl.widthAnchor.constraintGreaterThanOrEqualToConstant_(
        280.0),
      segmentedControl.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      segmentedControl.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('segmentCustom')
class SegmentCustom(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    segmentedControl = UISegmentedControl.alloc().initWithItems_(
      segments)#.autorelease()
    # xxx: ベタ打ち
    segmentedControl.frame = CGRectMake(47.5, 6.5, 280.0, 32.0)
    segmentedControl.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(segmentedControl)

    NSLayoutConstraint.activateConstraints_([
      segmentedControl.widthAnchor.constraintGreaterThanOrEqualToConstant_(
        280.0),
      segmentedControl.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      segmentedControl.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('segmentCustomBackground')
class SegmentCustomBackground(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    #view = UIView.alloc().init().autorelease()
    view = UIView.new()
    # xxx: ベタ打ち
    view.frame = CGRectMake(47.5, 6.0, 280.0, 32.0)
    view.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(view)

    NSLayoutConstraint.activateConstraints_([
      view.widthAnchor.constraintEqualToConstant_(280.0),
      view.heightAnchor.constraintEqualToConstant_(32.0),
      view.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      view.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('segmentAction')
class SegmentAction(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    segmentedControl = UISegmentedControl.alloc().initWithItems_(
      segments)#.autorelease()
    # xxx: ベタ打ち
    segmentedControl.frame = CGRectMake(47.5, 6.5, 280.0, 32.0)
    segmentedControl.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(segmentedControl)

    NSLayoutConstraint.activateConstraints_([
      segmentedControl.widthAnchor.constraintGreaterThanOrEqualToConstant_(
        280.0),
      segmentedControl.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      segmentedControl.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])

