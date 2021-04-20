import sys
from PyQt5.QtWidgets import QApplication
from app import App


aplication = QApplication(sys.argv)
app = App()

app.show()
aplication.exec_()