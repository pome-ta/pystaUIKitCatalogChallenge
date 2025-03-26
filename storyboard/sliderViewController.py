from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

from ._prototype import CustomTableViewCell

UISlider = ObjCClass('UISlider')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')


def add_prototype(identifier: str):

  def _create_reuse_dict(cellClass: CustomTableViewCell):
    prototypes.append({
      'cellClass': cellClass,
      'identifier': identifier,
    })

  return _create_reuse_dict


prototypes: list[dict[CustomTableViewCell | str, str]] = []


@add_prototype('sliderDefault')
class SliderDefault(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')
    slider = UISlider.new()
    slider.value = 0.5
    slider.minimumValue = 0.0
    slider.maximumValue = 1.0
    slider.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(slider)

    NSLayoutConstraint.activateConstraints_([
      slider.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      slider.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
      slider.leadingAnchor.constraintEqualToAnchor_constant_(
        self.contentView.leadingAnchor, 20.0),
      slider.trailingAnchor.constraintEqualToAnchor_constant_(
        self.contentView.trailingAnchor, -20.0),
    ])


@add_prototype('sliderTinted')
class SliderTinted(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')
    slider = UISlider.new()
    slider.value = 0.5
    slider.minimumValue = 0.0
    slider.maximumValue = 1.0
    slider.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(slider)

    NSLayoutConstraint.activateConstraints_([
      slider.leadingAnchor.constraintEqualToAnchor_constant_(
        self.contentView.leadingAnchor, 20.0),
      slider.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      slider.trailingAnchor.constraintEqualToAnchor_constant_(
        self.contentView.trailingAnchor, -20.0),
      slider.centerYAnchor.constraintEqualToAnchor_constant_(
        self.contentView.centerYAnchor, -0.5),
    ])


@add_prototype('sliderCustom')
class SliderCustom(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')
    slider = UISlider.new()
    slider.value = 0.5
    slider.minimumValue = 0.0
    slider.maximumValue = 1.0
    slider.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(slider)

    NSLayoutConstraint.activateConstraints_([
      slider.leadingAnchor.constraintEqualToAnchor_constant_(
        self.contentView.leadingAnchor, 20.0),
      slider.trailingAnchor.constraintEqualToAnchor_constant_(
        self.contentView.trailingAnchor, -20.0),
      slider.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      slider.centerYAnchor.constraintEqualToAnchor_constant_(
        self.contentView.centerYAnchor, -0.5),
    ])


#sliderMaxMinImage
@add_prototype('sliderMaxMinImage')
class SliderMaxMinImage(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')
    slider = UISlider.new()
    slider.value = 0.5
    slider.minimumValue = 0.0
    slider.maximumValue = 1.0
    slider.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(slider)

    NSLayoutConstraint.activateConstraints_([
      slider.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      slider.leadingAnchor.constraintEqualToAnchor_constant_(
        self.contentView.leadingAnchor, 20.0),
      slider.centerYAnchor.constraintEqualToAnchor_constant_(
        self.contentView.centerYAnchor, -0.5),
      slider.trailingAnchor.constraintEqualToAnchor_constant_(
        self.contentView.trailingAnchor, -20.0),
    ])

