import ctypes

from objc_util import ObjCInstance, create_objc_class, class_getSuperclass, sel, c

from objcista import *

# todo: 後ほど関数化
objc_msgSendSuper = c.objc_msgSendSuper
objc_msgSendSuper.argtypes = [
  ctypes.c_void_p,  # super
  ctypes.c_void_p,  # selector
  ctypes.c_void_p,
  ctypes.c_void_p,
]
objc_msgSendSuper.restype = ctypes.c_void_p


class objc_super(ctypes.Structure):
  #ref: [id | Apple Developer Documentation](https://developer.apple.com/documentation/objectivec/id?language=objc)
  # ref: [Class | Apple Developer Documentation](https://developer.apple.com/documentation/objectivec/class?language=objc)
  _fields_ = [
    ('receiver', ctypes.c_void_p),  # encoding(b"@")
    ('super_class', ctypes.c_void_p),  # encoding(b"#")
  ]


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
class ButtonSystemAddContact(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.contactAdd
    button = UIButton.buttonWithType_(type)
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
    name = 'buttonSystemAddContact'
    cls.reuseIdentifier = name
    return name


class ButtonDetailDisclosure(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.detailDisclosure
    button = UIButton.buttonWithType_(type)
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
    name = 'buttonDetailDisclosure'
    cls.reuseIdentifier = name
    return name


class ButtonStyleGray(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    button = UIButton.buttonWithType_(type)
    config = UIButtonConfiguration.plainButtonConfiguration()
    config.setTitle_('Button')
    button.setConfiguration_(config)
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
    name = 'buttonStyleGray'
    cls.reuseIdentifier = name
    return name


class ButtonUpdateActivityHandler(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    button = UIButton.buttonWithType_(type)
    button.setSelected_(True)
    config = UIButtonConfiguration.plainButtonConfiguration()
    config.setTitle_('Button')
    button.setConfiguration_(config)

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
    name = 'buttonUpdateActivityHandler'
    cls.reuseIdentifier = name
    return name


class ButtonAttrText(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    button = UIButton.buttonWithType_(type)
    config = UIButtonConfiguration.plainButtonConfiguration()
    config.setTitle_('Button')
    button.setConfiguration_(config)

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
    name = 'buttonAttrText'
    cls.reuseIdentifier = name
    return name


class ButtonSymbol(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    button = UIButton.buttonWithType_(type)
    config = UIButtonConfiguration.plainButtonConfiguration()
    button.setConfiguration_(config)

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
    name = 'buttonSymbol'
    cls.reuseIdentifier = name
    return name


class AddToCartButton(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    button = UIButton.buttonWithType_(type)
    config = UIButtonConfiguration.plainButtonConfiguration()
    button.setConfiguration_(config)

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
    name = 'addToCartButton'
    cls.reuseIdentifier = name
    return name


class ButtonMultiTitle(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    button = UIButton.buttonWithType_(type)
    config = UIButtonConfiguration.plainButtonConfiguration()
    config.setTitle_('Button')
    button.setConfiguration_(config)

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
    name = 'buttonMultiTitle'
    cls.reuseIdentifier = name
    return name


class ButtonSystem(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    state = UIControl_State.normal
    button = UIButton.buttonWithType_(type)
    button.setTitle_forState_('Button', state)
    #config = UIButtonConfiguration.plainButtonConfiguration()
    #config.setTitle_('Button')
    #button.setConfiguration_(config)

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
    name = 'buttonSystem'
    cls.reuseIdentifier = name
    return name


class ButtonTitleColor(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    button = UIButton.buttonWithType_(type)
    config = UIButtonConfiguration.plainButtonConfiguration()
    config.setTitle_('Button')
    button.setConfiguration_(config)

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
    name = 'buttonTitleColor'
    cls.reuseIdentifier = name
    return name


class ButtonUpdateHandler(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    button = UIButton.buttonWithType_(type)
    config = UIButtonConfiguration.plainButtonConfiguration()
    config.setTitle_('Button')
    button.setConfiguration_(config)

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
    name = 'buttonUpdateHandler'
    cls.reuseIdentifier = name
    return name


class ButtonToggle(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    button = UIButton.buttonWithType_(type)
    config = UIButtonConfiguration.plainButtonConfiguration()
    config.setTitle_('Toggle')
    button.setConfiguration_(config)

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
    name = 'buttonToggle'
    cls.reuseIdentifier = name
    return name


class ButtonImageUpdateHandler(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    button = UIButton.buttonWithType_(type)
    config = UIButtonConfiguration.plainButtonConfiguration()
    config.setTitle_('Toggle')
    button.setConfiguration_(config)

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
    name = 'buttonImageUpdateHandler'
    cls.reuseIdentifier = name
    return name


class ButtonTextSymbol(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    button = UIButton.buttonWithType_(type)
    config = UIButtonConfiguration.plainButtonConfiguration()
    config.setTitle_('Button')
    button.setConfiguration_(config)

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
    name = 'buttonTextSymbol'
    cls.reuseIdentifier = name
    return name


class ButtonSymbolText(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    button = UIButton.buttonWithType_(type)
    config = UIButtonConfiguration.plainButtonConfiguration()
    config.setTitle_('Button')
    button.setConfiguration_(config)

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
    name = 'buttonSymbolText'
    cls.reuseIdentifier = name
    return name


class ButtonBackground(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    button = UIButton.buttonWithType_(type)
    config = UIButtonConfiguration.plainButtonConfiguration()
    config.setTitle_('Button')
    button.setConfiguration_(config)

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
    name = 'buttonBackground'
    cls.reuseIdentifier = name
    return name


class ButtonClose(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.close
    button = UIButton.buttonWithType_(type)
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
    name = 'buttonClose'
    cls.reuseIdentifier = name
    return name


class ButtonLargeSymbol(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    button = UIButton.buttonWithType_(type)
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
    name = 'buttonLargeSymbol'
    cls.reuseIdentifier = name
    return name


class ButtonStyleTinted(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    button = UIButton.buttonWithType_(type)
    config = UIButtonConfiguration.plainButtonConfiguration()
    config.setTitle_('Button')
    button.setConfiguration_(config)

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
    name = 'buttonStyleTinted'
    cls.reuseIdentifier = name
    return name


class ButtonStyleFilled(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    button = UIButton.buttonWithType_(type)
    config = UIButtonConfiguration.plainButtonConfiguration()
    config.setTitle_('Button')
    button.setConfiguration_(config)

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
    name = 'buttonStyleFilled'
    cls.reuseIdentifier = name
    return name


class ButtonImage(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    button = UIButton.buttonWithType_(type)
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
    name = 'buttonImage'
    cls.reuseIdentifier = name
    return name


class ButtonCornerStyle(CstmUITableViewCell):

  def init_cell(self, cell: UITableViewCell):
    type = UIButton_ButtonType.system
    button = UIButton.buttonWithType_(type)
    config = UIButtonConfiguration.plainButtonConfiguration()
    config.setTitle_('Button')
    button.setConfiguration_(config)

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
    name = 'buttonCornerStyle'
    cls.reuseIdentifier = name
    return name


prototypes = [
  ButtonSystemAddContact,
  ButtonDetailDisclosure,
  ButtonStyleGray,
  ButtonUpdateActivityHandler,
  ButtonAttrText,
  ButtonSymbol,
  AddToCartButton,
  ButtonMultiTitle,
  ButtonSystem,
  ButtonTitleColor,
  ButtonUpdateHandler,
  ButtonToggle,
  ButtonImageUpdateHandler,
  ButtonTextSymbol,
  ButtonSymbolText,
  ButtonBackground,
  ButtonClose,
  ButtonLargeSymbol,
  ButtonStyleTinted,
  ButtonStyleFilled,
  ButtonImage,
  ButtonCornerStyle,
]

