import sys
from app import App
from PyQt5.QtWidgets import QApplication


application = QApplication(sys.argv)
app = App()

app.show()
application.exec_()