from pyrubicon.objc.api import ObjCClass, objc_method
from pyrubicon.objc.types import CGRectMake
from rbedge.enumerations import UITextBorderStyle

from ._prototype import CustomTableViewCell
from rbedge import pdbr

UIStepper = ObjCClass('UIStepper')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')


def add_prototype(identifier: str):

  def _create_reuse_dict(cellClass: CustomTableViewCell):
    prototypes.append({
      'cellClass': cellClass,
      'identifier': identifier,
    })

  return _create_reuse_dict


prototypes: list[dict[CustomTableViewCell, str]] = []


@add_prototype('defaultStepper')
class DefaultStepper(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
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
  def overrideCell(self):
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
  def overrideCell(self):
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

