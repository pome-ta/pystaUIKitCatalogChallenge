'''
  note: Storyboard 実装なし
'''
import ctypes

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method, objc_const
from pyrubicon.objc.runtime import send_super, objc_id, load_library
from pyrubicon.objc.types import CGRectMake, CGSizeMake

from rbedge.functions import NSDirectionalEdgeInsetsMake

from rbedge.enumerations import (
  UILayoutConstraintAxis,
  NSTextAlignment,
  UITextBorderStyle,
  NSLineBreakMode,
  UIButtonType,
)

from rbedge import pdbr

UIKit = load_library('UIKit')
UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UIStackView = ObjCClass('UIStackView')

UILabel = ObjCClass('UILabel')
UIFont = ObjCClass('UIFont')
UITextField = ObjCClass('UITextField')
UIButton = ObjCClass('UIButton')
UIButtonConfiguration = ObjCClass('UIButtonConfiguration')
UIImage = ObjCClass('UIImage')

UIColor = ObjCClass('UIColor')

# --- Global Variables
UIFontTextStyleHeadline = objc_const(UIKit, 'UIFontTextStyleHeadline')
UIFontTextStyleBody = objc_const(UIKit, 'UIFontTextStyleBody')
UIFontTextStyleFootnote = objc_const(UIKit, 'UIFontTextStyleFootnote')
# --- Symbols
plusSymbol = UIImage.systemImageNamed('plus')
minusSymbol = UIImage.systemImageNamed('minus')


