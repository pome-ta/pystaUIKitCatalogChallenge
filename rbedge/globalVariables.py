from dataclasses import dataclass

from pyrubicon.objc.api import objc_const
from pyrubicon.objc.runtime import load_library
from pyrubicon.objc.collections import ObjCStrInstance

UIKit = load_library('UIKit')

# xxx: PEP8では非推奨
constUIKit = lambda const_name: objc_const(UIKit, const_name)

UITextFieldTextDidChangeNotification = constUIKit(
  'UITextFieldTextDidChangeNotification')

UIKeyboardAnimationDurationUserInfoKey = constUIKit(
  'UIKeyboardAnimationDurationUserInfoKey')
UIKeyboardFrameBeginUserInfoKey = constUIKit('UIKeyboardFrameBeginUserInfoKey')
UIKeyboardFrameEndUserInfoKey = constUIKit('UIKeyboardFrameEndUserInfoKey')

UICollectionElementKindSectionHeader = constUIKit(
  'UICollectionElementKindSectionHeader')


# ref: [UIFontTextStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uifont/textstyle?language=objc)
@dataclass
class UIFontTextStyle:
  body: ObjCStrInstance = constUIKit('UIFontTextStyleBody')
  callout: ObjCStrInstance = constUIKit('UIFontTextStyleCallout')
  caption1: ObjCStrInstance = constUIKit('UIFontTextStyleCaption1')
  caption2: ObjCStrInstance = constUIKit('UIFontTextStyleCaption2')
  footnote: ObjCStrInstance = constUIKit('UIFontTextStyleFootnote')
  headline: ObjCStrInstance = constUIKit('UIFontTextStyleHeadline')
  subheadline: ObjCStrInstance = constUIKit('UIFontTextStyleSubheadline')
  largeTitle: ObjCStrInstance = constUIKit('UIFontTextStyleLargeTitle')
  extraLargeTitle: ObjCStrInstance = constUIKit(
    'UIFontTextStyleExtraLargeTitle')
  extraLargeTitle2: ObjCStrInstance = constUIKit(
    'UIFontTextStyleExtraLargeTitle2')
  title1: ObjCStrInstance = constUIKit('UIFontTextStyleTitle1')
  title2: ObjCStrInstance = constUIKit('UIFontTextStyleTitle2')
  title3: ObjCStrInstance = constUIKit('UIFontTextStyleTitle3')


