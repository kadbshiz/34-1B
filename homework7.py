import sys
import sqlite3

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QListWidget
)
class PeopleDatabaseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("People Database")
        self.setFixedSize(400, 500)

        self.db = sqlite3.connect("people.db")
        self.cursor = self.db.cursor()
        self.create_table()

        self.init_ui()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS people (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER
            )
        """)
        self.db.commit()

    def init_ui(self):
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("ID")

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Age")

        btn_add = QPushButton("Add")
        btn_add.clicked.connect(self.add_person)

        btn_read = QPushButton("Show All")
        btn_read.clicked.connect(self.show_all)

        btn_delete = QPushButton("Delete")
        btn_delete.clicked.connect(self.delete_person)

        btn_update = QPushButton("Edit")
        btn_update.clicked.connect(self.update_person)

        self.status = QLabel("")

        layout = QVBoxLayout()

        layout.addWidget(self.id_input)
        layout.addWidget(self.name_input)
        layout.addWidget(self.age_input)
        layout.addWidget(self.status)

        layout.addWidget(btn_add)
        layout.addWidget(btn_read)
        layout.addWidget(btn_delete)
        layout.addWidget(btn_update)
        
        self.people_list = QListWidget()

        layout.addWidget(self.people_list)

        self.setLayout(layout)
    
    def add_person(self):
        name = self.name_input.text()
        age = self.age_input.text()

        if not name or not age:
            self.status.setText("Please enter both name and age.")
            return
        
        self.cursor.execute("INSERT INTO people (name, age) VALUES (?, ?)", (name, age))
        self.db.commit()

        self.clear_inputs()

    def show_all(self):
        self.people = self.cursor.execute("SELECT * FROM people").fetchall()

        if not self.people:
            self.status.setText("No Data")
            return

        self.people_list.clear()
        for data in self.people:
            self.people_list.addItem(f"ID: {data[0]}: {data[1]} ({data[2]} years old)")
        

    def delete_person(self):
        person_id = self.id_input.text()

        if not person_id:
            self.status.setText("Please enter an ID to delete.")
            return
        
        self.cursor.execute("DELETE FROM people WHERE id = ?", (person_id))
        self.db.commit()

        self.clear_inputs()

    def update_person(self):
        person_id = self.id_input.text()
        name = self.name_input.text()
        age = self.age_input.text()

        if not person_id:
            self.status.setText("Please enter an ID to edit.")
            return
        
        self.cursor.execute("UPDATE people SET name = ?, age = ? WHERE id = ?", (name, age, person_id))
        self.db.commit()

        self.clear_inputs()
    
    def clear_inputs(self):
        self.id_input.clear()
        self.name_input.clear()
        self.age_input.clear()

app = QApplication(sys. argv)
window = PeopleDatabaseApp()
window.show()
sys.exit(app.exec())

        
