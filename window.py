# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\\Users\\95863\\Desktop\\window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 723)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.xianshi = QtWidgets.QFrame(self.centralwidget)
        self.xianshi.setStyleSheet("#xianshi{\n"
"    background-color:white\n"
"}")
        self.xianshi.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.xianshi.setFrameShadow(QtWidgets.QFrame.Raised)
        self.xianshi.setLineWidth(1)
        self.xianshi.setObjectName("xianshi")
        self.headline = QtWidgets.QLabel(self.xianshi)
        self.headline.setGeometry(QtCore.QRect(360, 20, 231, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.headline.setFont(font)
        self.headline.setObjectName("headline")
        self.caidan = QtWidgets.QFrame(self.xianshi)
        self.caidan.setGeometry(QtCore.QRect(10, 100, 321, 561))
        self.caidan.setStyleSheet("#caidan{\n"
"    background-color:rgbrgb(216, 216, 216)\n"
"}")
        self.caidan.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.caidan.setFrameShadow(QtWidgets.QFrame.Raised)
        self.caidan.setObjectName("caidan")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.caidan)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame3 = QtWidgets.QFrame(self.caidan)
        self.frame3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3.setObjectName("frame3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.photobutton = QtWidgets.QPushButton(self.frame3)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.photobutton.setFont(font)
        self.photobutton.setObjectName("photobutton")
        self.verticalLayout_2.addWidget(self.photobutton)
        self.photoinput = QtWidgets.QLineEdit(self.frame3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.photoinput.setFont(font)
        self.photoinput.setObjectName("photoinput")
        self.verticalLayout_2.addWidget(self.photoinput)
        self.verticalLayout.addWidget(self.frame3)
        self.frame2 = QtWidgets.QFrame(self.caidan)
        self.frame2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.videobutton = QtWidgets.QPushButton(self.frame2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.videobutton.setFont(font)
        self.videobutton.setObjectName("videobutton")
        self.verticalLayout_3.addWidget(self.videobutton)
        self.videoinput = QtWidgets.QLineEdit(self.frame2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.videoinput.setFont(font)
        self.videoinput.setObjectName("videoinput")
        self.verticalLayout_3.addWidget(self.videoinput)
        self.verticalLayout.addWidget(self.frame2)
        self.frame1 = QtWidgets.QFrame(self.caidan)
        self.frame1.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.camerabutton = QtWidgets.QPushButton(self.frame1)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.camerabutton.setFont(font)
        self.camerabutton.setObjectName("camerabutton")
        self.verticalLayout_4.addWidget(self.camerabutton)
        self.camerainput = QtWidgets.QLineEdit(self.frame1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.camerainput.setFont(font)
        self.camerainput.setObjectName("camerainput")
        self.verticalLayout_4.addWidget(self.camerainput)
        self.verticalLayout.addWidget(self.frame1)
        self.outputheadline = QtWidgets.QLabel(self.xianshi)
        self.outputheadline.setGeometry(QtCore.QRect(380, 340, 211, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        self.outputheadline.setFont(font)
        self.outputheadline.setObjectName("outputheadline")
        self.output = QtWidgets.QTextEdit(self.xianshi)
        self.output.setGeometry(QtCore.QRect(560, 360, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.output.setFont(font)
        self.output.setStyleSheet("#output{\n"
"    background-color:rgb(235, 235, 235)\n"
"}")
        self.output.setObjectName("output")
        self.gridLayout.addWidget(self.xianshi, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 981, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.headline.setText(_translate("MainWindow", "手势识别系统"))
        self.photobutton.setText(_translate("MainWindow", "点击选择图片识别"))
        self.videobutton.setText(_translate("MainWindow", "点击选择视频识别"))
        self.camerabutton.setText(_translate("MainWindow", "点击打开摄像头识别"))
        self.camerainput.setText(_translate("MainWindow", "摄像头关闭"))
        self.outputheadline.setText(_translate("MainWindow", "识别结果："))