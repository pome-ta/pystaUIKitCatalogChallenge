from pyrubicon.objc.api import ObjCClass, objc_method
from pyrubicon.objc.runtime import send_super

from rbedge.functions import NSStringFromClass

from rbedge import pdbr

#ObjCClass.auto_rename = True

# --- UIViewController
UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UILabel = ObjCClass('UILabel')
UIFont = ObjCClass('UIFont')
UIColor = ObjCClass('UIColor')


class MainViewController(UIViewController):

  @objc_method
  def viewDidLoad(self):
    # --- Navigation
    title = NSStringFromClass(__class__)
    self.navigationItem.title = title

    # --- View
    backgroundColor = UIColor.systemBackgroundColor()
    self.view.backgroundColor = backgroundColor

    self.label = UILabel.new()
    self.label.text = 'UIKitCatalog'
    self.label.font = UIFont.systemFontOfSize_(26.0)
    self.label.sizeToFit()

    self.view.addSubview_(self.label)

    # --- Layout
    self.label.translatesAutoresizingMaskIntoConstraints = False

    NSLayoutConstraint.activateConstraints_([
      self.label.centerXAnchor.constraintEqualToAnchor_(
        self.view.centerXAnchor),
      self.label.centerYAnchor.constraintEqualToAnchor_(
        self.view.centerYAnchor),
    ])


if __name__ == '__main__':
  from rbedge import present_viewController

  vc = MainViewController.new()
  present_viewController(vc)

