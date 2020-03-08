import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Todo app")
root.geometry("800x600")

label_style = ttk.Style()
label_style.configure("Bordered.TLabel", borderwidth=2, relief="sunken")

label = ttk.Label(root, text="Hello", style="Bordered.TLabel")
label.grid(row=0, column=0, columnspan=2)

root.mainloop()
# label
