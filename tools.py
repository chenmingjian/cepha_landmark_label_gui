from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow

from Digitize import Ui_MainWindow


class ToolWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def display(self):
        self.show()
