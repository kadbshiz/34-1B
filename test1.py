import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QListWidget,
    QVBoxLayout,
    QMessageBox,
    QLabel
)

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sostoyanye")
        self.setFixedSize(300, 200)

        self.label = QLabel("Состояние: выключено")
        self.add_btn = QPushButton("Включить")

        self.add_btn.clicked.connect(self.toggle_state)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.add_btn)

        self.setLayout(self.layout)


    def toggle_state(self):
        if self.label.text() == "Состояние: выключено":
            self.label.setText("Состояние: включено")
            self.add_btn.setText("Выключить")
        else:
            self.label.setText("Состояние: выключено")
            self.add_btn.setText("Включить")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())