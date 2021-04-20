import sys
from PyQt5.QtWidgets import QApplication
from calculador import Calculadora

aplicacao = QApplication(sys.argv)
app = Calculadora()

app.show()
aplicacao.exec_()
