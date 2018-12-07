from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QPen, QGuiApplication
from PyQt5.QtWidgets import QLabel
import cv2


class ImgLabel(QLabel):
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0

    def mousePressEvent(self, event):
        self.x0 = event.x()
        self.y0 = event.y()
        print(self.x0, self.y0)
        self.update()

    def mouseMoveEvent(self, event):
        self.x1 = event.x()
        self.y1 = event.y()
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        point = QPoint(self.x0, self.y0)
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 4, Qt.SolidLine))
        painter.drawPoint(point)


