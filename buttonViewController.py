from objc_util import ObjCInstance, sel, create_objc_class
from objcista import *
#from objcista._controller import _Controller
from objcista.objcNavigationController import PlainNavigationController
from objcista.objcViewController import ObjcViewController
from objcista.objcLabel import ObjcLabel

from storyboard_ButtonViewController import prototypes

import pdbg


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
    return cell.contentView().subviews().objectAtIndexedSubscript_(
      0) if cell != None else None


# todo: まずはここで作りつつ、モジュール化するケアも考慮
#UITableViewController
class ObjcTableViewController:

  def __init__(self, *args, **kwargs):
    self._msgs: list['def'] = []  # xxx: 型名ちゃんとやる
    self.controller_instance: ObjCInstance
    self.prototypes = prototypes
    self.testCells = []

  def override(self):
    # todo: objc で独自にmethod 生やしたいときなど
    # todo: この関数内に関数を作り`@self.add_msg`
    @self.add_msg
    def buttonClicked_(_self, _cmd, _sender):
      print('Button was clicked.')

    @self.add_msg
    def configureSystemTextButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)
      state = UIControl_State.normal
      button.setTitle_forState_('Button', state)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside

      button.addTarget_action_forControlEvents_(this, selector, event)

  def add_msg(self, msg):
    if not (hasattr(self, '_msgs')):
      self._msgs: list['def'] = []
    self._msgs.append(msg)

  def _override_controller(self):
    # todo: 既存method と独自追加method をシュッと持ちたい
    def viewDidLoad(_self, _cmd):
      this = ObjCInstance(_self)
      view = this.view()
      for proto in self.prototypes:
        _args = [
          proto.this(),
          proto.reuseIdentifier_name(),
        ]
        view.registerClass_forCellReuseIdentifier_(*_args)

      self.testCells.append(
        CaseElement('DefaultTitle', 'buttonSystem',
                    this.configureSystemTextButton_))

    # --- UITableViewDelegate
    def tableView_numberOfRowsInSection_(_self, _cmd, _tableView, _section):
      return 1

    def numberOfSectionsInTableView_(_self, _cmd, _tableView):
      return 1  #len(self.identifiers)

    def tableView_cellForRowAtIndexPath_(_self, _cmd, _tableView, _indexPath):
      tableView = ObjCInstance(_tableView)
      indexPath = ObjCInstance(_indexPath)

      #cell_identifier = self.identifiers[indexPath.section()]
      cellTest = self.testCells[indexPath.section()]

      cell = tableView.dequeueReusableCellWithIdentifier(
        cellTest.cellID, forIndexPath=indexPath)

      if (view := cellTest.targetView(cell)):
        cellTest.configHandler(view)
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

