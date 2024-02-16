import ctypes

from objc_util import ObjCInstance, sel, create_objc_class, class_getSuperclass, c

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

  # todo: 変数名とか諸々考える
  def init_cell(self, cell: UITableViewCell):
    contactAdd = UIButton_ButtonType.contactAdd
    button = UIButton.buttonWithType_(contactAdd)
    button.setTranslatesAutoresizingMaskIntoConstraints_(False)

    #pdbg.state(button)
    cell.addSubview_(button)

    NSLayoutConstraint.activateConstraints_([
      button.centerXAnchor().constraintEqualToAnchor_(cell.centerXAnchor()),
      button.centerYAnchor().constraintEqualToAnchor_(cell.centerYAnchor()),
    ])

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


# todo: まずはここで作りつつ、モジュール化するケアも考慮
#UITableViewController
class ObjcTableViewController:

  def __init__(self, *args, **kwargs):
    self._msgs: list['def'] = []  # xxx: 型名ちゃんとやる
    self.cell_identifier = 'cell1'
    self.controller_instance: ObjCInstance
    self.storyboard_templates: list[dict]

  def override(self):
    # todo: objc で独自にmethod 生やしたいときなど
    # todo: この関数内に関数を作り`@self.add_msg`
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

      _args = [
        CstmUITableViewCell.this(),
        self.cell_identifier,
      ]
      view.registerClass_forCellReuseIdentifier_(*_args)

    # --- UITableViewDelegate
    def tableView_numberOfRowsInSection_(_self, _cmd, _tableView, _section):

      return 1

    def tableView_cellForRowAtIndexPath_(_self, _cmd, _tableView, _indexPath):
      tableView = ObjCInstance(_tableView)
      indexPath = ObjCInstance(_indexPath)
      cell = tableView.dequeueReusableCellWithIdentifier(
        self.cell_identifier, forIndexPath=indexPath)
      #pdbg.state(cell)
      return cell.ptr

    _methods = [
      viewDidLoad,
      tableView_numberOfRowsInSection_,
      tableView_cellForRowAtIndexPath_,
    ]
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
                             viewController: UIViewController, animated: bool):

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


if __name__ == "__main__":
  LAYOUT_DEBUG = True
  #LAYOUT_DEBUG = False
  #vc = ButtonViewController.new()
  vc = ObjcTableViewController.new()
  nv = TopNavigationController.new(vc, True)
  style = UIModalPresentationStyle.pageSheet
  #style = UIModalPresentationStyle.fullScreen

  run_controller(nv, style)

