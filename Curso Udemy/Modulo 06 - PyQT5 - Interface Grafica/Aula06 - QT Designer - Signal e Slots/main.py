import sys
from app import App
from PyQt5.QtWidgets import QApplication


aplicacao = QApplication(sys.argv)
app = App()


app.show()
aplicacao.exec_()

