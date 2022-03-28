import sys
import textwrap
from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyQt5 import QtCore, QtGui, QtWidgets, uic

class ToolsTranlator(QtWidgets.QWidget):
    # Create Contructor
    def __init__(self,textTranslate):
        # Get text from QTextEdit
        self.textTranslate = textTranslate
        # Find components and assing properties
        super(ToolsTranlator, self).__init__()

        # Open UI-Template
        uic.loadUi('Templates/FormTools.ui',self)
        self.setMinimumSize(QtCore.QSize(330,200))
        self.setMaximumSize(QtCore.QSize(330,200))

        # --------------- QPushButtons ---------------- #
        self.BtnOptionPDF = self.findChild(QtWidgets.QPushButton, 'BtnPdf')
        self.BtnOptionDOC = self.findChild(QtWidgets.QPushButton, 'BtnWord')

        self.BtnSave = self.findChild(QtWidgets.QPushButton, 'BtnSave')
        self.BtnSave.clicked.connect(self.CheckStateButtons)

        self.BtnCancel = self.findChild(QtWidgets.QPushButton, 'BtnCancel')
        self.BtnCancel.clicked.connect(self.close)

    def CheckStateButtons(self):
        if(self.BtnOptionPDF.isChecked()):
            self.SavePdf()
        if(self.BtnOptionDOC.isChecked()):
            self.SaveDocx()

    def SavePdf(self):
        fileName,_ = QtWidgets.QFileDialog.getSaveFileName(self,"Save file...",filter="PDF Files (*.pdf)")
        if(fileName):            
            self.CreatePDF(fileName)
            self.ResetFields()

    def SaveDocx(self):
        fileName,_ = QtWidgets.QFileDialog.getSaveFileName(self,"Save file...",filter="Word Files (*.docx)")
        if(fileName):            
            self.CreateNewDocx(fileName)
            self.ResetFields()
            
            
    def CreatePDF(self, filename):
        # Validamos que el texto no este vacio
        if(len(self.textTranslate) == 0):
            self.ShowMessage('No se encontro texto para crear el Documento', 'Atención')
            return

        # Establecemos el numero de caracteres antes de saltar la linea
        wrapper = textwrap.TextWrapper(width=103)
        newtext = wrapper.wrap(text=self.textTranslate)

        # Creamos el PDF y le asignamos propiedades
        newFilePDF = canvas.Canvas(filename, pagesize=letter)
        # Se asigna el margen izquierdo done empezara a dibujar el texto
        pointX = 30
        # Se asigna la altura donde empieza a dibujar el texto
        pointY = 720

        for word in newtext:
            # Escribimos el texto
            newFilePDF.drawString(pointX,pointY,word)
            # Se decrementa para saltar a una nueva linea
            pointY -= 20

        # Se Guarda el Documento
        newFilePDF.save()

        self.ShowMessage("Documento creado con Exito", 'Atención')

    def CreateNewDocx(self, filename):
        # Validamos que el texto no este vacio
        if(len(self.textTranslate) == 0):
            self.ShowMessage('No se encontro texto para crear el Documento', 'Atención')
            return

        # Creamos una instancia
        newDocument = Document()
        # Escribimos en el Documento
        newDocument.add_paragraph(self.textTranslate)
        # Guardamos el Documento
        newDocument.save(filename)

        self.ShowMessage("Documento creado con Exito", 'Atención')   

    def ShowMessage(self,message,title):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()
        return

    def ResetFields(self):
        self.BtnOptionPDF.setChecked(False)
        self.BtnOptionDOC.setChecked(False)
        self.textTranslate = ''

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    window = ToolsTranlator()

    app.exec_()