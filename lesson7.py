import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox


class UpdateUserApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRUD - Update part")
        self.setFixedSize(300, 360)

        self.db = sqlite3.connect('users.db')
        self.cursor = self.db.cursor()
        self.create_table()

        self.init_ui()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER
            )
        ''')
        self.db.commit()

    def init_ui(self):
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("User ID")

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Age")

        self.status = QLabel("")

        btn_add = QPushButton("Add User")
        btn_add.clicked.connect(self.add_user)

        btn_update = QPushButton("Update User")
        btn_update.clicked.connect(self.update_user)

        btn_delete = QPushButton("Delete User")
        btn_delete.clicked.connect(self.delete_user)

        btn_read = QPushButton("Read Users")
        btn_read.clicked.connect(self.read_users)

        layout = QVBoxLayout()
        layout.addWidget(self.id_input)
        layout.addWidget(self.name_input)
        layout.addWidget(self.age_input)
        layout.addWidget(btn_add)
        layout.addWidget(btn_update)
        layout.addWidget(btn_delete)
        layout.addWidget(btn_read)
        layout.addWidget(self.status)

        self.setLayout(layout)

    def add_user(self):
        name = self.name_input.text()
        age = self.age_input.text()
        if name and age.isdigit():
            self.cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, int(age)))
            self.db.commit()
            self.status.setText("User added successfully.")
        else:
            self.status.setText("Invalid input for name or age.")
        self.db.commit()

        self.status.setText("User added successfully.")
        self.clear_inputs()

    def read(self):
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()

        if not users:
            self.status.setText("Table is empty.")
            return
        
        text = ""
        for user in users:
            text += f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}\n"

        self.status.setText(text)

    def update_user(self):
        user_id = self.id_input.text()
        name = self.name_input.text()
        age = self.age_input.text()
        if user_id.isdigit() and name and age.isdigit():
            self.cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, int(age), int(user_id)))
            if self.cursor.rowcount == 0:
                self.status.setText("
                
                " \
                "")
            else:
                self.db.commit()
                self.status.setText("User updated successfully.")
        else:
            self.status.setText("Invalid input for ID, name, or age.")
        self.clear_inputs()