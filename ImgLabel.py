import numpy

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QPoint, pyqtSignal
from PyQt5.QtGui import QPainter, QPen, QPixmap, QImage
from PyQt5.QtWidgets import QLabel, QDesktopWidget, QSizePolicy
import cv2
import numpy as np


def cv_resize_img(img_path):
    cv_img = cv2.imread(img_path)
    height, width, channel = cv_img.shape
    cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB, cv_img)
    cp = QDesktopWidget().availableGeometry()
    scale = height / cp.bottom()*1.1
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
    points_list = []
    cv_img = None
    cv_img_red_dot = None
    scale = 0
    i = 0
    modify = False
    modify_index = -1
    noRedDot = False

    def __init__(self, img_path):
        super().__init__()
        self.setupUI()
        if img_path is None:
            return
        cv_img, self.scale = cv_resize_img(img_path)
        self.cv_img = np.array(cv_img)
        self.cv_img_red_dot = np.array(cv_img)
        q_pixmap = cv2qt(cv_img)
        self.setPixmap(q_pixmap)

    def change_img(self, img_path):
        self.points_list = []
        self.cv_img = None
        self.cv_img_red_dot = None
        self.scale = 0
        self.i = 0
        self.modify = False
        self.modify_index = -1
        self.noRedDot = False
        cv_img, self.scale = cv_resize_img(img_path)
        self.cv_img = np.array(cv_img)
        self.cv_img_red_dot = np.array(cv_img)
        q_pixmap = cv2qt(cv_img)
        self.setPixmap(q_pixmap)


    def setupUI(self):
        self.setCursor(QtCore.Qt.CrossCursor)
        self.setEnabled(True)
        self.setAlignment(Qt.AlignCenter)
        # size_policy = QSizePolicy()
        # size_policy.setHorizontalStretch(0)
        # size_policy.setVerticalStretch(0)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setObjectName("img_label")
        self.setMouseTracking(True)

    mouseClicked = pyqtSignal(name='mouseClicked')

    def mousePressEvent(self, event):
        if self.noRedDot is False:
            x = event.x()
            y = event.y()
            point = QPoint(x, y)
            if self.modify:
                self.points_list[self.modify_index] = point
                self.modify = False
                self.modify_index = -1
            else:
                self.points_list.append(point)
            self.cv_img_red_dot = np.array(self.cv_img)
            for point in self.points_list:
                cv2.rectangle(self.cv_img_red_dot, (point.x()-2, point.y()-2), (point.x()+2, point.y()+2), (255, 0, 0), -1)
                print((point.x(), point.y()))
            self.update()
            self.mouseMoveEvent(event)
            self.save_points_txt()
            self.mouseClicked.emit()

    mouseMoved = pyqtSignal(QPixmap, name='mouseMoved')

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        w = 50

        cv_now = self.cv_img_red_dot
        cv_img_part = numpy.array(cv_now[y-w:y+w, x-w:x+w])
        if cv_img_part.shape != (w*2, w*2, 3):
            return
        cv_img_part = cv2.resize(cv_img_part, (w*4, w*4))
        cv2.line(cv_img_part, (0, 2*w), (4*w, 2*w), (255, 255, 255), 1)
        cv2.line(cv_img_part, (2*w, 0), (2*w, 4*w), (255, 255, 255), 1)
        cv_enlarged_img_part = cv2qt(cv_img_part)
        self.mouseMoved.emit(cv_enlarged_img_part)
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 4, Qt.SolidLine))
        for p in self.points_list:
            painter.drawPoint(p)

    def on_list_clicked(self, i):
        self.noRedDot = False
        if i < len(self.points_list):
            self.modify = True
            self.modify_index = i

    def no_item(self):
        self.noRedDot =True

    def save_points_txt(self, dir='.'):
        with open('test.txt', 'w') as f:
            for i in self.points_list:
                x = int(i.x() * self.scale)
                y = int(i.y() * self.scale)
                f.write(str(x)+', '+str(y)+'\n')


