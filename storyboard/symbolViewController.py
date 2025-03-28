from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super
from pyrubicon.objc.types import CGRectMake, NSMakeSize

from rbedge.enumerations import UIViewContentMode
from rbedge.functions import NSStringFromClass
from rbedge import pdbr

from ._prototype import CustomTableViewCell

UIImageView = ObjCClass('UIImageView')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')


def add_prototype(identifier: str):

  def _create_reuse_dict(cellClass: CustomTableViewCell):
    prototypes.append({
      'cellClass': cellClass,
      'identifier': identifier,
    })

  return _create_reuse_dict


prototypes: list[dict[CustomTableViewCell | str, str]] = []


@add_prototype('tintedSymbol')
class TintedSymbol(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')
    _width = 40.0
    _height = 40.0
    imageView = UIImageView.alloc().initWithFrame_(
      CGRectMake(167.5, 2.0, _width, _height))
    imageView.contentMode = UIViewContentMode.scaleAspectFit

    imageView.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(imageView)

    NSLayoutConstraint.activateConstraints_([
      imageView.widthAnchor.constraintEqualToConstant_(_width),
      imageView.heightAnchor.constraintEqualToConstant_(_height),
      imageView.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      imageView.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('preferringMultiColorSymbol')
class PreferringMultiColorSymbol(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')
    _width = 40.0
    _height = 40.0
    imageView = UIImageView.alloc().initWithFrame_(
      CGRectMake(167.5, 2.0, _width, _height))
    imageView.contentMode = UIViewContentMode.scaleAspectFit

    imageView.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(imageView)

    NSLayoutConstraint.activateConstraints_([
      imageView.widthAnchor.constraintEqualToConstant_(_width),
      imageView.heightAnchor.constraintEqualToConstant_(_height),
      imageView.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      imageView.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('largeSizeSymbol')
class LargeSizeSymbol(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')
    _width = 82.0
    _height = 87.0
    imageView = UIImageView.alloc().initWithFrame_(
      CGRectMake(146.5, 0.0, _width, _height))
    imageView.contentMode = UIViewContentMode.scaleAspectFit

    imageView.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(imageView)

    # 高さを指定: デフォルトが44.0 のため、この要素のみ反映
    _size = NSMakeSize(self.contentView.size.width, _height)
    self.contentView.setSize_(_size)

    NSLayoutConstraint.activateConstraints_([
      imageView.widthAnchor.constraintEqualToConstant_(_width),
      imageView.heightAnchor.constraintEqualToConstant_(_height),
      imageView.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      imageView.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('paletteColorsSymbol')
class PaletteColorsSymbol(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')
    _width = 40.0
    _height = 40.0
    imageView = UIImageView.alloc().initWithFrame_(
      CGRectMake(167.5, 2.0, _width, _height))
    imageView.contentMode = UIViewContentMode.scaleAspectFit

    imageView.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(imageView)

    NSLayoutConstraint.activateConstraints_([
      imageView.widthAnchor.constraintEqualToConstant_(_width),
      imageView.heightAnchor.constraintEqualToConstant_(_height),
      imageView.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      imageView.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('plainSymbol')
class PlainSymbol(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')
    _width = 40.0
    _height = 40.0
    imageView = UIImageView.alloc().initWithFrame_(
      CGRectMake(167.5, 2.0, _width, _height))
    imageView.contentMode = UIViewContentMode.scaleAspectFit

    imageView.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(imageView)

    NSLayoutConstraint.activateConstraints_([
      imageView.widthAnchor.constraintEqualToConstant_(_width),
      imageView.heightAnchor.constraintEqualToConstant_(_height),
      imageView.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      imageView.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('hierarchicalColorSymbol')
class HierarchicalColorSymbol(CustomTableViewCell):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def overrideCell(self) -> None:
    send_super(__class__, self, 'overrideCell')
    _width = 40.0
    _height = 40.0
    imageView = UIImageView.alloc().initWithFrame_(
      CGRectMake(167.5, 2.0, _width, _height))
    imageView.contentMode = UIViewContentMode.scaleAspectFit

    imageView.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(imageView)

    NSLayoutConstraint.activateConstraints_([
      imageView.widthAnchor.constraintEqualToConstant_(_width),
      imageView.heightAnchor.constraintEqualToConstant_(_height),
      imageView.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      imageView.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])

