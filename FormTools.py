# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormToolsImport.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from docx import Document
import textwrap
import sys

class Ui_FormTools(object):
    #Se Crean el Contructor y pedimos el Texto 
    def __init__(self,getText):
        self.getText = getText

    def setupUi(self, FormTools):

        FormTools.resize(332, 337)
        FormTools.setMinimumSize(QtCore.QSize(332, 337))
        mainIcon = QtGui.QIcon()
        mainIcon.addPixmap(QtGui.QPixmap("Images/IMG-Tools.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormTools.setWindowIcon(mainIcon)
        FormTools.setStyleSheet("background-color: rgb(44, 62, 80);")
        FormTools.setObjectName("FormTools")

        self.groupBox = QtWidgets.QGroupBox(FormTools)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 311, 161))
        self.groupBox.setStyleSheet("QGroupBox{color:white;}")
        self.groupBox.setObjectName("groupBox")

        self.BtnPdf = QtWidgets.QPushButton(self.groupBox)
        self.BtnPdf.setGeometry(QtCore.QRect(10, 50, 141, 71))
        self.BtnPdf.setStyleSheet("QPushButton#BtnPdf{background-color:rgb(128, 139, 150);;border:solid 1px black;color:white;\n"
        "border-radius: 10px;}\n"
        "QPushButton#BtnPdf:hover{background-color:rgb(205, 97, 85);}")
        self.BtnPdf.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/IMG-Pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnPdf.setIcon(icon)
        self.BtnPdf.setIconSize(QtCore.QSize(50, 50))
        self.BtnPdf.setCheckable(True)
        self.BtnPdf.setChecked(False)
        self.BtnPdf.setObjectName("BtnPdf")
        self.BtnPdf.clicked.connect(self.CheckBtnPdf)

        self.BtnWord = QtWidgets.QPushButton(self.groupBox)
        self.BtnWord.setGeometry(QtCore.QRect(160, 50, 141, 71))
        self.BtnWord.setStyleSheet("QPushButton#BtnWord{background-color:rgb(128, 139, 150);;border:solid 1px black;\n"
        "border-radius: 10px;}\n"
        "QPushButton#BtnWord:hover{background-color:rgb(59, 134, 204);}")
        self.BtnWord.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/IMG-Word.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnWord.setIcon(icon1)
        self.BtnWord.setIconSize(QtCore.QSize(50, 50))
        self.BtnWord.setCheckable(True)
        self.BtnWord.setObjectName("BtnWord")
        self.BtnWord.clicked.connect(self.CheckBtnWord)

        self.groupBox_2 = QtWidgets.QGroupBox(FormTools)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 180, 311, 151))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())

        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(311, 151))
        self.groupBox_2.setMaximumSize(QtCore.QSize(151, 151))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")

        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 30, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(144, 148, 151);")
        self.label.setObjectName("label")

        self.textTitle = QtWidgets.QLineEdit(self.groupBox_2)
        self.textTitle.setGeometry(QtCore.QRect(60, 30, 211, 20))
        self.textTitle.setStyleSheet("QLineEdit#textTitle{color:white;}")
        self.textTitle.setObjectName("textTitle")

        self.BtnAccept = QtWidgets.QPushButton(self.groupBox_2)
        self.BtnAccept.setGeometry(QtCore.QRect(20, 110, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.BtnAccept.setFont(font)
        self.BtnAccept.setStyleSheet("QPushButton{color:white;background-color: rgb(205, 97, 85);border:solid 1px black;}\n"
        "QPushButton:hover{background-color: rgb(229, 152, 102);}\n"
        "QPushButton:pressed{background-color: rgb(220, 118, 51);}")
        self.BtnAccept.setObjectName("BtnAccept")
        self.BtnAccept.clicked.connect(self.StatusCheckButton)
      

        self.BtnCancel = QtWidgets.QPushButton(self.groupBox_2)
        self.BtnCancel.setGeometry(QtCore.QRect(180, 110, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.BtnCancel.setFont(font)
        self.BtnCancel.setStyleSheet("QPushButton{color:white;background-color: rgb(205, 97, 85);border:solid 1px black;}\n"
        "QPushButton:hover{background-color: rgb(229, 152, 102);}\n"
        "QPushButton:pressed{background-color: rgb(220, 118, 51);}")
        self.BtnCancel.setObjectName("BtnCancel")

        self.retranslateUi(FormTools)
        QtCore.QMetaObject.connectSlotsByName(FormTools)

    def retranslateUi(self, FormTools):
        _translate = QtCore.QCoreApplication.translate
        FormTools.setWindowTitle(_translate("FormTools", "Tools"))
        self.groupBox.setTitle(_translate("FormTools", "Save as"))
        self.groupBox_2.setStyleSheet(_translate("FormTools", "QGroupBox{color:white;}"))
        self.label.setText(_translate("FormTools", "Title:"))
        self.BtnAccept.setText(_translate("FormTools", "Accept"))
        self.BtnCancel.setText(_translate("FormTools", "Cancel"))

    #Se Activa el Button Pdf
    def CheckBtnPdf(self):
        if(self.BtnWord.isChecked()):
            #Si retorna True, cambia su valor a Falso
            self.BtnWord.setChecked(False)
            #Se le Aplica el Estilo Original
            self.BtnWord.setStyleSheet("QPushButton#BtnWord{background-color:rgb(128, 139, 150);;border:solid 1px black;border-radius: 10px;}\n"
            "QPushButton#BtnWord:hover{background-color:rgb(59, 134, 204);}")

            #Se Activa el Button 
            self.BtnPdf.setChecked(True)
            #Se le dan Estilos CSS
            self.BtnPdf.setStyleSheet("background-color:rgb(205, 97, 85);border-radius: 10px;")
        else:
            self.BtnPdf.setChecked(True)
            self.BtnPdf.setStyleSheet("background-color:rgb(205, 97, 85);border-radius: 10px;")
    
    #Se Activa el Button Word
    def CheckBtnWord(self):
        if(self.BtnPdf.isChecked()):
            #Si retorna True, cambia su valor a Falso
            self.BtnPdf.setChecked(False)
            #Se le Aplica el Estilo Original
            self.BtnPdf.setStyleSheet("QPushButton#BtnPdf{background-color:rgb(128, 139, 150);;border:solid 1px black;color:white;border-radius: 10px;}\n"
            "QPushButton#BtnPdf:hover{background-color:rgb(205, 97, 85);}")

            #Se Activa el Button 
            self.BtnWord.setChecked(True)
            #Se le dan Estilos CSS
            self.BtnWord.setStyleSheet("background-color:rgb(59, 134, 204);border-radius: 10px;")
        else:
            self.BtnWord.setChecked(True)
            self.BtnWord.setStyleSheet("background-color:rgb(59, 134, 204);border-radius: 10px;")

    #Obtiene el Button Activo
    def StatusCheckButton(self):
        if(self.BtnPdf.isChecked()):
           self.CreateNewPDF()
        if(self.BtnWord.isChecked()):
           self.CreateNewDocx()

    def CreateNewPDF(self):
        #Se Obtiene el Texto
        newText = self.getText

        if(len(self.textTitle.text()) == 0):
            self.MessageBox("Porfavor Coloque un Titulo","Atención")
            return

        #Se valida que el texto no este vacio
        if(len(newText) == 0):
           self.MessageBox("No se encontro Texto para crear el Documento","Atención")
           return
        else:
            #Establecemos el numero de caracteres antes de saltar la linea
            wrapper = textwrap.TextWrapper(width=103)
            lstText = wrapper.wrap(text=newText)

            #Le colocamos el titulo y establecemos el tipo de pagina
            newPDF = canvas.Canvas(self.textTitle.text() + ".pdf",pagesize=letter)
            #Se asigna el margen izquierdo done empezara a dibujar el texto
            pointX = 30
            #Se asigna la altura donde empieza a dibujar el texto
            pointY = 720

            #Se Recorre el Texto
            for row in lstText:
                #Se dibuja el texto
                newPDF.drawString(pointX,pointY,row)
                #Se decrementa para saltar a una nueva linea
                pointY -= 20
            
            #Se Guarda el Documento
            newPDF.save()

    def CreateNewDocx(self):
        #Se obtiene el Texto
        newText = self.getText

        #Se valida que el Texto no este Vacio
        if(len(newText) == 0):
            self.MessageBox("No se encontro Texto para crear el Documento","Atención")
            return
        else:
            #Se crea la instancia 
            document = Document()
            #Escribimos en el documento el texto
            p = document.add_paragraph(newText)
            #Guardamos el archivo
            document.save(self.textTitle.text()+".docx")
    
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

    FormTools = QtWidgets.QWidget()
    
    ui = Ui_FormTools()
    
    ui.setupUi(FormTools)
    
    FormTools.show()
    
    sys.exit(app.exec_())
