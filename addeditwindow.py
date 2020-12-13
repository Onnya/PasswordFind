from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow


class AddEditWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi('addeditwindow.ui', self)
        self.setFixedSize(319, 304)