class StackViewController(UIViewController):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    #print('\tdealloc')
    pass

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    self.navigationItem.title = localizedString('StackViewsTitle') if (
      title := self.navigationItem.title) is None else title

    #self.view.backgroundColor = UIColor.systemBackgroundColor()
    self.view.backgroundColor = UIColor.systemIndigoColor()

    # xxx: あとで、`setup` 的なのを作る
    # --- showingHidingExampleStackView
    # --- --- showingHidingLabel
    showingHidingLabel = UILabel.new()
    showingHidingLabel.text = 'Showing/hiding views'
    showingHidingLabel.textAlignment = NSTextAlignment.center
    showingHidingLabel.setFont_(
      UIFont.preferredFontForTextStyle_(UIFontTextStyleHeadline))
    # xxx: 確認用
    showingHidingLabel.backgroundColor = UIColor.systemYellowColor()

    # --- --- / detailStackView
    # --- --- ---- detailLabel
    detailLabel = UILabel.new()
    detailLabel.setContentHuggingPriority_forAxis_(
      251.0, UILayoutConstraintAxis.horizontal)
    detailLabel.setContentHuggingPriority_forAxis_(
      251.0, UILayoutConstraintAxis.vertical)
    detailLabel.text = 'Detail'
    detailLabel.lineBreakMode = NSLineBreakMode.byTruncatingTail
    detailLabel.numberOfLines = 0
    detailLabel.setFont_(
      UIFont.preferredFontForTextStyle_(UIFontTextStyleBody))
    # todo: 確認用
    detailLabel.backgroundColor = UIColor.systemOrangeColor()

    # --- --- ---- detailTextField
    detailTextField = UITextField.new()
    detailTextField.setContentHuggingPriority_forAxis_(
      249.0, UILayoutConstraintAxis.horizontal)
    detailTextField.setFrame_(CGRectMake(301.5, 0.0, 41.5, 34.0))
    detailTextField.borderStyle = UITextBorderStyle.roundedRect
    detailTextField.setFont_(UIFont.systemFontOfSize_(14.0))
    detailTextField.font.systemMinimumFontSize = 17.0
    pdbr.state(detailTextField)

    # --- --- ---- detailPlusButton
    detailPlusButton = UIButton.buttonWithType_(UIButtonType.system)
    #detailPlusButton.setFrame_(CGRectMake(114.0, 0.0, 177.5, 34.0))
    _detailPlusButtonConfig = UIButtonConfiguration.plainButtonConfiguration()
    _detailPlusButtonConfig.image = plusSymbol
    _detailPlusButtonConfig.contentInsets = NSDirectionalEdgeInsetsMake(
      0.0, 10.0, 0.0, 10.0)
    detailPlusButton.configuration = _detailPlusButtonConfig
    # todo: 確認用
    detailPlusButton.backgroundColor = UIColor.systemBrownColor()

    # --- --- detailStackView
    detailStackView = UIStackView.alloc().initWithArrangedSubviews_([
      detailLabel,
      detailTextField,
      detailPlusButton,
    ])
    detailStackView.spacing = 10.0
    # todo: 確認用
    detailStackView.backgroundColor = UIColor.systemDarkRedColor()
    # --- --- detailStackView /

    # --- --- / furtherStackView
    # --- --- --- furtherlLabel
    furtherlLabel = UILabel.new()
    furtherlLabel.text = 'Further Detail'
    furtherlLabel.lineBreakMode = NSLineBreakMode.byTruncatingTail
    furtherlLabel.numberOfLines = 0
    furtherlLabel.setFont_(
      UIFont.preferredFontForTextStyle_(UIFontTextStyleBody))

    # --- --- --- furtherTextField
    furtherTextField = UITextField.new()
    furtherTextField.borderStyle = UITextBorderStyle.roundedRect
    furtherTextField.setFont_(UIFont.systemFontOfSize_(14.0))
    furtherTextField.font.systemMinimumFontSize = 17.0

    # --- --- --- furtherMinusButton
    furtherMinusButton = UIButton.buttonWithType_(UIButtonType.system)
    _furtherMinusButtonConfig = UIButtonConfiguration.plainButtonConfiguration(
    )
    _furtherMinusButtonConfig.image = minusSymbol
    furtherMinusButton.configuration = _furtherMinusButtonConfig
    # todo: 確認用
    furtherMinusButton.backgroundColor = UIColor.systemDarkPurpleColor()

    # --- --- furtherStackView
    furtherStackView = UIStackView.alloc().initWithArrangedSubviews_([
      furtherlLabel,
      furtherTextField,
      furtherMinusButton,
    ])
    furtherStackView.spacing = 10.0
    # todo: 確認用
    furtherStackView.backgroundColor = UIColor.systemCyanColor()
    # --- --- furtherStackView /

    footerLabel = UILabel.new()
    footerLabel.text = 'Footer Label'
    footerLabel.textAlignment = NSTextAlignment.center
    footerLabel.setFont_(
      UIFont.preferredFontForTextStyle_(UIFontTextStyleFootnote))

    # --- showingHidingExampleStackView

    showingHidingExampleStackView = UIStackView.alloc(
    ).initWithArrangedSubviews_([
      showingHidingLabel,
      detailStackView,
      furtherStackView,
      footerLabel,
    ])
    showingHidingExampleStackView.axis = UILayoutConstraintAxis.vertical
    showingHidingExampleStackView.spacing = 10.0
    # todo: 確認用
    showingHidingExampleStackView.backgroundColor = UIColor.systemGreenColor()

    self.view.addSubview_(showingHidingExampleStackView)
    # --- Layout
    showingHidingExampleStackView.translatesAutoresizingMaskIntoConstraints = False

    layoutMarginsGuide = self.view.layoutMarginsGuide
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide

    NSLayoutConstraint.activateConstraints_([
      showingHidingExampleStackView.leadingAnchor.constraintEqualToAnchor_(
        layoutMarginsGuide.leadingAnchor),
      showingHidingExampleStackView.trailingAnchor.constraintEqualToAnchor_(
        layoutMarginsGuide.trailingAnchor),
      showingHidingExampleStackView.topAnchor.
      constraintEqualToAnchor_constant_(safeAreaLayoutGuide.topAnchor, 8.0),
    ])

  @objc_method
  def viewDidAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print('viewDidAppear')
    #pdbr.state(self.view.subviews()[0].arrangedSubviews[1].arrangedSubviews)

  @objc_method
  def viewDidDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print('viewDidDisappear')

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'{__class__}: didReceiveMemoryWarning')


if __name__ == '__main__':
  from rbedge.functions import NSStringFromClass
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController

  main_vc = StackViewController.new()
  _title = NSStringFromClass(StackViewController)
  main_vc.navigationItem.title = _title

  presentation_style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, presentation_style)