# ref: [NSAttributedStringKey | Apple Developer Documentation](https://developer.apple.com/documentation/foundation/nsattributedstringkey?language=objc)
@dataclass
class NSAttributedStringKey:
  backgroundColor: ObjCStrInstance = constUIKit(
    'NSBackgroundColorAttributeName')
  baselineOffset: ObjCStrInstance = constUIKit('NSBaselineOffsetAttributeName')
  font: ObjCStrInstance = constUIKit('NSFontAttributeName')
  foregroundColor: ObjCStrInstance = constUIKit(
    'NSForegroundColorAttributeName')
  glyphInfo: ObjCStrInstance = constUIKit('NSGlyphInfoAttributeName')
  kern: ObjCStrInstance = constUIKit('NSKernAttributeName')
  ligature: ObjCStrInstance = constUIKit('NSLigatureAttributeName')
  paragraphStyle: ObjCStrInstance = constUIKit('NSParagraphStyleAttributeName')
  strikethroughColor: ObjCStrInstance = constUIKit(
    'NSStrikethroughColorAttributeName')
  strikethroughStyle: ObjCStrInstance = constUIKit(
    'NSStrikethroughStyleAttributeName')
  strokeColor: ObjCStrInstance = constUIKit('NSStrokeColorAttributeName')
  strokeWidth: ObjCStrInstance = constUIKit('NSStrokeWidthAttributeName')
  superscript: ObjCStrInstance = constUIKit('NSSuperscriptAttributeName')
  tracking: ObjCStrInstance = constUIKit('NSTrackingAttributeName')
  underlineColor: ObjCStrInstance = constUIKit('NSUnderlineColorAttributeName')
  underlineStyle: ObjCStrInstance = constUIKit('NSUnderlineStyleAttributeName')
  writingDirection: ObjCStrInstance = constUIKit(
    'NSWritingDirectionAttributeName')
  cursor: ObjCStrInstance = constUIKit('NSCursorAttributeName')
  link: ObjCStrInstance = constUIKit('NSLinkAttributeName')
  markedClauseSegment: ObjCStrInstance = constUIKit(
    'NSMarkedClauseSegmentAttributeName')
  replacementIndex: ObjCStrInstance = constUIKit(
    'NSReplacementIndexAttributeName')
  shadow: ObjCStrInstance = constUIKit('NSShadowAttributeName')
  spellingState: ObjCStrInstance = constUIKit('NSSpellingStateAttributeName')
  #suggestionHighlight: ObjCStrInstance = constUIKit('CSSuggestionHighlightAttributeName')
  textAlternatives: ObjCStrInstance = constUIKit(
    'NSTextAlternativesAttributeName')
  textEffect: ObjCStrInstance = constUIKit('NSTextEffectAttributeName')
  #textHighlightColorScheme: ObjCStrInstance = constUIKit('NSTextHighlightColorSchemeAttributeName')
  #textHighlightStyle: ObjCStrInstance = constUIKit('NSTextHighlightStyleAttributeName')
  textItemTag: ObjCStrInstance = constUIKit('UITextItemTagAttributeName')
  toolTip: ObjCStrInstance = constUIKit('NSToolTipAttributeName')
  #adaptiveImageGlyph: ObjCStrInstance = constUIKit('NSAdaptiveImageGlyphAttributeName')
  attachment: ObjCStrInstance = constUIKit('NSAttachmentAttributeName')
  #accessibilityAlignment: ObjCStrInstance = constUIKit('NSAccessibilityTextAlignmentAttribute')
  #accessibilityAnnotationTextAttribute: ObjCStrInstance = constUIKit('NSAccessibilityAnnotationTextAttribute')
  #accessibilityAttachment: ObjCStrInstance = constUIKit('NSAccessibilityAttachmentTextAttribute')
  #accessibilityAutocorrected: ObjCStrInstance = constUIKit('NSAccessibilityAutocorrectedTextAttribute')
  #accessibilityBackgroundColor: ObjCStrInstance = constUIKit('NSAccessibilityBackgroundColorTextAttribute')
  #accessibilityCustomText: ObjCStrInstance = constUIKit('NSAccessibilityCustomTextAttribute')
  #accessibilityFont: ObjCStrInstance = constUIKit('NSAccessibilityFontTextAttribute')
  #accessibilityForegroundColor: ObjCStrInstance = constUIKit('NSAccessibilityForegroundColorTextAttribute')
  #accessibilityLanguage: ObjCStrInstance = constUIKit('NSAccessibilityLanguageTextAttribute')
  #accessibilityLink: ObjCStrInstance = constUIKit('NSAccessibilityLinkTextAttribute')
  #accessibilityListItemIndex: ObjCStrInstance = constUIKit('NSAccessibilityListItemIndexTextAttribute')
  #accessibilityListItemLevel: ObjCStrInstance = constUIKit('NSAccessibilityListItemLevelTextAttribute')
  #accessibilityListItemPrefix: ObjCStrInstance = constUIKit('NSAccessibilityListItemPrefixTextAttribute')
  #accessibilityMarkedMisspelled: ObjCStrInstance = constUIKit('NSAccessibilityMarkedMisspelledTextAttribute')
  #accessibilityMisspelled: ObjCStrInstance = constUIKit('NSAccessibilityMisspelledTextAttribute')
  #accessibilityShadow: ObjCStrInstance = constUIKit('NSAccessibilityShadowTextAttribute')
  accessibilitySpeechAnnouncementPriority: ObjCStrInstance = constUIKit(
    'UIAccessibilitySpeechAttributeAnnouncementPriority')
  accessibilitySpeechIPANotation: ObjCStrInstance = constUIKit(
    'UIAccessibilitySpeechAttributeIPANotation')
  accessibilitySpeechLanguage: ObjCStrInstance = constUIKit(
    'UIAccessibilitySpeechAttributeLanguage')
  accessibilitySpeechPitch: ObjCStrInstance = constUIKit(
    'UIAccessibilitySpeechAttributePitch')
  accessibilitySpeechPunctuation: ObjCStrInstance = constUIKit(
    'UIAccessibilitySpeechAttributePunctuation')
  accessibilitySpeechQueueAnnouncement: ObjCStrInstance = constUIKit(
    'UIAccessibilitySpeechAttributeQueueAnnouncement')
  accessibilitySpeechSpellOut: ObjCStrInstance = constUIKit(
    'UIAccessibilitySpeechAttributeSpellOut')
  accessibilityTextCustom: ObjCStrInstance = constUIKit(
    'UIAccessibilityTextAttributeCustom')
  accessibilityTextHeadingLevel: ObjCStrInstance = constUIKit(
    'UIAccessibilityTextAttributeHeadingLevel')
  #accessibilityStrikethrough: ObjCStrInstance = constUIKit('NSAccessibilityStrikethroughTextAttribute')
  #accessibilityStrikethroughColor: ObjCStrInstance = constUIKit('NSAccessibilityStrikethroughColorTextAttribute')
  #accessibilitySuperscript: ObjCStrInstance = constUIKit('NSAccessibilitySuperscriptTextAttribute')
  #accessibilityUnderline: ObjCStrInstance = constUIKit('NSAccessibilityUnderlineTextAttribute')
  #accessibilityUnderlineColor: ObjCStrInstance = constUIKit('NSAccessibilityUnderlineColorTextAttribute')
  UIAccessibilityTextAttributeContext: ObjCStrInstance = constUIKit(
    'UIAccessibilityTextAttributeContext')
  inlinePresentationIntent: ObjCStrInstance = constUIKit(
    'NSInlinePresentationIntentAttributeName')
  presentationIntentAttributeName: ObjCStrInstance = constUIKit(
    'NSPresentationIntentAttributeName')
  markdownSourcePosition: ObjCStrInstance = constUIKit(
    'NSMarkdownSourcePositionAttributeName')
  alternateDescription: ObjCStrInstance = constUIKit(
    'NSAlternateDescriptionAttributeName')
  imageURL: ObjCStrInstance = constUIKit('NSImageURLAttributeName')
  languageIdentifier: ObjCStrInstance = constUIKit(
    'NSLanguageIdentifierAttributeName')
  morphology: ObjCStrInstance = constUIKit('NSMorphologyAttributeName')
  inflectionRule: ObjCStrInstance = constUIKit('NSInflectionRuleAttributeName')
  inflectionAlternative: ObjCStrInstance = constUIKit(
    'NSInflectionAlternativeAttributeName')
  agreeWithArgument: ObjCStrInstance = constUIKit(
    'NSInflectionAgreementArgumentAttributeName')
  agreeWithConcept: ObjCStrInstance = constUIKit(
    'NSInflectionAgreementConceptAttributeName')
  referentConcept: ObjCStrInstance = constUIKit(
    'NSInflectionReferentConceptAttributeName')
  #localizedNumberFormat: ObjCStrInstance = constUIKit('NSLocalizedNumberFormatAttributeName')
  expansion: ObjCStrInstance = constUIKit('NSExpansionAttributeName')
  obliqueness: ObjCStrInstance = constUIKit('NSObliquenessAttributeName')
  verticalGlyphForm: ObjCStrInstance = constUIKit(
    'NSVerticalGlyphFormAttributeName')
  characterShapeAttributeName: ObjCStrInstance = constUIKit(
    'NSCharacterShapeAttributeName')
  #usesScreenFontsDocumentAttribute: ObjCStrInstance = constUIKit('NSUsesScreenFontsDocumentAttribute')


# ref: [NSNotificationName | Apple Developer Documentation](https://developer.apple.com/documentation/foundation/nsnotificationname?language=objc)
@dataclass
class NSNotificationName:
  keyboardWillShowNotification: ObjCStrInstance = constUIKit(
    'UIKeyboardWillShowNotification')
  keyboardWillHideNotification: ObjCStrInstance = constUIKit(
    'UIKeyboardWillHideNotification')


# ref: [UIImagePickerControllerInfoKey | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey?language=objc)
@dataclass
class UIImagePickerControllerInfoKey:
  originalImage: ObjCStrInstance = constUIKit(
    'UIImagePickerControllerOriginalImage')

