from enum import Enum

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, objc_id

from rbedge.enumerations import (
  UITableViewStyle,
  UIImageSymbolWeight,
  UIImageSymbolScale,
)

from caseElement import CaseElement
from pyLocalizedString import localizedString
from rbedge import pdbr

from baseTableViewController import BaseTableViewController
from storyboard.symbolViewController import prototypes

UIImage = ObjCClass('UIImage')
UIImageSymbolConfiguration = ObjCClass('UIImageSymbolConfiguration')
UIColor = ObjCClass('UIColor')


# Cell identifier for each SF Symbol table view cell.
class SymbolKind(Enum):
  plainSymbol = 'plainSymbol'
  tintedSymbol = 'tintedSymbol'
  largeSizeSymbol = 'largeSizeSymbol'
  hierarchicalColorSymbol = 'hierarchicalColorSymbol'
  paletteColorsSymbol = 'paletteColorsSymbol'
  preferringMultiColorSymbol = 'preferringMultiColorSymbol'


class SymbolViewController(BaseTableViewController):

  @objc_method
  def init(self):
    send_super(__class__, self, 'init')  # xxx: 不要?
    tableViewStyle = UITableViewStyle.grouped
    self.initWithStyle_(tableViewStyle)

    self.testCells = []
    self.initPrototype()

    return self

  @objc_method
  def initPrototype(self):
    [
      self.tableView.registerClass_forCellReuseIdentifier_(
        prototype['cellClass'], prototype['identifier'])
      for prototype in prototypes
    ]

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')  # xxx: 不要?
    self.navigationItem.title = localizedString('SymbolsTitle') if (
      title := self.navigationItem.title) is None else title

    '''
    self.testCells.extend([
      CaseElement(localizedString('PlainSymbolTitle'),
                  SymbolKind.plainSymbol.value, self.configurePlainSymbol_),
      CaseElement(localizedString('TintedSymbolTitle'),
                  SymbolKind.tintedSymbol.value, self.configureTintedSymbol_),
      CaseElement(localizedString('LargeSymbolTitle'),
                  SymbolKind.largeSizeSymbol.value,
                  self.configureLargeSizeSymbol_),
    ])
    '''
    
    self.testCells.extend([
      CaseElement(localizedString('LargeSymbolTitle'),
                  SymbolKind.largeSizeSymbol.value,
                  self.configureLargeSizeSymbol_),
    ])

  @objc_method
  def viewWillAppear_(self, animated: bool):
    import ctypes
    send_super(__class__,
               self,
               'viewWillAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    # ---
    #pdbr.state(self)
    




  # MARK: - UITableViewDataSource
  
  @objc_method
  def tableView_heightForRowAtIndexPath_(self, tableView, indexPath)->float:
    cellTest = self.testCells[indexPath.section]
    cell = tableView.dequeueReusableCellWithIdentifier_(cellTest.cellID)
    #print(cellTest.cellID)
    #pdbr.state(tableView)
    #print(cell.contentView.bounds.size.height)
    #pdbr.state(cell.contentView)
    return cell.contentView.bounds.size.height
    #return 200
  
  

  # MARK: - Configuration
  @objc_method
  def configurePlainSymbol_(self, imageView):
    image = UIImage.systemImageNamed_('cloud.sun.rain.fill')
    imageView.image = image

  @objc_method
  def configureTintedSymbol_(self, imageView):
    image = UIImage.systemImageNamed_('cloud.sun.rain.fill')
    imageView.image = image
    imageView.tintColor = UIColor.systemPurpleColor()

  @objc_method
  def configureLargeSizeSymbol_(self, imageView):
    image = UIImage.systemImageNamed_('cloud.sun.rain.fill')
    imageView.image = image
    #pdbr.state(imageView)
    #print(imageView)

    symbolConfig = UIImageSymbolConfiguration.configurationWithPointSize_weight_scale_(
      32.0, UIImageSymbolWeight.heavy, UIImageSymbolScale.large)
    imageView.preferredSymbolConfiguration = symbolConfig
    


if __name__ == '__main__':
  from rbedge.functions import NSStringFromClass
  from rbedge.enumerations import UIModalPresentationStyle
  from rbedge import present_viewController

  main_vc = SymbolViewController.new()
  _title = NSStringFromClass(SymbolViewController)
  main_vc.navigationItem.title = _title

  style = UIModalPresentationStyle.fullScreen
  #style = UIModalPresentationStyle.pageSheet
  #style = UIModalPresentationStyle.popover

  present_viewController(main_vc, style)

