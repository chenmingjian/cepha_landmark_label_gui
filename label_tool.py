import sys
import os

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel, QFileDialog, QDesktopWidget, QApplication,QMainWindow
from PyQt5 import QtGui, QtCore
from test import Ui_MainWindow
import cv2


class Example(QMainWindow, Ui_MainWindow):
    _img_file = ''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.center()
        self.setWindowTitle('Landmark Label Tool')
        self.actionOpen.triggered.connect(self.open_img)

    def open_img(self):
        # filename_choose, filetype = \
        #     QFileDialog.getOpenFileName(self,
        #                                 "选取图片",
        #                                 os.getcwd(),
        #                                 "jpg (*.jpg)")
        # if filename_choose == "":
        #     return
        # _img_file = filename_choose
        _img_file = R'D:\labwork\点集注册\red_dot\2_350\1-100\1-2.jpg'
        png = self.cvimg2qt(self, _img_file)

        # l1 = QLabel(self.img_widget)
        # png = QtGui.QPixmap(_img_file)
        self.img_label.setCursor(QtCore.Qt.CrossCursor)
        self.img_label.setPixmap(png)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.setGeometry(QDesktopWidget().availableGeometry())
        self.showMaximized()

    def cvimg2qt(self, img_path):
        print('debug0')
        img = cv2.imread(img_path, 1)
        height, width, channel = img.shape
        byte_per_line = channel * width
        print('debug1')
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
        print('debug2')
        q_img = QImage(img.data, width, height, byte_per_line, QImage.Format_RGB888)
        print('debug3')
        pixmap = QPixmap.fromImage(q_img)
        return pixmap


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
