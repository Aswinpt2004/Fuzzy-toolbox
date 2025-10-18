# main.py
import tkinter as tk
from gui.set_operations_gui import FuzzySetGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = FuzzySetGUI(root)
    root.mainloop()
