'''
  note: Storyboard 実装なし
  todo: 
    - 時々落ちる、稀に無限クラッシュ
    - 不要な呼び出しを整理
    - `viewDidLoad` 肥大化問題
'''
import ctypes

from pyrubicon.objc.api import ObjCClass, ObjCInstance, Block
from pyrubicon.objc.api import objc_method, objc_const
from pyrubicon.objc.runtime import send_super, objc_id, load_library, SEL
from pyrubicon.objc.types import CGRectMake, UIEdgeInsetsMake, NSTimeInterval

from rbedge.enumerations import (
  UILayoutConstraintAxis,
  NSTextAlignment,
  UITextBorderStyle,
  UIButtonType,
  UIControlState,
  UIControlEvents,
  NSLineBreakMode,
  UIStackViewAlignment,
  UIViewAnimationCurve,
)
from rbedge.functions import NSDirectionalEdgeInsetsMake
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

UIViewPropertyAnimator = ObjCClass('UIViewPropertyAnimator')

# --- Global Variables
UIFontTextStyleHeadline = objc_const(UIKit, 'UIFontTextStyleHeadline')
UIFontTextStyleBody = objc_const(UIKit, 'UIFontTextStyleBody')
UIFontTextStyleFootnote = objc_const(UIKit, 'UIFontTextStyleFootnote')


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

    self.view.backgroundColor = UIColor.systemBackgroundColor()
    #self.view.backgroundColor = UIColor.systemIndigoColor()

    # xxx: あとで、`setup` 的なのを作る？
    # --- Symbols
    plusSymbol = UIImage.systemImageNamed('plus')
    minusSymbol = UIImage.systemImageNamed('minus')

    touchUpInside = UIControlEvents.touchUpInside

    # --- showingHidingStackView
    showingHidingStackView = UIStackView.alloc()

    # --- --- showingHidingLabel
    showingHidingLabel = UILabel.new()
    showingHidingLabel.text = 'Showing/hiding views'
    showingHidingLabel.textAlignment = NSTextAlignment.center
    showingHidingLabel.setFont_(
      UIFont.preferredFontForTextStyle_(UIFontTextStyleHeadline))
    # xxx: 確認用
    #showingHidingLabel.backgroundColor = UIColor.systemYellowColor()

    # --- --- / detailStackView
    detailStackView = UIStackView.alloc()
    # --- --- ---- detailLabel
    detailLabel = UILabel.new()
    detailLabel.setContentHuggingPriority_forAxis_(
      251.0, UILayoutConstraintAxis.horizontal)
    detailLabel.setContentHuggingPriority_forAxis_(
      251.0, UILayoutConstraintAxis.vertical)
    detailLabel.text = 'Detail'
    detailLabel.lineBreakMode = NSLineBreakMode.byTruncatingTail
    detailLabel.setFont_(
      UIFont.preferredFontForTextStyle_(UIFontTextStyleBody))
    # todo: 確認用
    #detailLabel.backgroundColor = UIColor.systemOrangeColor()

    # --- --- ---- detailTextField
    detailTextField = UITextField.new()
    detailTextField.setContentHuggingPriority_forAxis_(
      249.0, UILayoutConstraintAxis.horizontal)
    detailTextField.borderStyle = UITextBorderStyle.roundedRect
    detailTextField.setFont_(UIFont.systemFontOfSize_(14.0))
    detailTextField.font.systemMinimumFontSize = 17.0

    # --- --- ---- detailPlusButton
    detailPlusButton = UIButton.buttonWithType_(UIButtonType.system)
    detailPlusButton.setImage_forState_(plusSymbol, UIControlState.normal)
    detailPlusButton.contentEdgeInsets = UIEdgeInsetsMake(0.0, 10.0, 0.0, 10.0)
    detailPlusButton.addTarget_action_forControlEvents_(
      self, SEL('showFurtherDetail:'), touchUpInside)
    # todo: 確認用
    #detailPlusButton.backgroundColor = UIColor.systemBrownColor()

    # --- --- arrangedSubviews
    detailStackView.initWithArrangedSubviews_([
      detailLabel,
      detailTextField,
      detailPlusButton,
    ])
    detailStackView.spacing = 10.0
    # todo: 確認用
    #detailStackView.backgroundColor = UIColor.systemDarkRedColor()
    # --- --- detailStackView /

    # --- --- / furtherStackView
    furtherStackView = UIStackView.alloc()
    # --- --- --- furtherlLabel
    furtherlLabel = UILabel.new()
    furtherlLabel.setContentHuggingPriority_forAxis_(
      251.0, UILayoutConstraintAxis.horizontal)
    furtherlLabel.setContentHuggingPriority_forAxis_(
      251.0, UILayoutConstraintAxis.vertical)
    furtherlLabel.text = 'Further Detail'
    furtherlLabel.lineBreakMode = NSLineBreakMode.byTruncatingTail
    furtherlLabel.setFont_(
      UIFont.preferredFontForTextStyle_(UIFontTextStyleBody))

    # --- --- --- furtherTextField
    furtherTextField = UITextField.new()
    furtherTextField.setContentHuggingPriority_forAxis_(
      249.0, UILayoutConstraintAxis.horizontal)
    furtherTextField.borderStyle = UITextBorderStyle.roundedRect
    furtherTextField.setFont_(UIFont.systemFontOfSize_(14.0))
    furtherTextField.font.systemMinimumFontSize = 17.0

    # --- --- --- furtherMinusButton
    furtherMinusButton = UIButton.buttonWithType_(UIButtonType.system)
    furtherMinusButton.setImage_forState_(minusSymbol, UIControlState.normal)
    furtherMinusButton.contentEdgeInsets = UIEdgeInsetsMake(
      0.0, 10.0, 0.0, 10.0)
    # todo: 確認用
    #furtherMinusButton.backgroundColor = UIColor.systemDarkPurpleColor()

    # --- --- arrangedSubviews
    furtherStackView.initWithArrangedSubviews_([
      furtherlLabel,
      furtherTextField,
      furtherMinusButton,
    ])
    furtherStackView.spacing = 10.0
    # todo: 確認用
    #furtherStackView.backgroundColor = UIColor.systemCyanColor()
    # --- --- furtherStackView /

    footerLabel = UILabel.new()
    footerLabel.text = 'Footer Label'
    footerLabel.textAlignment = NSTextAlignment.center
    footerLabel.setFont_(
      UIFont.preferredFontForTextStyle_(UIFontTextStyleFootnote))

    # --- --- arrangedSubviews
    showingHidingStackView.initWithArrangedSubviews_([
      showingHidingLabel,
      detailStackView,
      furtherStackView,
      footerLabel,
    ])
    showingHidingStackView.axis = UILayoutConstraintAxis.vertical
    showingHidingStackView.spacing = 10.0
    # todo: 確認用
    #showingHidingStackView.backgroundColor = UIColor.systemGreenColor()

    # --- addRemoveStackView
    addRemoveStackView = UIStackView.alloc()
    # --- --- ---- addRemoveLabel
    addRemoveLabel = UILabel.new()
    addRemoveLabel.setContentHuggingPriority_forAxis_(
      251.0, UILayoutConstraintAxis.horizontal)
    addRemoveLabel.setContentHuggingPriority_forAxis_(
      251.0, UILayoutConstraintAxis.vertical)
    addRemoveLabel.text = 'Add/remove views'
    addRemoveLabel.textAlignment = NSTextAlignment.center
    addRemoveLabel.setFont_(
      UIFont.preferredFontForTextStyle_(UIFontTextStyleHeadline))
    # todo: 確認用
    #addRemoveLabel.backgroundColor = UIColor.systemOrangeColor()

    # --- --- ---- addbutton
    addbutton = UIButton.buttonWithType_(UIButtonType.system)
    addbutton.setImage_forState_(plusSymbol, UIControlState.normal)
    addbutton.setContentHuggingPriority_forAxis_(
      252.0, UILayoutConstraintAxis.horizontal)
    addbutton.contentEdgeInsets = UIEdgeInsetsMake(10.0, 10.0, 10.0, 10.0)
    # todo: 確認用
    #addbutton.backgroundColor = UIColor.systemDarkPurpleColor()

    # --- --- ---- removebutton
    removebutton = UIButton.buttonWithType_(UIButtonType.system)
    removebutton.setImage_forState_(minusSymbol, UIControlState.normal)
    removebutton.setContentHuggingPriority_forAxis_(
      253.0, UILayoutConstraintAxis.horizontal)
    removebutton.contentEdgeInsets = UIEdgeInsetsMake(10.0, 10.0, 10.0, 10.0)
    # todo: 確認用
    #removebutton.backgroundColor = UIColor.systemBrownColor()

    # --- --- arrangedSubviews
    addRemoveStackView.initWithArrangedSubviews_([
      addRemoveLabel,
      addbutton,
      removebutton,
    ])
    # xxx: 確認用
    #addRemoveStackView.backgroundColor = UIColor.systemYellowColor()

    # --- addRemoveExampleStackView
    addRemoveExampleStackView = UIStackView.new()
    addRemoveExampleStackView.axis = UILayoutConstraintAxis.vertical
    addRemoveExampleStackView.alignment = UIStackViewAlignment.center
    addRemoveExampleStackView.spacing = 10.0
    # todo: 確認用
    addRemoveExampleStackView.backgroundColor = UIColor.systemGreenColor()

    self.view.addSubview_(showingHidingStackView)
    self.view.addSubview_(addRemoveStackView)
    self.view.addSubview_(addRemoveExampleStackView)

    # --- Layout
    showingHidingStackView.translatesAutoresizingMaskIntoConstraints = False
    addRemoveStackView.translatesAutoresizingMaskIntoConstraints = False
    addRemoveExampleStackView.translatesAutoresizingMaskIntoConstraints = False

    layoutMarginsGuide = self.view.layoutMarginsGuide
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide

    # --- showingHidingStackView
    NSLayoutConstraint.activateConstraints_([
      showingHidingStackView.leadingAnchor.constraintEqualToAnchor_(
        layoutMarginsGuide.leadingAnchor),
      showingHidingStackView.trailingAnchor.constraintEqualToAnchor_(
        layoutMarginsGuide.trailingAnchor),
      showingHidingStackView.topAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.topAnchor, 8.0),
    ])

    # todo: `detailLabel` と`furtherlLabel` の幅を連動
    NSLayoutConstraint.activateConstraints_([
      detailLabel.widthAnchor.constraintEqualToAnchor_(
        furtherlLabel.widthAnchor),
    ])

    # --- addRemoveStackView
    NSLayoutConstraint.activateConstraints_([
      addRemoveStackView.topAnchor.constraintEqualToAnchor_constant_(
        showingHidingStackView.bottomAnchor, 20.0),
      addRemoveStackView.leadingAnchor.constraintEqualToAnchor_(
        layoutMarginsGuide.leadingAnchor),
      addRemoveStackView.trailingAnchor.constraintEqualToAnchor_(
        layoutMarginsGuide.trailingAnchor),
    ])

    # --- addRemoveExampleStackView
    NSLayoutConstraint.activateConstraints_([
      addRemoveExampleStackView.topAnchor.constraintEqualToAnchor_constant_(
        addRemoveStackView.bottomAnchor, 8.0),
      addRemoveExampleStackView.leadingAnchor.constraintEqualToAnchor_(
        layoutMarginsGuide.leadingAnchor),
      addRemoveExampleStackView.trailingAnchor.constraintEqualToAnchor_(
        layoutMarginsGuide.trailingAnchor),
      #addRemoveExampleStackView.heightAnchor.constraintEqualToConstant_(42.0),
    ])

    self.plusButton = detailPlusButton
    self.furtherDetailStackView = furtherStackView
    self.addRemoveExampleStackView = addRemoveExampleStackView
    self.addArrangedViewButton = addbutton
    self.removeArrangedViewButton = removebutton

    self.maximumArrangedSubviewCount = 3

  # MARK: - View Life Cycle
  @objc_method
  def viewWillAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    self.furtherDetailStackView.setHidden_(True)
    self.plusButton.setHidden_(False)
    self.updateAddRemoveButtons()

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

  # MARK: - Actions
  @objc_method
  def showFurtherDetail_(self, _):
    # Animate the changes by performing them in a `UIViewPropertyAnimator` animation block.

    @Block
    def animationsBlock() -> None:
      # Reveal the further details stack view and hide the plus button.
      self.furtherDetailStackView.setHidden_(False)
      self.plusButton.setHidden_(True)

    showDetailAnimator = UIViewPropertyAnimator.alloc(
    ).initWithDuration_curve_animations_(NSTimeInterval(0.25),
                                         UIViewAnimationCurve.easeIn,
                                         animationsBlock)
    showDetailAnimator.startAnimation()
    

  # MARK: - Convenience
  @objc_method
  def updateAddRemoveButtons(self):
    arrangedSubviewCount = len(self.addRemoveExampleStackView.arrangedSubviews)
    self.addArrangedViewButton.setEnabled_(
      arrangedSubviewCount < self.maximumArrangedSubviewCount)
    self.removeArrangedViewButton.setEnabled_(arrangedSubviewCount > 0)


if __name__ == '__main__':
  from rbedge.functions import NSStringFromClass
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController

  main_vc = StackViewController.new()
  _title = NSStringFromClass(StackViewController)
  main_vc.navigationItem.title = _title

  presentation_style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, presentation_style)

