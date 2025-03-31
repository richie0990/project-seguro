import sys 
from PyQt6.QtWidgets import  QApplication,QWidget,QLabel,QVBoxLayout,QMessageBox,QMenuBar
from PyQt6.QtGui import QAction,QPixmap,QIcon
from PyQt6.QtCore import Qt
from docx import Document
from docx.oxml import OxmlElement
import os
from inicio import Inicio
from agregar import Agregar
from eliminar import Eliminar
from actualizar import Actualizar

doc = Document("./src/seguros.docx")
data = []
heads = []
for tabla in doc.tables:
    for d,fila in enumerate(tabla.rows):
        obj ={}
        index=0
        datos=False
        for i,celda in enumerate(fila.cells):
            if d == 0:
                heads.append(celda.text) 
            else:
                datos=True
                obj[heads[i]] = celda.text     
        if datos == True:   
            data.append(obj)


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.width =1080
        self.height =580
        self.setGeometry(0,100,self.width,self.height)
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QIcon("./src/img/favicon.ico"))
        self.setWindowTitle("Seguros atlanta")
        self.heads = heads
        self.valores = data
        self.start_window = Inicio(self)
        self.eliminar_window =  Eliminar(self)
        self.agregar_window = Agregar(self)
        self.agregar_window = Actualizar(self)
        self.option={
            "current":"inicio",
            "ventana":self.start_window
        } 

        self.msj = QMessageBox()
        self.menu_bar = QMenuBar(self)
        
       #pixmap
        pixmap = QPixmap("./src/img/logo.png")

        #layaout
        self.layout_ = QVBoxLayout()
        
        #titulo
        titulo_width  = 660
        titulo_height =150
        titulo = QLabel("",self)
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setGeometry(int(self.width/6),30,titulo_width,titulo_height)
        scale_pixmap= pixmap.scaled(titulo_width,titulo_height,Qt.AspectRatioMode.KeepAspectRatio)
        titulo.setPixmap(scale_pixmap)

        titulo.setFixedHeight(titulo_height)

        #add layout
        self.layout_.addWidget(titulo)
        self.layout_.addWidget(self.start_window)
        self.setLayout(self.layout_)

        #setmenuebar
        self.layout_.setMenuBar(self.menu_bar)
        
        #crear bar menu
        file_menu = self.menu_bar.addMenu("Archivo")

        #agregar acctiones
        agregar_action = QAction("Agregar",self)
        eliminar_action = QAction("Eliminar",self)
        salir_action = QAction("Salir",self)
        inicio_action = QAction("Inicio",self)
        actualizar_action = QAction("Actualizar",self)

        # conectando los acctiones
        inicio_action.triggered.connect(self.inicio)
        agregar_action.triggered.connect(self.agregar)
        eliminar_action.triggered.connect(self.eliminar)
        salir_action.triggered.connect(self.salir) 
        actualizar_action.triggered.connect(self.actualizar)       

        #agregarla acction al menu
        file_menu.addAction(inicio_action)
        file_menu.addAction(agregar_action)
        file_menu.addAction(eliminar_action)
        file_menu.addAction(actualizar_action)
        file_menu.addAction(salir_action)
        
    def salir(self):
        sys.exit()
    
    def agregar(self):

        self.option["current"] = "agregar"
        self.crear_windows()
        self.layout_.addWidget(self.agregar_window)

    def eliminar(self):
       
        self.option["current"] = "eliminar"
        self.crear_windows() 
        self.layout_.addWidget(self.eliminar_window)

    def inicio(self):
        self.option["current"] = "inicio"
        self.crear_windows() 
        self.layout_.addWidget(self.start_window)

    def actualizar(self):
        self.option["current"] = "actualizar"
        self.crear_windows() 
        self.layout_.addWidget(self.actualizar_window)

    def crear_windows(self):
        if self.option["current"] == "eliminar" :
            self.layout_.removeWidget(self.option["ventana"])
            self.option["ventana"].deleteLater()  
            self.eliminar_window= Eliminar(self)
            self.option["ventana"]=self.eliminar_window

        elif self.option["current"] == "inicio" :
            self.layout_.removeWidget(self.option["ventana"])
            self.option["ventana"].deleteLater()  
            self.start_window = Inicio(self)
            self.option["ventana"]=self.start_window

        elif self.option["current"] == "agregar" :
            self.layout_.removeWidget(self.option["ventana"])
            self.option["ventana"].deleteLater()  
            self.agregar_window= Agregar(self)
            self.option["ventana"]=self.agregar_window
        elif self.option["current"] == "actualizar" :
            self.layout_.removeWidget(self.option["ventana"])
            self.option["ventana"].deleteLater()  
            self.actualizar_window= Actualizar(self)
            self.option["ventana"]=self.actualizar_window
        
    def save(self,data):
        tables = doc.tables
        if tables:
            table_to_remove = tables[0]
            tbl = table_to_remove._element  # Accedemos al elemento XML de la tabla
            tbl.getparent().remove(tbl) 
        tabla = doc.add_table(rows=len(data),cols=7)
        tabla.style = 'Table Grid'
        for i, fila in enumerate(data):
            for j, valor in enumerate(fila):
                # Acceder a cada celda y asignar el valor
                tabla.cell(i, j).text = valor
        
        # Guardar el documento
        doc.save("./src/seguros.docx")
        #solo hay que poner donde el quiere que se guarde la informacion 
        #doc.save(os.)

    def convert_to_docx(self):
        converted_data=[self.heads]
        for valor in self.valores:
            converted_data.append(list(valor.values()))
        return converted_data 

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mi_ventana= Ventana()
    mi_ventana.show()
    sys.exit(app.exec())


    