# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette,QPixmap,QColor    #导入QtGui模块


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")  # 设置窗体对象名称
        MainWindow.resize(960, 786)    # 设置窗体大小
        MainWindow.setMinimumSize(QtCore.QSize(960, 786))  # 主窗体最小值
        MainWindow.setMaximumSize(QtCore.QSize(960, 786))  # 主窗体最大值
        self.centralwidget = QtWidgets.QWidget(MainWindow)   # 主窗体的Widget控件
        self.centralwidget.setObjectName("centralwidget")  # 设置对象名称
        # 通过label控件显示顶部图片
        self.label_title_img = QtWidgets.QLabel(self.centralwidget)
        self.label_title_img.setGeometry(QtCore.QRect(0, 0, 960, 91))
        self.label_title_img.setText("")
        self.label_title_img.setObjectName("label_title_img")
        title_img=QPixmap('..\\img\\bg.png')    # 打开顶部位图
        self.label_title_img.setPixmap(title_img)    # 设置调色板
        self.labe_train_img = QtWidgets.QLabel(self.centralwidget)
        self.labe_train_img.setGeometry(QtCore.QRect(0, 90, 960, 161))
        self.labe_train_img.setText("")
        self.labe_train_img.setObjectName("labe_train_img")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(0, 250, 960, 450))
        self.tableView.setObjectName("tableView")
        # 查询部分的widget
        self.widget_query = QtWidgets.QWidget(self.centralwidget)
        self.widget_query.setGeometry(QtCore.QRect(0, 90, 960, 80))
        self.widget_query.setObjectName("widget_query")
        # 开启自动填充背景
        self.widget_query.setAutoFillBackground(True)
        palette=QPalette()    # 调色板类
        # 设置背景图片
        palette.setBrush(QPalette.Background,QtGui.QBrush(QtGui.QPixmap('..\\img\\bg1.png')))
        self.widget_query.setPalette(palette)   # 为控件设置对应的调色板即可
        self.label = QtWidgets.QLabel(self.widget_query)
        self.label.setGeometry(QtCore.QRect(30, 30, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_query)
        self.label_2.setGeometry(QtCore.QRect(230, 30, 54, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_query)
        self.label_3.setGeometry(QtCore.QRect(440, 30, 54, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.widget_query)
        self.pushButton.setGeometry(QtCore.QRect(640, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.widget_query)
        self.textEdit.setGeometry(QtCore.QRect(80, 30, 101, 21))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget_query)
        self.textEdit_2.setGeometry(QtCore.QRect(290, 30, 101, 21))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.widget_query)
        self.textEdit_3.setGeometry(QtCore.QRect(490, 30, 101, 21))
        self.textEdit_3.setObjectName("textEdit_3")
        self.widget_checkBox = QtWidgets.QWidget(self.centralwidget)
        self.widget_checkBox.setGeometry(QtCore.QRect(0, 170, 960, 80))
        self.widget_checkBox.setObjectName("widget_checkBox")
        self.label_4 = QtWidgets.QLabel(self.widget_checkBox)
        self.label_4.setGeometry(QtCore.QRect(30, 27, 54, 20))
        self.label_4.setObjectName("label_4")
        self.checkBox_G = QtWidgets.QCheckBox(self.widget_checkBox)
        self.checkBox_G.setGeometry(QtCore.QRect(100, 30, 71, 16))
        self.checkBox_G.setObjectName("checkBox_G")
        self.checkBox_D = QtWidgets.QCheckBox(self.widget_checkBox)
        self.checkBox_D.setGeometry(QtCore.QRect(240, 30, 71, 16))
        self.checkBox_D.setObjectName("checkBox_D")
        self.checkBox_Z = QtWidgets.QCheckBox(self.widget_checkBox)
        self.checkBox_Z.setGeometry(QtCore.QRect(370, 30, 71, 16))
        self.checkBox_Z.setObjectName("checkBox_Z")
        self.checkBox_T = QtWidgets.QCheckBox(self.widget_checkBox)
        self.checkBox_T.setGeometry(QtCore.QRect(500, 30, 71, 16))
        self.checkBox_T.setObjectName("checkBox_T")
        self.checkBox_K = QtWidgets.QCheckBox(self.widget_checkBox)
        self.checkBox_K.setGeometry(QtCore.QRect(650, 30, 71, 16))
        self.checkBox_K.setObjectName("checkBox_K")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "车票查询"))
        self.label.setText(_translate("MainWindow", "出发地"))
        self.label_2.setText(_translate("MainWindow", "目的地"))
        self.label_3.setText(_translate("MainWindow", "出发日"))
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.label_4.setText(_translate("MainWindow", "车次类型"))
        self.checkBox_G.setText(_translate("MainWindow", "GC-高铁"))
        self.checkBox_D.setText(_translate("MainWindow", "D-动车"))
        self.checkBox_Z.setText(_translate("MainWindow", "Z-直达"))
        self.checkBox_T.setText(_translate("MainWindow", "T-特快"))
        self.checkBox_K.setText(_translate("MainWindow", "K-快速"))


def show_MainWindow():
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    show_MainWindow()