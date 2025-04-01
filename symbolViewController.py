import ctypes
from enum import Enum

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, objc_id
from pyrubicon.objc.types import NSInteger

from rbedge.enumerations import (
  UIImageSymbolWeight,
  UIImageSymbolScale,
)

from caseElement import CaseElement
from pyLocalizedString import localizedString

from baseTableViewController import BaseTableViewController
from storyboard.symbolViewController import prototypes

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

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
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    print(f'\t- {NSStringFromClass(__class__)}: dealloc')

  @objc_method
  def initWithStyle_(self, style: NSInteger) -> ObjCInstance:
    send_super(__class__,
               self,
               'initWithStyle:',
               style,
               restype=objc_id,
               argtypes=[
                 NSInteger,
               ])
    #print(f'\t{NSStringFromClass(__class__)}: initWithStyle_')
    return self

  @objc_method
  def loadView(self):
    send_super(__class__, self, 'loadView')
    #print(f'\t{NSStringFromClass(__class__)}: loadView')
    [
      self.tableView.registerClass_forCellReuseIdentifier_(
        prototype['cellClass'], prototype['identifier'])
      for prototype in prototypes
    ]

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    #print(f'\t{NSStringFromClass(__class__)}: viewDidLoad')
    
    # --- Navigation
    self.navigationItem.title = localizedString('SymbolsTitle') if (
      title := self.navigationItem.title) is None else title

    self.testCellsAppendContentsOf_([
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('PlainSymbolTitle'), SymbolKind.plainSymbol.value,
        'configurePlainSymbol:'),
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('TintedSymbolTitle'), SymbolKind.tintedSymbol.value,
        'configureTintedSymbol:'),
      CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
        localizedString('LargeSymbolTitle'), SymbolKind.largeSizeSymbol.value,
        'configureLargeSizeSymbol:'),
    ])

    if True:  # wip: `available(iOS 15, *)`
      # These type SF Sybols, and variants are available on iOS 15, Mac Catalyst 15 or later.
      self.testCellsAppendContentsOf_([
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('HierarchicalSymbolTitle'),
          SymbolKind.hierarchicalColorSymbol.value,
          'configureHierarchicalSymbol:'),
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('PaletteSymbolTitle'),
          SymbolKind.paletteColorsSymbol.value,
          'configurePaletteColorsSymbol:'),
        CaseElement.alloc().initWithTitle_cellID_configHandlerName_(
          localizedString('PreferringMultiColorSymbolTitle'),
          SymbolKind.preferringMultiColorSymbol.value,
          'configurePreferringMultiColorSymbol:'),
      ])

  @objc_method
  def viewWillAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print(f'\t{NSStringFromClass(__class__)}: viewWillAppear_')

  @objc_method
  def viewDidAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print(f'\t{NSStringFromClass(__class__)}: viewDidAppear_')

  @objc_method
  def viewWillDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    # print(f'\t{NSStringFromClass(__class__)}: viewWillDisappear_')

  @objc_method
  def viewDidDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    print(f'\t{NSStringFromClass(__class__)}: viewDidDisappear_')

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'\t{NSStringFromClass(__class__)}: didReceiveMemoryWarning')

  # MARK: - UITableViewDataSource
  @objc_method
  def tableView_heightForRowAtIndexPath_(self, tableView, indexPath) -> float:
    cellTest = self.testCells[indexPath.section]
    cell = tableView.dequeueReusableCellWithIdentifier_(cellTest.cellID)
    return cell.contentView.bounds.size.height

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
    symbolConfig = UIImageSymbolConfiguration.configurationWithPointSize_weight_scale_(
      32.0, UIImageSymbolWeight.heavy, UIImageSymbolScale.large)
    imageView.preferredSymbolConfiguration = symbolConfig

  # @available(iOS 15.0, *)
  @objc_method
  def configureHierarchicalSymbol_(self, imageView):
    imageConfig = UIImageSymbolConfiguration.configurationWithHierarchicalColor_(
      UIColor.systemRedColor())

    hierarchicalSymbol = UIImage.systemImageNamed_('cloud.sun.rain.fill')
    imageView.image = hierarchicalSymbol
    imageView.preferredSymbolConfiguration = imageConfig

  # @available(iOS 15.0, *)
  @objc_method
  def configurePaletteColorsSymbol_(self, imageView):
    palleteSymbolConfig = UIImageSymbolConfiguration.configurationWithPaletteColors_(
      [
        UIColor.systemRedColor(),
        UIColor.systemOrangeColor(),
        UIColor.systemYellowColor(),
      ])

    palleteSymbol = UIImage.systemImageNamed_('battery.100.bolt')
    imageView.image = palleteSymbol
    imageView.backgroundColor = UIColor.darkTextColor()
    imageView.preferredSymbolConfiguration = palleteSymbolConfig

  # @available(iOS 15.0, *)
  @objc_method
  def configurePreferringMultiColorSymbol_(self, imageView):
    preferredSymbolConfig = UIImageSymbolConfiguration.configurationPreferringMulticolor(
    )
    preferredSymbol = UIImage.systemImageNamed_('circle.hexagongrid.fill')
    imageView.image = preferredSymbol
    imageView.preferredSymbolConfiguration = preferredSymbolConfig


if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import (
    UITableViewStyle,
    UIModalPresentationStyle,
  )

  table_style = UITableViewStyle.grouped
  main_vc = SymbolViewController.alloc().initWithStyle_(table_style)
  _title = NSStringFromClass(SymbolViewController)
  main_vc.navigationItem.title = _title

  # presentation_style = UIModalPresentationStyle.fullScreen
  presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

