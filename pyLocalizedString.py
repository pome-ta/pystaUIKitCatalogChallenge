import re
from pathlib import Path

localizable_url = './UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Base.lproj/Localizable.strings'


class PyLocalizedString:

  def __init__(self, url: str | Path = localizable_url):
    localizable_path = Path(url)
    splitlines_list = localizable_path.read_text(encoding='utf-8').splitlines()

    # xxx: すごく雑に`Localizable.strings` format 確認してる
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
    # xxx: 特定の文字記号は置き換えを考えておく
    value = self.localizable_dic.get(key, '🙅‍♀️')
    return value

  @classmethod
  def new(cls, url: str | Path = localizable_url):
    this = cls(url)
    return this.__get_dict_value


localizedString = PyLocalizedString.new(localizable_url)


