'''
日历控件
QCalendarWidget
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyCalendar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.cal=QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1988,1,1))
        self.cal.setMaximumDate(QDate(2088,1,1))

        self.cal.setGridVisible(True)#以网格显示日期
        self.cal.move(20,20)

        self.setWindowTitle('日历演示')
        self.resize(300,270)

        self.cal.clicked.connect(self.showDate)
        self.label=QLabel(self)
        self.label.move(20,250)
        date=self.cal.selectedDate()
        self.label.setText(date.toString('yyyy-MM-dd dddd'))


    def showDate(self,date):
        #self.label.setText(date.toString('yyyy-MM-dd dddd'))
        self.label.setText(self.cal.selectedDate().toString('yyyy-MM-dd dddd'))
if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=MyCalendar()
    w.show()
    sys.exit(app.exec_())