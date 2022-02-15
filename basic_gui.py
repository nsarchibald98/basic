import numpy as np
import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
apps = []


def addApp():
    filename = filedialog.askopenfilename(initialdir='/', title='Select File',
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)


def bigNotation():
    var = txt.get()
    print("A linear search will have",var, "operations.")
    print(type(var))
    var = int(var)
    print("A binary search would take", np.log2(var), "operations.")


# GUI build
canvas = tk.Canvas(root, bg="navy", height=300, width=500)
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Buttons, labels, etc.
label = tk.Label(frame, bg="white", text="How many operations are needed?")
label.place(relx=0.5, rely=0.5, anchor='center')

txt = tk.Entry(frame, fg="black", bg="light gray", width=15)
txt.pack()

tk.Button(frame, text="Compute", padx=10, pady=10,
          fg="White", bg="navy", command=bigNotation).pack()

root.mainloop()
