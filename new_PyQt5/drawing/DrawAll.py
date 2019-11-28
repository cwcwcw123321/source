'''
绘制各种图形
弧，圆形，椭圆，矩形（正方形），多边形，绘制图像
'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DrawAll(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300,600)
        self.setWindowTitle('绘制各种图形')
    def paintEvent(self, Event):
        qp=QPainter()
        qp.begin(self)
        qp.setPen(Qt.blue)
        # 绘制弧
        rect=QRect(0,10,100,100) #确定一个区域
        #alen：1个alen等于1/16度
        qp.drawArc(rect,0,50*16)#起始角度 0   50*16 相当于50度
        #通过弧来绘制圆
        qp.setPen(Qt.red)
        qp.drawArc(130,10,100,100,0,360*16)
        #绘制带弦弧
        qp.drawChord(10,120,100,100,12,130*16)
        #绘制一个扇形
        qp.setPen(Qt.yellow)
        qp.drawPie(120,120,100,100,12,130*16)
        #绘制一个椭圆
        qp.drawEllipse(10,200,150,100)#宽150 高100
        #绘制五边形
        qp.setPen(Qt.blue)
        point1=QPoint(140,380)
        point2 = QPoint(270, 420)
        point3 = QPoint(290, 512)
        point4 = QPoint(290, 588)
        point5 = QPoint(200, 533)
        polygon=QPolygon([point1,point2,point3,point4,point5])
        qp.drawPolygon(polygon)
        # 绘制图像
        image=QImage('./images/book.png')
        rect=QRect(10,400,image.width()/3,image.height()/3)
        qp.drawImage(rect,image)

        qp.end()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=DrawAll()
    w.show()
    sys.exit(app.exec_())
