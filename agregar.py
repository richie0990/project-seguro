from PyQt6.QtWidgets import QWidget, QVBoxLayout,QLabel,QLineEdit,QHBoxLayout,QPushButton,QMessageBox
from PyQt6.QtCore import Qt
import re 

class Agregar(QWidget):
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

        self.msj = QMessageBox(self)
        self.padre = padre
        
        #variables
        titulo = QLabel("Agregar Seguro",self)
        titulo.setStyleSheet("font-size:25px;")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button=QPushButton("Aceptar",self)
        button.setFixedSize(125,55)
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
        button
        
        #labels
        label_nombre_apellido   =QLabel(self.padre.heads[0]+":",self)
        label_fecha_nacimiento  =QLabel(self.padre.heads[1]+":",self)
        label_cedula            =QLabel(self.padre.heads[2]+":",self)
        label_telefono          =QLabel(self.padre.heads[3]+":",self)
        label_fecha_inicio      =QLabel(self.padre.heads[4]+":",self)
        label_fecha_vencimiento =QLabel(self.padre.heads[5]+":",self)
        label_no_poliza         =QLabel(self.padre.heads[6]+":",self)
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
        
        self.layout_.addWidget(titulo)
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
        button.clicked.connect(self.agregar)

    def  agregar(self):
        
        re_fechas =r'^\d{2}/\d{2}/\d{4}$'
        re_cedula = r'^\d{3}-\d{7}-\d{1}$'
        re_telefono = r'^\d{3}-\d{3}-\d{4}$'

        regex = True
        bandera=False
        obj={}
        
        keys = self.padre.heads
        
        for i,input in enumerate(self.inputs):
            if input.text() == "":
                bandera=True
            obj[keys[i]] = input.text()
        for i,value in enumerate(list(obj.values())):
                if i == 1:
                    if not re.match(re_fechas,value):
                        regex = False 
                        self.inputs[i].setFocus()   
                elif i == 2:
                    if not re.match(re_cedula,value):
                        regex = False 
                        self.inputs[i].setFocus()    
                elif i == 3:
                    if not re.match(re_telefono,value):
                        regex = False  
                        self.inputs[i].setFocus()   
                elif i == 4:
                    if not re.match(re_fechas,value):
                        regex = False
                        self.inputs[i].setFocus() 
                elif i == 5:
                    if not re.match(re_fechas,value):
                        regex = False
                        self.inputs[i].setFocus() 
                if not regex:
                    self.msj.setWindowTitle("Error")
                    self.msj.setIcon(QMessageBox.Icon.Critical)
                    self.msj.setStandardButtons(QMessageBox.StandardButton.Ok)
                    self.msj.setText("Complete correctamente este campo")
                    self.msj.exec()
                    return

        if bandera == True:
            self.msj.setWindowTitle("Error")
            self.msj.setIcon(QMessageBox.Icon.Critical)
            self.msj.setStandardButtons(QMessageBox.StandardButton.Ok)
            self.msj.setText("Por favor complete los campos")
            self.msj.exec()
            return
        exits =False
        for valor in self.padre.valores:
            if valor[self.padre.heads[2]] == obj[self.padre.heads[2]] or valor[self.padre.heads[6]] == obj[self.padre.heads[6]]:
                exits =True
        if exits == True:
            self.msj.setWindowTitle("Error")
            self.msj.setText("Póliza ya existente, revisa el DNI o el número de póliza")
            self.msj.setIcon(QMessageBox.Icon.Critical)
            self.msj.setStandardButtons(QMessageBox.StandardButton.Ok)
            self.msj.exec()
            return
        self.padre.valores.insert(0,obj)
        self.padre.save(self.padre.convert_to_docx())
        for input in self.inputs:
            input.setText("")
        self.msj.setWindowTitle("Ok")
        self.msj.setText("Agregado con éxito")
        self.msj.setIcon(QMessageBox.Icon.NoIcon)
        self.msj.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.msj.exec()