import sys
from pathlib import Path

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QFileDialog,
    QPushButton,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from About import AboutWindow


class GradesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ''
        self.about_window = AboutWindow()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Student Grades")
        self.setMinimumSize(760, 560)
        self.setObjectName("gradesWindow")

        self.title_label = QLabel("Student Grades")
        self.title_label.setObjectName("titleLabel")

        self.load_button = QPushButton("Load File")
        self.load_button.clicked.connect(self.load_clicked)

        self.about_button = QPushButton("About")
        self.about_button.clicked.connect(self.about_clicked)

        self.bonus_label = QLabel("Bonus points")
        self.bonus_spinbox = QSpinBox()
        self.bonus_spinbox.setRange(0, 100)
        self.bonus_spinbox.lineEdit().returnPressed.connect(self.bonus_entered)

        self.update_button = QPushButton("Update File")
        self.update_button.setObjectName("updateButton")
        self.update_button.clicked.connect(self.update_clicked)

        self.grades_table = QTableWidget(50, 3)
        self.grades_table.setHorizontalHeaderLabels(
            ["ID", "Original Grades", "Corrected Grades"]
        )
        self.grades_table.horizontalHeader().setStretchLastSection(True)
        self.grades_table.horizontalHeader().setSectionResizeMode(
            self.grades_table.horizontalHeader().ResizeMode.Stretch
        )

        file_controls = QHBoxLayout()
        file_controls.addWidget(self.load_button)
        file_controls.addStretch()
        file_controls.addWidget(self.about_button)

        bonus_controls = QHBoxLayout()
        bonus_controls.addWidget(self.bonus_label)
        bonus_controls.addWidget(self.bonus_spinbox)
        bonus_controls.addStretch()
        bonus_controls.addWidget(self.update_button)

        layout = QVBoxLayout(self)
        layout.addWidget(self.title_label)
        layout.addLayout(file_controls)
        layout.addLayout(bonus_controls)
        layout.addWidget(self.grades_table)

    def load_clicked(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Load CSV File", "", "CSV Files (*.csv)"
        )
        pass  # my code here

    def bonus_entered(self):
        pass  # my code here

    def update_clicked(self):
        pass  # my code here

    def about_clicked(self):
        self.about_window.show()

    def update_table(self):
        self.grades_table.clearContents()
        for row, (student_id, original, corrected) in enumerate(
            zip(self.student_ids, self.original_grades, self.corrected_grades)
        ):
            if row >= self.grades_table.rowCount():
                break
            self.grades_table.setItem(row, 0, QTableWidgetItem(str(student_id)))
            self.grades_table.setItem(row, 1, QTableWidgetItem(str(original)))
            self.grades_table.setItem(row, 2, QTableWidgetItem(str(corrected)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stylesheet = Path(__file__).with_name("grades.qss")
    app.setStyleSheet(stylesheet.read_text(encoding="utf-8"))
    window = GradesWindow()
    window.show()
    sys.exit(app.exec())
