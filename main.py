from objc_util import ObjCInstance, sel

from objcista import *
from objcista.objcNavigationController import PlainNavigationController
from objcista.objcViewController import ObjcViewController
from objcista.objcLabel import ObjcLabel

import pdbg


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

    appearance = UINavigationBarAppearance.alloc()
    appearance.configureWithDefaultBackground()
    # --- navigationBar
    navigationBar = navigationController.navigationBar()

    navigationBar.standardAppearance = appearance
    navigationBar.scrollEdgeAppearance = appearance
    navigationBar.compactAppearance = appearance
    navigationBar.compactScrollEdgeAppearance = appearance

    systemItem = UIBarButtonItem_SystemItem.done
    done_btn = UIBarButtonItem.alloc(
    ).initWithBarButtonSystemItem_target_action_(systemItem,
                                                 navigationController,
                                                 sel('doneButtonTapped:'))

    visibleViewController = navigationController.visibleViewController()

    # --- navigationItem
    navigationItem = visibleViewController.navigationItem()
    navigationItem.rightBarButtonItem = done_btn


class TopViewController(ObjcViewController):

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
  LAYOUT_DEBUG = False
  tvc = TopViewController.new()
  tnc = TopNavigationController.new(tvc, True)
  run_controller(tnc)

