# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conversor.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 283)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 30, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 30, 47, 13))
        self.label_3.setObjectName("label_3")
        self.valorParaConverter = QtWidgets.QLineEdit(self.centralwidget)
        self.valorParaConverter.setGeometry(QtCore.QRect(20, 50, 113, 20))
        self.valorParaConverter.setObjectName("valorParaConverter")
        self.cbConverterDe = QtWidgets.QComboBox(self.centralwidget)
        self.cbConverterDe.setGeometry(QtCore.QRect(150, 50, 175, 20))
        self.cbConverterDe.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cbConverterDe.setObjectName("cbConverterDe")
        self.cbConverterDe.addItem("")
        self.cbConverterDe.addItem("")
        self.cbConverterDe.addItem("")
        self.cbConverterPara = QtWidgets.QComboBox(self.centralwidget)
        self.cbConverterPara.setGeometry(QtCore.QRect(340, 50, 111, 21))
        self.cbConverterPara.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cbConverterPara.setObjectName("cbConverterPara")
        self.cbConverterPara.addItem("")
        self.cbConverterPara.addItem("")
        self.cbConverterPara.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 131, 21))
        self.label_4.setObjectName("label_4")
        self.valorConvertido = QtWidgets.QLineEdit(self.centralwidget)
        self.valorConvertido.setGeometry(QtCore.QRect(20, 130, 141, 31))
        self.valorConvertido.setObjectName("valorConvertido")
        self.btnConverter = QtWidgets.QPushButton(self.centralwidget)
        self.btnConverter.setGeometry(QtCore.QRect(290, 120, 75, 23))
        self.btnConverter.setObjectName("btnConverter")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Conversor de Moedas"))
        self.label.setText(_translate("MainWindow", "Valor:"))
        self.label_2.setText(_translate("MainWindow", "Converter de"))
        self.label_3.setText(_translate("MainWindow", "Para"))
        self.cbConverterDe.setItemText(0, _translate("MainWindow", "Real(BRL)"))
        self.cbConverterDe.setItemText(1, _translate("MainWindow", "Dolar dos Estados Unidos(USD)"))
        self.cbConverterDe.setItemText(2, _translate("MainWindow", "Iene(JPY)"))
        self.cbConverterPara.setItemText(0, _translate("MainWindow", "Real(BRL)"))
        self.cbConverterPara.setItemText(1, _translate("MainWindow", "Dolar dos Estados Unidos(USD)"))
        self.cbConverterPara.setItemText(2, _translate("MainWindow", "Iene(JPY)"))
        self.label_4.setText(_translate("MainWindow", "Resultado da Conversao:"))
        self.btnConverter.setText(_translate("MainWindow", "Converter"))
