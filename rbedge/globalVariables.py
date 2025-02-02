from dataclasses import dataclass

from pyrubicon.objc.api import objc_const
from pyrubicon.objc.runtime import load_library

UIKit = load_library('UIKit')

# xxx: PEP8では非推奨
constUIKit = lambda const_name: str(objc_const(UIKit, const_name))

UITextFieldTextDidChangeNotification = constUIKit(
  'UITextFieldTextDidChangeNotification')

UIKeyboardAnimationDurationUserInfoKey = constUIKit(
  'UIKeyboardAnimationDurationUserInfoKey')
UIKeyboardFrameBeginUserInfoKey = constUIKit('UIKeyboardFrameBeginUserInfoKey')
UIKeyboardFrameEndUserInfoKey = constUIKit('UIKeyboardFrameEndUserInfoKey')

UICollectionElementKindSectionHeader = constUIKit('UICollectionElementKindSectionHeader')

#print()

# ref: [UIFontTextStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uifont/textstyle?language=objc)
@dataclass
class UIFontTextStyle:
  body: str = constUIKit('UIFontTextStyleBody')
  callout: str = constUIKit('UIFontTextStyleCallout')
  caption1: str = constUIKit('UIFontTextStyleCaption1')
  caption2: str = constUIKit('UIFontTextStyleCaption2')
  footnote: str = constUIKit('UIFontTextStyleFootnote')
  headline: str = constUIKit('UIFontTextStyleHeadline')
  subheadline: str = constUIKit('UIFontTextStyleSubheadline')
  largeTitle: str = constUIKit('UIFontTextStyleLargeTitle')
  extraLargeTitle: str = constUIKit('UIFontTextStyleExtraLargeTitle')
  extraLargeTitle2: str = constUIKit('UIFontTextStyleExtraLargeTitle2')
  title1: str = constUIKit('UIFontTextStyleTitle1')
  title2: str = constUIKit('UIFontTextStyleTitle2')
  title3: str = constUIKit('UIFontTextStyleTitle3')


