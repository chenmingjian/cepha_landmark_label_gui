# coding:utf-8
import os
import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow, QFileDialog
from test import Ui_MainWindow
from ImgLabel import ImgLabel
from tools import ToolWidget

IMG_FORMAT = ['bmp', 'jpg', 'png', 'tif', 'peg']


class Example(QMainWindow, Ui_MainWindow):
    tool_widget = None
    file_name = ''
    label_dir = ''
    img_dir = ''
    file_name_list =[]
    current_img_num = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.center()
        self.setWindowTitle('Landmark Label Tool')
        self.img_label = ImgLabel(None, None)

        self.horizontalLayout_2.addWidget(self.img_label)
        # self.open_img()
        self.actionOpen.triggered.connect(self.open_img)
        self.actionOpen_Dir.triggered.connect(self.open_dir)
        self.showMaximized()
        self.show()

    def set_tool_widget(self, tool_widget):
        self.tool_widget = tool_widget
        self.img_label.mouseMoved.connect(self.tool_widget.show_bigger_img)
        self.img_label.mouseClicked.connect(self.tool_widget.listWidget.select_next_item)

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

        self.label_dir = os.path.dirname(img_path) + '/' + 'label/'
        if not os.path.isdir(self.label_dir):
            os.mkdir(self.label_dir)
        save_path = self.label_dir + os.path.split(img_path)[-1][:-3] + 'txt'
        self.show_img_in_label(img_path, save_path)

    def show_img_in_label(self, img_path, save_path):
        self.img_label.change_img(img_path, save_path)
        self.tool_widget.show()

    def open_dir(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "选取文件夹", os.getcwd())
        if dir_choose == "":
            return
        dir_path = dir_choose
        self.img_dir = dir_path
        self.label_dir = dir_path + '/label'

        tmp_list = os.listdir(self.img_dir)
        for tmp in tmp_list:
            if tmp[-3:] in IMG_FORMAT:
                self.file_name_list.append(tmp)
        if self.file_name_list is []:
            return
        self.current_img_num = 0
        self.labeling_next_img()

    def labeling_next_img(self):
        if not os.path.isdir(self.label_dir):
            os.mkdir(self.label_dir)

        self.tool_widget.listWidget.clear_current_item_num()
        img_path = self.img_dir + '/' + self.file_name_list[self.current_img_num]
        label_path = self.label_dir + '/' + self.file_name_list[self.current_img_num][:-3] + 'txt'

        print(img_path, label_path)
        self.show_img_in_label(img_path, label_path)

    def next_img(self):
        self.current_img_num += 1
        if self.current_img_num >= len(self.file_name_list):
            return
        self.labeling_next_img()

    def closeEvent(self, e):
        super().closeEvent(e)
        QCoreApplication.instance().quit()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()

    tool = ToolWidget()
    ex.set_tool_widget(tool)
    ex.actionDigitize_Tools.triggered.connect(tool.show)
    tool.listWidget.itemClicked.connect(ex.img_label.on_list_clicked)
    tool.listWidget.noItemInList.connect(ex.img_label.no_item)
    tool.pushButton_2.clicked.connect(ex.next_img)
    sys.exit(app.exec_())


