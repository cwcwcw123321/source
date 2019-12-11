'''
设置单元格字体和颜色

'''
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QColor,QBrush,QFont

class CellFontAndColor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('设置单元格字体和颜色')
        self.resize(430,230)

        layout=QHBoxLayout()
        tableWidget=QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重(kg)'])

        newItem1=QTableWidgetItem('雷神')
        newItem1.setFont(QFont('Times',14,QFont.Black))
        newItem1.setForeground(QBrush(QColor(255,0,0)))
        tableWidget.setItem(0,0,newItem1)

        newItem2=QTableWidgetItem('女')
        newItem2.setForeground(QBrush(QColor(255,255,0)))
        newItem2.setBackground(QBrush(QColor(0,0,255)))
        tableWidget.setItem(0,1,newItem2)

        newItem2 = QTableWidgetItem('160')
        newItem2.setFont(QFont('Times',20,QFont.Black))
        newItem2.setBackground(QBrush(QColor(0, 0, 255)))
        tableWidget.setItem(0, 2, newItem2)

        self.setLayout(layout)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=CellFontAndColor()
    w.show()
    sys.exit(app.exec_())
