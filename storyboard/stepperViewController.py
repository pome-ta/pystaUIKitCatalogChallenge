from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super

from rbedge.enumerations import UITextBorderStyle

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

from ._prototype import CustomTableViewCell

UIStepper = ObjCClass('UIStepper')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')


def add_prototype(identifier: str):

  def _create_reuse_dict(cellClass: CustomTableViewCell):
    prototypes.append({
      'cellClass': cellClass,
      'identifier': identifier,
    })

  return _create_reuse_dict


prototypes: list[dict[CustomTableViewCell | str, str]] = []


@add_prototype('defaultStepper')
class DefaultStepper(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')
    stepper = UIStepper.new()
    stepper.maximumValue = 10

    stepper.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(stepper)

    NSLayoutConstraint.activateConstraints_([
      stepper.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      stepper.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('tintedStepper')
class TintedStepper(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')
    stepper = UIStepper.new()
    stepper.maximumValue = 10

    stepper.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(stepper)

    NSLayoutConstraint.activateConstraints_([
      stepper.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      stepper.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('customStepper')
class CustomStepper(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')
    stepper = UIStepper.new()
    stepper.maximumValue = 10

    stepper.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(stepper)

    NSLayoutConstraint.activateConstraints_([
      stepper.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      stepper.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])

