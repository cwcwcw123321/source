import sys

from PyQt5.QtWidgets import *


def onClick_Button():
    print('1')
    print('widget.x()={}'.format(widget.x()))  # 250 （窗口横坐标）
    print('widget.y()={}'.format(widget.y()))  # 200 （窗口纵坐标）
    print('widget.width()={}'.format(widget.width()))  # 300 （工作区宽度）
    print('widget.height()={}'.format(widget.height()))  # 240 （工作区高度）

    print('2')
    print('widget.geometry().x()={}'.format(widget.geometry().x()))  # 251（工作区横坐标）
    print('widget.geometry().y()={}'.format(widget.geometry().y()))  # 245（工作区纵坐标）
    print('widget.geometry().width()={}'.format(widget.geometry().width()))  # 300（工作区宽度）
    print('widget.geometry().height()={}'.format(widget.geometry().height()))  # 240（工作区高度）

    print('3')
    print('widget.frameGeometry().x()={}'.format(widget.frameGeometry().x()))  # 250 （窗口横坐标）
    print('widget.frameGeometry().y()={}'.format(widget.frameGeometry().y()))  # 200 （窗口纵坐标）
    print('widget.frameGeometry().width()={}'.format(widget.frameGeometry().width()))  # 302（窗口宽度）
    print('widget.frameGeometry().height()={}'.format(widget.frameGeometry().height()))  # 286（窗口高度）


app = QApplication(sys.argv)

widget = QWidget()
btn = QPushButton(widget)
btn.setText('按钮')
btn.clicked.connect(onClick_Button)
btn.move(24, 52)

widget.resize(300, 240)  # 设置工作区的尺寸
widget.move(250, 200)
widget.setWindowTitle('屏幕坐标系')
widget.show()

sys.exit(app.exec_())
