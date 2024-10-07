import ctypes

from pyrubicon.objc.api import ObjCClass, objc_method
from rbedge.functions import NSStringFromClass

UIViewController = ObjCClass('UIViewController')
UICollectionView = ObjCClass('UICollectionView')


class OutlineViewController(UIViewController):

  @objc_method
  def viewDidLoad(self):
    # --- Navigation
    title = NSStringFromClass(__class__)
    self.navigationItem.title = title


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  outline_vc = OutlineViewController.new()
  style = UIModalPresentationStyle.fullScreen
  present_viewController(outline_vc, style)

