import re
from pathlib import Path

localizable_url = './UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Base.lproj/Localizable.strings'

#localizable_path = Path(localizable_url)
'''
localizable_txt = localizable_path.read_text(encoding='utf-8')
localizable_plane_list = localizable_txt.splitlines()
'''
'''
splitlines_list = localizable_path.read_text(encoding='utf-8').splitlines()
pre_processing = [
  line for line in splitlines_list
  if len(line) and (line[0] == '"') and (line[-1] == ';')
]

compile = re.compile('"(.*?)"')
localizable_dic = dict([
  reg_result for line in pre_processing
  if (reg_result := compile.findall(line))
])
'''


class PyLocalizedString:

  def __init__(self, url: str | Path = localizable_url):
    localizable_path = Path(url)
    splitlines_list = localizable_path.read_text(encoding='utf-8').splitlines()

    # xxx: すごく雑に`Localizable.strings` format 確認してる
    pre_processing = [
      line for line in splitlines_list
      if len(line) and (line[0] == '"') and (line[-1] == ';')
    ]
    compile = re.compile('"(.*?)"')

    self.localizable_dic = dict([
      reg_result for line in pre_processing
      if (reg_result := compile.findall(line))
    ])

  def __get_dict_value(self, key):
    return self.localizable_dic.get(key, '🙅‍♀️')

  @classmethod
  def new(cls, url: str | Path = localizable_url):
    this = cls(url)
    return this.__get_dict_value


if __name__ == "__main__":
  py_localizedString = PyLocalizedString.new(localizable_url)
  l = py_localizedString('VisualEffectTextContent')
  ll = py_localizedString('AddContactTitle')
  
  

  #pyLocalizedString = PyLocalizedString()


