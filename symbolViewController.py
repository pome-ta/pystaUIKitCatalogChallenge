from enum import Enum

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import SEL, send_super, objc_id

from rbedge.enumerations import (
  UITableViewStyle,
  UIControlEvents,
  UISwitchStyle,
  UIUserInterfaceIdiom,
)

from caseElement import CaseElement
from pyLocalizedString import localizedString
from rbedge import pdbr

from baseTableViewController import BaseTableViewController
from storyboard.symbolViewController import prototypes

UIImage = ObjCClass('UIImage')
UIColor = ObjCClass('UIColor')


# Cell identifier for each SF Symbol table view cell.
class SymbolKind(Enum):
  plainSymbol='plainSymbol'
  tintedSymbol='tintedSymbol'
  largeSizeSymbol='largeSizeSymbol'
  hierarchicalColorSymbol='hierarchicalColorSymbol'
  paletteColorsSymbol='paletteColorsSymbol'
  preferringMultiColorSymbol='preferringMultiColorSymbol'


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

    
    self.testCells.extend([
      CaseElement(localizedString('PlainSymbolTitle'),
                  SymbolKind.plainSymbol.value,
                  self.configurePlainSymbol_),
    ])


  # MARK: - UITableViewDataSource
  # MARK: - Configuration
  @objc_method
  def configurePlainSymbol_(self, imageView):
    image = UIImage.systemImageNamed_('cloud.sun.rain.fill')
    imageView.image=image
    



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
