/*
See LICENSE folder for this sample’s licensing information.

Abstract:
A view controller that demonstrates how to use `UIButton`.
 The buttons are created using storyboards, but each of the system buttons can be created in code by
 using the UIButton.init(type buttonType: UIButtonType) initializer.
 
 See the UIButton interface for a comprehensive list of the various UIButtonType values.
 
「UIButton」の使用方法を示すビュー コントローラー。
   ボタンはストーリーボードを使用して作成されますが、各システム ボタンは次のようにコードで作成できます。
   UIButton.init(type buttonType: UIButtonType) イニシャライザを使用します。
 
さまざまな UIButtonType 値の包括的なリストについては、UIButton インターフェイスを参照してください。
*/

import UIKit

class ButtonViewController: BaseTableViewController {
    
    // Cell identifier for each button table view cell.
    // 各ボタンテーブルビューセルのセル識別子。
    enum ButtonKind: String, CaseIterable {
        case buttonSystem
        case buttonDetailDisclosure
        case buttonSystemAddContact
        case buttonClose
        case buttonStyleGray
        case buttonStyleTinted
        case buttonStyleFilled
        case buttonCornerStyle
        case buttonToggle
        case buttonTitleColor
        case buttonImage
        case buttonAttrText
        case buttonSymbol
        case buttonLargeSymbol
        case buttonTextSymbol
        case buttonSymbolText
        case buttonMultiTitle
        case buttonBackground
        case addToCartButton
        case buttonUpdateActivityHandler
        case buttonUpdateHandler
        case buttonImageUpdateHandler
    }
    
    // MARK: - Properties

    // "Add to Cart" Button
    var cartItemCount: Int = 0
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        testCells.append(contentsOf: [
            // 0
            CaseElement(title: NSLocalizedString("DefaultTitle", comment: ""),
                        cellID: ButtonKind.buttonSystem.rawValue,
                        configHandler: configureSystemTextButton),
            // 1
            CaseElement(title: NSLocalizedString("DetailDisclosureTitle", comment: ""),
                        cellID: ButtonKind.buttonDetailDisclosure.rawValue,
                        configHandler: configureSystemDetailDisclosureButton),
            // 2
            CaseElement(title: NSLocalizedString("AddContactTitle", comment: ""),
                        cellID: ButtonKind.buttonSystemAddContact.rawValue,
                        configHandler: configureSystemContactAddButton),
            // 3
            CaseElement(title: NSLocalizedString("CloseTitle", comment: ""),
                        cellID: ButtonKind.buttonClose.rawValue,
                        configHandler: configureCloseButton)
        ])
        
