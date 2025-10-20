import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from modules import fuzzy_relations

class FuzzyRelationsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fuzzy Relations and Composition - Soft Computing Toolbox")
        self.root.geometry("1150x800")

        self.frame = ttk.Frame(root, padding=10)
        self.frame.pack(fill="both", expand=True)

        # --- Control Panel ---
        control_frame = ttk.LabelFrame(self.frame, text="Controls", padding=10)
        control_frame.grid(row=0, column=0, columnspan=11, sticky="ew", pady=5)

        # ===== First Row =====
        ttk.Label(control_frame, text="Rows (X):").grid(row=0, column=0, sticky="w", padx=4, pady=3)
        self.rows_R = tk.IntVar(value=3)
        tk.Entry(control_frame, textvariable=self.rows_R, width=5).grid(row=0, column=1, padx=4)

        ttk.Label(control_frame, text="Cols (Y):").grid(row=0, column=2, sticky="w", padx=4)
        self.cols_R = tk.IntVar(value=3)
        tk.Entry(control_frame, textvariable=self.cols_R, width=5).grid(row=0, column=3, padx=4)

        ttk.Label(control_frame, text="Mode:").grid(row=0, column=4, sticky="w", padx=4)
        self.mode = tk.StringVar(value="Random")
        mode_combo = ttk.Combobox(control_frame, textvariable=self.mode,
                                  values=["Random", "Manual"], width=10)
        mode_combo.grid(row=0, column=5, padx=4)

        ttk.Button(control_frame, text="Generate Relations",
                   command=self.generate_relations).grid(row=0, column=6, padx=4)

        ttk.Label(control_frame, text="Composition Type:").grid(row=0, column=7, sticky="w", padx=4)
        self.comp_type = tk.StringVar(value="Max-Min")
        ttk.Combobox(control_frame, textvariable=self.comp_type,
                     values=["Max-Min", "Max-Product"], width=15).grid(row=0, column=8, padx=4)

        ttk.Button(control_frame, text="Compute Composition",
                   command=self.compute_composition).grid(row=0, column=9, padx=4)

        for col in range(10):
            control_frame.grid_columnconfigure(col, weight=1)

        # --- Manual Entry Area ---
        self.manual_frame = ttk.LabelFrame(self.frame, text="Manual Entry (for R and S)", padding=10)
        self.manual_frame.grid(row=1, column=0, columnspan=11, sticky="ew", pady=10)

        self.slider_R = []  # Sliders for R
        self.slider_S = []  # Sliders for S

        # --- Figures for visualization ---
        self.fig, self.axes = plt.subplots(1, 3, figsize=(10, 4))
        self.fig.subplots_adjust(wspace=0.4)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.get_tk_widget().grid(row=2, column=0, columnspan=11, pady=10)

        self.R = None
        self.S = None
        self.T = None

        self.generate_relations()

    # ===============================
    # Manual Sliders Generator
    # ===============================
    def create_manual_sliders(self):
        for widget in self.manual_frame.winfo_children():
            widget.destroy()

        ttk.Label(self.manual_frame, text="Matrix R(x, y)").grid(row=0, column=0, padx=10)
        ttk.Label(self.manual_frame, text="Matrix S(y, z)").grid(row=0, column=6, padx=10)

        rows, cols = self.rows_R.get(), self.cols_R.get()
        self.slider_R, self.slider_S = [], []

        # Sliders for R(x,y)
        for i in range(rows):
            row_sliders = []
            for j in range(cols):
                val = tk.DoubleVar(value=0.5)
                frame = ttk.Frame(self.manual_frame)
                frame.grid(row=i+1, column=j, padx=2, pady=2)
                tk.Scale(frame, variable=val, from_=0, to=1, resolution=0.05,
                         orient="vertical", length=80).pack()
                tk.Label(frame, textvariable=val, width=4).pack()
                row_sliders.append(val)
            self.slider_R.append(row_sliders)

        sep = ttk.Separator(self.manual_frame, orient='vertical')
        sep.grid(row=0, column=cols+1, rowspan=max(rows, cols)+2, sticky='ns', padx=30)

        # Sliders for S(y,z)
        for i in range(cols):
            row_sliders = []
            for j in range(rows):
                val = tk.DoubleVar(value=0.5)
                frame = ttk.Frame(self.manual_frame)
                frame.grid(row=i+1, column=j+6, padx=2, pady=2)
                tk.Scale(frame, variable=val, from_=0, to=1, resolution=0.05,
                         orient="horizontal", length=80).pack()
                tk.Label(frame, textvariable=val, width=4).pack()
                row_sliders.append(val)
            self.slider_S.append(row_sliders)

    def get_manual_matrices_from_sliders(self):
        """Read slider values for R and S matrices"""
        m, n = self.rows_R.get(), self.cols_R.get()
        R = np.zeros((m, n))
        S = np.zeros((n, m))
        for i in range(m):
            for j in range(n):
                R[i, j] = float(self.slider_R[i][j].get())
        for i in range(n):
            for j in range(m):
                S[i, j] = float(self.slider_S[i][j].get())
        return R, S

    # ===============================
    # Generate Relations
    # ===============================
    def generate_relations(self):
        mode = self.mode.get()
        m, n = self.rows_R.get(), self.cols_R.get()

        if mode == "Random":
            self.R = fuzzy_relations.random_relation(m, n)
            self.S = fuzzy_relations.random_relation(n, m)
            self.plot_relations()
        else:
            # Manual mode — show sliders but no plot yet
            self.create_manual_sliders()
            self.R, self.S, self.T = None, None, None
            for ax in self.axes:
                ax.clear()
            self.canvas.draw()
            messagebox.showinfo("Manual Mode Active",
                                "Adjust sliders for R(x,y) and S(y,z), then click 'Compute Composition'.")

    # ===============================
    # Plotting Relations
    # ===============================
    def plot_relations(self):
        for ax in self.axes:
            ax.clear()

        plots = [
            (self.R, "R(x, y)"),
            (self.S, "S(y, z)"),
            (self.T, "T(x, z)" if self.T is not None else "Result")
        ]

        for ax, (mat, title) in zip(self.axes, plots):
            if mat is not None:
                im = ax.imshow(mat, cmap="viridis", vmin=0, vmax=1)
                ax.set_title(title)
                for i in range(mat.shape[0]):
                    for j in range(mat.shape[1]):
                        ax.text(j, i, f"{mat[i, j]:.2f}", ha="center", va="center", color="w", fontsize=8)

        self.canvas.draw()

    # ===============================
    # Compute Composition
    # ===============================
    def compute_composition(self):
        if self.mode.get() == "Manual":
            R, S = self.get_manual_matrices_from_sliders()
            self.R, self.S = R, S
            self.T = None
            self.plot_relations()

        if self.comp_type.get() == "Max-Min":
            self.T = fuzzy_relations.max_min_composition(self.R, self.S)
        else:
            self.T = fuzzy_relations.max_product_composition(self.R, self.S)

        self.plot_relations()
