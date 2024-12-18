'''
  note: Storyboard 未定義
'''
import ctypes
from pathlib import Path
import json

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method, objc_property, objc_const
from pyrubicon.objc.runtime import send_super, objc_id, load_library

from pyrubicon.objc.types import NSRange

from rbedge.enumerations import (
  UIUserInterfaceStyle,
  NSLineBreakMode,
)
from rbedge import pdbr

from pyLocalizedString import localizedString

UIKit = load_library('UIKit')  # todo: `objc_const` 用

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UITextView = ObjCClass('UITextView')
UIFont = ObjCClass('UIFont')
UIFontDescriptor = ObjCClass('UIFontDescriptor')
NSMutableAttributedString = ObjCClass('NSMutableAttributedString')

UIColor = ObjCClass('UIColor')

# --- Global Variables
UIFontTextStyleBody = objc_const(UIKit, 'UIFontTextStyleBody')
NSForegroundColorAttributeName = objc_const(UIKit,
                                            'NSForegroundColorAttributeName')


def get_srgb_named_style(named: str,
                         userInterfaceStyle: UIUserInterfaceStyle) -> list:
  # todo: 本来`UIColor.colorNamed:` で呼び出す。asset(bundle) の取り込みが難しそうなので、独自に直で呼び出し
  _path = Path(
    f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/{named}.colorset/Contents.json'
  )
  _str = _path.read_text()
  _dict = json.loads(_str)

  def _pick_color(colors: list[dict], style: str | None = None) -> list:
    components: dict
    for color in colors:
      if color.get('idiom') != 'universal':
        continue
      appearance, *_ = appearances if (
        appearances := color.get('appearances')) is not None else [None]
      if style is None and appearance is None:
        components = color.get('color').get('components')
        break
      if appearance is not None and style == appearance.get('value'):
        components = color.get('color').get('components')
        break

    red, green, blue, alpha = (float(components.get(clr))
                               for clr in ('red', 'green', 'blue', 'alpha'))
    # wip: エラーハンドリング
    return [red, green, blue, alpha]

  color_dicts = _dict.get('colors')
  if userInterfaceStyle == UIUserInterfaceStyle.light:
    return _pick_color(color_dicts, 'light')
  elif userInterfaceStyle == UIUserInterfaceStyle.dark:
    return _pick_color(color_dicts, 'dark')
  else:
    return _pick_color(color_dicts)


class TextViewController(UIViewController):

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    self.view.backgroundColor = UIColor.systemBackgroundColor()

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
    self.textView = textView
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

  # MARK: - Configuration
  @objc_method
  def reflowTextAttributes(self):
    entireTextColor = UIColor.blackColor

    # The text should be white in dark mode.
    if self.traitCollection.userInterfaceStyle == UIUserInterfaceStyle.dark:
      entireTextColor = UIColor.whiteColor

    entireAttributedText = NSMutableAttributedString.alloc(
    ).initWithAttributedString_(self.textView.attributedText)

    entireRange = NSRange(0, entireAttributedText.length())
    #pdbr.state(entireRange)
    #length
    #NSMutableAttributedString
    #print(entireAttributedText.length())
    #print(NSForegroundColorAttributeName)
    entireAttributedText.addAttribute_value_range_(
      NSForegroundColorAttributeName, entireTextColor, entireRange)
    pdbr.state(entireAttributedText)

  @objc_method
  def configureTextView(self):
    bodyFontDescriptor = UIFontDescriptor.preferredFontDescriptorWithTextStyle_(
      UIFontTextStyleBody)

    bodyFont = UIFont.fontWithDescriptor_size_(bodyFontDescriptor, 0.0)
    self.textView.font = bodyFont

    _color_named = get_srgb_named_style(
      'text_view_background', self.traitCollection.userInterfaceStyle)
    self.textView.backgroundColor = UIColor.colorWithRed_green_blue_alpha_(
      *_color_named)

    self.textView.isScrollEnabled = True

    # Apply different attributes to the text (bold, tinted, underline, etc.).
    # テキストにさまざまな属性 (太字、色付き、下線など) を適用します。
    self.reflowTextAttributes()


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

