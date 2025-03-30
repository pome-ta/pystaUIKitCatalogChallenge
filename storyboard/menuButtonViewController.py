from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super

from rbedge.enumerations import (
  UIButtonType,
  UIControlState,
)
from rbedge.functions import NSStringFromClass
from rbedge import pdbr

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


prototypes: list[dict[CustomTableViewCell | str, str]] = []


@add_prototype('buttonMenuProgrammatic')
class ButtonMenuProgrammatic(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')

    type = UIButtonType.system
    button = UIButton.buttonWithType_(type)

    title = 'Drop Down'
    state = UIControlState.normal
    button.setTitle_forState_(title, state)

    button.translatesAutoresizingMaskIntoConstraints = False

    self.contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      button.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('buttonMenuMultiAction')
class ButtonMenuMultiAction(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')

    type = UIButtonType.system
    button = UIButton.buttonWithType_(type)

    title = 'Drop Down'
    state = UIControlState.normal
    button.setTitle_forState_(title, state)

    button.translatesAutoresizingMaskIntoConstraints = False

    self.contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      button.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('buttonSubMenu')
class ButtonSubMenu(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')

    type = UIButtonType.system
    button = UIButton.buttonWithType_(type)

    title = 'Drop Down Submenu'
    state = UIControlState.normal
    button.setTitle_forState_(title, state)

    button.translatesAutoresizingMaskIntoConstraints = False

    self.contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      button.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('buttonMenuSelection')
class ButtonMenuSelection(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')

    type = UIButtonType.system
    button = UIButton.buttonWithType_(type)

    title = 'Drop Down'
    state = UIControlState.normal
    button.setTitle_forState_(title, state)

    button.translatesAutoresizingMaskIntoConstraints = False

    self.contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      button.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])

