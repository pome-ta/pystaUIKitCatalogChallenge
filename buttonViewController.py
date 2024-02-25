import ctypes
from objc_util import ObjCInstance, sel, create_objc_class, c

from objcista import *
#from objcista._controller import _Controller
from objcista.objcNavigationController import PlainNavigationController
from objcista.objcViewController import ObjcViewController
from objcista.objcLabel import ObjcLabel

from caseElement import CaseElement
from storyboard_ButtonViewController import prototypes

import pdbg


# ref: [Picker wheel for lists (not just dates) | omz:forum](https://forum.omz-software.com/topic/4592/picker-wheel-for-lists-not-just-dates/2)
# [Pythonista/_2017/picker-wheel-for-lists.py at 3e082d53b6b9b501a3c8cf3251a8ad4c8be9c2ad · tdamdouni/Pythonista · GitHub](https://github.com/tdamdouni/Pythonista/blob/3e082d53b6b9b501a3c8cf3251a8ad4c8be9c2ad/_2017/picker-wheel-for-lists.py#L24)
def _str_symbol(name):
  return ObjCInstance(ctypes.c_void_p.in_dll(c, name))


# todo: まずはここで作りつつ、モジュール化するケアも考慮
#UITableViewController
class ObjcTableViewController:

  def __init__(self, *args, **kwargs):
    self._msgs: list['def'] = []  # xxx: 型名ちゃんとやる
    self.controller_instance: ObjCInstance
    self.prototypes = prototypes
    self.testCells = []

  def add_extensions(self):
    # todo: objc で独自にmethod 生やしたいときなど
    # todo: この関数内に関数を作り`@self.extension`

    @self.extension
    def configureSystemTextButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      state = UIControl_State.normal
      button.setTitle_forState_('Button', state)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureSystemDetailDisclosureButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureSystemContactAddButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureCloseButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    # todo: `@available(iOS 15.0, *)`
    # xxx: あとでやる
    def configureStyleGrayButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      config = UIButtonConfiguration.grayButtonConfiguration()
      button.setConfiguration_(config)
      state = UIControl_State.normal
      button.setTitle_forState_('Button', state)
      button.setToolTip_('GrayStyleButtonToolTipTitle')

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    # todo: `@available(iOS 15.0, *)`
    def configureStyleTintedButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      config = UIButtonConfiguration.tintedButtonConfiguration()
      # todo: `if traitCollection.userInterfaceIdiom == .mac`
      # xxx: あとでやる
      systemRed = UIColor.systemRedColor()
      config.setBaseBackgroundColor_(systemRed)
      config.setBaseForegroundColor_(systemRed)

      state = UIControl_State.normal
      button.setTitle_forState_('Button', state)
      button.setToolTip_('TintedStyleButtonToolTipTitle')
      button.setConfiguration_(config)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    # todo: `@available(iOS 15.0, *)`
    def configureStyleFilledButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      config = UIButtonConfiguration.filledButtonConfiguration()

      # todo: `if traitCollection.userInterfaceIdiom == .mac`
      # xxx: あとでやる
      systemRed = UIColor.systemRedColor()
      config.background().setBackgroundColor_(systemRed)
      button.setConfiguration_(config)

      state = UIControl_State.normal
      button.setTitle_forState_('Button', state)
      button.setToolTip_('FilledStyleButtonToolTipTitle')

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    # todo: `@available(iOS 15.0, *)`
    def configureCornerStyleButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      # todo: `if traitCollection.userInterfaceIdiom == .mac`
      config = UIButtonConfiguration.grayButtonConfiguration()
      cornerStyle = UIButton_Configuration_CornerStyle.capsule
      config.setCornerStyle_(cornerStyle)

      button.setConfiguration_(config)

      state = UIControl_State.normal
      button.setTitle_forState_('Button', state)
      button.setToolTip_('CapsuleStyleButtonToolTipTitle')

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureImageButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      image = UIImage.systemImageNamed('xmark')

      systemPurple = UIColor.systemPurpleColor()
      imageButtonNormalImage = image.imageWithTintColor_(systemPurple)
      state = UIControl_State.normal
      button.setImage_forState_(imageButtonNormalImage, state)

      # todo: `if traitCollection.userInterfaceIdiom == .mac`

      button.setToolTip_('XButtonToolTipTitle')

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureAttributedTextSystemButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      buttonTitle = 'Buttonnn'
      NSStrikethroughStyleAttributeName = _str_symbol(
        'NSStrikethroughStyleAttributeName')

      normalTitleAttributes = {
        NSStrikethroughStyleAttributeName: NSUnderlineStyle.single,
      }

      normalAttributedTitle = NSAttributedString.alloc(
      ).initWithString_attributes_(buttonTitle, normalTitleAttributes)

      state = UIControl_State.normal
      button.setAttributedTitle_forState_(normalAttributedTitle, state)

      NSForegroundColorAttributeName = _str_symbol(
        'NSForegroundColorAttributeName')
      NSStrikethroughStyleAttributeName = _str_symbol(
        'NSStrikethroughStyleAttributeName')

      highlightedTitleAttributes = {
        NSForegroundColorAttributeName: UIColor.systemGreenColor(),
        NSStrikethroughStyleAttributeName: NSUnderlineStyle.thick,
      }

      highlightedAttributedTitle = NSAttributedString.alloc(
      ).initWithString_attributes_(buttonTitle, highlightedTitleAttributes)

      state = UIControl_State.highlighted
      button.setAttributedTitle_forState_(highlightedAttributedTitle, state)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureSymbolButton_(_self, _cmd, _button):
      # xxx: 合ってる説ある？
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      buttonImage = UIImage.systemImageNamed('person')
      state = UIControl_State.normal
      if True:  # xxx: `available(iOS 15, *)`
        buttonConfig = UIButtonConfiguration.plainButtonConfiguration()
        buttonConfig.setImage_(buttonImage)
        button.setConfiguration_(buttonConfig)
        button.setToolTip_('PersonButtonToolTipTitle')
      else:
        button.setImage_forState_(buttonImage, state)

      UIFontTextStyleBody = _str_symbol('UIFontTextStyleBody')
      scale = UIImage_SymbolScale.large

      config = UIImageSymbolConfiguration.configurationWithTextStyle_scale_(
        UIFontTextStyleBody, scale)

      button.setPreferredSymbolConfiguration_forImageInState_(config, state)

      # todo: `button.accessibilityLabel = NSLocalizedString("Person", comment: "")`

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureLargeSymbolButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)
      buttonImage = UIImage.systemImageNamed('person')
      if True:  # xxx: `available(iOS 15, *)`
        buttonConfig = UIButtonConfiguration.plainButtonConfiguration()

        UIFontTextStyleLargeTitle = _str_symbol('UIFontTextStyleLargeTitle')

        _symbolConfiguration = UIImageSymbolConfiguration.configurationWithTextStyle_(
          UIFontTextStyleLargeTitle)

        buttonConfig.setPreferredSymbolConfigurationForImage_(
          _symbolConfiguration)
        buttonConfig.setImage_(buttonImage)
        button.setConfiguration_(buttonConfig)
      else:
        state = UIControl_State.normal
        button.setImage_forState_(buttonImage, state)

        UIFontTextStyleBody = _str_symbol('UIFontTextStyleBody')
        scale = UIImage_SymbolScale.small

        config = UIImageSymbolConfiguration.configurationWithTextStyle_scale_(
          UIFontTextStyleBody, scale)
        button.setPreferredSymbolConfiguration_forImageInState_(config, state)

      # todo: `button.accessibilityLabel = NSLocalizedString("Person", comment: "")`

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureSymbolTextButton_(_self, _cmd, _button):
      # Button with image to the left of the title.
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      buttonImage = UIImage.systemImageNamed('person')
      if True:  # xxx: `available(iOS 15, *)`
        buttonConfig = UIButtonConfiguration.plainButtonConfiguration()
        UIFontTextStyleBody = _str_symbol('UIFontTextStyleBody')
        _symbolConfiguration = UIImageSymbolConfiguration.configurationWithTextStyle_(
          UIFontTextStyleBody)

        buttonConfig.setPreferredSymbolConfigurationForImage_(
          _symbolConfiguration)
        buttonConfig.setImage_(buttonImage)
        button.setConfiguration_(buttonConfig)
      else:
        state = UIControl_State.normal
        button.setImage_forState_(buttonImage, state)

      state = UIControl_State.normal
      button.setTitle_forState_('Person', state)

      # xxx: 正解かは不明
      UIFontTextStyleBody = _str_symbol('UIFontTextStyleBody')
      preferredFont = UIFont.preferredFontForTextStyle_(UIFontTextStyleBody)

      button.titleLabel().setFont_(preferredFont)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureTextSymbolButton_(_self, _cmd, _button):
      # Button with image to the right of the title.
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      buttonImage = UIImage.systemImageNamed('person')
      if True:  # xxx: `available(iOS 15, *)`
        buttonConfig = UIButtonConfiguration.plainButtonConfiguration()

        UIFontTextStyleBody = _str_symbol('UIFontTextStyleBody')
        _symbolConfiguration = UIImageSymbolConfiguration.configurationWithTextStyle_(
          UIFontTextStyleBody)

        buttonConfig.setImage_(buttonImage)
        # todo: `if traitCollection.userInterfaceIdiom == .mac`
        imagePlacement = NSDirectionalRectEdge.trailing
        buttonConfig.setImagePlacement_(imagePlacement)
        button.setConfiguration_(buttonConfig)

      state = UIControl_State.normal
      button.setTitle_forState_('Person', state)

      # xxx: 正解かは不明
      UIFontTextStyleBody = _str_symbol('UIFontTextStyleBody')
      preferredFont = UIFont.preferredFontForTextStyle_(UIFontTextStyleBody)

      button.titleLabel().setFont_(preferredFont)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureMultiTitleButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      # todo: `,if traitCollection.userInterfaceIdiom == .mac`
      state = UIControl_State.normal
      button.setTitle_forState_('Button', state)

      state = UIControl_State.highlighted
      button.setTitle_forState_('Person', state)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def configureSystemTextButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)

      state = UIControl_State.normal
      button.setTitle_forState_('Button', state)

      selector = sel('buttonClicked:')
      event = UIControl_Event.touchUpInside
      button.addTarget_action_forControlEvents_(this, selector, event)

    @self.extension
    def buttonClicked_(_self, _cmd, _sender):
      print('Button was clicked.')

    @self.extension
    def toggleButtonClicked_(_self, _cmd, _sender):
      sender = ObjCInstance(_sender)
      print(f'Toggle action: {sender}')

  def extension(self, msg):
    if not (hasattr(self, '_msgs')):
      self._msgs: list['def'] = []
    self._msgs.append(msg)

  def _override_controller(self):
    # todo: 既存method と独自追加method をシュッと持ちたい
    def viewDidLoad(_self, _cmd):
      this = ObjCInstance(_self)
      view = this.view()
      for proto in self.prototypes:
        _args = [
          proto.this(),
          proto.reuseIdentifier_name(),
        ]
        view.registerClass_forCellReuseIdentifier_(*_args)
      '''
      self.testCells.append(
        CaseElement('DefaultTitle', 'buttonSystem',
                    this.configureSystemTextButton_))
      '''
      self.testCells.append(
        CaseElement('MultiTitleTitle', 'buttonMultiTitle',
                    this.configureMultiTitleButton_))

    # --- UITableViewDelegate
    def tableView_numberOfRowsInSection_(_self, _cmd, _tableView, _section):
      return 1

    def numberOfSectionsInTableView_(_self, _cmd, _tableView):
      return 1  #len(self.identifiers)

    def tableView_cellForRowAtIndexPath_(_self, _cmd, _tableView, _indexPath):
      tableView = ObjCInstance(_tableView)
      indexPath = ObjCInstance(_indexPath)

      cellTest = self.testCells[indexPath.section()]

      cell = tableView.dequeueReusableCellWithIdentifier(
        cellTest.cellID, forIndexPath=indexPath)

      if (view := cellTest.targetView(cell)):
        cellTest.configHandler(view)
      return cell.ptr

    _methods = [
      viewDidLoad,
      tableView_numberOfRowsInSection_,
      numberOfSectionsInTableView_,
      tableView_cellForRowAtIndexPath_,
    ]

    self.add_extensions()
    if self._msgs: _methods.extend(self._msgs)

    create_kwargs = {
      'name': '_vc',
      'superclass': UITableViewController,
      'methods': _methods,
    }
    _vc = create_objc_class(**create_kwargs)
    self.controller_instance = _vc

  def _init_controller(self):
    self._override_controller()
    vc = self.controller_instance.new().autorelease()
    return vc

  @classmethod
  def new(cls, *args, **kwargs) -> ObjCInstance:
    _cls = cls(*args, **kwargs)
    return _cls._init_controller()


