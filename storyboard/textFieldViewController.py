from pyrubicon.objc.api import ObjCClass, objc_method
from pyrubicon.objc.types import CGRectMake

from ._prototype import CustomTableViewCell
from rbedge import pdbr

UITextField = ObjCClass('UITextField')
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
    textField = UITextField.alloc().initWithFrame_(CGRectMake(
      16.0, 5.0, 343.0, 34.0)).autorelease()
    
    textField.translatesAutoresizingMaskIntoConstraints = False
    self.contentView.addSubview_(textField)

    NSLayoutConstraint.activateConstraints_([
      textField.leadingAnchor.constraintEqualToAnchor_constant_(
        self.contentView.leadingAnchor, 16.0),
      textField.trailingAnchor.constraintEqualToAnchor_constant_(
        self.contentView.trailingAnchor, -16.0),
      #textField.centerXAnchor.constraintEqualToAnchor_constant_(self.contentView.centerXAnchor, -0.5),
      textField.centerYAnchor.constraintEqualToAnchor_(
        self.contentView.centerYAnchor),
    ])



