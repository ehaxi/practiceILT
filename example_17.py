import sys
from PyQt6.QtWidgets import (
    QApplication, QCheckBox, QComboBox, QDateEdit,
    QDateTimeEdit, QDial, QDoubleSpinBox, QFontComboBox,
    QLabel, QLCDNumber, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QRadioButton, QSlider,
    QSpinBox, QTimeEdit, QVBoxLayout, QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widgets App")
        layout = QVBoxLayout()
        widgets = [
            QCheckBox, QComboBox, QDateEdit,
            QDateTimeEdit, QDial, QDoubleSpinBox, QFontComboBox, QLCDNumber,
            QLabel, QLineEdit, QProgressBar, QPushButton,
            QRadioButton, QSlider, QSpinBox, QTimeEdit,
        ]

        for widget in widgets:
            layout.addWidget(widget())

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())