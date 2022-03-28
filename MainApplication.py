import sys
import threading
from FrmTools import ToolsTranlator
from googletrans import Translator
from PyQt5 import QtCore, QtGui, QtWidgets, uic

class AppTranslator(QtWidgets.QWidget):
    # Contructor
    def __init__(self):
        # Find components and assing properties
        super(AppTranslator,self).__init__()

        uic.loadUi('Templates/MainForm.ui',self)

        self.gridLayout = self.findChild(QtWidgets.QGridLayout, 'gridLayout')

        # Create new MenuBar
        self.menuBar = QtWidgets.QMenuBar()
        self.fileMenu = QtWidgets.QMenu('File')

        self.menuBar.addMenu(self.fileMenu)
        self.fileMenu.addAction('Hello', lambda: print('Test Menu'))
        self.gridLayout.setMenuBar(self.menuBar)

        # ---------------------- QTextEdits ----------------------#
        self.textSrcLanguage = self.findChild(QtWidgets.QTextEdit, 'textSrcLanguage')
        self.textSrcLanguage.textChanged.connect(self.ExecuteTranslate)

        self.textDestLanguage = self.findChild(QtWidgets.QTextEdit, 'textDestLanguage')

        # ---------------------- QPushButtons ----------------------#
        self.BtnPaste = self.findChild(QtWidgets.QPushButton, 'BtnPaste')
        self.BtnPaste.clicked.connect(self.PasteText)

        self.BtnCopy = self.findChild(QtWidgets.QPushButton, 'BtnCopy')
        self.BtnCopy.clicked.connect(self.CopyText)

        self.BtnClear = self.findChild(QtWidgets.QPushButton, 'BtnClear')
        self.BtnClear.clicked.connect(self.ClearText)

        self.BtnTools = self.findChild(QtWidgets.QPushButton, 'BtnTools')
        self.BtnTools.clicked.connect(self.OpenFormTools)

        self.BtnChange = self.findChild(QtWidgets.QPushButton, 'BtnChange')
        self.BtnChange.clicked.connect(self.ChangeLanguage)

        # ---------------------- QComboBoxes ----------------------#
        self.CboSrcLaguage = self.findChild(QtWidgets.QComboBox, 'CboSrcLaguage')
        self.CboDestLanguage = self.findChild(QtWidgets.QComboBox, 'CboDestLanguage')

        self.InitCombobox()
        
        self.translator = Translator()

        self.show()

    def ExecuteTranslate(self):
        threading.Thread(target=self.TranslateWords()).start()

    def TranslateWords(self):
        try:
            listLanguages = ['en','es','de','fr','it','ja','zh-tw']
            SrcLanguage = self.CboSrcLaguage.currentIndex()
            DestLanguage = self.CboDestLanguage.currentIndex()

            translation = self.translator.translate(self.textSrcLanguage.toPlainText(), src=str(listLanguages[SrcLanguage]), dest=str(listLanguages[DestLanguage]))
            self.textDestLanguage.setPlainText(translation.text)
        except:
            if(len(self.textSrcLanguage.toPlainText()) == 0):               
                self.textDestLanguage.clear()
            self.MessageBox('Ocurrio un Error en el Servidor', 'Atención')

    def InitCombobox(self):
        self.CboSrcLaguage.addItems(["English","Spanish","German","French","Italian","Japanese","Chinese"])
        self.CboDestLanguage.addItems(["English","Spanish","German","French","Italian","Japanese","Chinese"])

    def PasteText(self):
        clipboard = QtGui.QGuiApplication.clipboard()
        mimeData = clipboard.mimeData()

        if mimeData.hasText():
            result = mimeData.text()
            self.textSrcLanguage.setPlainText(result)

    def CopyText(self):
        clipboard = QtGui.QGuiApplication.clipboard()
        clipboard.setText(self.textDestLanguage.toPlainText())

    def ClearText(self):
        self.textSrcLanguage.clear()
        self.textDestLanguage.clear()
    
    def ChangeLanguage(self):
        SrcLanguage = self.CboSrcLaguage.currentIndex()
        DestLanguage = self.CboDestLanguage.currentIndex()

        self.CboSrcLaguage.setCurrentIndex(DestLanguage)
        self.CboDestLanguage.setCurrentIndex(SrcLanguage)

        textLastlanguage = self.textDestLanguage.toPlainText()
        self.textSrcLanguage.setPlainText(textLastlanguage)

    def MessageBox(self,message,title):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()
        return

    def OpenFormTools(self):
        self.toolWindow = ToolsTranlator(self.textDestLanguage.toPlainText())
        self.toolWindow.show()

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    window = AppTranslator()

    app.exec_()
