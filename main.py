import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from ui.fuzzy_set_workspace.set_workspace_window import FuzzySetWindow
from ui.fuzzy_relation_workspace.relation_workspace_window import FuzzyRelationWindow
from ui.fis_designer.fis_designer_window import FISDesignerWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FuzzyLab")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        btn1 = QPushButton("Fuzzy Set Operations Workspace")
        btn1.clicked.connect(self.open_set_workspace)
        layout.addWidget(btn1)

        btn2 = QPushButton("Fuzzy Relations Workspace")
        btn2.clicked.connect(self.open_relation_workspace)
        layout.addWidget(btn2)

        btn3 = QPushButton("FIS Designer")
        btn3.clicked.connect(self.open_fis_designer)
        layout.addWidget(btn3)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_set_workspace(self):
        self.window = FuzzySetWindow()
        self.window.show()

    def open_relation_workspace(self):
        self.window = FuzzyRelationWindow()
        self.window.show()

    def open_fis_designer(self):
        self.window = FISDesignerWindow()
        self.window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
