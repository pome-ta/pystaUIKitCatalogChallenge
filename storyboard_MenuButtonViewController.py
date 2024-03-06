import ctypes

from objc_util import ObjCInstance, create_objc_class, class_getSuperclass, sel

from objcista import *


class CstmUITableViewCell:

  def __init__(self):
    self.tableViewCell_instance: None

  # todo: 変数名とか諸々考える
  def init_cell(self, cell: UITableViewCell):
    pass

  def _override_tableViewCell(self):

    def initWithStyle_reuseIdentifier_(_self, _cmd, _style, _reuseIdentifier):
      super_cls = class_getSuperclass(self.tableViewCell_instance)
      super_struct = objc_super(_self, super_cls)
      super_sel = sel('initWithStyle:reuseIdentifier:')

      _args = [
        ctypes.byref(super_struct),
        super_sel,
        _style,
        _reuseIdentifier,
      ]
      _this = objc_msgSendSuper(*_args)
      this = ObjCInstance(_this)
      self.init_cell(this)
      return _this

    _methods = [
      initWithStyle_reuseIdentifier_,
    ]
    create_kwargs = {
      'name': '_tvc',
      'superclass': UITableViewCell,
      'methods': _methods,
    }
    _tvc = create_objc_class(**create_kwargs)
    self.tableViewCell_instance = _tvc

  def _init_tableViewCell(self):
    self._override_tableViewCell()
    return self.tableViewCell_instance

  @classmethod
  def this(cls, *args, **kwargs) -> ObjCInstance:
    _cls = cls(*args, **kwargs)
    return _cls._init_tableViewCell()


# --- prototypes
class ButtonMenuProgrammatic(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    button = UIButton.buttonWithType_(type)
    state = UIControl_State.normal
    button.setTitle_forState_('Drop Down', state)
    button.setTranslatesAutoresizingMaskIntoConstraints_(False)
    contentView = cell.contentView()
    contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor().constraintEqualToAnchor_(
        contentView.centerXAnchor()),
      button.centerYAnchor().constraintEqualToAnchor_(
        contentView.centerYAnchor()),
    ])

  @classmethod
  def reuseIdentifier_name(cls) -> str:
    name = 'buttonMenuProgrammatic'
    cls.reuseIdentifier = name
    return name


class ButtonMenuMultiAction(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    button = UIButton.buttonWithType_(type)
    state = UIControl_State.normal
    button.setTitle_forState_('Drop Down', state)
    button.setTranslatesAutoresizingMaskIntoConstraints_(False)
    contentView = cell.contentView()
    contentView.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor().constraintEqualToAnchor_(
        contentView.centerXAnchor()),
      button.centerYAnchor().constraintEqualToAnchor_(
        contentView.centerYAnchor()),
    ])

  @classmethod
  def reuseIdentifier_name(cls) -> str:
    name = 'buttonMenuMultiAction'
    cls.reuseIdentifier = name
    return name




prototypes = [
  ButtonMenuProgrammatic,
  ButtonMenuMultiAction,
  
]