if __name__ == "__main__":

  class TopNavigationController(PlainNavigationController):

    def __init__(self):
      self.override()

    def override(self):

      @self.add_msg
      def doneButtonTapped_(_self, _cmd, _sender):
        this = ObjCInstance(_self)
        visibleViewController = this.visibleViewController()
        visibleViewController.dismissViewControllerAnimated_completion_(
          True, None)

    def willShowViewController(self,
                               navigationController: UINavigationController,
                               viewController: UIViewController,
                               animated: bool):

      super().willShowViewController(navigationController, viewController,
                                     animated)

      systemItem = UIBarButtonItem_SystemItem.done
      done_btn = UIBarButtonItem.alloc(
      ).initWithBarButtonSystemItem_target_action_(systemItem,
                                                   navigationController,
                                                   sel('doneButtonTapped:'))

      visibleViewController = navigationController.visibleViewController()

      # --- navigationItem
      navigationItem = visibleViewController.navigationItem()
      navigationItem.rightBarButtonItem = done_btn

  LAYOUT_DEBUG = True

  #LAYOUT_DEBUG = False
  #vc = ButtonViewController.new()
  #buttonSystemAddContact
  vc = ObjcTableViewController.new()
  nv = TopNavigationController.new(vc, True)
  style = UIModalPresentationStyle.pageSheet
  #style = UIModalPresentationStyle.fullScreen

  run_controller(nv, style)

