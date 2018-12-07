import sys
import os

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtWidgets import QLabel, QFileDialog, QDesktopWidget, QApplication, QMainWindow, QSizePolicy
from PyQt5 import QtGui, QtCore, QtWidgets
from test import Ui_MainWindow
import cv2
from ImgLabel import ImgLabel


class Example(QMainWindow, Ui_MainWindow):
    _img_file = ''

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
        self.setGeometry(QDesktopWidget().availableGeometry())
        self.showMaximized()

    def open_img(self):
        # filename_choose, filetype = \
        #     QFileDialog.getOpenFileName(self,
        #                                 "选取图片",
        #                                 os.getcwd(),
        #                                 "jpg (*.jpg)")
        # if filename_choose == "":
        #     return
        # _img_file = filename_choose
        _img_file = '1-3.jpg'

        png = self.cvimg2qt(_img_file)

        self.img_label = ImgLabel(self)
        # self.fb.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.img_label.setCursor(QtCore.Qt.CrossCursor)

        self.img_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_label.sizePolicy().hasHeightForWidth())
        self.img_label.setSizePolicy(sizePolicy)
        self.img_label.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.img_label.setText("")
        self.img_label.setObjectName("img_label")
        self.verticalLayout.addWidget(self.img_label)
        self.img_label.setPixmap(png)

    def cvimg2qt(self, img_path):
        img = cv2.imread(img_path)
        height, width, channel = img.shape
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
        cp = QDesktopWidget().availableGeometry()
        scale = height / cp.bottom()*1.13
        print(scale)
        print((int(cp.bottom()), int(width / scale)))
        img = cv2.resize(img, (int(height / scale), int(width / scale)))
        print(img.shape)
        height, width, channel = img.shape
        byte_per_line = channel * width
        q_img = QImage(img.data, width, height, byte_per_line, QImage.Format_RGB888)
        q_pixmap = QPixmap.fromImage(q_img)
        return q_pixmap


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
