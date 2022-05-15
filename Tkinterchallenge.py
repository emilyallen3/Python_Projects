#Script GUI Challenge

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd


root = tk.Tk()
root.title("Check files")
root.geometry('600x500')


#Text Widget
textwidget = tk.Text(root, width=50, height=10)
textwidgetlbl = tk.Label(root, text="Text Widget")
textwidgetlbl.pack()
textwidget.pack(side=RIGHT, fill=X, padx=10)

#Funtion to open dialog box and insert selected directory file path in text widget


def select_file():

    filename = fd.askdirectory(title='Open a folder', initialdir='/')

    textwidget.insert('1.0', filename)


open_button = Button(
    root, text="Get directory file path...", command=select_file)
open_button.pack(side=LEFT, padx=10, ipadx=10)

root.mainloop()