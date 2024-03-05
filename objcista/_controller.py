from objc_util import ObjCInstance


class _Controller:

  def __init__(self, *args, **kwargs):
    self._msgs: list['Callable'] = []  # xxx: 型名ちゃんとやる
    self.controller_instance: ObjCInstance

  def add_extensions(self):
    # todo: objc で独自にmethod 生やしたいときなど
    # todo: この関数内に関数を作り`@self.add_msg`
    pass

  def extension(self, msg):
    if not (hasattr(self, '_msgs')):
      self._msgs: list['Callable'] = []
    self._msgs.append(msg)

  def _override_controller(self):
    # todo: 既存method と独自追加method をシュッと持ちたい
    # if self._msgs: _methods.extend(self._msgs)
    pass

  def _init_controller(self):
    pass

  @classmethod
  def new(cls) -> ObjCInstance | None:
    return None
