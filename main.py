import sys 
from PyQt6.QtWidgets import  QApplication,QWidget,QLabel,QVBoxLayout,QMessageBox,QMenuBar
from PyQt6.QtGui import QAction,QPixmap,QIcon
from PyQt6.QtCore import Qt


from inicio import Inicio
from agregar import Agregar

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.width =1080
        self.height =580
        self.setGeometry(0,100,self.width,self.height)
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QIcon("./src/img/favicon.ico"))
        self.setWindowTitle("Seguros atlanta")
        self.option={
            "current":"inicio"
        } 
        self.start_window = Inicio()
        self.agregar_window= Agregar()
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
        inicio = QAction("Inicio",self)

        # conectando los acctiones
        agregar_action.triggered.connect(self.agregar)
        eliminar_action.triggered.connect(self.eliminar)
        salir_action.triggered.connect(self.salir)
        

        #agregarla acction al menu
        file_menu.addAction(agregar_action)
        file_menu.addAction(eliminar_action)
        file_menu.addAction(salir_action)
        
    def salir(self):
        sys.exit()
    
    def agregar(self):
        if self.option["current"] == "inicio":
            self.layout_.removeWidget(self.start_window)
            self.start_window.deleteLater()
            self.option["current"] = "agregar"
            self.layout_.addWidget(self.agregar_window)

        
  
    def eliminar(self):
        print("eliminar")

   
if __name__ == "__main__":
    app = QApplication(sys.argv)

    mi_ventana= Ventana()
    mi_ventana.show()
    sys.exit(app.exec())


    