import re
from pathlib import Path

localizable_url = './UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Base.lproj/Localizable.strings'

localizable_path = Path(localizable_url)
'''
localizable_txt = localizable_path.read_text(encoding='utf-8')

localizable_plane_list = localizable_txt.splitlines()

'''

localizable_plane_list = localizable_path.read_text(
  encoding='utf-8').splitlines()

compile = re.compile('"(.*?)"')
[print(compile.findall(s)) for s in localizable_plane_list]

