import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget, 
    QLineEdit, 
    QPushButton,
    QListWidget, 
    QVBoxLayout, 
    QMessageBox
)


class TodoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To-Do List by Geeks")
        self.setFixedSize(400, 300)

        self.input = QLineEdit()
        self.input.setPlaceholderText("...")

        self.add_btn = QPushButton("Добавить")
        self.delete_btn = QPushButton("Удалить выбранное")

        self.list = QListWidget()

        self.add_btn.clicked.connect(self.add_task)
        self.delete_btn.clicked.connect(self.delete_task)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.list)
        layout.addWidget(self.delete_btn)

        self.setLayout(layout)

    def add_task(self):
        text = self.input.text()
        if text == "":
            QMessageBox.warning(self, "Error")
        else:
            self.list.addItem(text)
            self.input.clear()

    def delete_task(self):
        row = self.list.currentRow()
        if row != -1:
            self.list.takeItem(row)


app = QApplication(sys.argv)
window = TodoApp()
window.show()
sys.exit(app.exec())
