# QT5 클래스 생성 윈도우 클래스
import sys 
from PyQt5.QtWidgets import *

# 윈도우 클래스 선언 (QMainWindow를 상속 받음)
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()



app = QApplication(sys.argv)
# button = QPushButton("Click me")
# button.show()
# label = QLabel("Hello QT5!!")
# label.show()
win = MyWindow()
win.show()

app.exec_()