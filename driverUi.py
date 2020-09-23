# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'driver.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 640)
        MainWindow.setMaximumSize(QtCore.QSize(360, 640))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 360, 640))
        self.frame.setMaximumSize(QtCore.QSize(360, 640))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgb(36, 37, 85);\n"
"border-style:solid;\n"
"border-width: 4px;\n"
"border-radius: 4px;\n"
"border-color: rgb(0, 0, 255);\n"
"}\n"
"\n"
"QFrame:hover {\n"
"border-style:solid;\n"
"border-width: 5px;\n"
"    border-color: rgb(0, 85, 255);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.title = QtWidgets.QLabel(self.frame)
        self.title.setGeometry(QtCore.QRect(120, 30, 81, 21))
        self.title.setMaximumSize(QtCore.QSize(111, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("QLabel{\n"
"color: rgb(202, 27, 27);\n"
"border-style:none;\n"
"\n"
"}\n"
"")
        self.title.setTextFormat(QtCore.Qt.AutoText)
        self.title.setObjectName("title")
        self.title2 = QtWidgets.QLabel(self.frame)
        self.title2.setGeometry(QtCore.QRect(200, 30, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title2.setFont(font)
        self.title2.setStyleSheet("QLabel {\n"
"color: rgb(55, 40, 233);\n"
"border-style:none;\n"
"}\n"
"")
        self.title2.setObjectName("title2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(94, 210, 181, 181))
        self.pushButton.setMaximumSize(QtCore.QSize(1000, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-left-color: rgb(0, 0, 255);\n"
"border-right-color: rgb(0, 0, 255);\n"
"border-top-color: rgb(191, 14, 14);\n"
"border-bottom-color: rgb(191, 14, 14);\n"
"border-width: 5px;\n"
"border-radius: 90px;\n"
"background-color: rgb(3, 6, 154);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"border-top-color: rgb(0, 0, 255);\n"
"border-bottom-color: rgb(0, 0, 255);\n"
"border-left-color: rgb(191, 14, 14);\n"
"border-right-color: rgb(191, 14, 14);\n"
"border-width: 5px;\n"
"\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.estado = QtWidgets.QLabel(self.frame)
        self.estado.setGeometry(QtCore.QRect(30, 580, 47, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        self.estado.setFont(font)
        self.estado.setStyleSheet("QLabel {\n"
"color: rgb(34, 141, 255);\n"
"border-style:none;        \n"
"}")
        self.estado.setObjectName("estado")
        self.estado1 = QtWidgets.QLabel(self.frame)
        self.estado1.setGeometry(QtCore.QRect(70, 580, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        self.estado1.setFont(font)
        self.estado1.setStyleSheet("QLabel { \n"
"color: rgb(255, 0, 0);\n"
"border-style:none;\n"
"}")
        self.estado1.setTextFormat(QtCore.Qt.AutoText)
        self.estado1.setObjectName("estado1")
        self.Dispositivo = QtWidgets.QLabel(self.frame)
        self.Dispositivo.setGeometry(QtCore.QRect(240, 580, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        self.Dispositivo.setFont(font)
        self.Dispositivo.setStyleSheet("QLabel {\n"
"color: rgb(0, 170, 255);\n"
"border-style:none;\n"
"}")
        self.Dispositivo.setObjectName("Dispositivo")
        self.namedevice = QtWidgets.QLabel(self.frame)
        self.namedevice.setGeometry(QtCore.QRect(300, 580, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(8)
        self.namedevice.setFont(font)
        self.namedevice.setStyleSheet("QLabel {\n"
"color: rgb(0, 170, 255);\n"
"border-style:none;\n"
"}")
        self.namedevice.setObjectName("namedevice")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(120, 610, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel {\n"
"color: rgb(16, 180, 255);\n"
"border-style: none\n"
"}")
        self.label_7.setObjectName("label_7")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(80, 420, 201, 110))
        self.frame_2.setMaximumSize(QtCore.QSize(201, 110))
        self.frame_2.setStyleSheet("QFrame {\n"
"background-color: rgb(36, 37, 85);\n"
"border-width : 2px;\n"
"border-color : blue;\n"
"border- style : none;\n"
"border-radius: 4px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar.setGeometry(QtCore.QRect(30, 20, 120, 15))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximumSize(QtCore.QSize(120, 15))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"color: black;\n"
"background-color: rgb(182, 182, 182);\n"
"border-style: none;\n"
"border-radius: 3px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"border-style: none;\n"
"border-radius: 3px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")
        self.progressBar.setMaximum(255)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar_2.setGeometry(QtCore.QRect(30, 50, 120, 15))
        self.progressBar_2.setMaximumSize(QtCore.QSize(120, 15))
        self.progressBar_2.setStyleSheet("QProgressBar{\n"
"color: black;\n"
"background-color: rgb(182, 182, 182);\n"
"border-style: none;\n"
"border-radius: 3px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"border-style: none;\n"
"border-radius: 3px;\n"
"background-color: rgb(0,255, 0);\n"
"}")
        self.progressBar_2.setMaximum(255)
        self.progressBar_2.setProperty("value", 95)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar_3.setGeometry(QtCore.QRect(30, 80, 120, 15))
        self.progressBar_3.setMaximumSize(QtCore.QSize(120, 15))
        self.progressBar_3.setStyleSheet("QProgressBar{\n"
"color: black;\n"
"background-color: rgb(182, 182, 182);\n"
"border-style: none;\n"
"border-radius: 3px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"border-style: none;\n"
"border-radius: 3px;\n"
"background-color: rgb(0, 0, 255);\n"
"}")
        self.progressBar_3.setMaximum(255)
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(15, 19, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"border-style:none;\n"
"color: rgb(255, 0, 0);\n"
"background-color: none;\n"
"}")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(14, 49, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"border-style:none;\n"
"color: rgb(0, 255, 0);\n"
"background-color: none;\n"
"}")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(15, 79, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"border-style:none;\n"
"color: rgb(0, 0, 255);\n"
"background-color: none;\n"
"}")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DriverRGB"))
        self.title.setText(_translate("MainWindow", "Driver"))
        self.title2.setText(_translate("MainWindow", "RGB"))
        self.pushButton.setText(_translate("MainWindow", "Seleccionar Color"))
        self.estado.setText(_translate("MainWindow", "Estado:"))
        self.estado1.setText(_translate("MainWindow", "\"\""))
        self.Dispositivo.setText(_translate("MainWindow", "Dispositivo:"))
        self.namedevice.setText(_translate("MainWindow", "\"\""))
        self.label_7.setText(_translate("MainWindow", "Developed by: Sonny Castro"))
        self.progressBar.setFormat(_translate("MainWindow", "%v"))
        self.progressBar_2.setFormat(_translate("MainWindow", "%v"))
        self.progressBar_3.setFormat(_translate("MainWindow", "%v"))
        self.label.setText(_translate("MainWindow", "R"))
        self.label_2.setText(_translate("MainWindow", "G"))
        self.label_3.setText(_translate("MainWindow", "B"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
