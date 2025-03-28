from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super
from pyrubicon.objc.types import CGRectMake

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

from ._prototype import CustomTableViewCell

UISwitch = ObjCClass('UISwitch')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')


def add_prototype(identifier: str):

  def _create_reuse_dict(cellClass: CustomTableViewCell):
    prototypes.append({
      'cellClass': cellClass,
      'identifier': identifier,
    })

  return _create_reuse_dict


prototypes: list[dict[CustomTableViewCell | str, str]] = []


@add_prototype('defaultSwitch')
class DefaultSwitch(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    switch = UISwitch.alloc().initWithFrame_(CGRectMake(
      163.5, 6.5, 51.0, 31.0))  #.autorelease()

    switch.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(switch)

    NSLayoutConstraint.activateConstraints_([
      switch.centerXAnchor.constraintEqualToAnchor_constant_(
        self.contentView.centerXAnchor, -0.5),
      switch.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('checkBoxSwitch')
class CheckBoxSwitch(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    switch = UISwitch.alloc().initWithFrame_(CGRectMake(
      163.5, 6.5, 51.0, 31.0))  #.autorelease()

    switch.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(switch)

    NSLayoutConstraint.activateConstraints_([
      switch.centerXAnchor.constraintEqualToAnchor_constant_(
        self.contentView.centerXAnchor, -0.5),
      switch.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('tintedSwitch')
class TintedSwitch(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    switch = UISwitch.alloc().initWithFrame_(CGRectMake(
      163.5, 6.5, 51.0, 31.0))  #.autorelease()

    switch.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(switch)

    NSLayoutConstraint.activateConstraints_([
      switch.centerXAnchor.constraintEqualToAnchor_constant_(
        self.contentView.centerXAnchor, -0.5),
      switch.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])

