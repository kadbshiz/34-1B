import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt

class ClickCounterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Счётчик кликов")
        self.setFixedSize(300, 200)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.counter = 0

        self.label = QLabel(f"Количество кликов: {self.counter}")
        self.button = QPushButton("Нажми меня")
        self.button.clicked.connect(self.increment_counter)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def increment_counter(self):
        self.counter += 1
        self.label.setText(f"Количество кликов: {self.counter}")

app = QApplication(sys.argv)
window = ClickCounterApp()
window.show()
sys.exit(app.exec())
