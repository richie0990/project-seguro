from PyQt6.QtWidgets import QWidget, QVBoxLayout,QLabel,QLineEdit,QHBoxLayout,QPushButton,QTableWidget,QMessageBox,QTableWidgetItem
from PyQt6.QtCore import Qt

class Eliminar(QWidget):
    def __init__(self,padre):
        super().__init__()
        self.width = 1004
        self.height = 300
        self.setGeometry(0,0,self.width,self.height)        
        self.layout_ = QVBoxLayout(self)
        self.layout_buscador = QHBoxLayout(self)
        self.layout_tabla =  QVBoxLayout(self)
        self.msj = QMessageBox(self)
        self.padre = padre
        self.poliza = None
        
        #variables
        titulo = QLabel("Eliminar Seguro",self)
        titulo.setStyleSheet("font-size:25px;")

        buscardo_label = QLabel("Buscador",self)
        self.buscardo_input = QLineEdit(self)
        buscardo_button = QPushButton("Buscar",self)
        buscardo_button.setCursor(Qt.CursorShape.PointingHandCursor)
        buscardo_button.setStyleSheet('''
            QPushButton{
                        font-size:15px;
                        background-color:blue;
                        color:#f1f1f1;
                                      }
            QPushButton:hover{
                                      color:black;
                                      }
''')
        eliminar_button = QPushButton("Eliminar",self)
        eliminar_button.setFixedSize(130,80)
        eliminar_button.setStyleSheet('''
            QPushButton{
                        font-size:15px;
                        background-color:blue;
                        color:#f1f1f1;
                                      }
            QPushButton:hover{
                                      color:black;
                                      }
''')
        eliminar_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.buscardo_input.setFixedSize(250,35)
        self.buscardo_input.setPlaceholderText("Introduzca el DNI")
        buscardo_button.setFixedSize(60,35)
        buscardo_label.setStyleSheet("font-size:15px;color:blue;")

        
        self.layout_buscador.addWidget(buscardo_label)
        self.layout_buscador.addWidget(self.buscardo_input)
        self.layout_buscador.addWidget(buscardo_button)
        self.layout_buscador.setAlignment(buscardo_label,Qt.AlignmentFlag.AlignRight)
      
        self.layout_.addWidget(titulo)
        self.layout_.addLayout(self.layout_buscador)
        self.layout_.setAlignment(titulo,Qt.AlignmentFlag.AlignCenter)
        self.table = QTableWidget(self)
        self.table.setStyleSheet("font-size:15px")
        self.table.setRowCount(0)
        self.table.setColumnCount(len(self.padre.heads))
        self.table.setHorizontalHeaderLabels(self.padre.heads)
        self.table.resizeColumnsToContents()
        self.table.setHorizontalHeaderLabels(self.padre.heads)
        self.layout_.addWidget(self.table)
        self.layout_.addWidget(eliminar_button)
        self.layout_.setAlignment(eliminar_button,Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.layout_)

        #conect btn
        buscardo_button.clicked.connect(self.buscar)
        eliminar_button.clicked.connect(self.eliminar)
        
    def buscar(self):
        value = self.buscardo_input.text()
        if value == "":
            self.msj.setText("No se encontró dicha póliza")
            self.msj.setWindowTitle("Error")
            self.msj.setIcon(QMessageBox.Icon.Critical)
            self.msj.exec()
            return
        poliza=False
        for i,element in enumerate(self.padre.valores):
            if element[self.padre.heads[3]] == value:
                poliza = [i,element]
            
        if poliza == False:
            self.msj.setText("No se encontró dicha póliza")
            self.msj.setWindowTitle("Error")
            self.msj.setIcon(QMessageBox.Icon.Critical)
            self.msj.exec()
            return
        self.table.setRowCount(1)
        
        for i,keys in enumerate(self.padre.heads):
             print(poliza[1][self.padre.heads[i]])
             self.table.setItem(0,i,QTableWidgetItem(str(poliza[1][self.padre.heads[i]])))
        self.poliza =poliza
        
    def eliminar(self):
            if self.poliza == None:
                self.msj.setText("Busque una póliza para eliminar")
                self.msj.setWindowTitle("Error")
                self.msj.setIcon(QMessageBox.Icon.Critical)
                self.msj.setStandardButtons(QMessageBox.StandardButton.Ok)
                self.msj.exec()
                return
            self.msj.setText("Quieres eliminar esta póliza?")
            self.msj.setWindowTitle("Info")
            self.msj.setIcon(QMessageBox.Icon.Information)
            self.msj.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel )
            respuesta = self.msj.exec()
            if respuesta == QMessageBox.StandardButton.Cancel:
                 return
            del self.padre.valores[self.poliza[0]]
            self.padre.save_excel(self.padre.convert_to_excel())
            self.table.setRowCount(0)
            self.msj.setText("Eliminado correctamente")
            self.msj.setWindowTitle("Ok")
            self.msj.setIcon(QMessageBox.Icon.NoIcon)
            self.msj.setStandardButtons(QMessageBox.StandardButton.Ok)
            self.msj.exec()
            self.poliza =None
