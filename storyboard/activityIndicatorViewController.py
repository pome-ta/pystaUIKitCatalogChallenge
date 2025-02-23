from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import objc_id, send_super
from pyrubicon.objc.types import CGRectMake, NSInteger

from rbedge.enumerations import (
  UIActivityIndicatorViewStyle, )

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

from ._prototype import CustomTableViewCell

UIActivityIndicatorView = ObjCClass('UIActivityIndicatorView')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')


def add_prototype(identifier: str):

  def _create_reuse_dict(cellClass: CustomTableViewCell):
    prototypes.append({
      'cellClass': cellClass,
      'identifier': identifier,
    })

  return _create_reuse_dict


prototypes: list[dict[CustomTableViewCell | str, str]] = []


@add_prototype('mediumIndicator')
class MediumIndicator(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')

    activityIndicatorView = UIActivityIndicatorView.alloc().initWithFrame_(
      CGRectMake(177.5, 12.0, 20.0, 20.0))
    _style = UIActivityIndicatorViewStyle.medium
    activityIndicatorView.setActivityIndicatorViewStyle_(_style)

    activityIndicatorView.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(activityIndicatorView)

    NSLayoutConstraint.activateConstraints_([
      activityIndicatorView.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      activityIndicatorView.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('largeTintedIndicator')
class LargeTintedIndicator(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')

    activityIndicatorView = UIActivityIndicatorView.alloc().initWithFrame_(
      CGRectMake(168.0, -41.0, 39.0, 126.0))

    _style = UIActivityIndicatorViewStyle.large
    activityIndicatorView.setActivityIndicatorViewStyle_(_style)

    activityIndicatorView.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(activityIndicatorView)

    NSLayoutConstraint.activateConstraints_([
      activityIndicatorView.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      activityIndicatorView.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('mediumTintedIndicator')
class MediumTintedIndicator(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')

    activityIndicatorView = UIActivityIndicatorView.alloc().initWithFrame_(
      CGRectMake(177.5, 12.0, 20.0, 20.0))

    _style = UIActivityIndicatorViewStyle.medium
    activityIndicatorView.setActivityIndicatorViewStyle_(_style)

    activityIndicatorView.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(activityIndicatorView)

    NSLayoutConstraint.activateConstraints_([
      activityIndicatorView.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      activityIndicatorView.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('largeIndicator')
class LargeIndicator(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')

    activityIndicatorView = UIActivityIndicatorView.alloc().initWithFrame_(
      CGRectMake(168.0, -41.0, 39.0, 126.0))

    _style = UIActivityIndicatorViewStyle.large
    activityIndicatorView.setActivityIndicatorViewStyle_(_style)

    activityIndicatorView.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(activityIndicatorView)

    NSLayoutConstraint.activateConstraints_([
      activityIndicatorView.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      activityIndicatorView.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])
