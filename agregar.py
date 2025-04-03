from PyQt6.QtWidgets import QWidget, QVBoxLayout,QLabel,QLineEdit,QHBoxLayout,QPushButton,QMessageBox
from PyQt6.QtCore import Qt
import re 

class Agregar(QWidget):
    def __init__(self,padre):
        super().__init__()
        self.setGeometry(0,0,500,300)
        self.check_input = True
        self.layout_main = QVBoxLayout(self)
        self.layout_p = QVBoxLayout(self)
        self.layout_s = QVBoxLayout(self)
        self.layout_1 = QHBoxLayout()
        self.layout_2 = QHBoxLayout()
        self.layout_3 = QHBoxLayout()
        self.layout_4 = QHBoxLayout()
        self.layout_5 = QHBoxLayout()
        self.layout_6 = QHBoxLayout()
        self.layout_7 = QHBoxLayout()
        self.layout_8 = QHBoxLayout()
        self.layout_9 = QHBoxLayout()
        self.layout_10 = QHBoxLayout()
        self.layout_11 = QHBoxLayout()
        self.layout_12 = QHBoxLayout()

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
        label_no_poliza         =QLabel(self.padre.heads[0]+":",self)
        label_nombre_apellido   =QLabel(self.padre.heads[1]+":",self)
        label_telefono          =QLabel(self.padre.heads[2]+":",self)
        label_cedula            =QLabel(self.padre.heads[3]+":",self)
        label_fecha_inicio      =QLabel(self.padre.heads[4]+":",self)
        label_fecha_vencimiento =QLabel(self.padre.heads[5]+":",self)
        label_direccion         =QLabel(self.padre.heads[6]+":",self)
        label_pagada            =QLabel(self.padre.heads[7]+":",self)
        label_total_poliza      =QLabel(self.padre.heads[8]+":",self)
        label_fecha_de_pago     =QLabel(self.padre.heads[9]+":",self)
        label_pago_total        =QLabel(self.padre.heads[10]+":",self)
        label_pago_restante     =QLabel(self.padre.heads[11]+":",self)
        self.labels = [
            label_no_poliza,         
label_nombre_apellido   ,
label_telefono          ,
label_cedula            ,
label_fecha_inicio      ,
label_fecha_vencimiento ,
label_direccion         ,
label_pagada            ,
label_total_poliza      ,
label_fecha_de_pago     ,
label_pago_total        ,
label_pago_restante     ]
        
        
        #inputs
        input_no_poliza         = QLineEdit(self)
        input_nombre_apellido   = QLineEdit(self)
        input_telefono          = QLineEdit(self)
        input_cedula            = QLineEdit(self)
        input_fecha_inicio      = QLineEdit(self)
        input_fecha_vencimiento = QLineEdit(self)
        input_direccion         = QLineEdit(self)
        input_pagada            = QLineEdit(self)
        input_total_poliza      = QLineEdit(self)
        input_fecha_de_pago     = QLineEdit(self)
        input_pago_total        = QLineEdit(self)
        input_pago_restante     = QLineEdit(self)
        
        input_no_poliza.setPlaceholderText("No. póliza")          
        input_nombre_apellido.setPlaceholderText("Nombre y apellido")   
        input_telefono.setPlaceholderText("000-000-0000")           
        input_cedula.setPlaceholderText("000-0000000-0")             
        input_fecha_inicio.setPlaceholderText("dd/mm/aaaa")       
        input_fecha_vencimiento.setPlaceholderText("dd/mm/aaaa")  
        input_direccion.setPlaceholderText("Dirección")          
        input_pagada.setPlaceholderText("Ha pagado el monto de la póliza")             
        input_total_poliza.setPlaceholderText("Total valor de la póliza")       
        input_fecha_de_pago.setPlaceholderText("dd/mm/aaaa" )      
        input_pago_total.setPlaceholderText("Pago total")         
        input_pago_restante.setPlaceholderText("Pago restante") 
        input_pago_total.textChanged.connect(self.resta)
        self.inputs = [ 
         input_no_poliza        ,
        input_nombre_apellido   ,
        input_telefono          ,
        input_cedula            ,
        input_fecha_inicio      ,
        input_fecha_vencimiento ,
        input_direccion         ,
        input_pagada            ,
        input_total_poliza      ,
        input_fecha_de_pago     ,
        input_pago_total        ,
        input_pago_restante              
]
        
        #for labels
        for element in self.labels:
            element.setStyleSheet("font-size:15px;")
            element.setFixedWidth(160)

        #for inputs
        for element in self.inputs:
            element.setStyleSheet("font-size:15px;")
            element.setFixedWidth(250)
           
        self.layout_1.addWidget(label_no_poliza)
        self.layout_1.addWidget(input_no_poliza)
        self.layout_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_2.addWidget(label_nombre_apellido)
        self.layout_2.addWidget(input_nombre_apellido)
        self.layout_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_3.addWidget(label_telefono)
        self.layout_3.addWidget(input_telefono)
        self.layout_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_4.addWidget(label_cedula)
        self.layout_4.addWidget(input_cedula)
        self.layout_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_5.addWidget(label_fecha_inicio)
        self.layout_5.addWidget(input_fecha_inicio)
        self.layout_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.layout_6.addWidget(label_fecha_vencimiento)
        self.layout_6.addWidget(input_fecha_vencimiento)
        self.layout_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_7.addWidget(label_direccion)
        self.layout_7.addWidget(input_direccion)
        self.layout_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_8.addWidget(label_pagada)
        self.layout_8.addWidget(input_pagada)
        self.layout_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_9.addWidget(label_total_poliza)
        self.layout_9.addWidget(input_total_poliza)
        self.layout_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_10.addWidget(label_fecha_de_pago)
        self.layout_10.addWidget(input_fecha_de_pago)
        self.layout_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_11.addWidget(label_pago_total)
        self.layout_11.addWidget(input_pago_total)
        self.layout_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_12.addWidget(label_pago_restante)
        self.layout_12.addWidget(input_pago_restante)
        self.layout_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_main.addWidget(titulo)
        self.layout_p.addLayout(self.layout_1)
        self.layout_p.addLayout(self.layout_2)
        self.layout_p.addLayout(self.layout_3)
        self.layout_p.addLayout(self.layout_4)
        self.layout_p.addLayout(self.layout_5)
        self.layout_p.addLayout(self.layout_6)

        self.layout_s.addLayout(self.layout_7)
        self.layout_s.addLayout(self.layout_8)
        self.layout_s.addLayout(self.layout_9)
        self.layout_s.addLayout(self.layout_10)
        self.layout_s.addLayout(self.layout_11)
        self.layout_s.addLayout(self.layout_12)

        self.layout_main.addLayout(self.layout_p)
        self.layout_main.addLayout(self.layout_s)
        self.layout_main
        self.layout_main.addWidget(button)
        self.layout_main.setAlignment(button,Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.layout_main)

        #agregar evento al button
        button.clicked.connect(self.agregar)

    def  agregar(self):
        
        regex = True
        bandera=False
        obj={}
        
        keys = self.padre.heads
        
        for i,input in enumerate(self.inputs):
            
            if input.text() == "":
                self.msj.setWindowTitle("Error")
                self.msj.setIcon(QMessageBox.Icon.Critical)
                self.msj.setStandardButtons(QMessageBox.StandardButton.Ok)
                self.msj.setText("Por favor complete los campos")
                self.msj.exec()
                input.setFocus()
                return
            obj[keys[i]] = input.text()
            text=''
        
            
        for i,value in enumerate(list(obj.values())):
                
                if i == 2:
                    if not re.match(self.padre.re_telefono,value):
                        regex = False 
                        self.inputs[i].setFocus() 
                        text =f"Complete {self.padre.heads[i]} correctamente "  
                elif i == 3:
                    if not re.match(self.padre.re_cedula,value):
                        regex = False 
                        self.inputs[i].setFocus() 
                        text =f"Complete {self.padre.heads[i]} correctamente "     
                elif i == 4:
                    if not re.match(self.padre.re_fechas,value):
                        regex = False  
                        self.inputs[i].setFocus()   
                        text =f"Complete {self.padre.heads[i]} correctamente "  
                elif i == 5:
                    if not re.match(self.padre.re_fechas,value):
                        regex = False
                        self.inputs[i].setFocus() 
                        text =f"Complete {self.padre.heads[i]} correctamente "  
                elif i == 9:
                    if not re.match(self.padre.re_fechas,value):
                        regex = False
                        self.inputs[i].setFocus() 
                        text =f"Complete {self.padre.heads[i]} correctamente "  
                if not regex:
                    self.msj.setWindowTitle("Error")
                    self.msj.setIcon(QMessageBox.Icon.Critical)
                    self.msj.setStandardButtons(QMessageBox.StandardButton.Ok)
                    self.msj.setText(text)
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
        self.padre.save_excel(self.padre.convert_to_excel())
        for input in self.inputs:
            self.check_input = False
            input.setText("")
            
        self.msj.setWindowTitle("Ok")
        self.msj.setText("Agregado con éxito")
        self.msj.setIcon(QMessageBox.Icon.NoIcon)
        self.msj.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.msj.exec()
    def resta(self):
        if self.check_input: 
            try:
                poliza_total = int(self.inputs[8].text())
                total_pago  = int(self.inputs[10].text())
            except:
                self.msj.setWindowTitle("Error")
                self.msj.setIcon(QMessageBox.Icon.Critical)
                self.msj.setStandardButtons(QMessageBox.StandardButton.Ok)
                self.msj.setText(f"Por favor ingrese números enteros en los campos {self.padre.heads[8]} y {self.padre.heads[10]}")
                self.msj.exec()
                return

            total = poliza_total - total_pago
            self.inputs[11].setText(str(total))
        else:
            self.check_input = True