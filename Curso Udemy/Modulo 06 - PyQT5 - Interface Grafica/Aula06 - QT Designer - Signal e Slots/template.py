# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'template.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 276)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonCopiar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCopiar.setGeometry(QtCore.QRect(300, 50, 91, 41))
        self.pushButtonCopiar.setObjectName("pushButtonCopiar")
        self.pushButtonColar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonColar.setGeometry(QtCore.QRect(300, 110, 91, 41))
        self.pushButtonColar.setObjectName("pushButtonColar")
        self.lineEditInserir = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditInserir.setGeometry(QtCore.QRect(160, 50, 121, 41))
        self.lineEditInserir.setObjectName("lineEditInserir")
        self.LineEditColar = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEditColar.setGeometry(QtCore.QRect(160, 110, 121, 41))
        self.LineEditColar.setObjectName("LineEditColar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.pushButtonCopiar.pressed.connect(self.lineEditInserir.selectAll)
        self.pushButtonCopiar.released.connect(self.lineEditInserir.copy)
        self.pushButtonColar.clicked.connect(self.LineEditColar.paste)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonCopiar.setText(_translate("MainWindow", "Copiar"))
        self.pushButtonColar.setText(_translate("MainWindow", "Colar"))