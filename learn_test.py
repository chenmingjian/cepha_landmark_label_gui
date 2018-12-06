import sys
from PyQt5 import QtWidgets, QtGui


# 定义窗口函数window
def window():
    # 我事实上不太明白干嘛要这一句话，只是pyqt窗口的建立都必须调用QApplication方法
    app = QtWidgets.QApplication(sys.argv)
    # 新建一个窗口，名字叫做w
    w = QtWidgets.QWidget()
    # 定义w的大小
    w.setGeometry(100, 100, 300, 200)
    # 给w一个Title
    w.setWindowTitle('lesson 2')
    # 在窗口w中，新建一个lable，名字叫做l1
    l1 = QtWidgets.QLabel(w)
    # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
    png = QtGui.QPixmap(R'D:\labwork\点集注册\red_dot\2_350\1-100\1-2.jpg')
    # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
    l1.setPixmap(png)



    # 调整l1和l2的位置
    l1.move(100, 20)

    # 显示整个窗口
    w.show()
    # 退出整个app
    app.exit(app.exec_())


# 调用window这个函数
window()
