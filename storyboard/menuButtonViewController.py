from pyrubicon.objc.api import ObjCClass, objc_method

from rbedge.enumerations import UIButtonType, UIControlState
from ._prototype import CustomTableViewCell

UIButton = ObjCClass('UIButton')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')


def add_prototype(identifier: str):

  def _create_reuse_dict(cellClass: CustomTableViewCell):
    prototypes.append({
      'cellClass': cellClass,
      'identifier': identifier,
    })

  return _create_reuse_dict


prototypes: list[dict[CustomTableViewCell, str]] = []


@add_prototype('buttonMenuProgrammatic')
class ButtonMenuProgrammatic(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    type = UIButtonType.system
    button = UIButton.buttonWithType_(type)

    title = 'Drop Down'
    state = UIControlState.normal
    button.setTitle_forState_(title, state)

    button.translatesAutoresizingMaskIntoConstraints = False

    contentView = self.contentView
    contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor.constraintEqualToAnchor_(contentView.centerXAnchor),
      button.centerYAnchor.constraintEqualToAnchor_(contentView.centerYAnchor),
    ])


@add_prototype('buttonMenuMultiAction')
class ButtonMenuMultiAction(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    type = UIButtonType.system
    button = UIButton.buttonWithType_(type)

    title = 'Drop Down'
    state = UIControlState.normal
    button.setTitle_forState_(title, state)

    button.translatesAutoresizingMaskIntoConstraints = False

    contentView = self.contentView
    contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor.constraintEqualToAnchor_(contentView.centerXAnchor),
      button.centerYAnchor.constraintEqualToAnchor_(contentView.centerYAnchor),
    ])


@add_prototype('buttonSubMenu')
class ButtonSubMenu(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    type = UIButtonType.system
    button = UIButton.buttonWithType_(type)

    title = 'Drop Down Submenu'
    state = UIControlState.normal
    button.setTitle_forState_(title, state)

    button.translatesAutoresizingMaskIntoConstraints = False

    contentView = self.contentView
    contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor.constraintEqualToAnchor_(contentView.centerXAnchor),
      button.centerYAnchor.constraintEqualToAnchor_(contentView.centerYAnchor),
    ])


@add_prototype('buttonMenuSelection')
class ButtonMenuSelection(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    type = UIButtonType.system
    button = UIButton.buttonWithType_(type)

    title = 'Drop Down'
    state = UIControlState.normal
    button.setTitle_forState_(title, state)

    button.translatesAutoresizingMaskIntoConstraints = False

    contentView = self.contentView
    contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor.constraintEqualToAnchor_(contentView.centerXAnchor),
      button.centerYAnchor.constraintEqualToAnchor_(contentView.centerYAnchor),
    ])

