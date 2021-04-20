import sys
from PyQt5.QtWidgets import QApplication
from app import App


aplicacao = QApplication(sys.argv)
app = App()

app.show()
aplicacao.exec_()