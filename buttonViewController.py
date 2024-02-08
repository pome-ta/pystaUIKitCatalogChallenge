from objc_util import ObjCInstance, sel

from objcista import *
#from objcista._controller import _Controller
from objcista.objcNavigationController import PlainNavigationController
from objcista.objcViewController import ObjcViewController
from objcista.objcLabel import ObjcLabel

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
    #return cell.contentView.subviews[0] if cell != None else None
    print(cell)


c = CaseElement('h', 'f', 'p')
c.targetView('a')


# todo: まずはここで作りつつ、モジュール化するケアも考慮
class ObjcTableViewController:

  def __init__(self, *args, **kwargs):
    pass


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


class ButtonViewController(ObjcViewController):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.main_text = 'UIKitCatalog'

  def didLoad(self, this: UIViewController):
    view = this.view()
    background_color = UIColor.systemBackgroundColor()
    view.setBackgroundColor_(background_color)

    label_kwargs = {
      'text': self.main_text,
      'LAYOUT_DEBUG': LAYOUT_DEBUG,
    }
    self.main_label = ObjcLabel.new(**label_kwargs)
    self.main_label.setFont_(UIFont.systemFontOfSize_(26.0))

    view.addSubview(self.main_label)

    # --- layout
    layoutMarginsGuide = view.layoutMarginsGuide()

    NSLayoutConstraint.activateConstraints_([
      self.main_label.centerXAnchor().constraintEqualToAnchor_(
        layoutMarginsGuide.centerXAnchor()),
      self.main_label.centerYAnchor().constraintEqualToAnchor_(
        layoutMarginsGuide.centerYAnchor()),
    ])


if __name__ == "__main__":
  LAYOUT_DEBUG = True
  #LAYOUT_DEBUG = False
  vc = ButtonViewController.new()
  nv = TopNavigationController.new(vc, True)
  run_controller(nv)

