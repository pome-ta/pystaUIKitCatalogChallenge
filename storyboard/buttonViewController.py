import ctypes

from pyrubicon.objc.api import ObjCClass, ObjCInstance, objc_method
from pyrubicon.objc.runtime import send_super
from pyrubicon.objc.types import NSInteger

from rbedge.enumerations import UIButtonType, UIControlState

#ObjCClass.auto_rename = True # xxx: ここ含めて全部呼び出し？

UITableViewCell = ObjCClass('UITableViewCell')
UIButton = ObjCClass('UIButton')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

prototypes: list[dict[UITableViewCell, str]] = []


def add_prototype(identifier: str):

  def _create_reuse_dict(cellClass: UITableViewCell):
    prototypes.append({
      'cellClass': cellClass,
      'identifier': identifier,
    })

  return _create_reuse_dict


class CustomTableViewCell(UITableViewCell):

  @objc_method
  def initWithStyle_reuseIdentifier_(self, style: NSInteger, reuseIdentifier):

    super_args = [
      style,
      reuseIdentifier,
    ]
    super_argtypes = [
      NSInteger,
      ctypes.c_void_p,
    ]

    self_ptr = send_super(__class__,
                          self,
                          'initWithStyle:reuseIdentifier:',
                          *super_args,
                          argtypes=super_argtypes)
    # todo: `self` に再定義しない
    #self = ObjCInstance(self_ptr)
    self.overrideCell()
    return ObjCInstance(self_ptr)

  @objc_method
  def overrideCell(self):
    pass


@add_prototype('buttonSystemAddContact')
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


@add_prototype('buttonDetailDisclosure')
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


@add_prototype('buttonStyleGray')
class ButtonStyleGray(CustomTableViewCell):

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


@add_prototype('buttonUpdateActivityHandler')
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


@add_prototype('buttonAttrText')
class ButtonAttrText(CustomTableViewCell):

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


@add_prototype('buttonSymbol')
class ButtonSymbol(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    type = UIButtonType.system
    button = UIButton.buttonWithType_(type)

    button.translatesAutoresizingMaskIntoConstraints = False

    contentView = self.contentView
    contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor.constraintEqualToAnchor_(contentView.centerXAnchor),
      button.centerYAnchor.constraintEqualToAnchor_(contentView.centerYAnchor),
    ])


@add_prototype('addToCartButton')
class AddToCartButton(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    type = UIButtonType.system
    button = UIButton.buttonWithType_(type)
    button.translatesAutoresizingMaskIntoConstraints = False

    contentView = self.contentView
    contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor.constraintEqualToAnchor_(contentView.centerXAnchor),
      button.centerYAnchor.constraintEqualToAnchor_(contentView.centerYAnchor),
    ])


@add_prototype('buttonMultiTitle')
class ButtonMultiTitle(CustomTableViewCell):

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


@add_prototype('buttonSystem')
class ButtonSymbol(CustomTableViewCell):

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


@add_prototype('buttonTitleColor')
class ButtonTitleColor(CustomTableViewCell):

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


@add_prototype('buttonUpdateHandler')
class ButtonUpdateHandler(CustomTableViewCell):

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


@add_prototype('buttonToggle')
class ButtonToggle(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    type = UIButtonType.system
    button = UIButton.buttonWithType_(type)

    title = 'Toggle'
    state = UIControlState.normal
    button.setTitle_forState_(title, state)

    button.translatesAutoresizingMaskIntoConstraints = False

    contentView = self.contentView
    contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor.constraintEqualToAnchor_(contentView.centerXAnchor),
      button.centerYAnchor.constraintEqualToAnchor_(contentView.centerYAnchor),
    ])


@add_prototype('buttonImageUpdateHandler')
class ButtonImageUpdateHandler(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    type = UIButtonType.system
    button = UIButton.buttonWithType_(type)

    title = 'Toggle'
    state = UIControlState.normal
    button.setTitle_forState_(title, state)

    button.translatesAutoresizingMaskIntoConstraints = False

    contentView = self.contentView
    contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor.constraintEqualToAnchor_(contentView.centerXAnchor),
      button.centerYAnchor.constraintEqualToAnchor_(contentView.centerYAnchor),
    ])


@add_prototype('buttonTextSymbol')
class ButtonTextSymbol(CustomTableViewCell):

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


@add_prototype('buttonSymbolText')
class ButtonSymbolText(CustomTableViewCell):

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


@add_prototype('buttonBackground')
class ButtonBackground(CustomTableViewCell):

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


@add_prototype('buttonClose')
class ButtonClose(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    type = UIButtonType.close
    button = UIButton.buttonWithType_(type)
    button.translatesAutoresizingMaskIntoConstraints = False

    contentView = self.contentView
    contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor.constraintEqualToAnchor_(contentView.centerXAnchor),
      button.centerYAnchor.constraintEqualToAnchor_(contentView.centerYAnchor),
    ])


@add_prototype('buttonLargeSymbol')
class ButtonLargeSymbol(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    type = UIButtonType.system
    button = UIButton.buttonWithType_(type)
    button.translatesAutoresizingMaskIntoConstraints = False

    contentView = self.contentView
    contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor.constraintEqualToAnchor_(contentView.centerXAnchor),
      button.centerYAnchor.constraintEqualToAnchor_(contentView.centerYAnchor),
    ])


@add_prototype('buttonStyleTinted')
class ButtonStyleTinted(CustomTableViewCell):

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


@add_prototype('buttonStyleFilled')
class ButtonStyleFilled(CustomTableViewCell):

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


@add_prototype('buttonImage')
class ButtonImage(CustomTableViewCell):

  @objc_method
  def overrideCell(self):
    button = UIButton.new()
    button.translatesAutoresizingMaskIntoConstraints = False

    contentView = self.contentView
    contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor.constraintEqualToAnchor_(contentView.centerXAnchor),
      button.centerYAnchor.constraintEqualToAnchor_(contentView.centerYAnchor),
    ])


@add_prototype('buttonCornerStyle')
class ButtonCornerStyle(CustomTableViewCell):

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

