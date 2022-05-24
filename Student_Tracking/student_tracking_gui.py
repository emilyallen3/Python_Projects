#Student Traking GUI
#Emily Allen
#Python Version 3.10.4


from tkinter import *
import tkinter as tk

#importing other modules
import student_tracking_main
import student_tracking_functions


def load_gui(self):
    #Label sections
    #First Name
    self.lbl_fname = tk.Label(self.master,text='First Name: ')
    self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    #Last Name
    self.lbl_lname = tk.Label(self.master,text='Last Name: ')
    self.lbl_lname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    #Phone Number
    self.lbl_phone = tk.Label(self.master,text='Phone Number: ')
    self.lbl_phone.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    #Email
    self.lbl_email = tk.Label(self.master,text='Email Name: ')
    self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    #Current Course
    self.lbl_course = tk.Label(self.master,text='Current Course: ')
    self.lbl_course.grid(row=8,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

    #Text Box Entry Section
    #First Name
    self.txt_fname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    #Last Name
    self.txt_lname = tk.Entry(self.master,text='')
    self.txt_lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    #Phone Number
    self.txt_phone = tk.Entry(self.master,text='')
    self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    #Email
    self.txt_email = tk.Entry(self.master,text='')
    self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    #Current Course
    self.txt_course = tk.Entry(self.master,text='')
    self.txt_course.grid(row=9,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    #Define the listbox with a scrollbar and grid them
    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.studentList = Listbox(self.master, exportselection=0, yscrollcommand=self.scrollbar1.set)
    self.studentList.bind('<<ListboxSelect>>', lambda event: student_tracking_functions.onSelect(self,event))
    self.scrollbar1.config(command=self.studentList.yview)
    self.scrollbar1.grid(row=1,column=5,rowspan=9,columnspan=1,padx=(0,0), pady=(0,0),sticky=N+E+S)
    self.studentList.grid(row=1,column=2,rowspan=9,columnspan=4,padx=(0,0),pady=(0,0), sticky=N+E+S+W)

    #Button Sections
    #Submit Button
    self.btn_submit = tk.Button(self.master,width=12,height=2,text='Submit',command=lambda: student_tracking_functions.addToList(self))
    self.btn_submit.grid(row=10,column=0,padx=(25,0),pady=(45,10),sticky=W)
    #Delete Button
    self.btn_delete = tk.Button(self.master,width=12,height=2,text='Delete',command=lambda: student_tracking_functions.onDelete(self))
    self.btn_delete.grid(row=10,column=2,padx=(15,0),pady=(45,10),sticky=W)
    #Close Button
    self.btn_close = tk.Button(self.master,width=12, height=2,text='Close', command=lambda: student_tracking_functions.ask_quit(self))
    self.btn_close.grid(row=10,column=4,padx=(15,0), pady=(45,10),sticky=E)

    student_tracking_functions.create_db(self)
    student_tracking_functions.onRefresh(self)



if __name__ == "__main__":
    pass




