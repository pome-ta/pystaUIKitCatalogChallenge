from pyrubicon.objc.api import ObjCClass, objc_method
from pyrubicon.objc.types import CGRectMake

from ._prototype import CustomTableViewCell
from rbedge import pdbr

UIImageView = ObjCClass('UIImageView')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')


def add_prototype(identifier: str):

  def _create_reuse_dict(cellClass: CustomTableViewCell):
    prototypes.append({
      'cellClass': cellClass,
      'identifier': identifier,
    })

  return _create_reuse_dict


prototypes: list[dict[CustomTableViewCell, str]] = []


@add_prototype('tintedSymbol')
class TintedSymbol(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    _width = 40.0
    _height = 40.0
    imageView = UIImageView.alloc().initWithFrame_(
      CGRectMake(167.5, 2.0, _width, _height)).autorelease()

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
  def overrideCell(self):
    _width = 40.0
    _height = 40.0
    imageView = UIImageView.alloc().initWithFrame_(
      CGRectMake(167.5, 2.0, _width, _height)).autorelease()

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
  def overrideCell(self):
    _width = 82.0
    _height = 87.0
    imageView = UIImageView.alloc().initWithFrame_(
      CGRectMake(146.5, 0.0, _width, _height)).autorelease()

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


@add_prototype('paletteColorsSymbol')
class PaletteColorsSymbol(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    _width = 40.0
    _height = 40.0
    imageView = UIImageView.alloc().initWithFrame_(
      CGRectMake(167.5, 2.0, _width, _height)).autorelease()

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
  def overrideCell(self):
    _width = 40.0
    _height = 40.0
    imageView = UIImageView.alloc().initWithFrame_(
      CGRectMake(167.5, 2.0, _width, _height)).autorelease()

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
  def overrideCell(self):
    _width = 40.0
    _height = 40.0
    imageView = UIImageView.alloc().initWithFrame_(
      CGRectMake(167.5, 2.0, _width, _height)).autorelease()

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

