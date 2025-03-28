from PyQt6.QtWidgets import  QWidget,QLabel,QVBoxLayout,QHBoxLayout,QLineEdit,QPushButton,QTableWidget,QTableWidgetItem,QMessageBox
from PyQt6.QtCore import Qt

class Inicio(QWidget):
    def __init__(self):
        super().__init__()
        self.width=1000
        self.height=500
        self.setGeometry(10,200,self.width,self.height)

        #variables
        self.y_buscador = 300
        self.msj =QMessageBox()
        layout = QVBoxLayout()
        div_buscador= QHBoxLayout()

        #array fixticio
        self.valores =[
            {"nombre":"richie","fecha de nac.":"05/5/1996","cedula":"4-52020120-9","telefono":"809-999-5555","fecha de inicio":"05/3/2025","fecha de venc.":"20/2/2025","no. poliza":"892221132555"},
            {"nombre":"richie","fecha de nac.":"05/5/1996","cedula":"4-52020120-5","telefono":"809-999-5555","fecha de inicio":"05/3/2025","fecha de venc.":"20/2/2025","no. poliza":"892221132555"},
            {"nombre":"richie","fecha de nac.":"05/5/1996","cedula":"4-52020120-9","telefono":"809-999-5555","fecha de inicio":"05/3/2025","fecha de venc.":"20/2/2025","no. poliza":"892221132555"}
            ]
        
        #crear label
        label_width= 100
        label_height=30
        label = QLabel("buscador:",self)
        label.setStyleSheet("font-size: 20px; color: blue; text-align:") 
        label.setAlignment(Qt.AlignmentFlag.AlignRight)

        #input
        input_width=200
        input_height=35
        self.buscador_input = QLineEdit(self)
        self.buscador_input.setPlaceholderText("Introdusca el DNI o el mes")
        self.buscador_input.setGeometry(int(self.width/2)+100,self.y_buscador,input_width,input_height)
        self.buscador_input.setStyleSheet("font-size:15px;")    
        self.buscador_input.setFixedWidth(input_width)    
        
        #button
        button= QPushButton("Ok",self)
        button.setGeometry(int(self.width/2),self.y_buscador,60,35)
        button.setStyleSheet("font-size:15px;")
        button.setFixedWidth(60) 

        #button actualizar
        button_actualizar = QPushButton("Actualizar",self)
        button_actualizar.setGeometry(int(self.width/2),self.y_buscador,60,35)
        button_actualizar.setStyleSheet("font-size:15px;")
        button_actualizar.setFixedWidth(100) 

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
            self.msj.setText("Debes de rellenar el campo")
            self.msj.setIcon(QMessageBox.Icon.Warning)
            self.msj.setWindowTitle("Seguros Atlanta")
            self.msj.setStandardButtons(QMessageBox.StandardButton.Ok)
            self.msj.exec()
            
            return
        poliza = False
        for i,valor in enumerate(self.valores):
            if valor["cedula"] == input:
                poliza = self.valores[i]
            elif valor["fecha de inicio"] == input:
                poliza= self.valores[i]
        if poliza == False:
            self.msj.setText("No se pudo encontrar dicha poliza")
            self.msj.setIcon(QMessageBox.Icon.Critical)
            self.msj.setWindowTitle("Seguros atlanta")
            self.msj.exec()
            return
        self.table.clearContents() 
        self.table.setRowCount(1)
        self.table.setItem(0,0,QTableWidgetItem(poliza["nombre"]))
        self.table.setItem(0,1,QTableWidgetItem(poliza["fecha de nac."]))
        self.table.setItem(0,2,QTableWidgetItem(poliza["cedula"]))
        self.table.setItem(0,3,QTableWidgetItem(poliza["telefono"]))
        self.table.setItem(0,4,QTableWidgetItem(poliza["fecha de inicio"]))
        self.table.setItem(0,5,QTableWidgetItem(poliza["fecha de venc."]))
        self.table.setItem(0,6,QTableWidgetItem(poliza["no. poliza"]))


    def actulizar(self):
        self.table.clearContents() 
        self.table.setRowCount(len(self.valores))
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["Nombre","Fecha de Nac.","Cedula","Telefono","Fecha de inicio","Fecha de Venc.","No. poliza"])
        self.table.setColumnWidth(0, int((self.width+15)/7))
        self.table.setColumnWidth(1, int((self.width+15)/7))
        self.table.setColumnWidth(2, int((self.width+15)/7))
        self.table.setColumnWidth(3, int((self.width+15)/7))
        self.table.setColumnWidth(4, int((self.width+15)/7))
        self.table.setColumnWidth(5, int((self.width+15)/7))
        self.table.setColumnWidth(6, int((self.width+15)/7))
        
        #bucle parea anadir los item
        item=0
        for i,key in enumerate(self.valores) :
            item_1=QTableWidgetItem(key["nombre"])
            item_2=QTableWidgetItem(key["fecha de nac."])
            item_3=QTableWidgetItem(key["cedula"])
            item_4=QTableWidgetItem(key["telefono"])
            item_5=QTableWidgetItem(key["fecha de inicio"])
            item_6=QTableWidgetItem(key["fecha de venc."])
            item_7=QTableWidgetItem(key["no. poliza"])
            self.table.setItem(i,item,item_1)
            self.table.setItem(i,item+1,item_2)
            self.table.setItem(i,item+2,item_3)
            self.table.setItem(i,item+3,item_4)
            self.table.setItem(i,item+4,item_5)
            self.table.setItem(i,item+5,item_6)
            self.table.setItem(i,item+6,item_7)