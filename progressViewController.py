import ctypes
from enum import Enum

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method, objc_property, at
from pyrubicon.objc.runtime import send_super, objc_id
from pyrubicon.objc.types import NSInteger

from rbedge.enumerations import (
  UIProgressViewStyle,
  NSKeyValueObservingOptions,
)
from rbedge import pdbr

from caseElement import CaseElement
from pyLocalizedString import localizedString

from baseTableViewController import BaseTableViewController
from storyboard.progressViewController import prototypes

NSProgress = ObjCClass('NSProgress')
NSTimer = ObjCClass('NSTimer')

UIColor = ObjCClass('UIColor')


# Cell identifier for each progress view table view cell.
class ProgressViewKind(Enum):
  defaultProgress = 'defaultProgress'
  barProgress = 'barProgress'
  tintedProgress = 'tintedProgress'


class ProgressViewController(BaseTableViewController):

  # MARK: - Properties
  # An `NSProgress` object whose `fractionCompleted` is observed using KVO to update the `UIProgressView`s' `progress` properties.
  progress: NSProgress = objc_property()
  # A repeating timer that, when fired, updates the `NSProgress` object's `completedUnitCount` property.
  updateTimer: NSTimer = objc_property()

  # MARK: - Initialization
  @objc_method
  def initWithStyle_(self, style: int) -> ObjCInstance:
    send_super(__class__,
               self,
               'initWithStyle:',
               style,
               restype=objc_id,
               argtypes=[
                 NSInteger,
               ])
    self.setupPrototypes_(prototypes)

    # Accumulated progress views from all table cells for progress updating.
    self.progressViews: list = []
    self.progress = NSProgress.progressWithTotalUnitCount_(10)
    self.progress.addObserver_forKeyPath_options_context_(
      self, at('fractionCompleted'), NSKeyValueObservingOptions.new, None)
    return self

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    #print('\tdealloc')
    # Unregister as an observer of the `NSProgress`'s `fractionCompleted` property.
    self.progress.removeObserver_forKeyPath_(self, at('fractionCompleted'))

  @objc_method
  def observeValueForKeyPath_ofObject_change_context_(self, keyPath, objct,
                                                      change, context):
    fractionCompleted = self.progress.fractionCompleted
    # Update the progress views.
    [
      progressView.setProgress_animated_(fractionCompleted, True)
      for progressView in self.progressViews
    ]

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    self.navigationItem.title = localizedString('ProgressViewsTitle') if (
      title := self.navigationItem.title) is None else title

    self.testCells.extend([
      CaseElement(localizedString('ProgressDefaultTitle'),
                  ProgressViewKind.defaultProgress.value,
                  self.configureDefaultStyleProgressView_),
      CaseElement(localizedString('ProgressBarTitle'),
                  ProgressViewKind.barProgress.value,
                  self.configureBarStyleProgressView_),
    ])
    if True:  # wip: `traitCollection.userInterfaceIdiom != .mac`
      # Tinted progress views available only on iOS.
      self.testCells.extend([
        CaseElement(localizedString('ProgressTintedTitle'),
                    ProgressViewKind.tintedProgress.value,
                    self.configureTintedProgressView_),
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

    # Reset the `completedUnitCount` of the `NSProgress` object and create a repeating timer to increment it over time.
    self.progress.completedUnitCount = 0

    # Update the `completedUnitCount` of the `NSProgress` object if it's not completed. Otherwise, stop the timer.
    def timerBlock(timer: objc_id) -> objc_id:
      if self.progress.completedUnitCount < self.progress.totalUnitCount:
        self.progress.completedUnitCount += 1
      else:
        self.updateTimer.invalidate()

    self.updateTimer = NSTimer.scheduledTimerWithTimeInterval_repeats_block_(
      1.0, True, timerBlock)

  @objc_method
  def viewDidDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    # Stop the timer from firing.
    self.updateTimer.invalidate()
    # todo: インスタンス変数初期化のおまじない
    self.progressViews = None

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'{__class__}: didReceiveMemoryWarning')


# MARK: - Configuration

  @objc_method
  def configureDefaultStyleProgressView_(self, progressView):
    progressView.progressViewStyle = UIProgressViewStyle.default
    # Reset the completed progress of the `UIProgressView`s.
    progressView.setProgress_animated_(0.0, False)
    self.progressViews.append(progressView)

  @objc_method
  def configureBarStyleProgressView_(self, progressView):
    progressView.progressViewStyle = UIProgressViewStyle.bar
    # Reset the completed progress of the `UIProgressView`s.
    progressView.setProgress_animated_(0.0, False)
    self.progressViews.append(progressView)

  @objc_method
  def configureTintedProgressView_(self, progressView):
    progressView.progressViewStyle = UIProgressViewStyle.default
    progressView.trackTintColor = UIColor.systemBlueColor()
    progressView.progressTintColor = UIColor.systemPurpleColor()

    # Reset the completed progress of the `UIProgressView`s.
    progressView.setProgress_animated_(0.0, False)
    self.progressViews.append(progressView)

if __name__ == '__main__':
  from rbedge.functions import NSStringFromClass
  from rbedge.enumerations import (
    UITableViewStyle,
    UIModalPresentationStyle,
  )

  from rbedge import present_viewController

  table_style = UITableViewStyle.grouped
  main_vc = ProgressViewController.alloc().initWithStyle_(table_style)
  _title = NSStringFromClass(ProgressViewController)
  main_vc.navigationItem.title = _title

  presentation_style = UIModalPresentationStyle.fullScreen
  present_viewController(main_vc, presentation_style)

