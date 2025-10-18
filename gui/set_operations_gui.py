# gui/set_operations_gui.py
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from modules import fuzzy_sets

class FuzzySetGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fuzzy Set Operations - Soft Computing Toolbox")
        self.root.geometry("900x600")

        # --- UI Elements ---
        self.frame = ttk.Frame(root, padding=10)
        self.frame.pack(fill="both", expand=True)

        # X universe
        self.x = np.linspace(0, 10, 100)

        # Dropdown for operation
        self.op_var = tk.StringVar()
        ttk.Label(self.frame, text="Select Operation:").grid(row=0, column=0, sticky="w")
        op_menu = ttk.Combobox(self.frame, textvariable=self.op_var,
                               values=["Union", "Intersection", "Complement"], width=20)
        op_menu.grid(row=0, column=1, padx=5, pady=5)
        op_menu.current(0)

        # Buttons
        ttk.Button(self.frame, text="Compute", command=self.compute_operation).grid(row=0, column=2, padx=5)
        ttk.Button(self.frame, text="Reset", command=self.reset_plot).grid(row=0, column=3, padx=5)

        # Matplotlib Figure
        self.fig, self.ax = plt.subplots(figsize=(7, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=4)

        # Example Sets
        self.A = fuzzy_sets.triangular(self.x, 2, 4, 6)
        self.B = fuzzy_sets.gaussian(self.x, 5, 1)

        self.plot_sets()

    def plot_sets(self):
        self.ax.clear()
        self.ax.plot(self.x, self.A, label='Set A', color='blue')
        self.ax.plot(self.x, self.B, label='Set B', color='orange')
        self.ax.set_ylim(-0.05, 1.05)
        self.ax.legend()
        self.ax.set_title("Fuzzy Sets Visualization")
        self.canvas.draw()

    def compute_operation(self):
        op = self.op_var.get()
        if op == "Union":
            result = fuzzy_sets.fuzzy_union(self.A, self.B)
            label = "A ∪ B"
        elif op == "Intersection":
            result = fuzzy_sets.fuzzy_intersection(self.A, self.B)
            label = "A ∩ B"
        else:
            result = fuzzy_sets.fuzzy_complement(self.A)
            label = "¬A"

        self.ax.clear()
        self.ax.plot(self.x, self.A, 'b--', label='A')
        self.ax.plot(self.x, self.B, 'r--', label='B')
        self.ax.plot(self.x, result, 'g', linewidth=2.5, label=f'Result: {label}')
        self.ax.legend()
        self.ax.set_ylim(-0.05, 1.05)
        self.ax.set_title(f"Operation: {label}")
        self.canvas.draw()

    def reset_plot(self):
        self.plot_sets()
