import sys 
from PyQt6.QtWidgets import QWidget, QApplication,QMainWindow,QMenuBar
from PyQt6.QtGui import QAction

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(0,0,1080,580)
        self.setWindowTitle("Sistemas de seguro")
        menu_bar = self.menuBar()
        #crear bar menu
        file_menu = menu_bar.addMenu("Archivo")
        #agregar acctiones
        agregar_action = QAction("Agregar",self)
        eliminar_action = QAction("Eliminar",self)
        Salir_action = QAction("Salir",self)
        # conectando los acctiones
        agregar_action.triggered.connect(self.agregar)
        eliminar_action.triggered.connect(self.eliminar)
        Salir_action.triggered.connect(self.salir)
        #agregarla acction al menu
        file_menu.addAction(agregar_action)
        file_menu.addAction(eliminar_action)
        file_menu.addAction(Salir_action)

    def salir(self):
        sys.exit()
    
    def agregar(self):
        print("agregar")
    def eliminar(self):

        print("eliminar")
if __name__ == "__main__":
    app = QApplication(sys.argv)

    mi_ventana= Ventana()
    mi_ventana.show()
    sys.exit(app.exec())


    