import sys


from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Programme(QWidget):
    def __init__(self):
        super().__init__()
        self.can_draw = False
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("Случайные круги")

        self.btn = QPushButton("Кнопка", self)
        self.btn.resize(75, 23)
        self.btn.move(150, 240)
        self.btn.clicked.connect(self.draw)

    def draw(self):
        self.can_draw = True
        self.repaint()

    def paintEvent(self, event):
        if self.can_draw:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            size = randint(10, 210)
            qp.drawEllipse(90, 10, size, size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Programme()
    ex.show()
    sys.exit(app.exec())

