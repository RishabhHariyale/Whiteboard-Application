from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1031, 698)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_drawarea = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_drawarea.sizePolicy().hasHeightForWidth())
        self.frame_drawarea.setSizePolicy(sizePolicy)
        self.frame_drawarea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_drawarea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_drawarea.setObjectName("frame_drawarea")
        self.verticalLayout.addWidget(self.frame_drawarea)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_pen = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.pushButton_pen.setFont(font)
        self.pushButton_pen.setObjectName("pushButton_pen")
        self.horizontalLayout.addWidget(self.pushButton_pen)
        self.pushButton_eraser = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_eraser.setFont(font)
        self.pushButton_eraser.setObjectName("pushButton_eraser")
        self.horizontalLayout.addWidget(self.pushButton_eraser, 0, QtCore.Qt.AlignBottom)
        self.pushButton_chngcolor = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.pushButton_chngcolor.setFont(font)
        self.pushButton_chngcolor.setObjectName("pushButton_chngcolor")
        self.horizontalLayout.addWidget(self.pushButton_chngcolor)
        self.pushButton_save = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save, 0, QtCore.Qt.AlignBottom)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton_insize = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.pushButton_insize.setFont(font)
        self.pushButton_insize.setObjectName("pushButton_insize")
        self.horizontalLayout.addWidget(self.pushButton_insize)
        self.pushButton_decsize = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.pushButton_decsize.setFont(font)
        self.pushButton_decsize.setObjectName("pushButton_decsize")
        self.horizontalLayout.addWidget(self.pushButton_decsize)
        self.pushButton_clear = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WhiteBoardApp"))
        self.pushButton_pen.setText(_translate("MainWindow", "🖊"))
        self.pushButton_eraser.setText(_translate("MainWindow", "Eraser"))
        self.pushButton_chngcolor.setText(_translate("MainWindow", "Change Color"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.label.setText(_translate("MainWindow", "Pen Size"))
        self.pushButton_insize.setText(_translate("MainWindow", "➕"))
        self.pushButton_decsize.setText(_translate("MainWindow", "➖"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())