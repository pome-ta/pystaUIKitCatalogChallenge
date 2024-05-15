import ctypes

from pyrubicon.objc.api import ObjCClass, ObjCInstance, objc_method
from pyrubicon.objc.runtime import send_super
from pyrubicon.objc.types import NSInteger

from rbedge.enumerations import UIButtonType

from rbedge import pdbr

#ObjCClass.auto_rename = True # xxx: ここ含めて全部呼び出し？

UITableViewCell = ObjCClass('UITableViewCell')

UIButton = ObjCClass('UIButton')
UIButtonConfiguration = ObjCClass('UIButtonConfiguration')

NSLayoutConstraint = ObjCClass('NSLayoutConstraint')


class CustomTableViewCell(UITableViewCell):

  @objc_method
  def initWithStyle_reuseIdentifier_(self, style: NSInteger, reuseIdentifier):

    self_ptr = send_super(__class__,
                          self,
                          'initWithStyle:reuseIdentifier:',
                          style,
                          reuseIdentifier,
                          argtypes=[
                            NSInteger,
                            ctypes.c_void_p,
                          ])

    # todo: `self` に再定義しない
    #self = ObjCInstance(self_ptr)
    self.initCell()
    return ObjCInstance(self_ptr)

  @objc_method
  def initCell(self):
    pass


class ButtonSystemAddContact(CustomTableViewCell):

  @objc_method
  def initCell(self):
    type = UIButtonType.contactAdd
    button = UIButton.buttonWithType_(type)
    button.translatesAutoresizingMaskIntoConstraints = False

    contentView = self.contentView
    contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor.constraintEqualToAnchor_(contentView.centerXAnchor),
      button.centerYAnchor.constraintEqualToAnchor_(contentView.centerYAnchor),
    ])


class ButtonDetailDisclosure(CustomTableViewCell):

  @objc_method
  def initCell(self):
    type = UIButtonType.detailDisclosure
    button = UIButton.buttonWithType_(type)
    button.translatesAutoresizingMaskIntoConstraints = False

    contentView = self.contentView
    contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor.constraintEqualToAnchor_(contentView.centerXAnchor),
      button.centerYAnchor.constraintEqualToAnchor_(contentView.centerYAnchor),
    ])


class ButtonStyleGray(CustomTableViewCell):

  @objc_method
  def initCell(self):
    type = UIButtonType.system
    button = UIButton.buttonWithType_(type)
    config = UIButtonConfiguration.plainButtonConfiguration()
    config.title = 'Button'
    button.configuration = config

    button.translatesAutoresizingMaskIntoConstraints = False

    contentView = self.contentView
    contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor.constraintEqualToAnchor_(contentView.centerXAnchor),
      button.centerYAnchor.constraintEqualToAnchor_(contentView.centerYAnchor),
    ])


def create_reuse_dict(cellClass: UITableViewCell, identifier: str) -> dict:
  return {
    'cellClass': cellClass,
    'identifier': identifier,
  }


prototypes = [
  create_reuse_dict(ButtonSystemAddContact, 'buttonSystemAddContact'),
  create_reuse_dict(ButtonDetailDisclosure, 'buttonDetailDisclosure'),
  create_reuse_dict(ButtonStyleGray, 'buttonStyleGray')
]

