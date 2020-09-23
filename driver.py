from driverUi import *
import sys
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog
import serial, time
import serial.tools.list_ports




class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.colorpick)
        


    def colorpick(self,pt):
        pt = str(self.puertos(self.puertos))
        if 'COM' in pt:
            arduino = serial.Serial(pt,9600)
            color = QColorDialog.getColor()
            rgbc = list(color.getRgb())
            rgb1 = str(color.getRgb())
            r = rgbc[0]
            g = rgbc[1]
            b = rgbc[2]
            self.indicadores(r,g,b)
            rgb1 = rgb1[1:14]
            arduino.write(rgb1.encode())
        else:
            print("error el arduino no esta conectado")
 



    def puertos(self,prts):
        prts = list(serial.tools.list_ports.comports())   
        for p in prts:
            p = p[1]
            c = p[18:23]
            if "USB-SERIAL CH340" in p:
                c = str(c)
                self.estado1.setText("Conectado")
                self.estado1.setStyleSheet("QLabel { \n"
                "color: rgb(0, 255, 0);\n"
                "border-style:none;\n"
                "}")
                self.namedevice.setText(c)
                time.sleep(0.1)
                return c
            else:
                self.estado1.setText("No conectado")
                time.sleep(0.1)

   
    
    def indicadores(self,r,g,b):
        self.progressBar.setValue(r)
        self.progressBar_2.setValue(g)
        self.progressBar_3.setValue(b)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

