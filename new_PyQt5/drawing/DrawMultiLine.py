'''
绘制不同
'''

import math
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class DrawPoint(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300,300)
        self.setWindowTitle('设置pen的样式')
    def paintEvent(self, QPaintEvent):
        paint=QPainter()
        paint.begin(self)

        pen=QPen(Qt.red,3,Qt.SolidLine)# 红色 粗细为3 默认实线
        paint.setPen(pen)
        paint.drawLine(20,40,250,40)

        pen.setStyle(Qt.DashLine)       #虚线
        paint.setPen(pen)
        paint.drawLine(20,80,250,80)

        pen.setStyle(Qt.DashDotDotLine) #点划线
        paint.setPen(pen)
        paint.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)        #
        paint.setPen(pen)
        paint.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)
        paint.setPen(pen)
        paint.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.CustomDashLine)#自定义点划线风格
        pen.setDashPattern([1,10,5,12])
        paint.setPen(pen)
        paint.drawLine(20, 240, 250, 240)


        paint.end()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=DrawPoint()
    w.show()
    sys.exit(app.exec_())