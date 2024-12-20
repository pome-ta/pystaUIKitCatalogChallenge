'''
  note: Storyboard 未定義
'''
import ctypes
from pathlib import Path
import json

from pyrubicon.objc.api import ObjCClass, NSString, NSData
from pyrubicon.objc.api import objc_method, objc_property, objc_const
from pyrubicon.objc.runtime import send_super, objc_id, load_library, SEL
from pyrubicon.objc.types import NSRange, CGPointMake, CGRect

from rbedge.enumerations import (
  NSLayoutAttribute,
  NSLayoutRelation,
  UIUserInterfaceStyle,
  NSLineBreakMode,
  UIFontDescriptorSymbolicTraits,
  NSUnderlineStyle,
  UIImageRenderingMode,
)

from pyLocalizedString import localizedString
from rbedge import pdbr

UIKit = load_library('UIKit')  # todo: `objc_const` 用
UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UIScreen = ObjCClass('UIScreen')
NSURL = ObjCClass('NSURL')

UITextView = ObjCClass('UITextView')
UIFont = ObjCClass('UIFont')
UIFontDescriptor = ObjCClass('UIFontDescriptor')
NSAttributedString = ObjCClass('NSAttributedString')
NSMutableAttributedString = ObjCClass('NSMutableAttributedString')
NSTextAttachment = ObjCClass('NSTextAttachment')

NSNotificationCenter = ObjCClass('NSNotificationCenter')

UIColor = ObjCClass('UIColor')
UIImage = ObjCClass('UIImage')
UIImageSymbolConfiguration = ObjCClass('UIImageSymbolConfiguration')

# --- Global Variables
UIFontTextStyleBody = objc_const(UIKit, 'UIFontTextStyleBody')
NSForegroundColorAttributeName = objc_const(UIKit,
                                            'NSForegroundColorAttributeName')
NSFontAttributeName = objc_const(UIKit, 'NSFontAttributeName')
NSBackgroundColorAttributeName = objc_const(UIKit,
                                            'NSBackgroundColorAttributeName')
NSUnderlineStyleAttributeName = objc_const(UIKit,
                                           'NSUnderlineStyleAttributeName')
UIKeyboardWillShowNotification = objc_const(UIKit,
                                            'UIKeyboardWillShowNotification')
UIKeyboardWillHideNotification = objc_const(UIKit,
                                            'UIKeyboardWillHideNotification')
UIKeyboardAnimationDurationUserInfoKey = objc_const(
  UIKit, 'UIKeyboardAnimationDurationUserInfoKey')
UIKeyboardFrameBeginUserInfoKey = objc_const(
  UIKit, 'UIKeyboardFrameBeginUserInfoKey')
