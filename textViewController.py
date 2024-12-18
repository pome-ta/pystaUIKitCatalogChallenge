'''
  note: Storyboard 未定義
'''
import ctypes

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super

from rbedge.enumerations import (
  NSLineBreakMode, )
from rbedge import pdbr

from pyLocalizedString import localizedString

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UITextView = ObjCClass('UITextView')
UIFont = ObjCClass('UIFont')
UIFontDescriptor = ObjCClass('UIFontDescriptor')



UIColor = ObjCClass('UIColor')


class TextViewController(UIViewController):

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    self.view.backgroundColor = UIColor.systemBrownColor()  # todo: 確認用

    textView = UITextView.alloc().initWithFrame_(self.view.bounds)
    textView.text = 'This is a UITextView that uses attributed text. You can programmatically modify the display of the text by making it bold, highlighted, underlined, tinted, symbols, and more. These attributes are defined in NSAttributedString.h. You can even embed attachments in an NSAttributedString!'
    textView.font = UIFont.fontWithName_size_('HelveticaNeue', 14.0)
    textView.textContainer.lineBreakMode = NSLineBreakMode.byWordWrapping

    # --- Layout
    self.view.addSubview_(textView)
    textView.translatesAutoresizingMaskIntoConstraints = False
    areaLayoutGuide = self.view.safeAreaLayoutGuide
    #areaLayoutGuide = self.view
    NSLayoutConstraint.activateConstraints_([
      textView.bottomAnchor.constraintEqualToAnchor_constant_(
        areaLayoutGuide.bottomAnchor, -20.0),
      textView.topAnchor.constraintEqualToAnchor_(areaLayoutGuide.topAnchor),
      textView.trailingAnchor.constraintEqualToAnchor_constant_(
        areaLayoutGuide.trailingAnchor, -16.0),
      textView.leadingAnchor.constraintEqualToAnchor_constant_(
        areaLayoutGuide.leadingAnchor, 16.0),
    ])
    self.configureTextView()

  @objc_method
  def viewWillAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #pdbr.state(self.collectionView)
    #print('viewWillAppear')

  @objc_method
  def viewDidDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #pdbr.state(self.collectionView)
    #print('viewDidDisappear')
    
    
  @objc_method
  def configureTextView(self):
    pass


if __name__ == '__main__':
  from rbedge.functions import NSStringFromClass
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController

  main_vc = TextViewController.new()
  _title = NSStringFromClass(TextViewController)
  main_vc.navigationItem.title = _title

  style = UIModalPresentationStyle.fullScreen
  #style = UIModalPresentationStyle.pageSheet
  #style = UIModalPresentationStyle.popover

  present_viewController(main_vc, style)

