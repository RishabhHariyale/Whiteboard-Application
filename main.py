import sys
from win import Ui_MainWindow
from PyQt5 import QtWidgets , QtCore
from PyQt5.QtGui import *
from PyQt5 import QtCore

class WhiteBoard(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.image = QImage(self.size() , QImage.Format_ARGB32)
        self.image.fill(QtCore.Qt.white)
        self.ui.pushButton_clear.pressed.connect(lambda: self.clearScreen())
        self.lastPenColor = QtCore.Qt.black
        self.ui.pushButton_pen.pressed.connect(lambda: self.switchPenAndEraser("pen"))
        self.ui.pushButton_eraser.pressed.connect(lambda: self.switchPenAndEraser("eraser"))
        self.ui.pushButton_insize.pressed.connect(lambda : self.changeSize(1))
        self.ui.pushButton_decsize.pressed.connect(lambda : self.changeSize(0))
        self.ui.pushButton_chngcolor.pressed.connect(lambda: self.selectColor())
        self.ui.pushButton_save.pressed.connect(lambda: self.save())
        self.ui.pushButton_chngcolor.setToolTip("Change the color")
        self.ui.pushButton_clear.setToolTip("Clear the screen")
        self.ui.pushButton_eraser.setToolTip("Erase the Window")
        self.ui.pushButton_pen.setToolTip("Select the pen")
        self.drawing  = False 
        self.brushsize = None
        self.brushcolor = self.lastPenColor
        self.isPenSelected = True
        self.penSize = 2
        self.eraserSize = 2
        self.buttonColor = None
        self.lastpoint  =  QtCore.QPoint()
        self.show()

    def save(self):
        filePath , _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Image" ,"","PNG(*.png);; JPEG(*.jpeg);;All Files(*.*)")
        if filePath=="":
            return
        self.image.save(filePath)


    def selectColor(self):
        dialog = QtWidgets.QColorDialog(self)
        self.lastPenColor = dialog.getColor()
        self.buttonColor = self.lastPenColor.getRgb()[0:3]
        self.ui.pushButton_chngcolor.setStyleSheet(f"background-color : rgb({self.buttonColor[0]},{self.buttonColor[1]},{self.buttonColor[2]}); \n color rgb(0,0,0)")

    def changeSize(self, option):
        if self.isPenSelected == True:
            if option == 1:
                self.penSize += 2
            else:
                self.penSize -= 2
        else:
            if option == 1:
                self.eraserSize += 2
            else:
                self.eraserSize -= 2
                

    def switchPenAndEraser(self,option):
        if option == "pen":
            self.brushcolor = self.lastPenColor
        else:
            self.brushcolor =  QtCore.Qt.white
           

    def clearScreen(self):
        self.image.fill(QtCore.Qt.white)
        self.update()
        
    def mousePressEvent(self,event):
        #if left mouse button is pressed
        if event.button() == QtCore.Qt.LeftButton:
            #make drawing flag true
            self.drawing = True
            #make last point to the point of cursor
            self.lastpoint = event.pos()
             
    # method for tracking mouse activity 
    def mouseMoveEvent(self, event):
        if (event.buttons() & QtCore.Qt.LeftButton) & self.drawing :
             
            # creating painter object
            painter = QPainter(self.image) 
            if self.isPenSelected == True:
                self.brushsize = self.penSize
                self.isPenSelected = True
            else:
                self.brushsize = self.eraserSize
                self.isPenSelected = False
            #set the pen of the painter
            painter.setPen(QPen(self.brushcolor,self.brushsize,QtCore.Qt.SolidLine,QtCore.Qt.RoundCap , QtCore.Qt.RoundJoin))
            painter.drawLine(self.lastpoint,event.pos())

            #change the lastpoint 
            self.lastpoint = event.pos()
            self.update()
    
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            # make drawing flag false
            self.drawing = False
 
    # paint event
    def paintEvent(self, event):
        # create a canvas
        canvasPainter = QPainter(self)
        # drawing the rectangle on the screen
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())
 


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    whiteBoard = WhiteBoard()
    sys.exit(app.exec_())