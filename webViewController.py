"""
  note: Storyboard 実装なし
"""
import ctypes
from pathlib import Path

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.runtime import send_super, objc_id
from pyrubicon.objc.types import CGRectMake

from rbedge.enumerations import NSURLErrorNotConnectedToInternet
from rbedge.functions import NSStringFromClass

from pyLocalizedString import localizedString

from rbedge import pdbr

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')
UIColor = ObjCClass('UIColor')

WKWebView = ObjCClass('WKWebView')
WKWebViewConfiguration = ObjCClass('WKWebViewConfiguration')
NSURL = ObjCClass('NSURL')
"""
  NOTE:
    If your app customizes, interacts with, or controls the display of web content, use the WKWebView class.
    If you want to view a website from anywhere on the Internet, use the SFSafariViewController class.
    アプリが Web コンテンツの表示をカスタマイズ、操作、または制御する場合は、WKWebView クラスを使用します。
    インターネット上のどこからでも Web サイトを表示したい場合は、SFSafariViewController クラスを使用します。
"""


class WebViewController(UIViewController):

  wkWebView: WKWebView = objc_property()

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    #print(f'\t - {NSStringFromClass(__class__)}: dealloc')
    pass

  @objc_method
  def loadView(self):
    send_super(__class__, self, 'loadView')
    #print(f'\t{NSStringFromClass(__class__)}: loadView')

  # MARK: - View Life Cycle
  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    self.navigationItem.title = localizedString('WebViewTitle') if (
      title := self.navigationItem.title) is None else title
    self.view.backgroundColor = UIColor.systemBackgroundColor()

    _zero = CGRectMake(0.0, 0.0, 0.0, 0.0)

    _configuration = WKWebViewConfiguration.new()
    _configuration.setMediaPlaybackRequiresUserAction_(True)

    # todo: method の名前衝突を避けるため
    wkWebView = WKWebView.alloc().initWithFrame_configuration_(
      _zero, _configuration)
    # So we can capture failures in "didFailProvisionalNavigation".
    wkWebView.navigationDelegate = self

    # --- Layout
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide

    self.view.addSubview_(wkWebView)
    wkWebView.translatesAutoresizingMaskIntoConstraints = False
    NSLayoutConstraint.activateConstraints_([
      wkWebView.topAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.topAnchor),
      wkWebView.leadingAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.leadingAnchor),
      wkWebView.trailingAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.trailingAnchor),
      wkWebView.bottomAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.bottomAnchor),
    ])

    self.wkWebView = wkWebView
    self.loadAddressURL()

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
    #print('\t↓ ---')

  @objc_method
  def viewWillDisappear_(self, animated: bool):
    #print('\t↑ ---')
    send_super(__class__,
               self,
               'viewWillDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print(f'\t{NSStringFromClass(__class__)}: viewWillDisappear_')

  @objc_method
  def viewDidDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #print(f'\t{NSStringFromClass(__class__)}: viewDidDisappear_')

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'\t{NSStringFromClass(__class__)}: didReceiveMemoryWarning')

  # MARK: - Loading
  @objc_method
  def loadAddressURL(self):
    # Set the content to local html in our app bundle.
    if (url := NSURL.fileURLWithPath_(
        str(
          Path(
            './UIKitCatalogCreatingAndCustomizingViewsAndControls/UIKitCatalog/Base.lproj/content.html'
          ).absolute()))):
      self.wkWebView.loadFileURL_allowingReadAccessToURL_(url, url)

  # MARK: - WKNavigationDelegate
  @objc_method
  def webView_didFailProvisionalNavigation_withError_(self, webView,
                                                      navigation, error):
    webKitError = error
    if webKitError.code == NSURLErrorNotConnectedToInternet:
      localizedErrorMessage = localizedString('An error occurred:')
      message = f'{localizedErrorMessage} {error.localizedDescription}'
      errorHTML = f'<!doctype html><html><body><font color = "red"><div style=\"width: 100%%; text-align: center; font-size: 36pt;\">{message}</div></font></body></html>'
      webView.loadHTMLString_baseURL_(errorHTML, None)


if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import UIModalPresentationStyle

  main_vc = WebViewController.new()
  _title = NSStringFromClass(WebViewController)
  main_vc.navigationItem.title = _title

  presentation_style = UIModalPresentationStyle.fullScreen

  app = App(main_vc)
  app.main_loop(presentation_style)

