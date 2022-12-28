from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(909, 544)
        MainWindow.setAnimated(True)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.backgroundFrame = QtWidgets.QFrame(self.centralwidget)
        self.backgroundFrame.setEnabled(True)
        self.backgroundFrame.setGeometry(QtCore.QRect(-1, -1, 941, 551))
        self.backgroundFrame.setStyleSheet("QLabel {\n"
"font-family: \"Microsoft Sans Serif\", sans-serif;\n"
"color: white;\n"
"}\n"
"\n"
"#backgroundFrame\n"
"{\n"
"background-color: #060321;\n"
"}\n"
"\n"
"#infoBar\n"
"{\n"
"background-color: #0F0334;\n"
"}")
        self.backgroundFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.backgroundFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backgroundFrame.setObjectName("backgroundFrame")
        self.infoBar = QtWidgets.QFrame(self.backgroundFrame)
        self.infoBar.setGeometry(QtCore.QRect(-10, -10, 921, 71))
        self.infoBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.infoBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.infoBar.setObjectName("infoBar")
        self.exitButton = QtWidgets.QPushButton(self.infoBar)
        self.exitButton.setGeometry(QtCore.QRect(874, 26, 31, 31))
        self.exitButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/Exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitButton.setIcon(icon)
        self.exitButton.setIconSize(QtCore.QSize(32, 32))
        self.exitButton.setObjectName("exitButton")
        self.pushButton = QtWidgets.QPushButton(self.infoBar)
        self.pushButton.setGeometry(QtCore.QRect(827, 30, 31, 31))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/Minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.infoBar)
        self.pushButton_2.setGeometry(QtCore.QRect(26, 26, 34, 31))
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Resources/Settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.infoBar)
        self.label.setGeometry(QtCore.QRect(390, 23, 145, 40))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Resources/Titan Window.png"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Titan"))

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())