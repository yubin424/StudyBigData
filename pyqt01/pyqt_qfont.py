import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None:  # -> None 의미: return 값이 없다
        super().__init__()
        self.initUI()

    # 화면 정의를 위해 만든 사용자 함수
    def initUI(self) -> None:
        self.setGeometry(300, 100, 640, 400)  # x축, y축, 폼의 가로, 세로
        self.setWindowTitle('QTemplate !')
        self.text = 'What a day!!'
        self.show()

    def paintEvent(self, event) -> None:
        paint = QPainter()
        paint.begin(self)
        # 그리는 함수 추가
        self.drawText(event, paint)
        paint.end()

    # 텍스트 그리기 위한 함수
    def drawText(self, event, paint):
        paint.setPen(QColor(50,50,50))
        paint.setFont(QFont('NanumGothic',20))
        paint.drawText(105, 100, 'GOOD DAY')
        paint.setPen(QColor(10,250,200))
        paint.setFont(QFont('Impact',20))
        paint.drawText(event.rect(), Qt.AlignCenter, self.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins =  qTemplate()
    app.exec_()