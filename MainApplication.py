# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Translate.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from googletrans import Translator
import sys

class Ui_MainForm(object):
    def setupUi(self, MainForm):

        MainForm.setObjectName("MainForm")
        MainForm.resize(942, 458)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/IMG-TranslateForm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainForm.setWindowIcon(icon)
        MainForm.setStyleSheet("background-color: rgb(39, 55, 70);")

        self.textFirstLanguage = QtWidgets.QTextEdit(MainForm)
        self.textFirstLanguage.setGeometry(QtCore.QRect(20, 50, 441, 351))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.textFirstLanguage.setFont(font)
        self.textFirstLanguage.setStyleSheet("border-style:insert;\n"
		"border:1px solid;\n"
		"border-color:rgb(88, 214, 141);\n"
		"color:white;\n"
		"")
        self.textFirstLanguage.setObjectName("textFirstLanguage")
        self.textFirstLanguage.textChanged.connect(self.Translate)

        self.textLastLanguage = QtWidgets.QTextEdit(MainForm)
        self.textLastLanguage.setGeometry(QtCore.QRect(480, 50, 441, 351))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.textLastLanguage.setFont(font)
        self.textLastLanguage.setStyleSheet("border-style:insert;\n"
		"border:1px solid;\n"
		"border-color:rgb(88, 214, 141);\n"
		"color:white;\n"
		"")
        self.textLastLanguage.setObjectName("textLastLanguage")

        self.BtnTranslate = QtWidgets.QPushButton(MainForm)
        self.BtnTranslate.setGeometry(QtCore.QRect(340, 410, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BtnTranslate.setFont(font)
        self.BtnTranslate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BtnTranslate.setStyleSheet("QPushButton{border-style:insert;border:1px solid;\n"
		"background-color:rgb(40, 116, 166);\n"
		"color:white;}\n"
		"QPushButton:hover{background-color:rgb(46, 134, 193);}\n"
		"QPushButton:Pressed{background-color:rgb(52, 152, 219);}")
        icon.addPixmap(QtGui.QPixmap("Images/IMG-Ttranslate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnTranslate.setIcon(icon)
        self.BtnTranslate.setIconSize(QtCore.QSize(16, 16))
        self.BtnTranslate.setAutoDefault(False)
        self.BtnTranslate.setObjectName("BtnTranslate")
        self.BtnTranslate.clicked.connect(self.Translate)

        self.BtnPaste = QtWidgets.QPushButton(MainForm)
        self.BtnPaste.setGeometry(QtCore.QRect(20, 410, 101, 31))
        self.BtnPaste.setFont(font)
        self.BtnPaste.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BtnPaste.setStyleSheet("QPushButton{border-style:insert;border:1px solid;\n"
		"background-color:rgb(40, 116, 166);\n"
		"color:white;}\n"
		"QPushButton:hover{background-color:rgb(46, 134, 193);}\n"
		"QPushButton:Pressed{background-color:rgb(52, 152, 219);}")
        icon.addPixmap(QtGui.QPixmap("Images/IMG-Paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnPaste.setIcon(icon)
        self.BtnPaste.setIconSize(QtCore.QSize(16, 16))
        self.BtnPaste.setAutoDefault(False)
        self.BtnPaste.setObjectName("BtnPaste")
        self.BtnPaste.clicked.connect(self.PasteText)

        self.BtnClean = QtWidgets.QPushButton(MainForm)
        self.BtnClean.setGeometry(QtCore.QRect(130, 410, 101, 31))
        self.BtnClean.setFont(font)
        self.BtnClean.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BtnClean.setStyleSheet("QPushButton{border-style:insert;border:1px solid;\n"
		"background-color:rgb(40, 116, 166);\n"
		"color:white;}\n"
		"QPushButton:hover{background-color:rgb(46, 134, 193);}\n"
		"QPushButton:Pressed{background-color:rgb(52, 152, 219);}")
        icon.addPixmap(QtGui.QPixmap("Images/IMG-Clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnClean.setIcon(icon)
        self.BtnClean.setIconSize(QtCore.QSize(16, 16))
        self.BtnClean.setAutoDefault(False)
        self.BtnClean.setObjectName("BtnClean")
        self.BtnClean.clicked.connect(self.ClearText)

        self.BtnCopy = QtWidgets.QPushButton(MainForm)
        self.BtnCopy.setGeometry(QtCore.QRect(800, 410, 121, 31))
        self.BtnCopy.setFont(font)
        self.BtnCopy.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BtnCopy.setStyleSheet("QPushButton{border-style:insert;border:1px solid;\n"
		"background-color:rgb(40, 116, 166);\n"
		"color:white;}\n"
		"QPushButton:hover{background-color:rgb(46, 134, 193);}\n"
		"QPushButton:Pressed{background-color:rgb(52, 152, 219);}")
        icon.addPixmap(QtGui.QPixmap("Images/IMG-Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnCopy.setIcon(icon)
        self.BtnCopy.setIconSize(QtCore.QSize(16, 16))
        self.BtnCopy.setAutoDefault(False)
        self.BtnCopy.setObjectName("BtnCopy")
        self.BtnCopy.clicked.connect(self.CopyText)

        self.BtnChange = QtWidgets.QPushButton(MainForm)
        self.BtnChange.setGeometry(QtCore.QRect(420, 10, 111, 31))
        self.BtnChange.setFont(font)
        self.BtnChange.setStyleSheet("QPushButton{border-style:insert;border:1px solid;\n"
		"background-color:rgb(225, 116, 16);\n"
		"color:white;}\n"
		"QPushButton:hover{background-color:rgb(243, 142, 50);}\n"
		"QPushButton:Pressed{background-color:rgb(221, 139, 64);}")
        icon.addPixmap(QtGui.QPixmap("Images/IMG-Trasfer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnChange.setIcon(icon)
        self.BtnChange.setObjectName("BtnChange")
        self.BtnChange.clicked.connect(self.ChangeLanguage)

        self.CboFirstLanguage = QtWidgets.QComboBox(MainForm)
        self.CboFirstLanguage.setGeometry(QtCore.QRect(20, 20, 181, 22))
        self.CboFirstLanguage.setFont(font)
        self.CboFirstLanguage.setStyleSheet("border-style:insert;\n"
		"border:1px solid;\n"
		"border-color:rgb(52, 152, 219);\n"
		"background-color:rgb(39, 55, 70);\n"
		"color:gray;\n"
		"")
        self.CboFirstLanguage.setObjectName("CboFirstLanguage")

        self.CboLastLanguage = QtWidgets.QComboBox(MainForm)
        self.CboLastLanguage.setGeometry(QtCore.QRect(740, 20, 181, 22))
        self.CboLastLanguage.setFont(font)
        self.CboLastLanguage.setStyleSheet("border-style:insert;\n"
		"border:1px solid;\n"
		"border-color:rgb(52, 152, 219);\n"
		"background-color:rgb(39, 55, 70);\n"
		"color:gray;\n"
		"")
        self.CboLastLanguage.setObjectName("CboLastLanguage")

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Language Translate"))

        self.BtnTranslate.setText(_translate("MainForm", "Traducir"))
        self.BtnPaste.setText(_translate("MainForm", "Pegar"))
        self.BtnClean.setText(_translate("MainForm", "Limpiar"))
        self.BtnCopy.setText(_translate("MainForm", "Copiar"))
        self.BtnChange.setText(_translate("MainForm", "Cambiar"))

        self.InitCombox()

        #Creamos una Instancion a la Clase Translator
        self.translator = Translator()

    def InitCombox(self):
    	self.CboFirstLanguage.addItems(["English","Spanish","German","French","Italian","Japanese","Chinese"])
    	self.CboLastLanguage.addItems(["English","Spanish","German","French","Italian","Japanese","Chinese"])

    def Translate(self):
        #Controlamos los Errores que se Puedan Generar
        try:
             #Arreglo de Idiomas
            listLanguages=['en','es','de',"fr","it","ja","zh-tw"]

            SrcLanguage  = self.CboFirstLanguage.currentIndex()
            DestLanguage = self.CboLastLanguage.currentIndex()        

            result = self.translator.translate(self.textFirstLanguage.toPlainText(),src=str(listLanguages[SrcLanguage]),
                                            dest=str(listLanguages[DestLanguage]))
            self.textLastLanguage.setPlainText(result.text)
        except:
            if(len(self.textLastLanguage.toPlainText()) == 1):
                self.textLastLanguage.clear()
            return

    def PasteText(self):
        clipboard = QtGui.QGuiApplication.clipboard()
        mimeData = clipboard.mimeData()

        if mimeData.hasText():
            result = mimeData.text()
            self.textFirstLanguage.setPlainText(result)

    def CopyText(self):
        clipboard = QtGui.QGuiApplication.clipboard()
        clipboard.setText(self.textLastLanguage.toPlainText())

    def ClearText(self):
        self.textFirstLanguage.clear()
        self.textLastLanguage.clear()

    def ChangeLanguage(self):
        SrcLanguage = self.CboFirstLanguage.currentIndex()
        DestLanguage = self.CboLastLanguage.currentIndex()

        self.CboFirstLanguage.setCurrentIndex(DestLanguage)
        self.CboLastLanguage.setCurrentIndex(SrcLanguage)

        textLastlanguage = self.textLastLanguage.toPlainText()
        self.textFirstLanguage.setPlainText(textLastlanguage)

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    MainForm = QtWidgets.QWidget()

    ui = Ui_MainForm()

    ui.setupUi(MainForm)

    MainForm.show()

    sys.exit(app.exec_())
