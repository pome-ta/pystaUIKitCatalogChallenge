'''
  note: Storyboard 実装なし
'''
import ctypes

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method, objc_const
from pyrubicon.objc.runtime import send_super, objc_id, load_library
from pyrubicon.objc.types import CGRectMake

from rbedge.enumerations import (
  UILayoutConstraintAxis,
  NSTextAlignment,
  UITextBorderStyle,
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
    showingHidingExampleStackView = UIStackView.alloc().initWithFrame_(
      CGRectMake(16.0, 52.0, 343.0, 134.5))
    # todo: 確認用
    showingHidingExampleStackView.backgroundColor = UIColor.systemGreenColor()
    showingHidingExampleStackView.axis = UILayoutConstraintAxis.vertical
    showingHidingExampleStackView.spacing = 10.0

    showingHidingLabel = UILabel.new()
    showingHidingLabel.text = 'Showing/hiding views'
    showingHidingLabel.textAlignment = NSTextAlignment.center
    showingHidingLabel.setFont_(
      UIFont.preferredFontForTextStyle_(UIFontTextStyleHeadline))
    
    
    
    # --- subShowingHidingStackView
    detailStackView = UIStackView.alloc().initWithFrame_(
      CGRectMake(0.0, 30.5, 343.0, 34.0))
    #detailStackView = UIStackView.alloc().initWithFrame_(CGRectMake(0.0,0.0,0.0,0.0))
    detailStackView.spacing = 10.0
    # todo: 確認用
    detailStackView.backgroundColor = UIColor.systemDarkRedColor()

    detailLabel = UILabel.new()
    detailLabel.text = 'Detail'
    detailLabel.setFont_(
      UIFont.preferredFontForTextStyle_(UIFontTextStyleBody))

    detailLabel.backgroundColor = UIColor.systemOrangeColor()
    
    
    detailTextField = UITextField.alloc().initWithFrame_(CGRectMake(114.0, 0.0, 177.5, 34.0))
    #detailTextField = UITextField.alloc().initWithFrame_(CGRectMake(0.0, 0.0, 0.0, 0.0))
    #detailTextField = UITextField.new()
    detailTextField.borderStyle = UITextBorderStyle.roundedRect
    detailTextField.setFont_(UIFont.systemFontOfSize_(14.0))
    detailTextField.font.systemMinimumFontSize = 17.0

    detailPlusButton = UIButton.buttonWithType_(UIButtonType.system)
    detailPlusButtonConfig = UIButtonConfiguration.plainButtonConfiguration()
    detailPlusButtonConfig.image = plusSymbol
    detailPlusButton.configuration = detailPlusButtonConfig

    detailPlusButton.backgroundColor = UIColor.systemBrownColor()
    #pdbr.state(detailPlusButton)
    detailPlusButton.translatesAutoresizingMaskIntoConstraints = False

    detailStackView.addArrangedSubview_(detailLabel)
    detailStackView.addArrangedSubview_(detailTextField)
    detailStackView.addArrangedSubview_(detailPlusButton)

    showingHidingExampleStackView.addArrangedSubview_(showingHidingLabel)
    showingHidingExampleStackView.addArrangedSubview_(detailStackView)

    # --- furtherDetailStackView
    furtherDetailStackView = UIStackView.alloc().initWithFrame_(
      CGRectMake(0.0, 74.5, 343.0, 34.0))
    furtherDetailStackView.spacing = 10.0
    # todo: 確認用
    furtherDetailStackView.backgroundColor = UIColor.systemCyanColor()

    furtherDetailLabel = UILabel.new()
    furtherDetailLabel.text = 'Further Detail'
    furtherDetailLabel.setFont_(
      UIFont.preferredFontForTextStyle_(UIFontTextStyleBody))

    furtherDetailTextField = UITextField.alloc().initWithFrame_(
      CGRectMake(114.0, 0.0, 177.5, 34.0))
    furtherDetailTextField.borderStyle = UITextBorderStyle.roundedRect
    furtherDetailTextField.setFont_(UIFont.systemFontOfSize_(14.0))
    furtherDetailTextField.font.systemMinimumFontSize = 17.0

    furtherDetailMinusButton = UIButton.buttonWithType_(UIButtonType.system)
    furtherDetailMinusButtonConfig = UIButtonConfiguration.plainButtonConfiguration(
    )
    furtherDetailMinusButtonConfig.image = minusSymbol
    furtherDetailMinusButton.configuration = furtherDetailMinusButtonConfig

    furtherDetailMinusButton.backgroundColor = UIColor.systemDarkPurpleColor()

    furtherDetailStackView.addArrangedSubview_(furtherDetailLabel)
    furtherDetailStackView.addArrangedSubview_(furtherDetailTextField)
    furtherDetailStackView.addArrangedSubview_(furtherDetailMinusButton)

    showingHidingExampleStackView.addArrangedSubview_(furtherDetailStackView)

    self.view.addSubview_(showingHidingExampleStackView)
    # --- Layout
    showingHidingExampleStackView.translatesAutoresizingMaskIntoConstraints = False
    #detailTextField.translatesAutoresizingMaskIntoConstraints = False

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

