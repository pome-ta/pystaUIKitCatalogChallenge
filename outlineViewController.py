"""
note: まずは参照してるのやりきってみる
ref: [Diffable DataSource 入門 #Swift - Qiita](https://qiita.com/maiyama18/items/28039293b4bbf886ce8e)
  - Diffable DataSource
"""

import ctypes

from pyrubicon.objc.api import ObjCClass, objc_method
from pyrubicon.objc.runtime import send_super
from pyrubicon.objc.types import CGRectMake

from rbedge.functions import NSStringFromClass

UIViewController = ObjCClass('UIViewController')
UICollectionView = ObjCClass('UICollectionView')
UICollectionViewCompositionalLayout = ObjCClass(
  'UICollectionViewCompositionalLayout')

CGRectZero = CGRectMake(0, 0, 0, 0)


class TodoListViewController(UIViewController):

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    # --- Navigation
    title = NSStringFromClass(__class__)
    self.navigationItem.title = title
    self.configureCollectionView()

  @objc_method
  def configureCollectionView(self):

    #collectionView = UICollectionView.alloc().initWithFrame_(CGRectZero)
    #pdbr.state(collectionView)
    pdbr.state(self.view)


if __name__ == '__main__':
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController
  from rbedge import pdbr

  todo_vc = TodoListViewController.new()
  style = UIModalPresentationStyle.fullScreen
  present_viewController(todo_vc, style)
  #print(CGRectZero)

