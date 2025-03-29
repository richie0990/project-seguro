from PyQt6.QtWidgets import QWidget, QVBoxLayout,QLabel,QLineEdit,QHBoxLayout,QPushButton
from PyQt6.QtCore import Qt

class Eliminar(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,300)        

        #variables
        titulo = QLabel("Eliminar Seguro",self)
        titulo.setStyleSheet("font-size:25px;")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

     