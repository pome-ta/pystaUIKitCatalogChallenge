from dataclasses import dataclass

from pyrubicon.objc.api import objc_const
from pyrubicon.objc.runtime import load_library

UIKit = load_library('UIKit')

# xxx: PEP8では非推奨
constUIKit = lambda const_name: objc_const(UIKit, const_name)


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
  pass
  
