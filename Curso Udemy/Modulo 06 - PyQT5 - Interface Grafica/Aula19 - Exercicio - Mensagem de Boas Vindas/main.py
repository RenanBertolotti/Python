import sys
from app import App
from PyQt5.QtWidgets import QApplication


aplication = QApplication(sys.argv)
app = App()

app.show()
aplication.exec_()