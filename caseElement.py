from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.api import NSObject, NSString
from pyrubicon.objc.runtime import send_super

from rbedge.functions import NSStringFromClass
from rbedge import pdbr


class CaseElement(NSObject):
  # セルの視覚的なタイトル (テーブル セクションのヘッダー タイトル)
  title: NSString = objc_property()
  # nib ファイル内でセルを検索するためのテーブルビューのセルの識別子
  cellID: NSString = objc_property()
  # セルのサブビューを設定するための構成ハンドラー。（は、面倒なのでハンドラ名の文字列）
  # xxx: ガバガバ
  configHandlerName: NSString = objc_property()

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def initWithTitle_cellID_configHandlerName_(self, title, cellID,
                                              configHandlerName):
    self.title = title
    self.cellID = cellID
    self.configHandlerName = configHandlerName
    return self

  @objc_method
  def targetView(self, cell):
    return cell.contentView.subviews()[0] if cell is not None else None

