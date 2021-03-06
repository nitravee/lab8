#import sys
#from PySide.QtCore import*
#from PySide.QtGui import*

#class Simple_drawing_window(QWidget):
#    def __init__(self):
#        QWidget.__init__(self,None)
#        self.setWindowTitle("Simple Drawing")
        
#    def paintEvent(self,e):
#        p = QPainter()
#        p.begin(self)
#        p.setPen(QColor(0,0,0))
#        p.setBrush(QColor(0,127,0)
#        p.drawPolygon([
#            QPoint(70,100),QPoint(100,110),
#            QPoint(130,100),QPoint(100,150)
#        ])
#        p.setPen(QColor(255,127,0))
#        p.setBrush(QColor(255,127,0)
#        p.drawPie(50,150,100,100,0,180*16)

#        p.drawPolygon([
#            QPoint(50,200),QPoint(150,200),QPoint(100,400)])
#        p.end()

#def main():
#    app = QApplication(sys.argv)

#    w = Simple_drawing_window()
#    w.show()

#    return app.exec_()

#if __name__ == "__main__":
#    sys.exit(main())


import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QImage("C:\\Users\\MSI\\Documents\\GitHub\\lab8\\HelloWorld\\HelloWorld\\dog.jpg")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([
            QPoint( 70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150),
        ])

        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        p.drawPolygon([
            QPoint(50, 200), QPoint(150, 200), QPoint(100, 400),
        ])

        p.drawImage(QRect(200, 100, 320, 320), self.rabbit)
        p.end()


class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        

        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))

        p.drawPolygon([
            QPoint(50, 200), QPoint(200, 200), QPoint(200, 400),QPoint(50, 400)
        ])
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 0, 0))
        p.drawEllipse(100,220,15,15)
        p.drawEllipse(150,220,15,15)

        p.drawPolygon([
            QPoint(100, 320), QPoint(150, 320), QPoint(125, 350)
        ])

        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()

    w2 = Simple_drawing_window2()
    w2.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
