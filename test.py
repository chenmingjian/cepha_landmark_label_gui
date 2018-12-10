# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setIconSize(QtCore.QSize(0, 0))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setBaseSize(QtCore.QSize(1500, 1000))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.img_label = QtWidgets.QLabel(self.centralwidget)
        self.img_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_label.sizePolicy().hasHeightForWidth())
        self.img_label.setSizePolicy(sizePolicy)
        self.img_label.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.img_label.setText("")
        self.img_label.setObjectName("img_label")
        self.horizontalLayout_2.addWidget(self.img_label)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1150, 23))
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuDigitize = QtWidgets.QMenu(self.menubar)
        self.menuDigitize.setObjectName("menuDigitize")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setCheckable(False)
        self.actionOpen.setChecked(False)
        self.actionOpen.setEnabled(True)
        self.actionOpen.setObjectName("actionOpen")
        self.actionDigitize_Tools = QtWidgets.QAction(MainWindow)
        self.actionDigitize_Tools.setObjectName("actionDigitize_Tools")
        self.actionOpen_Dir = QtWidgets.QAction(MainWindow)
        self.actionOpen_Dir.setObjectName("actionOpen_Dir")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpen_Dir)
        self.menuFile.addSeparator()
        self.menuDigitize.addAction(self.actionDigitize_Tools)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDigitize.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Landmark Label Tool"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuDigitize.setTitle(_translate("MainWindow", "Digitize"))
        self.actionOpen.setText(_translate("MainWindow", "Open Image"))
        self.actionDigitize_Tools.setText(_translate("MainWindow", "Digitize Tools"))
        self.actionOpen_Dir.setText(_translate("MainWindow", "Open Dir"))

