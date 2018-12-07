from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class Win(QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.setObjectName("self")
        self.resize(400, 300)
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(280, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.pushButton.setText(_translate("self", "PushButton"))

    def add(self):
        self.listWidget.addItem('123')
        index=self.listWidget.currentRow()+1
        if index:
            self.listWidget.item(index-1).setBackground(QColor('green'))        
            self.listWidget.item(index).setBackground(QColor('red'))
        else:
            self.listWidget.item(index).setBackground(QColor('blue'))
        self.listWidget.setCurrentRow(self.listWidget.currentRow()+1)

app=QApplication(sys.argv)
win=Win()
win.show()
sys.exit(app.exec_())