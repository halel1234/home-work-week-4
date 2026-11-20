import sys
from pathlib import Path

import numpy as np
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar,
)
from matplotlib.figure import Figure
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from About import AboutWindow


class IceCreamWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.about_window = AboutWindow()
        self.temperatures = []
        self.revenues = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Ice Cream Sales")
        self.setMinimumSize(760, 560)
        self.setObjectName("iceCreamWindow")

        self.title_label = QLabel("Ice Cream Sales")
        self.title_label.setObjectName("titleLabel")

        self.load_button = QPushButton("Load File")
        self.load_button.clicked.connect(self.load_clicked)

        self.about_button = QPushButton("About")
        self.about_button.clicked.connect(self.about_clicked)

        self.figure = Figure()
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        file_controls = QHBoxLayout()
        file_controls.addWidget(self.load_button)
        file_controls.addStretch()
        file_controls.addWidget(self.about_button)

        layout = QVBoxLayout(self)
        layout.addWidget(self.title_label)
        layout.addLayout(file_controls)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        self.draw_graph()

    def load_clicked(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Load CSV File", "", "CSV Files (*.csv)"
        )
        with open(file_name, 'r') as f:
            next(f)
            for line in f:
                temp, revenue = line.strip().split(',')
                self.temperatures.append(float(temp))
                self.revenues.append(float(revenue))
        self.draw_graph()

    def draw_graph(self):
        self.ax.clear()
        self.ax.scatter(self.temperatures, self.revenues, s=1)
        if len(self.temperatures) > 1 and len(self.revenues) > 1:
            slope, intercept = np.polyfit(self.temperatures, self.revenues, 1)
            trend_x = np.array(
                [min(self.temperatures), max(self.temperatures)]
            )
            trend_y = slope * trend_x + intercept
            self.ax.plot(trend_x, trend_y)
            sign = "+" if intercept >= 0 else "-"
            self.ax.text(
                0.05,
                0.95,
                f"y = {slope:.2f}x {sign} {abs(intercept):.2f}",
                transform=self.ax.transAxes,
                verticalalignment="top",
            )
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.set_title('Ice Cream Revenue vs Temperature')
        self.ax.set_xlabel('Temperature [°C]')
        self.ax.set_ylabel('Revenue [$]')
        self.canvas.draw()

    def about_clicked(self):
        self.about_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stylesheet = Path(__file__).with_name("ice_cream.qss")
    app.setStyleSheet(stylesheet.read_text(encoding="utf-8"))
    window = IceCreamWindow()
    window.show()
    sys.exit(app.exec())
