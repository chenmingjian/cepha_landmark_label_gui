# coding=utf-8

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QSizePolicy
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
import cv2
import sys
from ImgLabel import ImgLabel

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(675, 300)
        self.setWindowTitle('关注微信公众号：学点编程吧--opencv、PyQt5的小小融合')

        self.lb = ImgLabel(self)
        self.lb.setGeometry(QRect(140, 30, 511, 241))

        img = cv2.imread('1-3.jpg')
        height, width, bytesPerComponent = img.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
        QImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(QImg)

        self.lb.setPixmap(pixmap)
        self.lb.setCursor(Qt.CrossCursor)
        self.lb.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())