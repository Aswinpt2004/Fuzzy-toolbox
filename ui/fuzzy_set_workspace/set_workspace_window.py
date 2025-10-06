from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel
from .set_plot_widget import FuzzySetPlot

class FuzzySetWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fuzzy Set Operation Workspace")
        self.setGeometry(150, 150, 800, 600)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Fuzzy Set Operation Workspace - Coming Soon"))

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


plot = FuzzySetPlot()
layout.addWidget(plot)