       if #available(iOS 15, *) {
            // These button styles are available on iOS 15 or later.
            // これらのボタン スタイルは、iOS 15 以降で利用できます。
            testCells.append(contentsOf: [
                // 4
                CaseElement(title: NSLocalizedString("GrayTitle", comment: ""),
                            cellID: ButtonKind.buttonStyleGray.rawValue,
                            configHandler: configureStyleGrayButton),
                
                // 5
                CaseElement(title: NSLocalizedString("TintedTitle", comment: ""),
                            cellID: ButtonKind.buttonStyleTinted.rawValue,
                            configHandler: configureStyleTintedButton),
                
                // 6
                CaseElement(title: NSLocalizedString("FilledTitle", comment: ""),
                            cellID: ButtonKind.buttonStyleFilled.rawValue,
                            configHandler: configureStyleFilledButton),
                
                // 7
                CaseElement(title: NSLocalizedString("CornerStyleTitle", comment: ""),
                            cellID: ButtonKind.buttonCornerStyle.rawValue,
                            configHandler: configureCornerStyleButton),
                
                // 8
                CaseElement(title: NSLocalizedString("ToggleTitle", comment: ""),
                            cellID: ButtonKind.buttonToggle.rawValue,
                            configHandler: configureToggleButton)
            ])
        }

        if traitCollection.userInterfaceIdiom != .mac {
            // Colored button titles only on iOS.
            testCells.append(contentsOf: [
                // 9
                CaseElement(title: NSLocalizedString("ButtonColorTitle", comment: ""),
                            cellID: ButtonKind.buttonTitleColor.rawValue,
                            configHandler: configureTitleTextButton)
            ])
        }

        testCells.append(contentsOf: [
            // 10
            CaseElement(title: NSLocalizedString("ImageTitle", comment: ""),
                        cellID: ButtonKind.buttonImage.rawValue,
                        configHandler: configureImageButton),
            // 11
            CaseElement(title: NSLocalizedString("AttributedStringTitle", comment: ""),
                        cellID: ButtonKind.buttonAttrText.rawValue,
                        configHandler: configureAttributedTextSystemButton),
            // 12
            CaseElement(title: NSLocalizedString("SymbolTitle", comment: ""),
                        cellID: ButtonKind.buttonSymbol.rawValue,
                        configHandler: configureSymbolButton)
        ])
        
        if #available(iOS 15, *) {
            // This case uses UIButtonConfiguration which is available on iOS 15 or later.
            if traitCollection.userInterfaceIdiom != .mac {
                // UIButtonConfiguration for large images available only on iOS.
                // iOS でのみ使用できる大きな画像の UIButtonConfiguration。
                testCells.append(contentsOf: [
                    // 13
                    CaseElement(title: NSLocalizedString("LargeSymbolTitle", comment: ""),
                                cellID: ButtonKind.buttonLargeSymbol.rawValue,
                                configHandler: configureLargeSymbolButton)
                ])
            }
        }
        
        if #available(iOS 15, *) {
            testCells.append(contentsOf: [
                // 14
                CaseElement(title: NSLocalizedString("StringSymbolTitle", comment: ""),
                            cellID: ButtonKind.buttonTextSymbol.rawValue,
                            configHandler: configureTextSymbolButton),
                // 15
                CaseElement(title: NSLocalizedString("SymbolStringTitle", comment: ""),
                            cellID: ButtonKind.buttonSymbolText.rawValue,
                            configHandler: configureSymbolTextButton),
                
                // 16
                CaseElement(title: NSLocalizedString("BackgroundTitle", comment: ""),
                            cellID: ButtonKind.buttonBackground.rawValue,
                            configHandler: configureBackgroundButton),
                
                // Multi-title button: title for normal and highlight state, setTitle(.highlighted) is for iOS 15 and later.
                // 17
                CaseElement(title: NSLocalizedString("MultiTitleTitle", comment: ""),
                            cellID: ButtonKind.buttonMultiTitle.rawValue,
                            configHandler: configureMultiTitleButton),
                
                // Various button effects done to the addToCartButton are available only on iOS 15 or later.
                // 18
                CaseElement(title: NSLocalizedString("AddToCartTitle", comment: ""),
                            cellID: ButtonKind.addToCartButton.rawValue,
                            configHandler: configureAddToCartButton),
                
                // UIButtonConfiguration with updateHandlers is available only on iOS 15 or later.
                // 19
                CaseElement(title: NSLocalizedString("UpdateActivityHandlerTitle", comment: ""),
                            cellID: ButtonKind.buttonUpdateActivityHandler.rawValue,
                            configHandler: configureUpdateActivityHandlerButton),
                // 20
                CaseElement(title: NSLocalizedString("UpdateHandlerTitle", comment: ""),
                            cellID: ButtonKind.buttonUpdateHandler.rawValue,
                            configHandler: configureUpdateHandlerButton),
                
                // 21
                CaseElement(title: NSLocalizedString("UpdateImageHandlerTitle", comment: ""),
                            cellID: ButtonKind.buttonImageUpdateHandler.rawValue,
                            configHandler: configureUpdateImageHandlerButton)
            ])
        }
    }

}
