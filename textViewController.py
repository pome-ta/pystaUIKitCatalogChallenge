"""
  note: Storyboard 未定義
"""
import ctypes

from pyrubicon.objc.api import ObjCClass, Block
from pyrubicon.objc.api import NSString
from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.runtime import send_super, SEL
from pyrubicon.objc.types import NSRange, CGRect, CGPointMake

from rbedge.enumerations import (
  NSLayoutAttribute,
  NSLayoutRelation,
  UIViewAnimationCurve,
  UIUserInterfaceStyle,
  NSLineBreakMode,
  UIFontDescriptorSymbolicTraits,
  NSUnderlineStyle,
  UIImageRenderingMode,
  UIBarButtonSystemItem,
)

from rbedge.globalVariables import (
  UIFontTextStyle,
  NSAttributedStringKey,
  NSNotificationName,
  UIKeyboardAnimationDurationUserInfoKey,
  UIKeyboardFrameBeginUserInfoKey,
  UIKeyboardFrameEndUserInfoKey,
)
from rbedge.pythonProcessUtils import (
  mainScreen_scale,
  dataWithContentsOfURL,
  get_srgb_named_style,
)

from pyLocalizedString import localizedString

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UITextView = ObjCClass('UITextView')
UIFont = ObjCClass('UIFont')
UIFontDescriptor = ObjCClass('UIFontDescriptor')
NSAttributedString = ObjCClass('NSAttributedString')
NSMutableAttributedString = ObjCClass('NSMutableAttributedString')
NSTextAttachment = ObjCClass('NSTextAttachment')

NSNotificationCenter = ObjCClass('NSNotificationCenter')
UIViewPropertyAnimator = ObjCClass('UIViewPropertyAnimator')

UIBarButtonItem = ObjCClass('UIBarButtonItem')

UIColor = ObjCClass('UIColor')
UIImage = ObjCClass('UIImage')
UIImageSymbolConfiguration = ObjCClass('UIImageSymbolConfiguration')


