#Emily Allen

#import modules
import shutil
import os
import time
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd

#create tkinter window gui
root = tk.Tk()
root.title("File Copying Tool")
root.geometry('900x500')
root.resizable(False,False)


#Text Widgets where folder paths will be inserted
text1 = tk.Text(root, width=22, height=15)
text1.pack(side=LEFT, padx=10)

text2 = tk.Text(root, width=22, height=15)
text2.pack(side=RIGHT, padx=10)


#Funtion to open dialog box and insert selected directory folder path in text widget
def select_folder1():

    folderpath1 = fd.askdirectory(initialdir='/')
    text1.insert('1.0',folderpath1)

def select_folder2():

    folderpath2 = fd.askdirectory(initialdir='/')
    text2.insert('1.0',folderpath2)

#buttons
select_button1 = Button(root, text="Select folder to copy from...", command=select_folder1)
select_button1.pack(side=LEFT, padx=10, ipadx=10)
select_button2 = Button(root, text="Select folder to copy to...", command=select_folder2)
select_button2.pack(side=RIGHT, padx=10, ipadx=10)



def copy_files():
    #get the folder path where the source of the files are
    source = (text1.get('1.0', 'end-1c') + '/')

    #get the folder path where the files will be coppied too
    destination = (text2.get('1.0', 'end-1c') + '/')
    
    files = os.listdir(source)
    for i in files:
        if i.endswith('.txt'):
            modTime = os.path.getmtime(source + i)
            currentTime = time.time()
            modDiff = currentTime - modTime
            if modDiff < 86400.0:
                #we are saying move the files represented by i to their new destination
                shutil.copy2(source+i, destination)
                text2.insert('2.0','\nFile copied successfully!')

#button
copy_button = Button(root, text="Copy modified files...", width=20,command=copy_files)
copy_button.pack(side=TOP, pady=10, ipadx=15, ipady=15)


