import ctypes

from pyrubicon.objc.api import ObjCInstance
from pyrubicon.objc.types import CGSize, CGFloat, with_preferred_encoding, __LP64__
from pyrubicon.objc.runtime import libc, Foundation, Class, load_library, objc_id

UIKit = load_library('UIKit')


def NSStringFromClass(cls: Class) -> ObjCInstance:
  _NSStringFromClass = Foundation.NSStringFromClass
  _NSStringFromClass.restype = ctypes.c_void_p
  _NSStringFromClass.argtypes = [Class]
  return ObjCInstance(_NSStringFromClass(cls))


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
  _fnc = UIKit.UIGraphicsBeginImageContextWithOptions
  _fnc.restype = ctypes.c_void_p
  _fnc.argtypes = [
    CGSize,
    ctypes.c_bool,
    CGFloat,
  ]
  return ObjCInstance(_fnc(size, opaque, scale))

# ref: [UIGraphicsGetImageFromCurrentImageContext | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uigraphicsgetimagefromcurrentimagecontext()?language=objc)
def UIGraphicsGetImageFromCurrentImageContext() -> ObjCInstance:
  _fnc = UIKit.UIGraphicsGetImageFromCurrentImageContext
  _fnc.restype = objc_id
  _fnc.argtypes = []
  return ObjCInstance(_fnc())

# ref: [UIGraphicsEndImageContext | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uigraphicsendimagecontext()?language=objc)
def UIGraphicsEndImageContext():
  _fnc = UIKit.UIGraphicsEndImageContext
  _fnc.restype = ctypes.c_void_p
  _fnc.argtypes = []
  _fnc()

