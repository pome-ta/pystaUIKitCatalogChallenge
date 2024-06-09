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


