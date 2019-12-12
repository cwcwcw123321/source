'''
设置单元格尺寸

'''
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QColor,QBrush,QFont

class CellSize(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('设置单元格尺寸')
        self.resize(430,230)

        layout=QHBoxLayout()
        tableWidget=QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重(kg)'])
        tableWidget.setRowHeight(0,80)
        tableWidget.setColumnWidth(0,150)
        tableWidget.setColumnWidth(2,160)
        newItem=QTableWidgetItem('雷神')
        newItem.setFont(QFont('Times',40,QFont.Black))
        newItem.setForeground(QBrush(QColor(255,0,0)))
        tableWidget.setItem(0,0,newItem)

        newItem=QTableWidgetItem('女')
        newItem.setForeground(QBrush(QColor(255,255,0)))
        newItem.setBackground(QBrush(QColor(0,0,255)))
        tableWidget.setItem(0,1,newItem)

        newItem = QTableWidgetItem('160')
        newItem.setFont(QFont('Times',60,QFont.Black))
        newItem.setBackground(QBrush(QColor(0, 0, 255)))
        tableWidget.setItem(0, 2, newItem)

        self.setLayout(layout)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=CellSize()
    w.show()
    sys.exit(app.exec_())
