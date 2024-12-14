from pyrubicon.objc.api import ObjCClass, objc_method
from pyrubicon.objc.types import CGRectMake

from rbedge.enumerations import (
  UIActivityIndicatorViewStyle, )

from ._prototype import CustomTableViewCell
from rbedge import pdbr

UISearchTextField = ObjCClass('UISearchTextField')
UITextField = ObjCClass('UITextField')

UIActivityIndicatorView = ObjCClass('UIActivityIndicatorView')
UIFont = ObjCClass('UIFont')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')


def add_prototype(identifier: str):

  def _create_reuse_dict(cellClass: CustomTableViewCell):
    prototypes.append({
      'cellClass': cellClass,
      'identifier': identifier,
    })

  return _create_reuse_dict


prototypes: list[dict[CustomTableViewCell, str]] = []


@add_prototype('mediumIndicator')
class MediumIndicator(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    activityIndicatorView = UIActivityIndicatorView.alloc().initWithFrame_(
      CGRectMake(177.5, 12.0, 20.0, 20.0)).autorelease()
    _style = UIActivityIndicatorViewStyle.medium
    activityIndicatorView.setActivityIndicatorViewStyle_(_style)
    #activityIndicatorView = UIActivityIndicatorView.alloc().initWithActivityIndicatorStyle_(_style)

    activityIndicatorView.startAnimating()
    #activityIndicatorView.startAnimation()

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
  def overrideCell(self):
    activityIndicatorView = UIActivityIndicatorView.alloc().initWithFrame_(
      CGRectMake(168.0, -41.0, 39.0, 126.0)).autorelease()
    _style = UIActivityIndicatorViewStyle.large
    activityIndicatorView.setActivityIndicatorViewStyle_(_style)
    #activityIndicatorView = UIActivityIndicatorView.alloc().initWithActivityIndicatorStyle_(_style)

    activityIndicatorView.startAnimating()
    #activityIndicatorView.startAnimation()

    activityIndicatorView.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(activityIndicatorView)

    NSLayoutConstraint.activateConstraints_([
      activityIndicatorView.widthAnchor.constraintEqualToConstant_(39.0),
      activityIndicatorView.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      activityIndicatorView.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
      #activityIndicatorView.topAnchor.constraintEqualToConstant_(-52.0),
    ])

