from pyrubicon.objc.api import ObjCClass, objc_method
from pyrubicon.objc.types import CGRectMake
from rbedge.enumerations import UITextBorderStyle

from ._prototype import CustomTableViewCell
from rbedge import pdbr

UISearchTextField = ObjCClass('UISearchTextField')
UITextField = ObjCClass('UITextField')
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


@add_prototype('searchTextField')
class SearchTextField(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    #textField = UITextField.alloc().initWithFrame_(CGRectMake(16.0, 5.0, 343.0, 34.0)).autorelease()
    textField = UISearchTextField.alloc().initWithFrame_(
      CGRectMake(16.0, 5.0, 343.0, 34.0)).autorelease()

    textField.minimumFontSize = 17.0
    textField.borderStyle = UITextBorderStyle.roundedRect

    textField.font = UIFont.systemFontOfSize_(14.0)

    #textField.backgroundColor = ObjCClass('UIColor').systemRedColor()

    textField.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(textField)

    NSLayoutConstraint.activateConstraints_([
      textField.leadingAnchor.constraintEqualToAnchor_constant_(
        self.contentView.leadingAnchor, 16.0),
      textField.trailingAnchor.constraintEqualToAnchor_constant_(
        self.contentView.trailingAnchor, -16.0),
      textField.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('tintedTextField')
class TintedTextField(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    textField = UITextField.alloc().initWithFrame_(
      CGRectMake(77.5, 5.0, 220.0, 34.0)).autorelease()

    textField.minimumFontSize = 17.0
    textField.font = UIFont.systemFontOfSize_(14.0)
    textField.borderStyle = UITextBorderStyle.roundedRect

    #textField.backgroundColor = ObjCClass('UIColor').systemRedColor()

    textField.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(textField)

    NSLayoutConstraint.activateConstraints_([
      textField.widthAnchor.constraintEqualToConstant_(220.0),
      textField.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      textField.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('customTextField')
class CustomTextField(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    # todo: 遅延import
    from textFieldViewController import CustomTextField as _CustomTextField
    '''
    textField = _CustomTextField.alloc().initWithFrame_(
      CGRectMake(77.5, 7.0, 220.0, 30.0)).autorelease()
    '''
    # xxx: `.alloc().initWithFrame_` だと、`init` が呼べない
    #      `objc_property` の定義位置を考慮すると
    #      `new` or `alloc().init()` とするしかない状況
    textField = _CustomTextField.new()
    textField.frame = CGRectMake(77.5, 7.0, 220.0, 30.0)

    textField.minimumFontSize = 17.0
    textField.font = UIFont.systemFontOfSize_(14.0)
    textField.borderStyle = UITextBorderStyle.roundedRect

    #textField.backgroundColor = ObjCClass('UIColor').systemBlueColor()

    textField.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(textField)

    NSLayoutConstraint.activateConstraints_([
      textField.heightAnchor.constraintEqualToConstant_(30.0),
      textField.widthAnchor.constraintEqualToConstant_(220.0),
      textField.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      textField.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('textField')
class TextField(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    textField = UITextField.alloc().initWithFrame_(
      CGRectMake(77.5, 5.0, 220.0, 34.0)).autorelease()

    textField.minimumFontSize = 17.0
    textField.font = UIFont.systemFontOfSize_(14.0)
    textField.borderStyle = UITextBorderStyle.roundedRect

    #textField.backgroundColor = ObjCClass('UIColor').systemRedColor()

    textField.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(textField)

    NSLayoutConstraint.activateConstraints_([
      textField.widthAnchor.constraintEqualToConstant_(220.0),
      textField.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      textField.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('secureTextField')
class SecureTextField(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    textField = UITextField.alloc().initWithFrame_(
      CGRectMake(77.5, 5.0, 220.0, 34.0)).autorelease()

    textField.minimumFontSize = 17.0
    textField.font = UIFont.systemFontOfSize_(14.0)
    textField.borderStyle = UITextBorderStyle.roundedRect

    #textField.backgroundColor = ObjCClass('UIColor').systemRedColor()

    textField.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(textField)

    NSLayoutConstraint.activateConstraints_([
      textField.widthAnchor.constraintEqualToConstant_(220.0),
      textField.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      textField.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])


@add_prototype('specificKeyboardTextField')
class SpecificKeyboardTextField(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    textField = UITextField.alloc().initWithFrame_(
      CGRectMake(77.5, 5.0, 220.0, 34.0)).autorelease()

    textField.minimumFontSize = 17.0
    textField.font = UIFont.systemFontOfSize_(14.0)
    textField.borderStyle = UITextBorderStyle.roundedRect

    #textField.backgroundColor = ObjCClass('UIColor').systemRedColor()

    textField.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(textField)

    NSLayoutConstraint.activateConstraints_([
      textField.widthAnchor.constraintEqualToConstant_(220.0),
      textField.centerXAnchor.constraintEqualToAnchor_(
        self.contentView.centerXAnchor),
      textField.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])

