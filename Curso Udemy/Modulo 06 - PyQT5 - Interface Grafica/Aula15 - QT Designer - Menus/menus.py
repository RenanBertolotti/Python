# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menus.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 409)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setTearOffEnabled(False)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuAbrir = QtWidgets.QMenu(self.menuArquivo)
        self.menuAbrir.setObjectName("menuAbrir")
        self.menuEditar = QtWidgets.QMenu(self.menubar)
        self.menuEditar.setObjectName("menuEditar")
        MainWindow.setMenuBar(self.menubar)
        self.actionSalvar = QtWidgets.QAction(MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionTexto = QtWidgets.QAction(MainWindow)
        self.actionTexto.setObjectName("actionTexto")
        self.actionPython = QtWidgets.QAction(MainWindow)
        self.actionPython.setObjectName("actionPython")
        self.menuAbrir.addAction(self.actionTexto)
        self.menuAbrir.addAction(self.actionPython)
        self.menuArquivo.addAction(self.menuAbrir.menuAction())
        self.menuArquivo.addAction(self.actionSalvar)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuAbrir.setTitle(_translate("MainWindow", "Abrir"))
        self.menuEditar.setTitle(_translate("MainWindow", "Editar"))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar"))
        self.actionSalvar.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionTexto.setText(_translate("MainWindow", "Texto"))
        self.actionTexto.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionPython.setText(_translate("MainWindow", "Python"))
        self.actionPython.setShortcut(_translate("MainWindow", "Ctrl+P"))
