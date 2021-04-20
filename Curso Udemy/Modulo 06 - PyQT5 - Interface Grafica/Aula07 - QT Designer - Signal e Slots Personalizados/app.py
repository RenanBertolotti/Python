from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from templatebotao import Ui_MainWindow


class Sinais(QtCore.QObject):
    sinal1 = QtCore.pyqtSignal()
    sinal2 = QtCore.pyqtSignal(str, name="sinalStr")


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.sinais = Sinais()

        self.pushButton.clicked.connect(self.funcao1)

    def funcao1(self):
        print("botao1 clickado")
        self.sinais.sinal1.connect(self.recebeSinal)
        self.sinais.sinal1.emit()
        self.sinais.sinal1.disconnect()

        self.sinais.sinal2.connect(self.recebeSinal2)
        self.sinais.sinal2.emit("str")
        self.sinais.sinal2.disconnect()

    def recebeSinal(self):
        print("Sinal emitido com sucesso!")

    def recebeSinal2(self, str):
        print(str)
