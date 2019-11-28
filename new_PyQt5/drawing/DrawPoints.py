'''
用像素点绘制正弦曲线
-2PI 2PI
drawPoint(x,y) 绘制一个像素点
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
        self.setWindowTitle('在窗口用像素点绘制2个周期的正弦曲线')
    def paintEvent(self, QPaintEvent):
        paint=QPainter()
        paint.begin(self)
        paint.setPen(Qt.blue)
        #获得窗口尺寸
        size=self.size()

        for i in range(1000):
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width() / 2.0) * math.pi / 50 )+ size.height() / 2.0
            paint.drawPoint(x,y)

        paint.end()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=DrawPoint()
    w.show()
    sys.exit(app.exec_())
