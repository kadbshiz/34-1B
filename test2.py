import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QSpinBox, QLabel, QProgressBar, QMessageBox, QHBoxLayout
)
from PyQt6.QtCore import QTimer, Qt
class WaterReminderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Таймер напоминаний о воде")
        self.setMinimumSize(400, 300)

        self.interval_input = QSpinBox()
        self.interval_input.setRange(1, 1440)  
        self.interval_input.setSuffix(" min")
        self.interval_input.setValue(30)

        self.count_input = QSpinBox()
        self.count_input.setRange(1, 100)
        self.count_input.setValue(5)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_timer)

        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.pause_timer)
        self.pause_button.setEnabled(False)

        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_timer)
        self.reset_button.setEnabled(False)

        self.time_label = QLabel("Time until next reminder: 00:00")
        self.reminder_label = QLabel("Current reminder: 0")
        self.status_label = QLabel("Status: Waiting")

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)

        layout = QVBoxLayout()
        
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Interval:"))
        input_layout.addWidget(self.interval_input)
        input_layout.addWidget(QLabel("Total Reminders:"))
        input_layout.addWidget(self.count_input)
        
        layout.addLayout(input_layout)
        layout.addWidget(self.start_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.reset_button)
        layout.addWidget(self.time_label)
        layout.addWidget(self.reminder_label)
        layout.addWidget(self.status_label)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.total_reminders = 0
        self.current_reminder = 0
        self.remaining_time = 0
        self.is_paused = False

    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            minutes, seconds = divmod(self.remaining_time, 60)
            self.time_label.setText(f"Time until next reminder: {minutes:02}:{seconds:02}")
            progress = int(((self.interval_input.value() * 60 - self.remaining_time) / (self.interval_input.value() * 60)) * 100)
            self.progress_bar.setValue(progress)
        else:
            self.current_reminder += 1
            QMessageBox.information(self, "Reminder", "Time to drink water!")
            if self.current_reminder >= self.total_reminders:
                self.timer.stop()
                QMessageBox.information(self, "Completed", "All reminders completed!")
                self.reset_timer()
            else:
                self.remaining_time = self.interval_input.value() * 60
                self.update_ui_on_start()

    def start_timer(self):
        interval = self.interval_input.value() * 60  
        count = self.count_input.value()

        if interval <= 0 or count <= 0:
            QMessageBox.warning(self, "Warning", "Values must be greater than zero.")
            return

        self.total_reminders = count
        self.current_reminder = 0
        self.remaining_time = interval
        self.is_paused = False

        self.timer.start(1000)  
        self.update_ui_on_start()

    def update_ui_on_start(self):
        self.time_label.setText(f"Time until next reminder: {self.interval_input.value():02}:00")
        self.reminder_label.setText(f"Current reminder: {self.current_reminder}")
        self.status_label.setText("Status: Running")
        self.start_button.setEnabled(False)
        self.pause_button.setEnabled(True)
        self.reset_button.setEnabled(True)
        self.progress_bar.setValue(0)

    def pause_timer(self):
        if self.is_paused:
            self.timer.start(1000)
            self.status_label.setText("Status: Running")
            self.pause_button.setText("Pause")
            self.is_paused = False
        else:
            self.timer.stop()
            self.status_label.setText("Status: Paused")
            self.pause_button.setText("Resume")
            self.is_paused = True
    def reset_timer(self):
        self.timer.stop()
        self.remaining_time = 0
        self.current_reminder = 0
        self.time_label.setText("Time until next reminder: 00:00")
        self.reminder_label.setText("Current reminder: 0")
        self.status_label.setText("Status: Waiting")
        self.progress_bar.setValue(0)
        self.start_button.setEnabled(True)
        self.pause_button.setEnabled(False)
        self.reset_button.setEnabled(False)
        self.pause_button.setText("Pause")
        self.is_paused = False
    
    
        
app = QApplication(sys.argv)
window = WaterReminderApp()
window.show()
sys.exit(app.exec())