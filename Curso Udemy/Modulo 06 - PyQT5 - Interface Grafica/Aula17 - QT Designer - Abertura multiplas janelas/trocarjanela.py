# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trocarjanela.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Janela2(object):
    def setupUi(self, Janela2):
        Janela2.setObjectName("Janela2")
        Janela2.resize(497, 479)
        self.centralwidget = QtWidgets.QWidget(Janela2)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 260, 231, 141))
        self.pushButton.setObjectName("pushButton")
        Janela2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Janela2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 497, 21))
        self.menubar.setObjectName("menubar")
        Janela2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Janela2)
        self.statusbar.setObjectName("statusbar")
        Janela2.setStatusBar(self.statusbar)

        self.retranslateUi(Janela2)
        QtCore.QMetaObject.connectSlotsByName(Janela2)

    def retranslateUi(self, Janela2):
        _translate = QtCore.QCoreApplication.translate
        Janela2.setWindowTitle(_translate("Janela2", "MainWindow"))
        self.pushButton.setText(_translate("Janela2", "Voltar"))
