import sys 
from PyQt6.QtWidgets import  QApplication,QMainWindow,QLabel,QVBoxLayout,QTextEdit,QPushButton,QTableWidget,QTableWidgetItem,QMessageBox
from PyQt6.QtGui import QAction

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width =1080
        self.height =580
        self.setGeometry(0,0,self.width,self.height)
        self.setWindowTitle("Sistemas de seguro")
        self.setFixedSize(self.width, self.height)
        menu_bar = self.menuBar()
        self.msj = QMessageBox()

        #variables
        y_buscador = 180
        
        #array fixticio
        self.valores =[
            {"nombre":"richie","fecha de nac.":"05/5/1996","cedula":"4-52020120-9","telefono":"809-999-5555","fecha de inicio":"05/3/2025","fecha de venc.":"20/2/2025","no. poliza":"892221132555"},
            {"nombre":"richie","fecha de nac.":"05/5/1996","cedula":"4-52020120-5","telefono":"809-999-5555","fecha de inicio":"05/3/2025","fecha de venc.":"20/2/2025","no. poliza":"892221132555"},
            {"nombre":"richie","fecha de nac.":"05/5/1996","cedula":"4-52020120-9","telefono":"809-999-5555","fecha de inicio":"05/3/2025","fecha de venc.":"20/2/2025","no. poliza":"892221132555"}
            ]
        
        #layaout
        layout =QVBoxLayout()

        #crear label
        label_width= 100
        label_height=30
        label = QLabel("buscador:",self)
        label.setGeometry(int(self.width/2),y_buscador,label_width,label_height)
        label.setStyleSheet("font-size: 20px; color: blue; text-align:") 

        #titulo
        titulo_width  = 450
        titulo_height =80
        titulo = QLabel("Seguros Atlanta",self)
        titulo.setGeometry(int(self.width/3.5),60,titulo_width,titulo_height)
        titulo.setStyleSheet("font-size:60px;border:1px solid black;")
        
         #input
        input_width=200
        input_height=35
        self.buscador_input = QTextEdit(self)
        self.buscador_input.setPlaceholderText("Introdusca el DNI o el mes")
        self.buscador_input.setGeometry(int(self.width/2)+100,y_buscador,input_width,input_height)
        self.buscador_input.setStyleSheet("font-size:15px;")

       #button
        button= QPushButton("Ok",self)
        button.setGeometry(int(self.width/2)+input_width+label_width,y_buscador,60,35)
        button.setStyleSheet("font-size:15px;")

        #add layout
        layout.addWidget(label)
        layout.addWidget(self.buscador_input)
        layout.addWidget(button)

        self.table = QTableWidget(self)  
        self.table.setGeometry(50,y_buscador+80,int(self.width/1.1),int(self.height/2.5))
        self.table.setStyleSheet("font-size:15px")
        self.table.setRowCount(len(self.valores))
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["Nombre","Fecha de Nac.","Cedula","Telefono","Fecha de inicio","Fecha de Venc.","No. poliza"])
        self.table.setColumnWidth(0, int((self.width/1.1)/7))
        self.table.setColumnWidth(1, int((self.width/1.1)/7))
        self.table.setColumnWidth(2, int((self.width/1.1)/7))
        self.table.setColumnWidth(3, int((self.width/1.1)/7))
        self.table.setColumnWidth(4, int((self.width/1.1)/7))
        self.table.setColumnWidth(5, int((self.width/1.1)/7))
        self.table.setColumnWidth(6, int((self.width/1.1)/7))

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

        layout.addWidget(self.table)
        self.setLayout(layout)
        
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
        button.clicked.connect(self.buscar)

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

    def buscar(self):
        
        input = self.buscador_input.toPlainText()
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

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mi_ventana= Ventana()
    mi_ventana.show()
    sys.exit(app.exec())


    