import sys

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QListWidget, QApplication, QWidget, QHBoxLayout, QLineEdit, \
    QPushButton

from Digitize import Ui_MainWindow
import numpy as np
from ImgLabel import cv2qt

tmp_landmark_name_list = ['N', 'S', 'P', 'Ba', 'Bo', 'Or', 'Ptm', 'ANS', 'PNS', 'SPr', 'A', 'UI', 'UIA', 'LI', 'LIA', 'Id', 'Pog', 'B', 'Me', 'Gn', 'Go', 'Ar', 'Co', 'G', 'N', 'Prn', 'Sn', 'Ls', 'St', 'Li', 'Si', 'Pog', 'Gn', 'Me']


# class ItemWidget(QWidget):
#
#     item = pyqtSignal(QListWidgetItem)
#
#     def __init__(self, text, item, *args, **kwargs):
#         super(ItemWidget, self).__init__(*args, **kwargs)
#         self._item = item
#         layout = QHBoxLayout(self)
#         layout.setContentsMargins(0, 0, 0, 0)
#         line_edit = QLineEdit(text, self)
#         line_edit.setAlignment(Qt.AlignCenter)
#         line_edit.setFrame(False)
#         # line_edit.setEnabled(False)
#         line_edit.setFocusPolicy(Qt.NoFocus)
#         layout.addWidget(line_edit)
#         line_edit.setCursor(Qt.ArrowCursor)
#
#
#     def doDeleteItem(self):
#         self.item.emit(self._item)
#
#     def sizeHint(self):
#         # 决定item的高度
#         return QSize(100, 40)


class ToolWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_list_widget()
        self.move(100, 200)

        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # 取消置顶
        # self.setWindowFlags(Qt.Widget)
        self.show()

    def display(self):
        self.show()

    def set_list_widget(self):
        self.listWidget.insertItems(0, tmp_landmark_name_list)
        self.listWidget.setMinimumWidth(self.listWidget.sizeHintForColumn(0))

    def show_biger_img(self, part):
        # tmp = cv2qt(part)
        # print(str(part[0][0]))
        # self.label_3.setText(str(part))
        # print(1)
        self.label_3.setPixmap(part)


# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     tool = ToolWidget()
#     app.exec_()
