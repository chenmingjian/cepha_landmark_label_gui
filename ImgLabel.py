import numpy

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QPoint, pyqtSignal
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QPen, QGuiApplication, QPixmap, QImage
from PyQt5.QtWidgets import QLabel, QDesktopWidget, QSizePolicy
import cv2
import numpy as np

def cv_resize_img(img_path):
    cv_img = cv2.imread(img_path)
    height, width, channel = cv_img.shape
    cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB, cv_img)
    cp = QDesktopWidget().availableGeometry()
    scale = height / cp.bottom()
    cv_img = cv2.resize(cv_img, (int(height / scale), int(width / scale)))
    return cv_img, scale


def cv2qt(cv_img):
    height, width, channel = cv_img.shape
    byte_per_line = channel * width
    q_img = QImage(cv_img.data, width, height, byte_per_line, QImage.Format_RGB888)
    q_pixmap = QPixmap.fromImage(q_img)
    return q_pixmap


def qt2cv(q_pixmap):

    q_img = q_pixmap.toImage()
    q_img = q_img.convertToFormat(4)

    width = q_img.width()
    height = q_img.height()

    ptr = q_img.bits()
    ptr.setsize(q_img.byteCount())
    cv_img = np.array(ptr).reshape(height, width, 4)
    cv_img = cv_img[:, :, 0:3]
    return cv_img


class ImgLabel(QLabel):
    x = 0
    y = 0
    points_list = []
    cv_img_list = []
    scale = 0
    i = 0

    def __init__(self, img_path):
        super().__init__()
        self.setupUI()
        cv_img, self.scale = cv_resize_img(img_path)
        self.cv_img_list.append(cv_img)
        q_pixmap = cv2qt(self.cv_img_list[0])
        self.setPixmap(q_pixmap)

    def setupUI(self):
        self.setCursor(QtCore.Qt.CrossCursor)
        self.setEnabled(True)
        self.setAlignment(Qt.AlignCenter)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setObjectName("img_label")
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        print(self.x, self.y)
        cv_img_new = qt2cv(self.pixmap())
        cv2.circle(cv_img_new, (200, 200), 1, (0, 0, 255))
        self.cv_img_list.append(cv_img_new)
        self.update()

    mouseMoved = pyqtSignal(QPixmap, name='mouseMoved')

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        w = 50
        last = len(self.cv_img_list) - 1
        cv_now = self.cv_img_list[last]
        cv_img_part = numpy.array(cv_now[y-w:y+w, x-w:x+w])
        if cv_img_part.shape != (w*2, w*2, 3):
            return
        cv_img_part = cv2.resize(cv_img_part, (w*4, w*4))
        cv2.line(cv_img_part, (0, 2*w), (4*w, 2*w), (255, 255, 255), 1)
        cv2.line(cv_img_part, (2*w, 0), (2*w, 4*w), (255, 255, 255), 1)
        cv_enlarged_img_part = cv2qt(cv_img_part)
        self.mouseMoved.emit(cv_enlarged_img_part)

    def paintEvent(self, event):
        super().paintEvent(event)
        point = QPoint(self.x, self.y)
        self.points_list.append(point)
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 4, Qt.SolidLine))
        for p in self.points_list:
            painter.drawPoint(p)


