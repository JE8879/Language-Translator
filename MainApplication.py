# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Translate.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from googletrans import Translator
from FormTools import Ui_FormTools
import socket
import sys

class Ui_MainForm(object):
    def setupUi(self, MainForm):

        MainForm.setObjectName("MainForm")
        MainForm.resize(942, 458)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/IMG-TranslateForm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainForm.setWindowIcon(icon)
        MainForm.setStyleSheet("background-color: rgb(39, 55, 70);")
        MainForm.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

        #Open Styles
        self.file = open('main.css','r')
        self.styleSheet = self.file.read()

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
        self.textFirstLanguage.textChanged.connect(self.ExecuteTranslate)

        self.textLastLanguage = QtWidgets.QTextEdit(MainForm)
        self.textLastLanguage.setGeometry(QtCore.QRect(480, 50, 441, 351))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.textLastLanguage.setFont(font)
        self.textLastLanguage.setStyleSheet("border-style:insert;border:1px solid;border-color:rgb(88, 214, 141);\n"
		"color:white;")
        self.textLastLanguage.setObjectName("textLastLanguage")

        self.BtnTools = QtWidgets.QPushButton(MainForm)
        self.BtnTools.setGeometry(QtCore.QRect(480, 410, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BtnTools.setFont(font)
        self.BtnTools.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BtnTools.setStyleSheet(self.styleSheet)
        iconTools = QtGui.QIcon()
        iconTools.addPixmap(QtGui.QPixmap("Images/IMG-Tools.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnTools.setIcon(iconTools)
        self.BtnTools.setIconSize(QtCore.QSize(16, 16))
        self.BtnTools.setAutoDefault(False)
        self.BtnTools.setObjectName("BtnTools")
        self.BtnTools.clicked.connect(self.OpenFormTools)

        self.BtnPaste = QtWidgets.QPushButton(MainForm)
        self.BtnPaste.setGeometry(QtCore.QRect(20, 410, 101, 31))
        self.BtnPaste.setFont(font)
        self.BtnPaste.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BtnPaste.setStyleSheet(self.styleSheet)
        iconPaste = QtGui.QIcon()
        iconPaste.addPixmap(QtGui.QPixmap("Images/IMG-Paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnPaste.setIcon(iconPaste)
        self.BtnPaste.setIconSize(QtCore.QSize(16, 16))
        self.BtnPaste.setAutoDefault(False)
        self.BtnPaste.setObjectName("BtnPaste")
        self.BtnPaste.clicked.connect(self.PasteText)

        self.BtnClean = QtWidgets.QPushButton(MainForm)
        self.BtnClean.setGeometry(QtCore.QRect(130, 410, 101, 31))
        self.BtnClean.setFont(font)
        self.BtnClean.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BtnClean.setStyleSheet(self.styleSheet)
        iconClear = QtGui.QIcon()
        iconClear.addPixmap(QtGui.QPixmap("Images/IMG-Clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnClean.setIcon(iconClear)
        self.BtnClean.setIconSize(QtCore.QSize(16, 16))
        self.BtnClean.setAutoDefault(False)
        self.BtnClean.setObjectName("BtnClean")
        self.BtnClean.clicked.connect(self.ClearText)

        self.BtnCopy = QtWidgets.QPushButton(MainForm)
        self.BtnCopy.setGeometry(QtCore.QRect(800, 410, 121, 31))
        self.BtnCopy.setFont(font)
        self.BtnCopy.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BtnCopy.setStyleSheet(self.styleSheet)
        iconCopy = QtGui.QIcon()
        iconCopy.addPixmap(QtGui.QPixmap("Images/IMG-Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnCopy.setIcon(iconCopy)
        self.BtnCopy.setIconSize(QtCore.QSize(16, 16))
        self.BtnCopy.setAutoDefault(False)
        self.BtnCopy.setObjectName("BtnCopy")
        self.BtnCopy.clicked.connect(self.CopyText)

        self.BtnChange = QtWidgets.QPushButton(MainForm)
        self.BtnChange.setGeometry(QtCore.QRect(420, 10, 111, 31))
        self.BtnChange.setFont(font)
        self.BtnChange.setStyleSheet(self.styleSheet)
        iconTransfer = QtGui.QIcon()
        iconTransfer.addPixmap(QtGui.QPixmap("Images/IMG-Trasfer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnChange.setIcon(iconTransfer)
        self.BtnChange.setObjectName("BtnChange")
        self.BtnChange.clicked.connect(self.ChangeLanguage)

        self.CboFirstLanguage = QtWidgets.QComboBox(MainForm)
        self.CboFirstLanguage.setGeometry(QtCore.QRect(20, 20, 181, 22))
        self.CboFirstLanguage.setFont(font)
        self.CboFirstLanguage.setStyleSheet(self.styleSheet)
        self.CboFirstLanguage.setObjectName("CboFirstLanguage")

        self.CboLastLanguage = QtWidgets.QComboBox(MainForm)
        self.CboLastLanguage.setGeometry(QtCore.QRect(740, 20, 181, 22))
        self.CboLastLanguage.setFont(font)
        self.CboLastLanguage.setStyleSheet(self.styleSheet)
        self.CboLastLanguage.setObjectName("CboLastLanguage")

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Language Translate"))

        self.BtnTools.setText(_translate("MainForm", "Tools..."))
        self.BtnPaste.setText(_translate("MainForm", "Paste"))
        self.BtnClean.setText(_translate("MainForm", "Clean"))
        self.BtnCopy.setText(_translate("MainForm", "Copy"))
        self.BtnChange.setText(_translate("MainForm", "Change"))

        self.InitCombox()

        #Creamos una Instancion a la Clase Translator
        self.translator = Translator()       

    def InitCombox(self):
    	self.CboFirstLanguage.addItems(["English","Spanish","German","French","Italian","Japanese","Chinese"])
    	self.CboLastLanguage.addItems(["English","Spanish","German","French","Italian","Japanese","Chinese"])
    
    #Se Ejecuta el Traductor
    def ExecuteTranslate(self):
        isConnected = self.CheckConnection()

        if(isConnected):
            self.Translate()
        else:
            self.MessageBox("No se pudo establecer la Conexion a Internet","Error")
            return

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

    def OpenFormTools(self):        
        self.window = QtWidgets.QWidget()
        
        self.ui = Ui_FormTools(self.textLastLanguage.toPlainText())
        self.ui.setupUi(self.window)
        self.window.show()

    #Se Verifica la Conexion a internet
    def CheckConnection(self):
        REMOTE_SERVER = "www.google.com"
        try:
            host = socket.gethostbyname(REMOTE_SERVER)
            connect = socket.create_connection((host,80),2)
            return True
        except:
            return False
    
    #Se Crea un Mensage Personalizable
    def MessageBox(self,message,title):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()
        return



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    MainForm = QtWidgets.QWidget()

    ui = Ui_MainForm()

    ui.setupUi(MainForm)

    MainForm.show()

    sys.exit(app.exec_())
