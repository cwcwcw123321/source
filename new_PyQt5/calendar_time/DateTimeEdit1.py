'''
输入各种风格的日期和时间
QDateTimeEdit
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DateTimeEdit1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        vlayout=QVBoxLayout()

        dateTimeEdit1=QDateTimeEdit()
        dateTimeEdit1.setMinimumDate(QDate.currentDate().addDays(-365))
        dateTimeEdit1.setMaximumDate(QDate.currentDate().addDays(365))

        self.dateTimeEdit=dateTimeEdit1

        dateTimeEdit2=QDateTimeEdit(QDateTime.currentDateTime())
        dateTimeEdit2.setCalendarPopup(True) #把上下剪头变成下拉框

        dateEdit=QDateTimeEdit(QDate.currentDate())
        timeEdit=QDateTimeEdit(QTime.currentTime())

        dateTimeEdit1.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        dateTimeEdit2.setDisplayFormat('yyyy/MM/dd HH-mm-ss')

        dateEdit.setDisplayFormat('yyyy-MM-dd')
        timeEdit.setDisplayFormat('HH:mm:ss')

        dateTimeEdit1.dateChanged.connect(self.onDateChanged)
        dateTimeEdit1.timeChanged.connect(self.onTimeChanged)
        dateTimeEdit1.dateTimeChanged.connect(self.onDateTimeChanged)

        vlayout.addWidget(dateTimeEdit1)
        vlayout.addWidget(dateTimeEdit2)
        vlayout.addWidget(dateEdit)
        vlayout.addWidget(timeEdit)

        btn=QPushButton('获取日期和时间')
        btn.clicked.connect(self.onButtonClick)
        vlayout.addWidget(btn)

        self.setLayout(vlayout)

        self.resize(300,100)
        self.setWindowTitle('设置不同风格的日期和时间')
    # 日期变化
    def onDateChanged(self,date):
        print(date)
    #时间变化
    def onTimeChanged(self,time):
        print(time)
    #日期和时间变化
    def onDateTimeChanged(self,datetime):
        print(datetime)

    def onButtonClick(self):
        dateTime=self.dateTimeEdit.dateTime()
        print(dateTime)

        #最大日期
        print(self.dateTimeEdit.maximumDate())
        #最大日期和时间
        print(self.dateTimeEdit.maximumDateTime())
        #获取最小日期
        print(self.dateTimeEdit.minimumDate())




if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=DateTimeEdit1()
    w.show()
    sys.exit(app.exec_())