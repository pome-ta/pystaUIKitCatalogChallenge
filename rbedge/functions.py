import ctypes

from pyrubicon.objc.api import ObjCInstance
from pyrubicon.objc.types import CGSize, CGFloat, with_preferred_encoding, __LP64__
from pyrubicon.objc.runtime import libc, Foundation, Class, load_library, objc_id

UIKit = load_library('UIKit')
CoreGraphics = load_library('CoreGraphics')


def NSStringFromClass(cls: Class) -> ObjCInstance:
  _function = Foundation.NSStringFromClass
  _function.restype = ctypes.c_void_p
  _function.argtypes = [
    Class,
  ]
  return ObjCInstance(_function(cls))


if __LP64__:
  _NSDirectionalEdgeInsetsEncoding = b'{NSDirectionalEdgeInsets=dddd}'
else:
  _NSDirectionalEdgeInsetsEncoding = b'{NSDirectionalEdgeInsets=ffff}'


@with_preferred_encoding(_NSDirectionalEdgeInsetsEncoding)
class NSDirectionalEdgeInsets(ctypes.Structure):
  _fields_ = [
    ('top', CGFloat),
    ('leading', CGFloat),
    ('bottom', CGFloat),
    ('right', CGFloat),
  ]

  def __repr__(self):
    return f'<NSEdgeInsets({self.top}, {self.leading}, {self.bottom}, {self.trailing})>'

  def __str__(self):
    return f'top={self.top}, left={self.leading}, bottom={self.bottom}, right={self.trailing}'


def NSDirectionalEdgeInsetsMake(top, leading, bottom, trailing):
  return NSDirectionalEdgeInsets(top, leading, bottom, trailing)


def arc4random_uniform(value: ctypes.c_uint32) -> int:
  return libc.arc4random_uniform(value)


# ref: [UIGraphicsBeginImageContextWithOptions | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uigraphicsbeginimagecontextwithoptions(_:_:_:)?language=objc)
def UIGraphicsBeginImageContextWithOptions(size: CGSize, opaque: bool,
                                           scale: CGFloat) -> ObjCInstance:
  _function = UIKit.UIGraphicsBeginImageContextWithOptions
  _function.restype = ctypes.c_void_p
  _function.argtypes = [
    CGSize,
    ctypes.c_bool,
    CGFloat,
  ]
  return ObjCInstance(_function(size, opaque, scale))


# ref: [UIGraphicsGetImageFromCurrentImageContext | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uigraphicsgetimagefromcurrentimagecontext()?language=objc)
def UIGraphicsGetImageFromCurrentImageContext() -> ObjCInstance:
  _function = UIKit.UIGraphicsGetImageFromCurrentImageContext
  _function.restype = objc_id
  _function.argtypes = []
  return ObjCInstance(_function())


# ref: [UIGraphicsEndImageContext | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uigraphicsendimagecontext()?language=objc)
def UIGraphicsEndImageContext() -> None:
  _function = UIKit.UIGraphicsEndImageContext
  _function.restype = ctypes.c_void_p
  _function.argtypes = []
  _function()


# ref: [CGImageGetDataProvider | Apple Developer Documentation](https://developer.apple.com/documentation/coregraphics/cgimage/dataprovider?language=objc)
def CGImageGetDataProvider(image: ctypes.c_void_p) -> ObjCInstance:
  _function = CoreGraphics.CGImageGetDataProvider
  _function.restype = ctypes.c_void_p
  _function.argtypes = [
    ctypes.c_void_p,
  ]
  return ObjCInstance(_function(image))


# ref: [CGDataProviderCopyData | Apple Developer Documentation](https://developer.apple.com/documentation/coregraphics/cgdataprovider/data?language=objc)
def CGDataProviderCopyData(provider: ObjCInstance) -> ObjCInstance:
  _function = CoreGraphics.CGDataProviderCopyData
  _function.restype = ctypes.c_void_p
  _function.argtypes = [
    ctypes.c_void_p,
  ]
  return ObjCInstance(_function(provider))

