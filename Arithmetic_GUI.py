import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        n1, n2 = float(e1.get()), float(e2.get())
        op = choice.get()
        result = {"add": n1+n2, "sub": n1-n2, "mul": n1*n2,
                  "div": n1/n2 if n2 else None}[op]
        if result is None:
            messagebox.showerror("Error", "Cannot divide by zero")
        else:
            messagebox.showinfo("Result", f"Result = {result}")
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")

root = tk.Tk()
root.title("Arithmetic Operations")

tk.Label(root, text="Number 1:").grid(row=0, column=0); e1 = tk.Entry(root); e1.grid(row=0, column=1)
tk.Label(root, text="Number 2:").grid(row=1, column=0); e2 = tk.Entry(root); e2.grid(row=1, column=1)

choice = tk.StringVar(value="add")
for i, (t, v) in enumerate([("+", "add"), ("-", "sub"), ("*", "mul"), ("/", "div")]):
    tk.Radiobutton(root, text=t, variable=choice, value=v).grid(row=2, column=i)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, columnspan=4, pady=10)
root.mainloop()