class TextViewController(UIViewController):

  textView: UITextView = objc_property()
  textViewBottomLayoutGuideConstraint: NSLayoutConstraint = objc_property()
  rightBarButtonItems: list = objc_property()

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t - {NSStringFromClass(__class__)}: dealloc')
    #pass

  @objc_method
  def loadView(self):
    send_super(__class__, self, 'loadView')
    #print(f'\t{NSStringFromClass(__class__)}: loadView')
    self.rightBarButtonItems = None

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    #print(f'\t{NSStringFromClass(__class__)}: viewDidLoad')
    self.navigationItem.title = localizedString('TextViewTitle') if (
      title := self.navigationItem.title) is None else title
    self.view.backgroundColor = UIColor.systemBackgroundColor()

    textView = UITextView.alloc().initWithFrame_(self.view.bounds)
    textView.delegate = self

    textView.text = 'This is a UITextView that uses attributed text. You can programmatically modify the display of the text by making it bold, highlighted, underlined, tinted, symbols, and more. These attributes are defined in NSAttributedString.h. You can even embed attachments in an NSAttributedString!\n'
    textView.font = UIFont.fontWithName_size_('HelveticaNeue', 14.0)
    textView.textContainer.lineBreakMode = NSLineBreakMode.byWordWrapping

    # --- Layout
    self.view.addSubview_(textView)
    textView.translatesAutoresizingMaskIntoConstraints = False

    layoutMarginsGuide = self.view.layoutMarginsGuide
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide

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

    self.textView = textView
    self.textViewBottomLayoutGuideConstraint = textViewBottomLayoutGuideConstraint

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
    #print(f'\t{NSStringFromClass(__class__)}: viewWillAppear_')

    # Listen for changes to keyboard visibility so that we can adjust the text view's height accordingly.
    notificationCenter = NSNotificationCenter.defaultCenter

    notificationCenter.addObserver_selector_name_object_(
      self, SEL('handleKeyboardNotification:'),
      NSNotificationName.keyboardWillShowNotification, None)
    notificationCenter.addObserver_selector_name_object_(
      self, SEL('handleKeyboardNotification:'),
      NSNotificationName.keyboardWillHideNotification, None)

  @objc_method
  def viewDidAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print(f'\t{NSStringFromClass(__class__)}: viewDidAppear_')

  @objc_method
  def viewWillDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    # print(f'\t{NSStringFromClass(__class__)}: viewWillDisappear_')

  @objc_method
  def viewDidDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    print(f'\t{NSStringFromClass(__class__)}: viewDidDisappear_')

    notificationCenter = NSNotificationCenter.defaultCenter
    notificationCenter.removeObserver_name_object_(
      self, NSNotificationName.keyboardWillShowNotification, None)
    notificationCenter.removeObserver_name_object_(
      self, NSNotificationName.keyboardWillHideNotification, None)

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'{__class__}: didReceiveMemoryWarning')

  # MARK: - Keyboard Event Notifications
  @objc_method
  def handleKeyboardNotification_(self, notification):
    if (userInfo := notification.userInfo) is None:
      return

    # Get the animation duration.
    animationDuration = 0
    if (value := userInfo[UIKeyboardAnimationDurationUserInfoKey]):
      animationDuration = value.doubleValue

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

    originDelta = keyboardViewEndFrame.origin.y - keyboardViewBeginFrame.origin.y

    # The text view should be adjusted, update the constant for this constraint.
    self.textViewBottomLayoutGuideConstraint.constant += originDelta

    # Inform the view that its autolayout constraints have changed and the layout should be updated.
    self.view.setNeedsUpdateConstraints()

    # Animate updating the view's layout by calling layoutIfNeeded inside a `UIViewPropertyAnimator` animation block.
    textViewAnimator = UIViewPropertyAnimator.alloc(
    ).initWithDuration_curve_animations_(
      animationDuration, UIViewAnimationCurve.easeIn,
      Block(lambda: self.view.layoutIfNeeded(), None))
    textViewAnimator.startAnimation()

    # Scroll to the selected text once the keyboard frame changes.
    selectedRange = self.textView.selectedRange
    self.textView.scrollRangeToVisible_(selectedRange)

  # MARK: - Configuration
  @objc_method
  def reflowTextAttributes(self):
    entireTextColor = UIColor.blackColor

    # The text should be white in dark mode.
    if self.traitCollection.userInterfaceStyle == UIUserInterfaceStyle.dark:
      entireTextColor = UIColor.whiteColor
      # entireTextColor = UIColor.redColor  # todo: 確認用

    entireAttributedText = NSMutableAttributedString.alloc(
    ).initWithAttributedString_(self.textView.attributedText)

    entireRange = NSRange(0, entireAttributedText.length())

    entireAttributedText.addAttribute(NSAttributedStringKey.foregroundColor,
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

    attributedText.addAttribute(NSAttributedStringKey.font,
                                value=boldFont,
                                range=boldRange)
    # Add highlight attribute.
    attributedText.addAttribute(NSAttributedStringKey.backgroundColor,
                                value=UIColor.systemGreenColor(),
                                range=highlightedRange)
    # Add underline attribute.
    attributedText.addAttribute(NSAttributedStringKey.underlineStyle,
                                value=NSUnderlineStyle.single,
                                range=underlinedRange)
    # Add tint color.
    attributedText.addAttribute(NSAttributedStringKey.foregroundColor,
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
      UIFontTextStyle.body)

    bodyFont = UIFont.fontWithDescriptor_size_(bodyFontDescriptor, 0.0)
    self.textView.font = bodyFont

    _color_named = get_srgb_named_style(
      'text_view_background', self.traitCollection.userInterfaceStyle)
    self.textView.backgroundColor = UIColor.colorWithRed_green_blue_alpha_(
      *_color_named)
    self.textView.setScrollEnabled_(True)

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
    text_view_attachment = './UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/text_view_attachment.imageset/Sunset_5.png'

    if (image := UIImage.alloc().initWithData_scale_(
        dataWithContentsOfURL(text_view_attachment), 1)):
      #textAttachment = NSTextAttachment.alloc().init()
      textAttachment = NSTextAttachment.new()
      textAttachment.image = image
      textAttachment.bounds = CGRect(CGPointMake(0.0, 0.0), image.size)
      textAttachmentString = NSAttributedString.attributedStringWithAttachment_(
        textAttachment)
      attributedText.appendAttributedString_(textAttachmentString)
      self.textView.attributedText = attributedText

    # When turned on, this changes the rendering scale of the text to match the standard text scaling and preserves the original font point sizes when the contents of the text view are copied to the pasteboard. Apps that show a lot of text content, such as a text viewer or editor, should turn this on and use the standard text scaling.
    # オンにすると、標準のテキスト スケーリングに一致するようにテキストのレンダリング スケールが変更され、テキスト ビューの内容がペーストボードにコピーされるときに元のフォント ポイント サイズが保持されます。テキスト ビューアやエディタなど、多くのテキスト コンテンツを表示するアプリでは、これをオンにして、標準のテキスト スケーリングを使用する必要があります。
    self.textView.usesStandardTextScaling = True
    # self.textView.setUsesStandardTextScaling_(True)

  # MARK: - Actions
  @objc_method
  def doneBarButtonItemClicked(self):
    # Dismiss the keyboard by removing it as the first responder.
    self.textView.resignFirstResponder()

    # todo: (独自実装) 全体実行と単体実行での場合分け
    if self.rightBarButtonItems is None:
      self.navigationItem.setRightBarButtonItem_animated_(None, True)
    else:
      self.navigationItem.setRightBarButtonItems_animated_([
        *self.rightBarButtonItems,
      ], True)

  # MARK: - UITextViewDelegate
  @objc_method
  def textViewDidBeginEditing_(self, textView):
    # Provide a "Done" button for the user to end text editing
    doneBarButtonItem = UIBarButtonItem.alloc(
    ).initWithBarButtonSystemItem_target_action_(
      UIBarButtonSystemItem.done, self, SEL('doneBarButtonItemClicked'))

    # todo: (独自実装) 全体実行と単体実行での場合分け
    self.rightBarButtonItems = rightBarButtonItems if (
      rightBarButtonItems := self.navigationItem.rightBarButtonItems
    ) is None else list(rightBarButtonItems)

    if self.rightBarButtonItems is None:
      self.navigationItem.setRightBarButtonItem_animated_(
        doneBarButtonItem, True)
    else:
      self.navigationItem.setRightBarButtonItems_animated_([
        *self.rightBarButtonItems,
        doneBarButtonItem,
      ], True)


if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import UIModalPresentationStyle

  main_vc = TextViewController.new()
  _title = NSStringFromClass(TextViewController)
  main_vc.navigationItem.title = _title

  #presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

