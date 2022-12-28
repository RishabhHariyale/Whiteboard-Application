from random import randrange
from PyQt5 import QtCore, QtWidgets, uic

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('overlay.ui', self)

        self.alerts = []

        self.centralWidget().installEventFilter(self)

        self.pushButton.clicked.connect(self.showAlert)
        QtCore.QTimer.singleShot(2000, self.showAlert)

    def showAlert(self, message=None, timeout=250):
        # create an alert that is a child of the central widget
        alert = QtWidgets.QLabel(message or 'Some message to the user', 
            self.centralWidget(), wordWrap=True, 
            alignment=QtCore.Qt.AlignCenter, 
            styleSheet='background: rgb({}, {}, {});'.format(
                randrange(192, 255), randrange(192, 255), randrange(192, 255)))
        self.alerts.append(alert)
        alert.animation = QtCore.QSequentialAnimationGroup(alert)
        alert.animation.addAnimation(QtCore.QPropertyAnimation(
            alert, b'geometry', duration=timeout))
        alert.animation.addAnimation(QtCore.QPauseAnimation(3000))
        alert.animation.addAnimation(QtCore.QPropertyAnimation(
            alert, b'geometry', duration=timeout))

        # delete the alert when the animation finishes
        def deleteLater():
            self.alerts.remove(alert)
            alert.deleteLater()
        alert.animation.finished.connect(deleteLater)

        # update all animations, including the new one; this is not very
        # performant, as it also updates all existing alerts; it is 
        # just done for simplicity;
        self.updateAnimations()
        # set the start geometry of the alert, show it, and start 
        # the new animation
        alert.setGeometry(alert.animation.animationAt(0).startValue())
        alert.show()
        alert.animation.start()

    def updateAnimations(self):
        width = self.centralWidget().width() - 20
        y = self.centralWidget().height()
        margin = self.fontMetrics().height() * 2
        for alert in self.alerts:
            height = alert.heightForWidth(width) + margin
            startRect = QtCore.QRect(10, y, width, height)
            endRect = startRect.translated(0, -height)
            alert.animation.animationAt(0).setStartValue(startRect)
            alert.animation.animationAt(0).setEndValue(endRect)
            alert.animation.animationAt(2).setStartValue(endRect)
            alert.animation.animationAt(2).setEndValue(startRect)

    def eventFilter(self, obj, event):
        if obj == self.centralWidget() and event.type() == event.Resize and self.alerts:
            self.updateAnimations()
            for alert in self.alerts:
                ani = alert.animation
                # if the animation is "paused", update the geometry
                if isinstance(ani.currentAnimation(), QtCore.QPauseAnimation):
                    alert.setGeometry(ani.animationAt(0).endValue())
        return super().eventFilter(obj, event)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec())