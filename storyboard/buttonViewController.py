import ctypes

from pyrubicon.objc.api import ObjCClass, ObjCInstance, objc_method
from pyrubicon.objc.runtime import send_super
from pyrubicon.objc.types import NSInteger

from rbedge.enumerations import UIButtonType, UIControlState

from rbedge import pdbr

#ObjCClass.auto_rename = True # xxx: ここ含めて全部呼び出し？

UITableViewCell = ObjCClass('UITableViewCell')

UIButton = ObjCClass('UIButton')
UIButtonConfiguration = ObjCClass('UIButtonConfiguration')

NSLayoutConstraint = ObjCClass('NSLayoutConstraint')


def create_reuse_dict(cellClass: UITableViewCell, identifier: str) -> dict:
  return {
    'cellClass': cellClass,
    'identifier': identifier,
  }


class CustomTableViewCell(UITableViewCell):

  @objc_method
  def initWithStyle_reuseIdentifier_(self, style: NSInteger, reuseIdentifier):

    super_args = []

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
    self.overrideCell()
    return ObjCInstance(self_ptr)

  @objc_method
  def overrideCell(self):
    pass


class ButtonSystemAddContact(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
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
  def overrideCell(self):
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
  def overrideCell(self):
    type = UIButtonType.system
    button = UIButton.buttonWithType_(type)
    config = UIButtonConfiguration.plainButtonConfiguration()

    title = 'Button'
    config.setTitle_(title)
    button.configuration = config

    button.translatesAutoresizingMaskIntoConstraints = False

    contentView = self.contentView
    contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor.constraintEqualToAnchor_(contentView.centerXAnchor),
      button.centerYAnchor.constraintEqualToAnchor_(contentView.centerYAnchor),
    ])


class ButtonUpdateActivityHandler(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    type = UIButtonType.system
    button = UIButton.buttonWithType_(type)

    title = 'Button'
    state = UIControlState.normal
    button.setTitle_forState_(title, state)

    button.translatesAutoresizingMaskIntoConstraints = False

    contentView = self.contentView
    contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor.constraintEqualToAnchor_(contentView.centerXAnchor),
      button.centerYAnchor.constraintEqualToAnchor_(contentView.centerYAnchor),
    ])


prototypes = [
  create_reuse_dict(
    ButtonSystemAddContact,
    'buttonSystemAddContact',
  ),
  create_reuse_dict(
    ButtonDetailDisclosure,
    'buttonDetailDisclosure',
  ),
  create_reuse_dict(
    ButtonStyleGray,
    'buttonStyleGray',
  ),
  create_reuse_dict(
    ButtonUpdateActivityHandler,
    'buttonUpdateActivityHandler',
  ),
]

