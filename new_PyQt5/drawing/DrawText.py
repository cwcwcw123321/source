'''
绘制api：绘制文本
1、文本
2、各种图形（直线，点，椭圆，弧，扇形，多边形）
3.图像

Qpainter
painter=QPainter()
painter.begin()
.....
painter.drawText(...)
......
painter.end()

必须在paintEvent事件方法中绘制各种元素

'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QColor,QFont
from PyQt5.QtCore import Qt

class DrawText(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('在窗口上绘制文本')
        self.resize(300,200)
        self.text='Python从菜鸟到高手'

    def paintEvent(self,event):
        painter=QPainter()
        painter.begin(self)
        print('aaa')
        painter.setPen(QColor(150,43,5))
        painter.setFont(QFont('SimSun',25))
        painter.drawText(event.rect(),Qt.AlignCenter,self.text)#整个窗口的尺寸

        painter.end()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=DrawText()
    w.show()
    sys.exit(app.exec_())