UIKeyboardFrameEndUserInfoKey = objc_const(UIKit,
                                           'UIKeyboardFrameEndUserInfoKey')


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
    textView.text = 'This is a UITextView that uses attributed text. You can programmatically modify the display of the text by making it bold, highlighted, underlined, tinted, symbols, and more. These attributes are defined in NSAttributedString.h. You can even embed attachments in an NSAttributedString!\n'
    textView.font = UIFont.fontWithName_size_('HelveticaNeue', 14.0)
    textView.textContainer.lineBreakMode = NSLineBreakMode.byWordWrapping

    # --- Layout
    self.view.addSubview_(textView)
    textView.translatesAutoresizingMaskIntoConstraints = False
    areaLayoutGuide = self.view.safeAreaLayoutGuide
    #areaLayoutGuide = self.view
    '''
    
    NSLayoutConstraint.activateConstraints_([
      textView.bottomAnchor.constraintEqualToAnchor_constant_(
        areaLayoutGuide.bottomAnchor, -20.0),
      textView.topAnchor.constraintEqualToAnchor_(areaLayoutGuide.topAnchor),
      textView.trailingAnchor.constraintEqualToAnchor_constant_(
        areaLayoutGuide.trailingAnchor, -16.0),
      textView.leadingAnchor.constraintEqualToAnchor_constant_(
        areaLayoutGuide.leadingAnchor, 16.0),
    ])
    '''

    layoutMarginsGuide = self.view.layoutMarginsGuide
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide

    #textViewBottomLayoutGuideConstraint =

    #addConstraints_
    #constraintWithItem_attribute_relatedBy_toItem_attribute_multiplier_constant_

    #textViewBottomLayoutGuideConstraint = NSLayoutConstraint.constraintWithItem_attribute_relatedBy_toItem_attribute_multiplier_constant_(textView, NSLayoutAttribute.bottom, NSLayoutRelation.equal, safeAreaLayoutGuide, NSLayoutAttribute.bottom, 1.0, 20.0)

    #NSLayoutAttribute,
    #NSLayoutRelation,

    textViewBottomLayoutGuideConstraint = NSLayoutConstraint.constraintWithItem(
      textView,
      attribute__1=NSLayoutAttribute.bottom,
      relatedBy=NSLayoutRelation.equal,
      toItem=safeAreaLayoutGuide,
      attribute__2=NSLayoutAttribute.bottom,
      multiplier=1.0,
      constant=-20.0)

    self.view.addConstraints_([
      textViewBottomLayoutGuideConstraint,
      NSLayoutConstraint.
      constraintWithItem_attribute_relatedBy_toItem_attribute_multiplier_constant_(
        textView, NSLayoutAttribute.top, NSLayoutRelation.equal,
        safeAreaLayoutGuide, NSLayoutAttribute.top, 1.0, 0.0),
      NSLayoutConstraint.
      constraintWithItem_attribute_relatedBy_toItem_attribute_multiplier_constant_(
        textView, NSLayoutAttribute.trailing, NSLayoutRelation.equal,
        safeAreaLayoutGuide, NSLayoutAttribute.trailing, 1.0, -16.0),
      NSLayoutConstraint.
      constraintWithItem_attribute_relatedBy_toItem_attribute_multiplier_constant_(
        textView, NSLayoutAttribute.leading, NSLayoutRelation.equal,
        safeAreaLayoutGuide, NSLayoutAttribute.leading, 1.0, 16.0),
    ])

    #pdbr.state(textView)
    #pdbr.state(textViewBottomLayoutGuideConstraint)
    #self.textViewBottomLayoutGuideConstraint = textView.bottomAnchor
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
    # Listen for changes to keyboard visibility so that we can adjust the text view's height accordingly.
    notificationCenter = NSNotificationCenter.defaultCenter

    notificationCenter.addObserver_selector_name_object_(
      self, SEL('handleKeyboardNotification:'), UIKeyboardWillShowNotification,
      None)
    notificationCenter.addObserver_selector_name_object_(
      self, SEL('handleKeyboardNotification:'), UIKeyboardWillHideNotification,
      None)
    #pdbr.state(notificationCenter)

  @objc_method
  def viewDidDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    notificationCenter = NSNotificationCenter.defaultCenter
    notificationCenter.removeObserver_name_object_(
      self, UIKeyboardWillShowNotification, None)
    notificationCenter.removeObserver_name_object_(
      self, UIKeyboardWillHideNotification, None)

  # MARK: - Keyboard Event Notifications
  @objc_method
  def handleKeyboardNotification_(self, notification):
    if (userInfo := notification.userInfo) is None:
      return

    # Get the animation duration.
    animationDuration = 0
    if (value := userInfo[UIKeyboardAnimationDurationUserInfoKey]):
      animationDuration = value

    # Convert the keyboard frame from screen to view coordinates.
    keyboardScreenBeginFrame: CGRect
    if (value := userInfo[UIKeyboardFrameBeginUserInfoKey]):
      keyboardScreenBeginFrame = value.CGRectValue

    keyboardScreenEndFrame: CGRect
    if (value := userInfo[UIKeyboardFrameEndUserInfoKey]):
      keyboardScreenEndFrame = value.CGRectValue

    keyboardViewBeginFrame = self.view.convertRect_fromView_(
      keyboardScreenBeginFrame, self.view.window())
    keyboardViewEndFrame = self.view.convertRect_fromView_(
      keyboardScreenEndFrame, self.view.window())
    #pdbr.state(keyboardScreenBeginFrame)
    #print(keyboardScreenBeginFrame)
    #print(self.view)
    #pdbr.state(self.view.window)
    #print(self.view.window())
    #pdbr.state(self.view.window())
    #print(self.view)
    originDelta = keyboardViewEndFrame.origin.y - keyboardViewBeginFrame.origin.y

    # The text view should be adjusted, update the constant for this constraint.
    #print(self.textViewBottomLayoutGuideConstraint)
    #pdbr.state(self.textViewBottomLayoutGuideConstraint)
    #print('---')

  # MARK: - Configuration
  @objc_method
  def reflowTextAttributes(self):
    entireTextColor = UIColor.blackColor

    # The text should be white in dark mode.
    if self.traitCollection.userInterfaceStyle == UIUserInterfaceStyle.dark:
      entireTextColor = UIColor.whiteColor
      #entireTextColor = UIColor.redColor

    entireAttributedText = NSMutableAttributedString.alloc(
    ).initWithAttributedString_(self.textView.attributedText)

    entireRange = NSRange(0, entireAttributedText.length())

    entireAttributedText.addAttribute(NSForegroundColorAttributeName,
                                      value=entireTextColor,
                                      range=entireRange)
    self.textView.attributedText = entireAttributedText

    # Modify some of the attributes of the attributed string. You can modify these attributes yourself to get a better feel for what they do.Note that the initial text is visible in the storyboard.
    # 属性付き文字列の属性の一部を変更します。これらの属性を自分で変更して、その機能をよりよく理解することができます。最初のテキストがストーリーボードに表示されることに注意してください。
    attributedText = NSMutableAttributedString.alloc(
    ).initWithAttributedString_(self.textView.attributedText)

    # Use NSString so the result of rangeOfString is an NSRange, not Range<String.Index>. This will then be the correct type to then pass to the addAttribute method of NSMutableAttributedString.
    # NSString を使用すると、rangeOfString の結果が Range<String.Index> ではなく NSRange になります。これは、NSMutableAttributedString の addAttribute メソッドに渡す正しい型になります。
    text = NSString(self.textView.text)

    # Find the range of each element to modify.
    boldRange = text.rangeOfString_(localizedString('bold'))
    highlightedRange = text.rangeOfString_(localizedString('highlighted'))
    underlinedRange = text.rangeOfString_(localizedString('underlined'))
    tintedRange = text.rangeOfString_(localizedString('tinted'))

    # Add bold attribute. Take the current font descriptor and create a new font descriptor with an additional bold trait.
    # 太字属性を追加します。現在のフォント記述子を使用して、追加の太字特性を持つ新しいフォント記述子を作成します。
    boldFontDescriptor = self.textView.font.fontDescriptor.fontDescriptorWithSymbolicTraits_(
      UIFontDescriptorSymbolicTraits.traitBold)
    boldFont = UIFont.fontWithDescriptor_size_(boldFontDescriptor, 0.0)

    attributedText.addAttribute(NSFontAttributeName,
                                value=boldFont,
                                range=boldRange)
    # Add highlight attribute.
    attributedText.addAttribute(NSBackgroundColorAttributeName,
                                value=UIColor.systemGreenColor(),
                                range=highlightedRange)
    # Add underline attribute.
    attributedText.addAttribute(NSUnderlineStyleAttributeName,
                                value=NSUnderlineStyle.single,
                                range=underlinedRange)
    # Add tint color.
    attributedText.addAttribute(NSForegroundColorAttributeName,
                                value=UIColor.systemBlueColor(),
                                range=tintedRange)

    self.textView.attributedText = attributedText

  @objc_method
  def symbolAttributedString_(self, name):
    symbolAttachment = NSTextAttachment.alloc().init()
    # wip: Dark Mode時の色が黒のまま
    # hint?: [ios - How to set color of templated image in NSTextAttachment - Stack Overflow](https://stackoverflow.com/questions/29041458/how-to-set-color-of-templated-image-in-nstextattachment)
    if (symbolImage := UIImage.systemImageNamed_(name).imageWithRenderingMode_(
        UIImageRenderingMode.alwaysTemplate)):
      symbolAttachment.image = symbolImage

    return NSAttributedString.attributedStringWithAttachment_(symbolAttachment)

  @objc_method
  def multiColorSymbolAttributedString_(self, name):
    symbolAttachment = NSTextAttachment.alloc().init()
    palleteSymbolConfig = UIImageSymbolConfiguration.configurationWithPaletteColors_(
      [
        UIColor.systemOrangeColor(),
        UIColor.systemRedColor(),
      ])

    if (symbolImage := UIImage.systemImageNamed_(name).imageWithConfiguration_(
        palleteSymbolConfig)):
      symbolAttachment.image = symbolImage
    return NSAttributedString.attributedStringWithAttachment_(symbolAttachment)

  @objc_method
  def configureTextView(self):
    bodyFontDescriptor = UIFontDescriptor.preferredFontDescriptorWithTextStyle_(
      UIFontTextStyleBody)

    bodyFont = UIFont.fontWithDescriptor_size_(bodyFontDescriptor, 0.0)
    self.textView.font = bodyFont

    _color_named = get_srgb_named_style(
      'text_view_background', self.traitCollection.userInterfaceStyle)
    #self.textView.backgroundColor = UIColor.colorWithRed_green_blue_alpha_(*_color_named)
    self.textView.backgroundColor = UIColor.redColor

    self.textView.isScrollEnabled = True

    # Apply different attributes to the text (bold, tinted, underline, etc.).
    # テキストにさまざまな属性 (太字、色付き、下線など) を適用します。
    self.reflowTextAttributes()

    # Insert symbols as image attachments.
    text = NSString(self.textView.text)
    attributedText = NSMutableAttributedString.alloc(
    ).initWithAttributedString_(self.textView.attributedText)

    symbolsSearchRange = text.rangeOfString_(localizedString('symbols'))

    insertPoint = symbolsSearchRange.location + symbolsSearchRange.length

    attributedText.insertAttributedString(
      self.symbolAttributedString_('heart'), atIndex=insertPoint)

    insertPoint += 1
    attributedText.insertAttributedString(
      self.symbolAttributedString_('heart.fill'), atIndex=insertPoint)

    insertPoint += 1
    attributedText.insertAttributedString(
      self.symbolAttributedString_('heart.slash'), atIndex=insertPoint)

    # Multi-color SF Symbols only in iOS 15 or later.
    if True:  # wip: `available(iOS 15, *)`
      insertPoint += 1

      attributedText.insertAttributedString(
        self.multiColorSymbolAttributedString_('arrow.up.heart.fill'),
        atIndex=insertPoint)

    # Add the image as an attachment.
    # xxx: `lambda` の使い方が悪い
    dataWithContentsOfURL = lambda path_str: NSData.dataWithContentsOfURL_(
      NSURL.fileURLWithPath_(str(Path(path_str).absolute())))

    text_view_attachment = './UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/text_view_attachment.imageset/Sunset_5.png'

    if (image := UIImage.alloc().initWithData_scale_(
        dataWithContentsOfURL(text_view_attachment), 1)):
      textAttachment = NSTextAttachment.alloc().init()
      textAttachment.image = image
      textAttachment.bounds = CGRect(CGPointMake(0.0, 0.0), image.size)
      textAttachmentString = NSAttributedString.attributedStringWithAttachment_(
        textAttachment)
      attributedText.appendAttributedString_(textAttachmentString)
      self.textView.attributedText = attributedText

    # When turned on, this changes the rendering scale of the text to match the standard text scaling and preserves the original font point sizes when the contents of the text view are copied to the pasteboard. Apps that show a lot of text content, such as a text viewer or editor, should turn this on and use the standard text scaling.
    # オンにすると、標準のテキスト スケーリングに一致するようにテキストのレンダリング スケールが変更され、テキスト ビューの内容がペーストボードにコピーされるときに元のフォント ポイント サイズが保持されます。テキスト ビューアやエディタなど、多くのテキスト コンテンツを表示するアプリでは、これをオンにして、標準のテキスト スケーリングを使用する必要があります。
    self.textView.usesStandardTextScaling = True
    #self.textView.setUsesStandardTextScaling_(True)


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

