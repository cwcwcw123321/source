import sys
from PyQt5.QtWidgets import *


def onClick_Button():
    print('1')
    print('widget.x()={}'.format(w.x()))
    print('widget.y()={}'.format(w.y()))
    print('widget.width()={}'.format(w.width()))
    print('widget.height()={}'.format(w.height()))

    print('2')
    print('widget.geometry().x()={}'.format(w.geometry().x()))
    print('widget.geometry().y()={}'.format(w.geometry().y()))
    print('widget.geometry().width()={}'.format(w.geometry().width()))
    print('widget.geometry().height()={}'.format(w.geometry().height()))

    print('3')
    print('widget.framegeometry().x()={}'.format(w.frameGeometry().x()))
    print('widget.framegeometry().y()={}'.format(w.frameGeometry().y()))
    print('widget.framegeometry().width()={}'.format(w.frameGeometry().width()))
    print('widget.framegeometry().height()={}'.format(w.frameGeometry().height()))


app = QApplication(sys.argv)
w = QWidget()
btn = QPushButton(w)
btn.setText('点击我')
btn.move(120, 120)
btn.clicked.connect(onClick_Button)

w.resize(400, 400)
w.move(400, 200)
w.setWindowTitle('屏幕坐标系')

w.show()
sys.exit(app.exec_())
