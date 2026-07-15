import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt

df = None

def load_file():
    global df
    path = filedialog.askopenfilename(filetypes=[("Excel", "*.xlsx *.xls")])
    if path:
        df = pd.read_excel(path)
        messagebox.showinfo("Loaded", f"Columns: {list(df.columns)}")

def plot_graph():
    if df is None:
        messagebox.showwarning("No Data", "Load an Excel file first")
        return
    x, y = e_x.get(), e_y.get()
    plt.bar(df[x].astype(str), df[y])
    plt.xlabel(x); plt.ylabel(y); plt.title(f"{y} vs {x}")
    plt.xticks(rotation=45)
    plt.show()

root = tk.Tk()
root.title("Excel Bar Graph")
tk.Button(root, text="Browse Excel File", command=load_file).pack(pady=5)
tk.Label(root, text="X column:").pack(); e_x = tk.Entry(root); e_x.pack()
tk.Label(root, text="Y column:").pack(); e_y = tk.Entry(root); e_y.pack()
tk.Button(root, text="Plot Bar Graph", command=plot_graph).pack(pady=10)
root.mainloop()
