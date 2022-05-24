#Student Tracking Assignment
#Emily Allen
#Python Ver: 3.10.4

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os


#importing other modules
import student_tracking_gui
import student_tracking_functions


#Fram is the Tkinter fram class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master fram configuration
        self.master = master
        self.master.minsize(600,400) #(height,width)
        self.master.maxsize(600,400)
        #This CenterWindow method will center our app on the user's screen
        student_tracking_functions.center_window(self,500,300)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")
        #This protocol method is a tkinter built-in method to catch
        #if the user clicks the upper corner,"X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_tracking_functions.ask_quit(self))
        arg = self.master

        #Loading in GUI widgets from a separate module to compparmentalize code and keep it clutter free
        student_tracking_gui.load_gui(self)





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()




    
