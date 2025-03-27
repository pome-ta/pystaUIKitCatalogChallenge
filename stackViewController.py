"""
  note: Storyboard 実装なし
"""
import ctypes

from pyrubicon.objc.api import ObjCClass, Block
from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.runtime import send_super, SEL
from pyrubicon.objc.types import CGRect, CGRectMake, CGSizeMake, NSZeroPoint, UIEdgeInsetsMake, NSTimeInterval

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

from rbedge.globalVariables import (
  UIFontTextStyle, )

from rbedge.functions import arc4random_uniform
from rbedge.functions import NSStringFromClass
from rbedge import pdbr

from pyLocalizedString import localizedString

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
UIView = ObjCClass('UIView')


class StackViewController(UIViewController):

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def loadView(self):
    send_super(__class__, self, 'loadView')
    #print(f'\t{NSStringFromClass(__class__)}: loadView')

  @objc_method
  def setupFurtherDetailStackView(self):
    pass

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    self.navigationItem.title = localizedString('StackViewsTitle') if (
      title := self.navigationItem.title) is None else title
    self.view.backgroundColor = UIColor.systemBackgroundColor()

    # xxx: あとで、`setup` 的なのを作る?
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
      UIFont.preferredFontForTextStyle_(UIFontTextStyle.headline))
      
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
      UIFont.preferredFontForTextStyle_(UIFontTextStyle.body))
    
    # --- --- ---- detailTextField
    detailTextField = UITextField.new()
    detailTextField.setContentHuggingPriority_forAxis_(
      249.0, UILayoutConstraintAxis.horizontal)

    #detailTextField.borderStyle = UITextBorderStyle.roundedRect
    detailTextField.setBorderStyle_(UITextBorderStyle.roundedRect)
    detailTextField.setFont_(UIFont.systemFontOfSize_(14.0))
    #detailTextField.font.systemMinimumFontSize = 17.0
    #pdbr.state(detailTextField.font, 1)
    
    # --- --- arrangedSubviews
    detailStackView.initWithArrangedSubviews_([
      detailLabel,
      detailTextField,
    ])
    detailStackView.spacing = 10.0


    # --- --- arrangedSubviews
    showingHidingStackView.initWithArrangedSubviews_([
      showingHidingLabel,
      detailStackView,
    ])
    showingHidingStackView.axis = UILayoutConstraintAxis.vertical
    showingHidingStackView.spacing = 10.0

    # --- Layout

    self.view.addSubview_(showingHidingStackView)

    showingHidingStackView.translatesAutoresizingMaskIntoConstraints = False

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

  @objc_method
  def viewWillAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])

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

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'\t{NSStringFromClass(__class__)}: didReceiveMemoryWarning')


