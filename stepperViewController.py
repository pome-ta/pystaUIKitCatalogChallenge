from enum import Enum

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, objc_id, SEL
from pyrubicon.objc.types import NSInteger

from rbedge.enumerations import (
  UIControlEvents,
  UIUserInterfaceStyle,
  UIControlState,
)
from rbedge.pythonProcessUtils import (
  mainScreen_scale,
  dataWithContentsOfURL,
  get_srgb_named_style,
)

from rbedge import pdbr

from caseElement import CaseElement
from pyLocalizedString import localizedString

from baseTableViewController import BaseTableViewController
from storyboard.stepperViewController import prototypes

UIColor = ObjCClass('UIColor')
UIImage = ObjCClass('UIImage')


# Cell identifier for each stepper table view cell.
# 各ステッパー テーブル ビュー セルのセル識別子。
class StepperKind(Enum):
  defaultStepper = 'defaultStepper'
  tintedStepper = 'tintedStepper'
  customStepper = 'customStepper'


class StepperViewController(BaseTableViewController):
  
  @objc_method
  def initWithStyle_(self, style: NSInteger) -> ObjCInstance:
    send_super(__class__,
               self,
               'initWithStyle:',
               style,
               restype=objc_id,
               argtypes=[
                 NSInteger,
               ])
    self.setupPrototypes_(prototypes)
    return self
  
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    
    self.navigationItem.title = localizedString('SteppersTitle') if (
                                                                      title := self.navigationItem.title) is None else title
    
    self.testCells_extend([
      CaseElement(localizedString('DefaultStepperTitle'),
                  StepperKind.defaultStepper.value,
                  self.configureDefaultStepper_),
      CaseElement(localizedString('TintedStepperTitle'),
                  StepperKind.tintedStepper.value,
                  self.configureTintedStepper_),
      CaseElement(localizedString('CustomStepperTitle'),
                  StepperKind.customStepper.value,
                  self.configureCustomStepper_),
    ])
  
  # MARK: - Configuration
  @objc_method
  def configureDefaultStepper_(self, stepper):
    # Setup the stepper range 0 to 10, initial value 0, increment/decrement factor of 1.
    # ステッパー範囲 0 ~ 10、初期値 0、増減係数 1 を設定します。
    stepper.value = 0.0
    stepper.minimumValue = 0.0
    stepper.maximumValue = 10.0
    stepper.stepValue = 1.0
    
    stepper.addTarget_action_forControlEvents_(self,
                                               SEL('stepperValueDidChange:'),
                                               UIControlEvents.valueChanged)
  
  @objc_method
  def configureTintedStepper_(self, stepper):
    # Setup the stepper range 0 to 20, initial value 20, increment/decrement factor of 1.
    # ステッパー範囲 0 ~ 20、初期値 20、増減係数 1 を設定します。
    stepper.value = 20.0
    stepper.minimumValue = 0.0
    stepper.maximumValue = 20.0
    stepper.stepValue = 1.0
    
    _style = self.traitCollection.userInterfaceStyle
    _srgb = get_srgb_named_style('tinted_stepper_control', _style)
    
    _color_named = UIColor.colorWithRed_green_blue_alpha_(*_srgb)
    stepper.tintColor = _color_named
    
    stepper.setDecrementImage_forState_(
      stepper.decrementImageForState_(UIControlState.normal),
      UIControlState.normal)
    stepper.setIncrementImage_forState_(
      stepper.incrementImageForState_(UIControlState.normal),
      UIControlState.normal)
    
    stepper.addTarget_action_forControlEvents_(self,
                                               SEL('stepperValueDidChange:'),
                                               UIControlEvents.valueChanged)
  
  @objc_method
  def configureCustomStepper_(self, stepper):
    scale = int(mainScreen_scale)
    
    background_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/background.imageset/stepper_and_segment_background_{scale}x.png'
    disabled_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/background_disabled.imageset/stepper_and_segment_background_disabled_{scale}x.png'
    
    stepperBackgroundImage = UIImage.alloc().initWithData_scale_(
      dataWithContentsOfURL(background_str), scale)
    
    # Set the background image.
    # 背景画像を設定します。
    stepper.setBackgroundImage_forState_(stepperBackgroundImage,
                                         UIControlState.normal)
    stepperDisabledBackgroundImage = UIImage.alloc().initWithData_scale_(
      dataWithContentsOfURL(disabled_str), scale)
    stepper.setBackgroundImage_forState_(stepperBackgroundImage,
                                         UIControlState.disabled)
    
    # Set the image which will be painted in between the two stepper segments. It depends on the states of both segments.
    # 2 つのステッパー セグメントの間にペイントするイメージを設定します。それは両方のセグメントの状態によって異なります。
    
    # xxx: `x1`,`x2` と`x3` だと、ファイル名が違う
    divider_scale = 'stepper_and_segment_divider_' if scale == 3 else 'stepper_and_segment_segment_divider_'
    divider_str = f'./UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Assets.xcassets/stepper_and_segment_divider.imageset/{divider_scale}{scale}x.png'
    
    # Set the divider image.
    # 分割画像を設定します。
    stepperSegmentDividerImage = UIImage.alloc().initWithData_scale_(
      dataWithContentsOfURL(divider_str), scale)
    stepper.setDividerImage_forLeftSegmentState_rightSegmentState_(
      stepperSegmentDividerImage, UIControlState.normal, UIControlState.normal)
    
    # Set the image for the + button.
    # +ボタンの画像を設定します。
    stepperIncrementImage = UIImage.systemImageNamed_('plus')
    
    stepper.setIncrementImage_forState_(stepperIncrementImage,
                                        UIControlState.normal)
    
    # Set the image for the - button.
    # -ボタンの画像を設定します。
    stepperDecrementImage = UIImage.systemImageNamed_('minus')
    stepper.setDecrementImage_forState_(stepperDecrementImage,
                                        UIControlState.normal)
    
    stepper.addTarget_action_forControlEvents_(self,
                                               SEL('stepperValueDidChange:'),
                                               UIControlEvents.valueChanged)
  
  # MARK: - Actions
  @objc_method
  def stepperValueDidChange_(self, stepper):
    print(f'A stepper changed its value: {stepper.value}')


if __name__ == '__main__':
  from rbedge.functions import NSStringFromClass
  from rbedge.enumerations import (
    UITableViewStyle,
    UIModalPresentationStyle,
  )
  from rbedge import present_viewController
  
  table_style = UITableViewStyle.grouped
  main_vc = StepperViewController.alloc().initWithStyle_(table_style)
  _title = NSStringFromClass(StepperViewController)
  main_vc.navigationItem.title = _title
  
  presentation_style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, presentation_style)
