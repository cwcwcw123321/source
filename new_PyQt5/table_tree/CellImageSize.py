'''
改变单元格中图片的尺寸
setIconSize(QSize(width,height))
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class CellImageSize(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('改变单元格中图片的尺寸')
        self.resize(600,600)

        layout=QHBoxLayout()

        tablewidget=QTableWidget()
        tablewidget.setIconSize(QSize(240,160))
        tablewidget.setColumnCount(3)
        tablewidget.setRowCount(5)

        tablewidget.setHorizontalHeaderLabels(['图片1','图片2','图片3'])
        #让列的宽度和图片的宽度一样
        for i in range(3):
            tablewidget.setColumnWidth(i,200)

        #让行的高度和图片高度相同
        for i in range(5):
            tablewidget.setRowHeight(i,160)

        for k in range(15):
            i=k/3  #行
            j=k%3  #列
            item=QTableWidgetItem()
            item.setIcon(QIcon('./images/bao{}.png'.format(k)))
            tablewidget.setItem(i,j,item)  #行 列 要放得东西

        layout.addWidget(tablewidget)

        self.setLayout(layout)






if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=CellImageSize()
    w.show()
    sys.exit(app.exec_())