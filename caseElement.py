#from pyrubicon.objc.api import ObjCInstance, ObjCBoundMethod
from pyrubicon.objc.api import objc_method ,objc_property
from pyrubicon.objc.api import NSObject, NSString
from pyrubicon.objc.runtime import send_super, objc_id, send_message, SEL

from rbedge.functions import NSStringFromClass
from rbedge import pdbr


class CaseElement(NSObject):

  # セルの視覚的なタイトル (テーブル セクションのヘッダー タイトル)
  title: NSString = objc_property()
  # nib ファイル内でセルを検索するためのテーブルビューのセルの識別子
  cellID: NSString = objc_property()
  # セルのサブビューを設定するための構成ハンドラー。
  # xxx: ガバガバ
  #configHandler = objc_property()
  #targetSelf = objc_property(weak=True)
  #targetSelf = objc_property()
  configHandlerName: NSString = objc_property()

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t\t- {NSStringFromClass(__class__)}: dealloc')
    self.title = None
    self.cellID = None
    self.configHandlerName = None

  '''
  @objc_method
  def initWithTitle_cellID_configHandler_(self, title, cellID, configHandler):
    #print(configHandler)
    self.title = NSString.stringWithString_(title)
    self.cellID = NSString.stringWithString_(cellID)
    #self.configHandler = configHandler
    return self
  '''
  '''
  @objc_method
  def initWithTitle_cellID_(self, title, cellID):
    #print(configHandler)
    self.title = NSString.stringWithString_(title)
    self.cellID = NSString.stringWithString_(cellID)
    #self.configHandler = configHandler
    pdbr.state(self)
    return self
  '''

  '''
  @objc_method
  def initWithTitle_cellID_configHandlerName_(
      self, title, cellID, configHandlerName):
    self.title = title#NSString.stringWithString_(title)
    self.cellID = cellID#NSString.stringWithString_(cellID)
    self.configHandlerName = configHandlerName#NSString.stringWithString_(configHandlerName)
    return self

  '''
  @objc_method
  def initWithTitle_cellID_targetSelf_configHandlerName_(
      self, title, cellID, targetSelf, configHandlerName):
    self.title = NSString.stringWithString_(title)
    self.cellID = NSString.stringWithString_(cellID)
    self.targetSelf = targetSelf
    self.configHandlerName = NSString.stringWithString_(configHandlerName)
    return self


  @objc_method
  def configHandler(self, view):
    #getattr(self.targetSelf, str(self.configHandlerName))(view)
    send_message(self.targetSelf, SEL(str(self.configHandlerName)), view, restype=None,argtypes=[objc_id])
  
  

  @objc_method
  def targetView(self,cell):
    return cell.contentView.subviews()[0] if cell != None else None


'''

class CaseElement:

  def __init__(self, title: str, cellID: str, configHandler):
    # セルの視覚的なタイトル (テーブル セクションのヘッダー タイトル)
    self.title = title
    # nib ファイル内でセルを検索するためのテーブルビューのセルの識別子。
    self.cellID = cellID
    # セルのサブビューを設定するための構成ハンドラー。
    # xxx: ガバガバ
    self.configHandler = configHandler

  #@staticmethod
  def targetView(self, cell):
    return cell.contentView.subviews()[0] if cell != None else None
'''

