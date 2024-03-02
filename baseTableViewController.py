import re
from pathlib import Path

localizable_url = './UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Base.lproj/Localizable.strings'

localizable_path = Path(localizable_url)
'''
localizable_txt = localizable_path.read_text(encoding='utf-8')
localizable_plane_list = localizable_txt.splitlines()
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



