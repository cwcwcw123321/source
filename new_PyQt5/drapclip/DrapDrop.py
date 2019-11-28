'''
让控件支持拖拽动作
A.setDragEnabled(True)    设置可以拖动
B.setAcceptDrops(True)      设置可以接受拖动

B需要两个事件
1、dragEnterEvent 将A拖到B触发
2、dropEvent     在B的区域放下A时触发
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyComboxBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
    def dragEnterEvent(self,e):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()
    def dropEvent(self, e):
        self.addItem(e.mimeData().text())

class DrapDropDemo(QWidget):
    def __init__(self):
        super().__init__()
        formlayout=QFormLayout()
        formlayout.addRow(QLabel('请将坐标的文件拖拽到右边的下拉列表中'))
        lineEdit=QLineEdit()
        lineEdit.setDragEnabled(True) #让QLineEdit控件可以拖动

        combo=MyComboxBox()
        formlayout.addRow(lineEdit,combo)
        self.setLayout(formlayout)
        self.setWindowTitle('拖拽案例')


if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=DrapDropDemo()
    w.show()
    sys.exit(app.exec_())