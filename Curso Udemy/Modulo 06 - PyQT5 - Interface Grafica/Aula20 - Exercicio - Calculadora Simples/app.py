from PyQt5.QtWidgets import QMainWindow
from calculadora import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.pushButton.clicked.connect(self.somar)
        self.pushButton_2.clicked.connect(self.subtrair)
        self.pushButton_3.clicked.connect(self.divisao)
        self.pushButton_4.clicked.connect(self.multiplicacao)

    def somar(self):
        numero1 = float(self.lineEdit_2.text())
        numero2 = float(self.lineEdit_3.text())
        resultado = numero1 + numero2

        self.lineEdit.setText(str(resultado))

    def subtrair(self):
        numero1 = float(self.lineEdit_2.text())
        numero2 = float(self.lineEdit_3.text())
        resultado = numero1 - numero2

        self.lineEdit.setText(str(resultado))

    def divisao(self):
        numero1 = float(self.lineEdit_2.text())
        numero2 = float(self.lineEdit_3.text())
        resultado = numero1 / numero2

        self.lineEdit.setText(str(resultado))

    def multiplicacao(self):
        numero1 = float(self.lineEdit_2.text())
        numero2 = float(self.lineEdit_3.text())
        resultado = numero1 * numero2

        self.lineEdit.setText(str(resultado))