'''
class StackViewController(UIViewController):

  furtherDetailStackView: UIStackView = objc_property()
  plusButton: UIButton = objc_property()
  addRemoveExampleStackView: UIStackView = objc_property()
  addArrangedViewButton: UIButton = objc_property()
  removeArrangedViewButton: UIButton = objc_property()

  maximumArrangedSubviewCount: int = objc_property(int)

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def loadView(self):
    send_super(__class__, self, 'loadView')
    #print(f'\t{NSStringFromClass(__class__)}: loadView')
    self.maximumArrangedSubviewCount = 3

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    self.navigationItem.title = localizedString('StackViewsTitle') if (
      title := self.navigationItem.title) is None else title

    self.view.backgroundColor = UIColor.systemBackgroundColor()

    # xxx: あとで、`setup` 的なのを作る?
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
      UIFont.preferredFontForTextStyle_(UIFontTextStyle.headline))

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
      UIFont.preferredFontForTextStyle_(UIFontTextStyle.body))

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

    # --- --- arrangedSubviews
    detailStackView.initWithArrangedSubviews_([
      detailLabel,
      detailTextField,
      detailPlusButton,
    ])
    detailStackView.spacing = 10.0
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
      UIFont.preferredFontForTextStyle_(UIFontTextStyle.body))

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
    furtherMinusButton.addTarget_action_forControlEvents_(
      self, SEL('hideFurtherDetail:'), touchUpInside)

    # --- --- arrangedSubviews
    furtherStackView.initWithArrangedSubviews_([
      furtherlLabel,
      furtherTextField,
      furtherMinusButton,
    ])
    furtherStackView.spacing = 10.0
    # --- --- furtherStackView /

    footerLabel = UILabel.new()
    footerLabel.text = 'Footer Label'
    footerLabel.textAlignment = NSTextAlignment.center
    footerLabel.setFont_(
      UIFont.preferredFontForTextStyle_(UIFontTextStyle.footnote))

    # --- --- arrangedSubviews
    showingHidingStackView.initWithArrangedSubviews_([
      showingHidingLabel,
      detailStackView,
      furtherStackView,
      footerLabel,
    ])
    showingHidingStackView.axis = UILayoutConstraintAxis.vertical
    showingHidingStackView.spacing = 10.0

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
      UIFont.preferredFontForTextStyle_(UIFontTextStyle.headline))

    # --- --- ---- addbutton
    addbutton = UIButton.buttonWithType_(UIButtonType.system)
    addbutton.setImage_forState_(plusSymbol, UIControlState.normal)
    addbutton.setContentHuggingPriority_forAxis_(
      252.0, UILayoutConstraintAxis.horizontal)
    addbutton.contentEdgeInsets = UIEdgeInsetsMake(10.0, 10.0, 10.0, 10.0)
    addbutton.addTarget_action_forControlEvents_(
      self, SEL('addArrangedSubviewToStack:'), touchUpInside)

    # --- --- ---- removebutton
    removebutton = UIButton.buttonWithType_(UIButtonType.system)
    removebutton.setImage_forState_(minusSymbol, UIControlState.normal)
    removebutton.setContentHuggingPriority_forAxis_(
      253.0, UILayoutConstraintAxis.horizontal)
    removebutton.contentEdgeInsets = UIEdgeInsetsMake(10.0, 10.0, 10.0, 10.0)
    removebutton.addTarget_action_forControlEvents_(
      self, SEL('removeArrangedSubviewFromStack:'), touchUpInside)

    # --- --- arrangedSubviews
    addRemoveStackView.initWithArrangedSubviews_([
      addRemoveLabel,
      addbutton,
      removebutton,
    ])

    # --- addRemoveExampleStackView
    addRemoveExampleStackView = UIStackView.new()
    addRemoveExampleStackView.axis = UILayoutConstraintAxis.vertical
    addRemoveExampleStackView.alignment = UIStackViewAlignment.center
    addRemoveExampleStackView.spacing = 10.0

    # --- Layout
    self.view.addSubview_(showingHidingStackView)
    self.view.addSubview_(addRemoveStackView)
    self.view.addSubview_(addRemoveExampleStackView)

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
      # addRemoveExampleStackView.heightAnchor.constraintEqualToConstant_(42.0),  # xxx: `placeholder="YES"` ?
    ])

    self.furtherDetailStackView = furtherStackView
    self.plusButton = detailPlusButton
    self.addRemoveExampleStackView = addRemoveExampleStackView
    self.addArrangedViewButton = addbutton
    self.removeArrangedViewButton = removebutton

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

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'\t{NSStringFromClass(__class__)}: didReceiveMemoryWarning')

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

  @objc_method
  def hideFurtherDetail_(self, _):
    # Animate the changes by performing them in a `UIViewPropertyAnimator` animation block.
    @Block
    def animationsBlock() -> None:
      # Reveal the further details stack view and hide the plus button.
      self.furtherDetailStackView.setHidden_(True)
      self.plusButton.setHidden_(False)

    hideDetailAnimator = UIViewPropertyAnimator.alloc(
    ).initWithDuration_curve_animations_(NSTimeInterval(0.25),
                                         UIViewAnimationCurve.easeOut,
                                         animationsBlock)
    hideDetailAnimator.startAnimation()

  @objc_method
  def addArrangedSubviewToStack_(self, _):
    # Create a simple, fixed-size, square view to add to the stack view.
    newViewSize = CGSizeMake(38.0, 38.0)
    newView = UIView.alloc().initWithFrame_(CGRect(NSZeroPoint, newViewSize))

    #newView.backgroundColor = self.randomColor()
    newView.backgroundColor = randomColor()

    NSLayoutConstraint.activateConstraints_([
      newView.widthAnchor.constraintEqualToConstant_(newViewSize.width),
      newView.heightAnchor.constraintEqualToConstant_(newViewSize.height),
    ])
    # Adding an arranged subview automatically adds it as a child of the stack view.
    self.addRemoveExampleStackView.addArrangedSubview_(newView)

    self.updateAddRemoveButtons()

  @objc_method
  def removeArrangedSubviewFromStack_(self, _):
    # Make sure there is an arranged view to remove.
    if (viewToRemove :=
        self.addRemoveExampleStackView.arrangedSubviews.lastObject()) is None:
      return

    self.addRemoveExampleStackView.removeArrangedSubview_(viewToRemove)
    # Calling `removeArrangedSubview` does not remove the provided view from the stack view's `subviews` array. Since we no longer want the view we removed to appear, we have to explicitly remove it from its superview.
    # `removeArrangedSubview` を呼び出しても、スタック ビューの `subviews` 配列から指定されたビューは削除されません。削除したビューを表示したくないので、スーパービューから明示的に削除する必要があります。
    viewToRemove.removeFromSuperview()

    self.updateAddRemoveButtons()

  # MARK: - Convenience
  @objc_method
  def updateAddRemoveButtons(self):
    arrangedSubviewCount = len(self.addRemoveExampleStackView.arrangedSubviews)

    self.addArrangedViewButton.setEnabled_(
      arrangedSubviewCount < self.maximumArrangedSubviewCount)
    self.removeArrangedViewButton.setEnabled_(arrangedSubviewCount > 0)

  @objc_method
  def randomColor(self):
    red = arc4random_uniform(255) / 255.0
    green = arc4random_uniform(255) / 255.0
    blue = arc4random_uniform(255) / 255.0
    return UIColor.colorWithRed_green_blue_alpha_(red, green, blue, 1.0)
'''

if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import UIModalPresentationStyle

  main_vc = StackViewController.new()
  _title = NSStringFromClass(StackViewController)
  main_vc.navigationItem.title = _title

  #presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

