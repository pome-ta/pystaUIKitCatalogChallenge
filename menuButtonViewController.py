from enum import Enum

import ctypes
from objc_util import ObjCInstance, sel, create_objc_class, ns, ObjCBlock

from objcista import *

from caseElement import CaseElement
from storyboard_MenuButtonViewController import prototypes
from pyLocalizedString import pylocalizedString

import pdbg


class MenuButtonKind(Enum):
  buttonMenuProgrammatic = 'buttonMenuProgrammatic'
  buttonMenuMultiAction = 'buttonMenuMultiAction'
  buttonSubMenu = 'buttonSubMenu'
  buttonMenuSelection = 'buttonMenuSelection'


# todo: まずはここで作りつつ、モジュール化するケアも考慮
#UITableViewController
class ObjcTableViewController:

  def __init__(self, *args, **kwargs):
    self._msgs: list['Callable'] = []  # xxx: 型名ちゃんとやる
    self.controller_instance: ObjCInstance
    self.prototypes = prototypes
    self.testCells = []

  def set_prototypes(self, view: UITableView):
    for proto in self.prototypes:
      cellClass = proto.this()
      identifier = proto.reuseIdentifier_name()
      view.registerClass_forCellReuseIdentifier_(cellClass, identifier)

  def _override_controller(self):
    # todo: 既存method と独自追加method をシュッと持ちたい
    def viewDidLoad(_self, _cmd):
      this = ObjCInstance(_self)

      _view = this.view()
      style = UITableViewStyle.grouped

      view = _view.initWithFrame_style_(_view.frame(), style)
      this.setView_(view)
      self.set_prototypes(view)

      self.testCells.extend([
        # 0
        CaseElement(pylocalizedString('DropDownProgTitle'),
                    MenuButtonKind.buttonMenuProgrammatic.value,
                    this.configureDropDownProgrammaticButton_),
      ])

    # --- UITableViewDelegate

    # xxx: `return` ができないので、`tableView_viewForHeaderInSection_` で処理
    '''
    def centeredHeaderView_(_self, _cmd, _title):
      title = ObjCInstance(_title)
      alignment = UIListContentTextAlignment.center

      headerView = UITableViewHeaderFooterView.new()
      content = UIListContentConfiguration.groupedHeaderConfiguration()
      content.setText_(title)
      content.textProperties().setAlignment_(alignment)
      headerView.setContentConfiguration_(content)
      return headerView.ptr
    '''

    # MARK: - UITableViewDataSource
    def tableView_viewForHeaderInSection_(_self, _cmd, _tableView, _section):
      title = self.testCells[_section].title
      alignment = UIListContentTextAlignment.center

      headerView = UITableViewHeaderFooterView.new()
      content = UIListContentConfiguration.groupedHeaderConfiguration()
      content.setText_(title)
      content.textProperties().setAlignment_(alignment)
      headerView.setContentConfiguration_(content)

      # xxx: `return` ができないので、`tableView_viewForHeaderInSection_` で処理
      #return ObjCInstance(_self).centeredHeaderView_(self.testCells[_section].title)

      return headerView.ptr

    def tableView_titleForHeaderInSection_(_self, _cmd, _tableView, _section):
      return ns(self.testCells[_section].title).ptr

    def tableView_numberOfRowsInSection_(_self, _cmd, _tableView, _section):
      return 1

    def numberOfSectionsInTableView_(_self, _cmd, _tableView):
      return len(self.testCells)

    def tableView_cellForRowAtIndexPath_(_self, _cmd, _tableView, _indexPath):
      tableView = ObjCInstance(_tableView)
      indexPath = ObjCInstance(_indexPath)

      cellTest = self.testCells[indexPath.section()]

      cell = tableView.dequeueReusableCellWithIdentifier(
        cellTest.cellID, forIndexPath=indexPath)

      if (view := cellTest.targetView(cell)):
        cellTest.configHandler(view)
      return cell.ptr

    _methods = [
      viewDidLoad,
      #centeredHeaderView_,
      tableView_viewForHeaderInSection_,
      tableView_titleForHeaderInSection_,
      tableView_numberOfRowsInSection_,
      numberOfSectionsInTableView_,
      tableView_cellForRowAtIndexPath_,
    ]

    self.add_extensions()
    if self._msgs: _methods.extend(self._msgs)

    create_kwargs = {
      'name': '_vc',
      'superclass': UITableViewController,
      'methods': _methods,
    }
    _vc = create_objc_class(**create_kwargs)
    self.controller_instance = _vc

  def add_extensions(self):
    # todo: objc で独自にmethod 生やしたいときなど
    # todo: この関数内に関数を作り`@self.extension`

    @self.extension
    def menuHandler_(_self, _cmd, _action):
      action = ObjCInstance(_action)

    # MARK: - Drop Down Menu Buttons
    @self.extension
    def configureDropDownProgrammaticButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)
      #menu = UIMenu.menuWithChildren_([])
      #actionWithTitle_image_identifier_handler_
      #action=UIAction.actionWithTitle_image_identifier_handler_(pylocalizedString('ItemTitle'), None, ns('item').ptr, this.menuHandler_)
      #button.setMenu_
      #menuWithChildren_
      #pdbg.state(UIMenu)
      #item1
      action = UIAction.actionWithTitle_image_identifier_handler_(
        pylocalizedString('ItemTitle'), None, 'item', None)
      #pdbg.state(action.identifier())
      '''
      action = UIAction.new()
      action.setTitle_(pylocalizedString('ItemTitle'))
      action.setHandler_(
        ObjCBlock(menuHandler_,
                  argtypes=[
                    ctypes.c_void_p,
                    ctypes.c_void_p,
                    ctypes.c_void_p,
                  ]))
      '''
      menu = UIMenu.menuWithChildren_([action])
      #pdbg.state(action.setHandler_)
      #pdbg.state(menu)
      #pdbg.state(button)
      #pdbg.state(this.tableView_cellForRowAtIndexPath_)
      button.setMenu_(menu)
      button.setShowsMenuAsPrimaryAction_(True)

  def extension(self, msg):
    if not (hasattr(self, '_msgs')):
      self._msgs: list['Callable'] = []
    self._msgs.append(msg)

  def _init_controller(self):
    self._override_controller()
    vc = self.controller_instance.new().autorelease()
    return vc

  @classmethod
  def new(cls, *args, **kwargs) -> ObjCInstance:
    _cls = cls(*args, **kwargs)
    return _cls._init_controller()


if __name__ == "__main__":
  from objcista.objcNavigationController import PlainNavigationController

  class TopNavigationController(PlainNavigationController):

    def __init__(self):
      self.add_extensions()

    def add_extensions(self):

      @self.extension
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

  vc = ObjcTableViewController.new()
  nv = TopNavigationController.new(vc, True)
  style = UIModalPresentationStyle.pageSheet
  #style = UIModalPresentationStyle.fullScreen

  run_controller(nv, style)

