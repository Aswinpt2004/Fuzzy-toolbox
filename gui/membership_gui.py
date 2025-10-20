# gui/membership_gui.py
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from modules import fuzzy_membership

class MembershipGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Membership Function Editor - Soft Computing Toolbox")
        self.root.geometry("1000x650")

        self.frame = ttk.Frame(root, padding=10)
        self.frame.pack(fill="both", expand=True)

        # Universe
        self.x = np.linspace(0, 10, 200)
        self.params = {}
        self.mf_type = tk.StringVar(value="Triangular")

        # Dropdown for MF type
        ttk.Label(self.frame, text="Select MF Type:").grid(row=0, column=0, sticky="w")
        self.mf_menu = ttk.Combobox(self.frame, textvariable=self.mf_type,
                                    values=["Triangular", "Trapezoidal", "Gaussian", "GBell", "Sigmoidal"], width=20)
        self.mf_menu.grid(row=0, column=1, padx=5)
        self.mf_menu.bind("<<ComboboxSelected>>", self.update_sliders)

        # Sliders Frame
        self.slider_frame = ttk.LabelFrame(self.frame, text="Parameters", padding=10)
        self.slider_frame.grid(row=1, column=0, columnspan=3, sticky="ew", pady=10)

        # Plot Area
        self.fig, self.ax = plt.subplots(figsize=(7, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.get_tk_widget().grid(row=2, column=0, columnspan=3, pady=10)

        # Buttons
        ttk.Button(self.frame, text="Plot MF", command=self.plot_mf).grid(row=3, column=0, padx=5)
        ttk.Button(self.frame, text="Reset", command=self.reset_plot).grid(row=3, column=1, padx=5)
        ttk.Button(self.frame, text="Save MF", command=self.save_mf).grid(row=3, column=2, padx=5)

        # Dynamic sliders for parameters
        self.update_sliders()

    def update_sliders(self, event=None):
        # Clear existing sliders
        for widget in self.slider_frame.winfo_children():
            widget.destroy()

        mf = self.mf_type.get()
        self.params = {}

        # Define parameter sliders based on MF type
        param_configs = {
            "Triangular": ["a", "b", "c"],
            "Trapezoidal": ["a", "b", "c", "d"],
            "Gaussian": ["mean", "sigma"],
            "GBell": ["a", "b", "c"],
            "Sigmoidal": ["a", "c"]
        }

        for i, p in enumerate(param_configs[mf]):
            ttk.Label(self.slider_frame, text=p).grid(row=0, column=i, padx=5)
            scale = tk.Scale(self.slider_frame, from_=0, to=10, resolution=0.1,
                             orient="horizontal", command=lambda val, key=p: self.update_param(key, val))
            scale.set(2 + i)  # default spread
            scale.grid(row=1, column=i, padx=5)
            self.params[p] = scale.get()

    def update_param(self, key, val):
        self.params[key] = float(val)
        self.plot_mf()

    def plot_mf(self):
        self.ax.clear()
        mf = self.mf_type.get()
        try:
            y = self.compute_mf(mf, self.params)
            self.ax.plot(self.x, y, color="blue", linewidth=2)
            self.ax.set_ylim(-0.05, 1.05)
            self.ax.set_title(f"{mf} Membership Function")
            self.ax.grid(True)
            self.canvas.draw()
        except Exception as e:
            self.ax.text(0.5, 0.5, f"Error: {str(e)}", ha="center", color="red")
            self.canvas.draw()

    def compute_mf(self, mf, p):
        if mf == "Triangular":
            return fuzzy_membership.triangular(self.x, p["a"], p["b"], p["c"])
        elif mf == "Trapezoidal":
            return fuzzy_membership.trapezoidal(self.x, p["a"], p["b"], p["c"], p["d"])
        elif mf == "Gaussian":
            return fuzzy_membership.gaussian(self.x, p["mean"], p["sigma"])
        elif mf == "GBell":
            return fuzzy_membership.gbell(self.x, p["a"], p["b"], p["c"])
        elif mf == "Sigmoidal":
            return fuzzy_membership.sigmoidal(self.x, p["a"], p["c"])
        else:
            raise ValueError("Invalid MF Type")

    def reset_plot(self):
        self.ax.clear()
        self.ax.set_title("Membership Function Editor")
        self.canvas.draw()

    def save_mf(self):
        mf_name = self.mf_type.get()
        print(f"Saved MF: {mf_name} with parameters {self.params}")
