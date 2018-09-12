from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import math
import random

class TableGUI(QWidget):
    def __init__(self, gx, gy, ga):
        app = QApplication(sys.argv)

        super().__init__()

        self._x = 0.5
        self._y = 0.5
        self._angle = 0.0 # radians

        self._gx = gx
        self._gy = gy
        self._ga = ga
        self._app = app

        self.initUI()

    def initUI(self):
        self.setFixedSize(800, 800)
        self.setWindowTitle('Table Environment')
        self.show()

    def display(self, x, y, angle):
        self._x = x
        self._y = y
        self._angle = angle

        self.repaint()
        self._app.processEvents()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)

        self.drawElement(qp, self._x, self._y, self._angle, Qt.black)
        self.drawElement(qp, self._gx, self._gy, self._ga, Qt.blue)

        qp.end()

    def drawElement(self, qp, x, y, angle, color):
        # Draw circle around the agent
        center = QPointF(x * self.width(), y * self.height())

        qp.setPen(color)
        qp.drawEllipse(center, 20, 20)

        # Draw the center of the agent as a big dot
        qp.setBrush(color)
        qp.drawEllipse(center, 2, 2)
        qp.setBrush(Qt.transparent)

        # Draw a line giving the orientation
        dx = 20.0 * math.cos(angle)
        dy = 20.0 * math.sin(angle)

        qp.drawLine(center, center + QPointF(dx, dy))

