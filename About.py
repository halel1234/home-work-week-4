from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QPixmap


class AboutWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('About')
        self.resize(320, 300)

        self.picture = QLabel(self)
        self.picture.setGeometry(75, 20, 150, 150)
        self.picture.setPixmap(QPixmap('profile.jpg'))
        self.picture.setScaledContents(True)

        self.name_label = QLabel('Name: Halel Harburger', self)
        self.name_label.setGeometry(20, 190, 260, 30)

        self.email_label = QLabel('Email: halelharburger@gmail.com', self)
        self.email_label.setGeometry(20, 220, 260, 30)

        self.github_label = QLabel('GitHub: <a href="https://github.com/halel1234/home-work-week-4">home-work-week-4</a>', self)
        self.github_label.setGeometry(20, 250, 280, 30)
        self.github_label.setOpenExternalLinks(True)