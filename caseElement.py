
class CaseElement:

  def __init__(self, title: str, cellID: str, configHandler):


    # セルの視覚的なタイトル (テーブル セクションのヘッダー タイトル)
    
    self.title = title
    # nib ファイル内でセルを検索するためのテーブルビューのセルの識別子。
    self.cellID = cellID
    
    #print(self.cellID)
    # セルのサブビューを設定するための構成ハンドラー。
    # xxx: ガバガバ
    self.configHandler = configHandler

  @staticmethod
  def targetView(cell):
    
    return cell.contentView.subviews()[0] if cell != None else None

