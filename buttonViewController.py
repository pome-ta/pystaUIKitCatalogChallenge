import ctypes

from objc_util import ObjCInstance, sel, create_objc_class, class_getSuperclass, c, ObjCClass

from objcista import *
#from objcista._controller import _Controller
from objcista.objcNavigationController import PlainNavigationController
from objcista.objcViewController import ObjcViewController
from objcista.objcLabel import ObjcLabel

import pdbg

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


class CaseElement:

  def __init__(self, title: str, cellID: str, configHandler):
    # xxx: ガバガバ
    # セルの視覚的なタイトル (テーブル セクションのヘッダー タイトル)
    self.title = title
    # nib ファイル内でセルを検索するためのテーブルビューのセルの識別子。
    self.cellID = cellID
    # セルのサブビューを設定するための構成ハンドラー。
    self.configHandler = configHandler

  @staticmethod
  def targetView(cell):
    #return cell.contentView.subviews[0] if cell != None else None
    print(cell)


class CstmUITableViewCell:

  def __init__(self):
    self.tableViewCell_instance: None
    self.reuseIdentifier: str = ''

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


# todo: まずはここで作りつつ、モジュール化するケアも考慮
#UITableViewController
class ObjcTableViewController:

  def __init__(self, *args, **kwargs):

    self._msgs: list['def'] = []  # xxx: 型名ちゃんとやる
    self.controller_instance: ObjCInstance

    self.prototypes = prototypes
    self.identifiers = []

    self.testCells = []

  def override(self):
    # todo: objc で独自にmethod 生やしたいときなど
    # todo: この関数内に関数を作り`@self.add_msg`
    @self.add_msg
    def configureSystemTextButton_(_self, _cmd, _button):
      pass

  def add_msg(self, msg):
    if not (hasattr(self, '_msgs')):
      self._msgs: list['def'] = []
    self._msgs.append(msg)

  def _override_controller(self):
    # todo: 既存method と独自追加method をシュッと持ちたい
    # if self._msgs: _methods.extend(self._msgs)

    def viewDidLoad(_self, _cmd):
      this = ObjCInstance(_self)
      view = this.view()
      pdbg.state(this)

      for proto in self.prototypes:
        _name = proto.reuseIdentifier_name()
        self.identifiers.append(_name)
        _args = [
          proto.this(),
          _name,
        ]
        view.registerClass_forCellReuseIdentifier_(*_args)

      #self.testCells.append()

    # --- UITableViewDelegate
    def tableView_numberOfRowsInSection_(_self, _cmd, _tableView, _section):
      return 1

    def numberOfSectionsInTableView_(_self, _cmd, _tableView):
      return 1  #len(self.identifiers)

    def tableView_cellForRowAtIndexPath_(_self, _cmd, _tableView, _indexPath):
      #pdbg.state(ObjCInstance(_self))
      tableView = ObjCInstance(_tableView)
      indexPath = ObjCInstance(_indexPath)
      #pdbg.state(indexPath)
      #print(indexPath)
      #pdbg.state(indexPath)
      cell_identifier = self.identifiers[indexPath.section()]
      cell = tableView.dequeueReusableCellWithIdentifier(
        cell_identifier, forIndexPath=indexPath)
      #pdbg.state(cell.contentView().subviews())
      #pdbg.state(cell.contentView())
      return cell.ptr

    _methods = [
      viewDidLoad,
      tableView_numberOfRowsInSection_,
      numberOfSectionsInTableView_,
      tableView_cellForRowAtIndexPath_,
    ]

    self.override()
    if self._msgs: _methods.extend(self._msgs)
    #print(self._msgs)

    create_kwargs = {
      'name': '_vc',
      'superclass': UITableViewController,
      'methods': _methods,
    }
    _vc = create_objc_class(**create_kwargs)
    self.controller_instance = _vc

  def _init_controller(self):
    self._override_controller()
    vc = self.controller_instance.new().autorelease()
    return vc

  @classmethod
  def new(cls, *args, **kwargs) -> ObjCInstance:
    _cls = cls(*args, **kwargs)
    return _cls._init_controller()


if __name__ == "__main__":

  class TopNavigationController(PlainNavigationController):

    def __init__(self):
      self.override()

    def override(self):

      @self.add_msg
      def doneButtonTapped_(_self, _cmd, _sender):
        this = ObjCInstance(_self)
        visibleViewController = this.visibleViewController()
        visibleViewController.dismissViewControllerAnimated_completion_(
          True, None)

    def willShowViewController(self,
                               navigationController: UINavigationController,
                               viewController: UIViewController,
                               animated: bool):

      super().willShowViewController(navigationController, viewController,
                                     animated)

      systemItem = UIBarButtonItem_SystemItem.done
      done_btn = UIBarButtonItem.alloc(
      ).initWithBarButtonSystemItem_target_action_(systemItem,
                                                   navigationController,
                                                   sel('doneButtonTapped:'))

      visibleViewController = navigationController.visibleViewController()

      # --- navigationItem
      navigationItem = visibleViewController.navigationItem()
      navigationItem.rightBarButtonItem = done_btn

  LAYOUT_DEBUG = True

  #LAYOUT_DEBUG = False
  #vc = ButtonViewController.new()
  #buttonSystemAddContact
  vc = ObjcTableViewController.new()
  nv = TopNavigationController.new(vc, True)
  style = UIModalPresentationStyle.pageSheet
  #style = UIModalPresentationStyle.fullScreen

  run_controller(nv, style)

