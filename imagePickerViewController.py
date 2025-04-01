"""
  note: Storyboard 実装なし
"""
import ctypes

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.runtime import send_super, SEL

from rbedge.enumerations import (
  UIButtonType,
  UIControlState,
  UIControlEvents,
  UILayoutConstraintAxis,
  UIViewContentMode,
  UIImagePickerControllerSourceType,
)

from rbedge.globalVariables import UIImagePickerControllerInfoKey
from rbedge.functions import NSStringFromClass
from rbedge import pdbr
from pyLocalizedString import localizedString

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')
UIColor = ObjCClass('UIColor')

UIButton = ObjCClass('UIButton')
UIImageView = ObjCClass('UIImageView')
UIImage = ObjCClass('UIImage')  # todo: 型確認用
UIImagePickerController = ObjCClass('UIImagePickerController')


class ImagePickerViewController(UIViewController):

  imageView: UIImageView = objc_property()
  imagePicker: UIImagePickerController = objc_property()

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t- {NSStringFromClass(__class__)}: dealloc')

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    #print(f'\t{NSStringFromClass(__class__)}: viewDidLoad')

    # --- Navigation
    self.navigationItem.title = localizedString('ImagePickerTitle') if (
      title := self.navigationItem.title) is None else title
    self.view.backgroundColor = UIColor.systemBackgroundColor()

    # --- imagePickerButton
    imagePickerButton = UIButton.buttonWithType_(UIButtonType.system)
    imagePickerButton.setTitle_forState_('Choose an Image',
                                         UIControlState.normal)
    imagePickerButton.addTarget_action_forControlEvents_(
      self, SEL('presentImagePicker:'), UIControlEvents.touchUpInside)

    # --- imageView
    imageView = UIImageView.new()
    imageView.clipsToBounds = True
    imageView.contentMode = UIViewContentMode.scaleAspectFill
    imageView.setContentHuggingPriority_forAxis_(
      251.0, UILayoutConstraintAxis.horizontal)
    imageView.setContentHuggingPriority_forAxis_(
      251.0, UILayoutConstraintAxis.vertical)

    # --- Layout
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide
    layoutMarginsGuide = self.view.layoutMarginsGuide

    self.view.addSubview_(imagePickerButton)
    imagePickerButton.translatesAutoresizingMaskIntoConstraints = False
    self.view.addSubview_(imageView)
    imageView.translatesAutoresizingMaskIntoConstraints = False

    NSLayoutConstraint.activateConstraints_([
      imageView.heightAnchor.constraintEqualToConstant_(244.0),
      imageView.widthAnchor.constraintEqualToConstant_(343.0),
    ])

    NSLayoutConstraint.activateConstraints_([
      imageView.topAnchor.constraintEqualToAnchor_constant_(
        imagePickerButton.bottomAnchor, 14.0),
      imagePickerButton.topAnchor.constraintEqualToAnchor_constant_(
        safeAreaLayoutGuide.topAnchor, 17.0),
      imagePickerButton.centerXAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerXAnchor),
      imageView.centerXAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerXAnchor),
    ])

    self.imageView = imageView
    self.configureImagePicker()

  @objc_method
  def viewWillAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print(f'\t{NSStringFromClass(__class__)}: viewWillAppear_')

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
    print(f'{__class__}: didReceiveMemoryWarning')

  @objc_method
  def configureImagePicker(self):
    imagePicker = UIImagePickerController.new()
    imagePicker.delegate = self
    imagePicker.mediaTypes = [
      'public.image',
    ]
    imagePicker.sourceType = UIImagePickerControllerSourceType.photoLibrary

    self.imagePicker = imagePicker

  @objc_method
  def presentImagePicker_(self, _):
    self.presentViewController(self.imagePicker,
                               animated=True,
                               completion=None)

  # MARK: - UIImagePickerControllerDelegate
  @objc_method
  def imagePickerController_didFinishPickingMediaWithInfo_(self, picker, info):
    if (image := info[UIImagePickerControllerInfoKey.originalImage]
        ).isKindOfClass_(UIImage):
      self.imageView.image = image
    picker.dismissViewControllerAnimated_completion_(True, None)


if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import UIModalPresentationStyle

  main_vc = ImagePickerViewController.new()
  _title = NSStringFromClass(ImagePickerViewController)
  main_vc.navigationItem.title = _title

  #presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

