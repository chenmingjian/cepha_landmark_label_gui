import sys
import os

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtWidgets import QLabel, QFileDialog, QDesktopWidget, QApplication, QMainWindow, QSizePolicy
from PyQt5 import QtGui, QtCore, QtWidgets
from test import Ui_MainWindow
import cv2
from ImgLabel import ImgLabel
from tools import ToolWidget


class Example(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.center()
        self.setWindowTitle('Landmark Label Tool')
        self.open_img()
        # self.actionOpen.triggered.connect(self.open_img)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        # self.setGeometry(QDesktopWidget().availableGeometry())
        self.showNormal()
        self.showMaximized()
        self.show()

    def open_img(self):
        # filename_choose, filetype = QFileDialog.getOpenFileName(self, "选取图片", os.getcwd(), "jpg (*.jpg)")
        # if filename_choose == "":
        #     return
        # img_path = filename_choose
        img_path = '1-3.jpg'
        self.img_label = ImgLabel(img_path)
        self.verticalLayout.addWidget(self.img_label)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()

    tool = ToolWidget()
    ex.img_label.mouseMoved.connect(tool.show_biger_img)
    ex.actionDigitize_Tools.triggered.connect(tool.display)
    sys.exit(app.exec_())
