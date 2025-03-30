from PyQt6.QtWidgets import QWidget, QVBoxLayout,QLabel,QLineEdit,QHBoxLayout,QPushButton,QMessageBox
from PyQt6.QtCore import Qt

class Actualizar(QWidget):
    def __init__(self,padre):
        super().__init__()
        self.setGeometry(0,0,500,300)
        self.layout_ = QVBoxLayout(self)
        self.layout_1 = QHBoxLayout()
        self.layout_2 = QHBoxLayout()
        self.layout_3 = QHBoxLayout()
        self.layout_4 = QHBoxLayout()
        self.layout_5 = QHBoxLayout()
        self.layout_6 = QHBoxLayout()
        self.layout_7 = QHBoxLayout()
        self.layout_buscador = QHBoxLayout()
        self.msj = QMessageBox(self)
        self.padre = padre
        self.poliza = False
        #variables
        titulo = QLabel("Actualizar Seguro",self)
        titulo.setStyleSheet("font-size:25px;")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button=QPushButton("Aceptar",self)
        button.setFixedSize(100,40)
        button.setStyleSheet("font-size:15px")
        btn_buscador = QPushButton("Buscar",self)
        btn_buscador.setStyleSheet("font-size:15px")
        btn_buscador.setFixedSize(60,30)
        
        #labels
        label_nombre_apellido   =QLabel("Nombre y apellido:",self)
        label_fecha_nacimiento  =QLabel("Fecha de nacimiento:",self)
        label_cedula            =QLabel("Cédula:",self)
        label_telefono          =QLabel("Teléfono:",self)
        label_fecha_inicio      =QLabel("Fecha de inicio:",self)
        label_fecha_vencimiento =QLabel("Fecha de vencimineto:",self)
        label_no_poliza         =QLabel("Número de poliza:",self)
        label_buscador          =QLabel("Buscador",self)
        label_buscador.setStyleSheet("font-size:15px")
        self.labels = [label_nombre_apellido,   
label_fecha_nacimiento,  
label_cedula,            
label_telefono,          
label_fecha_inicio,      
label_fecha_vencimiento, 
label_no_poliza         ]
        
        #inputs
        input_nombre_apellido   = QLineEdit(self)
        input_fecha_nacimiento  = QLineEdit(self)
        input_cedula            = QLineEdit(self)
        input_telefono          = QLineEdit(self)
        input_fecha_inicio      = QLineEdit(self)
        input_fecha_vencimiento = QLineEdit(self)
        input_no_poliza         = QLineEdit(self)
        self.input_buscador     = QLineEdit(self) 
        self.input_buscador.setFixedSize(250,25)
        self.input_buscador.setPlaceholderText("Ingrese en DNI")
        self.inputs = [input_nombre_apellido,   
input_fecha_nacimiento,  
input_cedula      ,      
input_telefono     ,     
input_fecha_inicio  ,    
input_fecha_vencimiento, 
input_no_poliza         
]
        
        #for labels
        for element in self.labels:
            element.setStyleSheet("font-size:15px;")
            element.setFixedWidth(160)

        #for inputs
        for element in self.inputs:
            element.setStyleSheet("font-size:15px;")
            element.setFixedWidth(250)
           
        self.layout_1.addWidget(label_nombre_apellido)
        self.layout_1.addWidget(input_nombre_apellido)
        self.layout_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_2.addWidget(label_fecha_nacimiento)
        self.layout_2.addWidget(input_fecha_nacimiento)
        self.layout_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_3.addWidget(label_cedula)
        self.layout_3.addWidget(input_cedula)
        self.layout_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_4.addWidget(label_telefono)
        self.layout_4.addWidget(input_telefono)
        self.layout_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.layout_5.addWidget(label_fecha_inicio)
        self.layout_5.addWidget(input_fecha_inicio)
        self.layout_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_6.addWidget(label_fecha_vencimiento)
        self.layout_6.addWidget(input_fecha_vencimiento)
        self.layout_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_7.addWidget(label_no_poliza)
        self.layout_7.addWidget(input_no_poliza)
        self.layout_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_buscador.addWidget(label_buscador)
        self.layout_buscador.addWidget(self.input_buscador)
        self.layout_buscador.addWidget(btn_buscador)
        self.layout_buscador.setAlignment(label_buscador,Qt.AlignmentFlag.AlignRight)
        
        self.layout_.addWidget(titulo)
        self.layout_.addLayout(self.layout_buscador)
        self.layout_.addLayout(self.layout_1)
        self.layout_.addLayout(self.layout_2)
        self.layout_.addLayout(self.layout_3)
        self.layout_.addLayout(self.layout_4)
        self.layout_.addLayout(self.layout_5)
        self.layout_.addLayout(self.layout_6)
        self.layout_.addLayout(self.layout_7)
        self.layout_.addWidget(button)
        self.layout_.setAlignment(button,Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.layout_)

        #agregar evento al button
        button.clicked.connect(self.actualizar)
        btn_buscador.clicked.connect(self.buscar)

    def  actualizar(self):
        if self.poliza == False:
            self.msj.setText("Busca la poliza que deseas actualizar")
            self.msj.setIcon(QMessageBox.Icon.Critical)
            self.msj.setStandardButtons(QMessageBox.StandardButton.Ok)
            self.msj.setWindowTitle("Error")
            self.msj.exec()
            return
        new_poliza = {}
        polizas = list(self.padre.valores[0].keys())
        for i,input in enumerate(self.inputs):
            new_poliza[polizas[i]] = input.text()
            input.setText("")
        del self.padre.valores[self.poliza["index"]]
        self.padre.valores.insert(self.poliza["index"],new_poliza)
        self.poliza = False
        self.msj.setText("Actulizado correctamente")
        self.msj.setIcon(QMessageBox.Icon.NoIcon)
        self.msj.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.msj.setWindowTitle("Ok")
        self.msj.exec()

    def buscar(self):

        if self.input_buscador == "":
            self.msj.setText("Introdusca un DNI")
            self.msj.setIcon(QMessageBox.Icon.Information)
            self.msj.setStandardButtons(QMessageBox.StandardButton.Ok)
            self.msj.setWindowTitle("Informacion")
            self.msj.exec()
            return
        bandera = False
       
        for i,poliza in enumerate(self.padre.valores):
            if poliza["cedula"] == self.input_buscador.text():
                bandera = True
                self.poliza = {"index":i,"poliza":poliza}
                polizas = list(poliza.keys())
                for i,input in enumerate(self.inputs):
                        input.setText(poliza[polizas[i]])  
                        
        
        if bandera == False:
            self.msj.setText("No se pudo encontrar dicha poliza")
            self.msj.setIcon(QMessageBox.Icon.Critical)
            self.msj.setStandardButtons(QMessageBox.StandardButton.Ok)
            self.msj.setWindowTitle("Error")
            self.msj.exec()
            return

        
