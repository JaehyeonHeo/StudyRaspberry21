# QT5 사용자 윈도우 화면 구성 예제
import sys
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *

# 윈도우 클래스 선언 (QMainWindow를 상속 받음) --> 여기다 모두 작업
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My QT5 Window") # 제목 표시줄(헤더)
        self.setGeometry(150, 150, 600, 400) # x,y, width, height
        self.setWindowIcon(QIcon('./image/chart.png'))

        # label 추가
        self.label = QLabel('메세지 : ', self)
        self.label.move(10, 20) #-->위치지정
        self.label.setFixedWidth(200) # --> 넓이 지정
         #self.label.setGeometry(10, 20, 300, 20) # --> 한번에 다
        # button 추가
        self.btn = QPushButton('Click', self)
        self.btn.move(10, 60)
        # signal 추가 (C#의 이벤트)
        self.btn.clicked.connect(self.btn_clicked)
    # 버튼 클릭signal 
    def btn_clicked(self):
        self.label.clear()
        self.label.setText('메세지 : button Clicked!')
        

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()