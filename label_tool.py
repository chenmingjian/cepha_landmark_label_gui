import sys
import os
from PyQt5.QtWidgets import QLabel, QFileDialog, QDesktopWidget, QApplication,QMainWindow
from PyQt5 import QtGui
from test import Ui_MainWindow


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
        _img_file = R'D:\labwork\点集注册\red_dot\2_350\1-100\1-2.jpg'# filename_choose
        print(_img_file)
        # l1 = QLabel(self.img_widget)
        png = QtGui.QPixmap(_img_file)
        print(png)
        self.img_label.setPixmap(png)

        self.img_label.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        # self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
