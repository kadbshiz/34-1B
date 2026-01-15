import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLineEdit, QListWidget, QMessageBox
)
class ShoppingListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shopping List by Geeks")
        self.setMinimumSize(400, 300)

        layout = QVBoxLayout()

        self.item_input = QLineEdit()
        self.item_input.setPlaceholderText("Enter new item")

        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_item)

        self.list_widget = QListWidget()

        self.delete_button = QPushButton("Delete Selected")
        self.delete_button.clicked.connect(self.delete_item)

        layout.addWidget(self.item_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.list_widget)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)

    def add_item(self):
        item_text = self.item_input.text().strip()
        if item_text:
            self.list_widget.addItem(item_text)
            self.item_input.clear()
        else:
            QMessageBox.warning(self, "Warning", "The input field cannot be empty.")

    def delete_item(self):
        selected_items = self.list_widget.selectedItems()
        if selected_items:
            for item in selected_items:
                self.list_widget.takeItem(self.list_widget.row(item))
        else:
            QMessageBox.warning(self, "Warning", "No item selected to delete.")
    

app = QApplication(sys.argv)
window = ShoppingListApp()
window.show()
sys.exit(app.exec())


