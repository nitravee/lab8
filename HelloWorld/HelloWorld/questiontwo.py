import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Writer(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")

        layout  = QHBoxLayout(self)

        self.label = QLabel("")

        layout.addWidget(self.label)

    def mousePressEvent(self, QMouseEvent):
        p = QPainter()
        p.begin(self)
        
        p.setPen(Qt.black)
        p.drawPoint(QMouseEvent.pos())

        p.end()

    #def paintEvent(self, e):
        


def main():
    app = QApplication(sys.argv)

    w = Writer()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
