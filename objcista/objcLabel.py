from ._classes import *
from ._view import _View


class ObjcLabel(_View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.instance = UILabel.new()
    self.instance.setText_(kwargs['text'])
    self.instance.sizeToFit()

