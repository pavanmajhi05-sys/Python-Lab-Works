import tkinter as tk
from tkinter import messagebox

def generate():
    try:
        b, h, d, ded = (float(e.get()) for e in (e_b, e_h, e_d, e_ded))
        net = b + h + d - ded
        messagebox.showinfo("Pay Slip", f"{e_name.get()} ({e_id.get()})\nGross: {b+h+d}\nNet Pay: {net}")
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")

root = tk.Tk()
root.title("Pay Slip")
fields = ["Name", "ID", "Basic", "HRA", "DA", "Deductions"]
entries = []
for i, f in enumerate(fields):
    tk.Label(root, text=f).grid(row=i, column=0)
    e = tk.Entry(root); e.grid(row=i, column=1)
    entries.append(e)
e_name, e_id, e_b, e_h, e_d, e_ded = entries

tk.Button(root, text="Generate", command=generate).grid(row=6, columnspan=2, pady=10)
root.mainloop()