# ref: [NSAttributedStringKey | Apple Developer Documentation](https://developer.apple.com/documentation/foundation/nsattributedstringkey?language=objc)
@dataclass
class NSAttributedStringKey:
  backgroundColor: str = constUIKit('NSBackgroundColorAttributeName')
  baselineOffset: str = constUIKit('NSBaselineOffsetAttributeName')
  font: str = constUIKit('NSFontAttributeName')
  foregroundColor: str = constUIKit('NSForegroundColorAttributeName')
  glyphInfo: str = constUIKit('NSGlyphInfoAttributeName')
  kern: str = constUIKit('NSKernAttributeName')
  ligature: str = constUIKit('NSLigatureAttributeName')
  paragraphStyle: str = constUIKit('NSParagraphStyleAttributeName')
  strikethroughColor: str = constUIKit('NSStrikethroughColorAttributeName')
  strikethroughStyle: str = constUIKit('NSStrikethroughStyleAttributeName')
  strokeColor: str = constUIKit('NSStrokeColorAttributeName')
  strokeWidth: str = constUIKit('NSStrokeWidthAttributeName')
  superscript: str = constUIKit('NSSuperscriptAttributeName')
  tracking: str = constUIKit('NSTrackingAttributeName')
  underlineColor: str = constUIKit('NSUnderlineColorAttributeName')
  underlineStyle: str = constUIKit('NSUnderlineStyleAttributeName')
  writingDirection: str = constUIKit('NSWritingDirectionAttributeName')
  cursor: str = constUIKit('NSCursorAttributeName')
  link: str = constUIKit('NSLinkAttributeName')
  markedClauseSegment: str = constUIKit('NSMarkedClauseSegmentAttributeName')
  replacementIndex: str = constUIKit('NSReplacementIndexAttributeName')
  shadow: str = constUIKit('NSShadowAttributeName')
  spellingState: str = constUIKit('NSSpellingStateAttributeName')
  #suggestionHighlight: str = constUIKit('CSSuggestionHighlightAttributeName')
  textAlternatives: str = constUIKit('NSTextAlternativesAttributeName')
  textEffect: str = constUIKit('NSTextEffectAttributeName')
  #textHighlightColorScheme: str = constUIKit('NSTextHighlightColorSchemeAttributeName')
  #textHighlightStyle: str = constUIKit('NSTextHighlightStyleAttributeName')
  textItemTag: str = constUIKit('UITextItemTagAttributeName')
  toolTip: str = constUIKit('NSToolTipAttributeName')
  #adaptiveImageGlyph: str = constUIKit('NSAdaptiveImageGlyphAttributeName')
  attachment: str = constUIKit('NSAttachmentAttributeName')
  #accessibilityAlignment: str = constUIKit('NSAccessibilityTextAlignmentAttribute')
  #accessibilityAnnotationTextAttribute: str = constUIKit('NSAccessibilityAnnotationTextAttribute')
  #accessibilityAttachment: str = constUIKit('NSAccessibilityAttachmentTextAttribute')
  #accessibilityAutocorrected: str = constUIKit('NSAccessibilityAutocorrectedTextAttribute')
  #accessibilityBackgroundColor: str = constUIKit('NSAccessibilityBackgroundColorTextAttribute')
  #accessibilityCustomText: str = constUIKit('NSAccessibilityCustomTextAttribute')
  #accessibilityFont: str = constUIKit('NSAccessibilityFontTextAttribute')
  #accessibilityForegroundColor: str = constUIKit('NSAccessibilityForegroundColorTextAttribute')
  #accessibilityLanguage: str = constUIKit('NSAccessibilityLanguageTextAttribute')
  #accessibilityLink: str = constUIKit('NSAccessibilityLinkTextAttribute')
  #accessibilityListItemIndex: str = constUIKit('NSAccessibilityListItemIndexTextAttribute')
  #accessibilityListItemLevel: str = constUIKit('NSAccessibilityListItemLevelTextAttribute')
  #accessibilityListItemPrefix: str = constUIKit('NSAccessibilityListItemPrefixTextAttribute')
  #accessibilityMarkedMisspelled: str = constUIKit('NSAccessibilityMarkedMisspelledTextAttribute')
  #accessibilityMisspelled: str = constUIKit('NSAccessibilityMisspelledTextAttribute')
  #accessibilityShadow: str = constUIKit('NSAccessibilityShadowTextAttribute')
  accessibilitySpeechAnnouncementPriority: str = constUIKit(
    'UIAccessibilitySpeechAttributeAnnouncementPriority')
  accessibilitySpeechIPANotation: str = constUIKit(
    'UIAccessibilitySpeechAttributeIPANotation')
  accessibilitySpeechLanguage: str = constUIKit(
    'UIAccessibilitySpeechAttributeLanguage')
  accessibilitySpeechPitch: str = constUIKit(
    'UIAccessibilitySpeechAttributePitch')
  accessibilitySpeechPunctuation: str = constUIKit(
    'UIAccessibilitySpeechAttributePunctuation')
  accessibilitySpeechQueueAnnouncement: str = constUIKit(
    'UIAccessibilitySpeechAttributeQueueAnnouncement')
  accessibilitySpeechSpellOut: str = constUIKit(
    'UIAccessibilitySpeechAttributeSpellOut')
  accessibilityTextCustom: str = constUIKit(
    'UIAccessibilityTextAttributeCustom')
  accessibilityTextHeadingLevel: str = constUIKit(
    'UIAccessibilityTextAttributeHeadingLevel')
  #accessibilityStrikethrough: str = constUIKit('NSAccessibilityStrikethroughTextAttribute')
  #accessibilityStrikethroughColor: str = constUIKit('NSAccessibilityStrikethroughColorTextAttribute')
  #accessibilitySuperscript: str = constUIKit('NSAccessibilitySuperscriptTextAttribute')
  #accessibilityUnderline: str = constUIKit('NSAccessibilityUnderlineTextAttribute')
  #accessibilityUnderlineColor: str = constUIKit('NSAccessibilityUnderlineColorTextAttribute')
  UIAccessibilityTextAttributeContext: str = constUIKit(
    'UIAccessibilityTextAttributeContext')
  inlinePresentationIntent: str = constUIKit(
    'NSInlinePresentationIntentAttributeName')
  presentationIntentAttributeName: str = constUIKit(
    'NSPresentationIntentAttributeName')
  markdownSourcePosition: str = constUIKit(
    'NSMarkdownSourcePositionAttributeName')
  alternateDescription: str = constUIKit('NSAlternateDescriptionAttributeName')
  imageURL: str = constUIKit('NSImageURLAttributeName')
  languageIdentifier: str = constUIKit('NSLanguageIdentifierAttributeName')
  morphology: str = constUIKit('NSMorphologyAttributeName')
  inflectionRule: str = constUIKit('NSInflectionRuleAttributeName')
  inflectionAlternative: str = constUIKit(
    'NSInflectionAlternativeAttributeName')
  agreeWithArgument: str = constUIKit(
    'NSInflectionAgreementArgumentAttributeName')
  agreeWithConcept: str = constUIKit(
    'NSInflectionAgreementConceptAttributeName')
  referentConcept: str = constUIKit('NSInflectionReferentConceptAttributeName')
  #localizedNumberFormat: str = constUIKit('NSLocalizedNumberFormatAttributeName')
  expansion: str = constUIKit('NSExpansionAttributeName')
  obliqueness: str = constUIKit('NSObliquenessAttributeName')
  verticalGlyphForm: str = constUIKit('NSVerticalGlyphFormAttributeName')
  characterShapeAttributeName: str = constUIKit(
    'NSCharacterShapeAttributeName')
  #usesScreenFontsDocumentAttribute: str = constUIKit('NSUsesScreenFontsDocumentAttribute')


# ref: [NSNotificationName | Apple Developer Documentation](https://developer.apple.com/documentation/foundation/nsnotificationname?language=objc)
@dataclass
class NSNotificationName:
  keyboardWillShowNotification: str = constUIKit(
    'UIKeyboardWillShowNotification')
  keyboardWillHideNotification: str = constUIKit(
    'UIKeyboardWillHideNotification')


# ref: [UIImagePickerControllerInfoKey | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey?language=objc)
@dataclass
class UIImagePickerControllerInfoKey:
  originalImage: str = constUIKit('UIImagePickerControllerOriginalImage')

