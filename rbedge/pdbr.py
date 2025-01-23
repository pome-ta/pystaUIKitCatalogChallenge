import ctypes
import json
from pprint import pprint

from pyrubicon.objc import ObjCInstance, ObjCClass, NSObject
from pyrubicon.objc.runtime import libobjc

__all__ = [
  'state',
]


def _get_className_methods(rubicon_object):
  if rubicon_object is None:
    return None
  objct_class = libobjc.object_getClass(rubicon_object)
  py_className_methods = {}
  is_flag = False
  
  while objct_class is not None:
    py_methods = []
    num_methods = ctypes.c_uint(0)
    method_list_ptr = libobjc.class_copyMethodList(objct_class,
                                                   ctypes.byref(num_methods))
    for i in range(num_methods.value):
      selector = libobjc.method_getName(method_list_ptr[i])
      sel_name = libobjc.sel_getName(selector).decode('ascii')
      py_method_name = sel_name.replace(':', '_')
      
      if '.' not in py_method_name:
        py_methods.append(py_method_name)
    libobjc.free(method_list_ptr)
    
    py_className_methods[str(ObjCInstance(objct_class.value))] = sorted(
      set(py_methods))
    
    objct_class = libobjc.class_getSuperclass(objct_class)
    
    if is_flag:
      break
    if objct_class.value == NSObject.ptr.value:
      is_flag = True
  
  return dict(reversed(list(py_className_methods.items())))


def state(rubicon_obj, is_merge_methods: bool = False):
  _dic = _get_className_methods(rubicon_obj)
  if _dic:
    pprint(sorted(set().union(
      *list(_dic.values())))) if is_merge_methods else print(
      json.dumps(_dic, indent=2))
    pprint(list(_dic.keys()))
    pprint(rubicon_obj)
  else:
    print(rubicon_obj)
