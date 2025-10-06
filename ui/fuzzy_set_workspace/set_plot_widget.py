from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from core.membership_functions import triangular

class FuzzySetPlot(QWidget):
    def __init__(self):
        super().__init__()
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.plot_triangular()

    def plot_triangular(self):
        x = np.linspace(0, 10, 200)
        y = triangular(x, 2, 5, 8)
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.plot(x, y, label="Triangular(2,5,8)")
        ax.set_ylim(0, 1.1)
        ax.legend()
        self.canvas.draw()
