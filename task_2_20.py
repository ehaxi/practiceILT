import sys
from PyQt6.QtGui import QMouseEvent, QPainter, QPen, QImage, QColor
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QTextEdit
from PyQt6.QtCore import QSize, Qt, QRectF


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.image = QImage()
        self.userlsResizing = False
        self.resize(320, 240)
        # self.init_image(self.size())
        self.setWindowTitle("My App")
        self.installEventFilter(self)

    def init_image(self, size: QSize):
        self.image = QImage(
            self.size().width(), self.size().height(),
            QImage.Format.Format_ARGB32
        )

    def paintEvent(self, event):
        width = self.image.width()
        height = self.image.height()

        for x in range(height):
            for y in range(width):
                self.image.setPixel(
                    x, y, QColor(255 - int(255 * x /
                    width), int(255 * x / width),
                    int(255 * y / height), 255).rgb()
                )
        painter = QPainter(self)
        painter.drawImage(QRectF(0, 0, width, height), self.image)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
