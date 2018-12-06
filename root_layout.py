# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'root_layout.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ROOT(object):
    def setupUi(self, ROOT):
        ROOT.setObjectName("ROOT")
        ROOT.setWindowModality(QtCore.Qt.WindowModal)
        ROOT.resize(1000, 600)
        ROOT.setMouseTracking(True)

        self.retranslateUi(ROOT)
        QtCore.QMetaObject.connectSlotsByName(ROOT)

    def retranslateUi(self, ROOT):
        _translate = QtCore.QCoreApplication.translate
        ROOT.setWindowTitle(_translate("ROOT", "Landmark Label Tool"))
        ROOT.setToolTip(_translate("ROOT", "<html><head/><body><p><br/></p></body></html>"))

