# main.py
import tkinter as tk
from gui.set_operations_gui import FuzzySetGUI
from gui.membership_gui import MembershipGUI
from gui.relations_gui import FuzzyRelationsGUI

def open_set_operations():
    win = tk.Toplevel()
    FuzzySetGUI(win)

def open_mf_editor():
    win = tk.Toplevel()
    MembershipGUI(win)

def open_relations():
    win = tk.Toplevel()
    FuzzyRelationsGUI(win)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Soft Computing Fuzzy Toolbox")
    root.geometry("400x250")

    tk.Label(root, text=" Soft Computing Toolbox", font=("Helvetica", 16, "bold")).pack(pady=15)
    tk.Button(root, text="Fuzzy Set Operations", command=open_set_operations, width=25).pack(pady=5)
    tk.Button(root, text="Membership Function Editor", command=open_mf_editor, width=25).pack(pady=5)
    tk.Button(root, text="Fuzzy Relations & Composition", command=open_relations, width=25).pack(pady=5)
    tk.Button(root, text="Exit", command=root.destroy, width=25).pack(pady=5)

    root.mainloop()
