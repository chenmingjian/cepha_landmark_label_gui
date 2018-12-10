from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QModelIndex, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QListWidget

from Digitize import Ui_MainWindow
import numpy as np

tmp_landmark_name_list = np.loadtxt('landmark_name.txt', dtype=str)


class ListWidget(QListWidget):
    current_item_num = 0
    modify = False

    def __init__(self, name_list = tmp_landmark_name_list):
        super().__init__()
        self.insertItems(0, name_list)
        self.setMinimumWidth(self.sizeHintForColumn(0))
        first_list_item = self.item(self.current_item_num)
        self.setCurrentItem(first_list_item)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.setObjectName("listWidget")

    noItemInList = pyqtSignal()

    def select_next_item(self):
        if self.modify:
            self.modify = False
        else:
            self.current_item_num += 1
        next_item = self.item(self.current_item_num)
        if next_item is None:
            self.noItemInList.emit()
        self.setCurrentItem(next_item)

    itemClicked = pyqtSignal(int)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        num = self.currentIndex().row()
        if num < self.current_item_num:
            super().mousePressEvent(event)
            self.itemClicked.emit(num)
            self.modify = True
        else:
            current_item_num = self.item(self.current_item_num)
            self.setCurrentItem(current_item_num)

    def clear_current_item_num(self):
        self.current_item_num = 0
        first_list_item = self.item(self.current_item_num)
        self.setCurrentItem(first_list_item)

    def mouseMoveEvent(self, *args, **kwargs):
        pass

    def on_item_selected(self):
        pass


class ToolWidget(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.move(20, 150)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # 取消置顶
        # self.setWindowFlags(Qt.Widget)
        self.listWidget = ListWidget()
        self.horizontalLayout_3.addWidget(self.listWidget)

    def show_bigger_img(self, part):
        self.label_3.setPixmap(part)

