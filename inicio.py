## this project was create by Richie Otero and Moises Zabala
## on 2025

from PyQt6.QtWidgets import  QWidget,QLabel,QVBoxLayout,QHBoxLayout,QLineEdit,QPushButton,QTableWidget,QTableWidgetItem,QMessageBox
from PyQt6.QtCore import Qt

class Inicio(QWidget):
    def __init__(self,padre):
        super().__init__()
        self.width=1000
        self.height=500
        self.padre = padre

        #variables
        self.y_buscador = 300
        self.msj =QMessageBox()
        layout = QVBoxLayout()
        div_buscador= QHBoxLayout()
        
        #array fixticio
        self.valores = self.padre.valores
        
        #crear label
        label = QLabel("Buscador:",self)
        label.setStyleSheet("font-size: 20px; color: blue; text-align:") 
        label.setAlignment(Qt.AlignmentFlag.AlignRight)

        #input
        input_width=200
        input_height=35
        self.buscador_input = QLineEdit(self)
        self.buscador_input.setPlaceholderText("Introduzca el DNI")
        self.buscador_input.setGeometry(int(self.width/2)+100,self.y_buscador,input_width,input_height)
        self.buscador_input.setStyleSheet("font-size:15px;")    
        self.buscador_input.setFixedWidth(input_width)    
        
        #button
        button= QPushButton("Ok",self)
        button.setGeometry(int(self.width/2),self.y_buscador,60,35)
        button.setStyleSheet('''
            QPushButton{
                        font-size:15px;
                        background-color:blue;
                        color:#f1f1f1;
                                      }
            QPushButton:hover{
                                      color:black;
                                      }
''')
        button.setFixedWidth(60) 
        button.setCursor(Qt.CursorShape.PointingHandCursor)

        #button actualizar
        button_actualizar = QPushButton("Actualizar",self)
        button_actualizar.setGeometry(int(self.width/2),self.y_buscador,60,35)
        button_actualizar.setStyleSheet('''
            QPushButton{
                        font-size:15px;
                        background-color:blue;
                        color:#f1f1f1;
                                      }
            QPushButton:hover{
                                      color:black;
                                      }
''')
        button_actualizar.setFixedWidth(100) 
        button_actualizar.setCursor(Qt.CursorShape.PointingHandCursor)

        #table
        self.table = QTableWidget(self)  
        self.table.setStyleSheet("font-size:15px")

        #cargar datos
        self.actulizar()

        div_buscador.addWidget(label)
        div_buscador.addWidget(self.buscador_input)
        div_buscador.addWidget(button)
        div_buscador.addWidget(button_actualizar)
        layout.addLayout(div_buscador)
        layout.addWidget(self.table)
        self.setLayout(layout)

        #cliked
        button.clicked.connect(self.buscar)
        button_actualizar.clicked.connect(self.actulizar)

    def buscar(self):
        input = self.buscador_input.text()
        if input == "" :
            self.msj.setText("Debes completar el campo")
            self.msj.setIcon(QMessageBox.Icon.Warning)
            self.msj.setWindowTitle("Seguros Atlanta")
            self.msj.setStandardButtons(QMessageBox.StandardButton.Ok)
            self.msj.exec()
            self.buscador_input.setFocus()
            return
        poliza = []
        for i,valor in enumerate(self.valores):
            if valor[self.padre.heads[3]] == input:
                poliza.append(valor)
            elif str(valor[self.padre.heads[4]]) == input:
                poliza.append(valor)

        if poliza == False or len(poliza) == 0:
            self.msj.setText("No se pudo encontrar dicha póliza")
            self.msj.setIcon(QMessageBox.Icon.Critical)
            self.msj.setWindowTitle("Seguros Atlanta")
            self.msj.exec()
            return
        
        self.table.clearContents() 
        self.table.setRowCount(len(poliza))
        for x,valor in enumerate(poliza):
            
            for y,keys in enumerate(self.padre.heads):
        
                item=QTableWidgetItem(str(valor[keys]))
                self.table.setItem(x,y,item)


    def actulizar(self):
        self.table.clearContents() 
        self.table.setRowCount(len(self.valores))
        self.table.setColumnCount(len(self.padre.heads))
        self.table.setHorizontalHeaderLabels(self.padre.heads)
        self.table.resizeColumnsToContents()

        for i,key in enumerate(self.padre.heads):
     
            for x,valor in enumerate(self.valores) :
                
                for y,keys in enumerate(self.padre.heads):
            
                    item=QTableWidgetItem(str(valor[keys]))
                    self.table.setItem(x,y,item)