# coding:utf-8
import os
import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow, QFileDialog
from test import Ui_MainWindow
from ImgLabel import ImgLabel
from tools import ToolWidget


class Example(QMainWindow, Ui_MainWindow):
    tool_widget = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.center()
        self.setWindowTitle('Landmark Label Tool')
        self.img_label = ImgLabel(None)
        self.horizontalLayout_2.addWidget(self.img_label)
        # self.open_img()
        self.actionOpen.triggered.connect(self.open_img)
        self.showMaximized()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        # self.setGeometry(QDesktopWidget().availableGeometry())

    def open_img(self):
        filename_choose, filetype = QFileDialog.getOpenFileName(self, "选取图片", os.getcwd(), "jpg (*.jpg)")
        if filename_choose == "":
            return
        img_path = filename_choose
        # img_path = '1-3.jpg'
        self.img_label.change_img(img_path)
        self.img_label.mouseMoved.connect(self.tool_widget.show_bigger_img)
        self.img_label.mouseClicked.connect(self.tool_widget.listWidget.select_next_item)

    def closeEvent(self, e):
        super().closeEvent(e)
        QCoreApplication.instance().quit()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()

    tool = ToolWidget()
    ex.tool_widget = tool
    ex.actionDigitize_Tools.triggered.connect(tool.show)
    ex.actionOpen.triggered.connect(tool.show)
    tool.listWidget.itemClicked.connect(ex.img_label.on_list_clicked)
    tool.listWidget.noItemInList.connect(ex.img_label.no_item)
    sys.exit(app.exec_())


