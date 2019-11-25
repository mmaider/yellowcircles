import random

from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
import sys

from PyQt5.QtGui import QPaintEvent, QPainter, QColor, QKeyEvent
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.pushButton.clicked.connect(self.drawc)
        self.show()

    def drawc(self):
        self.x = random.randint(0, 300)
        self.y = random.randint(0, 300)
        self.radius = random.randint(1, 100)
        self.flag = True
        self.repaint()

    def paintEvent(self, QPaintEvent):
        if self.flag:
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(QColor(255, 255, 0))
            painter.drawEllipse(self.x, self.y, self.radius, self.radius)
            painter.end()
        self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
