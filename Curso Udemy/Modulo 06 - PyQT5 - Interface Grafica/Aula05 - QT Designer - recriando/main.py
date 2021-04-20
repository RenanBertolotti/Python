from app import App
from PyQt5.QtWidgets import QApplication
import sys


aplicacao = QApplication(sys.argv)
app = App()

app.show()
aplicacao.exec_()