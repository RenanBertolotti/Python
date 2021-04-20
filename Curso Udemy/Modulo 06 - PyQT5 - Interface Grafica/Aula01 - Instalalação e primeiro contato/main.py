"""
PyQT é um toolkit desenvolvido em C++ utilizado por varios programas para criação de aplicações GUI(Interface Grafica).
Tambem inclui diversas funcionalidades, como: acesso a base de dados, threads, comunicação de rede, e etc...

pip install pyqt5
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.centralWidget = QWidget()
        self.grid = QGridLayout(self.centralWidget)

        self.button = QPushButton("Texto do Botao")
        self.button.setStyleSheet("Font-size: 20px;")
        # self.button.clicked.connect(lambda: print("Ola mundo"))
        self.button.clicked.connect(self.metodo)

        self.grid.addWidget(self.button, 0, 0, 1, 1)
        self.setCentralWidget(self.centralWidget)

    def metodo(self):
        print("Metodo chamado")


qt = QApplication(sys.argv)
app = App()

app.show()
qt.exec_()

if app.close() is True:
    print("programa finalizado")
