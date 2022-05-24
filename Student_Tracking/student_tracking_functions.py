#Student Tracking Fucntions
#Emily Allen
#Python Version 3.10.4

import os
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox


#Import other modules
import student_tracking_main
import student_tracking_gui

def center_window(self, w, h):
    #pass in the tkinter fram(master) reference and the w and h
    #get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    #calculate x and y coordinates to pain the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

#this catches if the user clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Sad to see you go.","Okay to exit application?"):
        #this closes app
        self.master.destroy()
        os._exit(0)

#================================================================================

def create_db(self):
    conn = sqlite3.connect('db_student_tracking.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_student_tracking(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT \
            );")
        #Commiting to save changes and closing the database connection
        conn.commit()
    conn.close()
    first_run(self)

#this fucntion will only run is the database is empty
def first_run(self):
    conn = sqlite3.connect('db_student_tracking.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count <1:
            cur.execute("INSERT INTO tbl_student_tracking ( \
                col_fname, col_lname, col_fullname, col_phone, col_email, col_course) \
                VALUES \
                ('Jane','Doe','Jane Doe','111-111-1111','jdoe@email.com','Python Course')");
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("SELECT COUNT(*) FROM tbl_student_tracking")
    count = cur.fetchone()[0]
    return cur,count

#Select and item in ListBox
def onSelect(self,event):
    #calling the event is the self.student_list widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('db_student_tracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT col_fname,col_lname,col_phone,col_email,col_course FROM tbl_student_tracking WHERE col_fullname = (?)",[value])
        varBody = cursor.fetchall()
        #This returns a tuple and we can slice into parts using data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_course.delete(0,END)
            self.txt_course.insert(0,data[4])

#Function to submit student information
def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    var_phone = self.txt_phone.get()
    var_email = self.txt_email.get()
    if not "@" or not "." in var_email:
        print("Incorrect email format")

    var_course = self.txt_course.get()
    var_fullname = ("{} {}".format(var_fname,var_lname))
    
    #enforce the user to provide all the information needed
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_course) > 0):
        conn = sqlite3.connect('db_student_tracking.db')
        with conn:
            cursor = conn.cursor()
            #Check the db for the existance of the fullname
            cursor.execute("SELECT COUNT(col_fullname) FROM tbl_student_tracking WHERE col_fullname = '{}'".format(var_fullname)) 
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0:
                cursor.execute("INSERT INTO tbl_student_tracking (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)", (var_fname,var_lname,var_fullname,var_phone,var_email,var_course))
                self.studentList.insert(END,var_fullname)
                onClear(self)
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database. Please choose a different name.".format(var_fullname))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","please ensure there is data in all five fields.")

def onDelete(self):
    var_select = self.studentList.get(self.studentList.curselection())
    conn = sqlite3.connect('db_student_tracking.db')
    with conn:
        cur = conn.cursor()
        #check to ensure this is not the last record in the database
        cur.execute("SELECT COUNT(*) FROM tbl_student_tracking")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation","All information associated with, '{}' \nwill be permenantly deleted from the database. \nProceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('db_student_tracking.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM tbl_student_tracking WHERE col_fullname = '{}'".format(var_select))
                onDeleted(self)
                conn.commit()
            else:
                confirm = messagebox.showerror("Last Record Error","'{}' is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete '{}'.".format(var_select,var_select))
        conn.close()

def onDeleted(self):
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)
    try:
        index = self.studentList.curselection()[0]
        self.studentList.delete(index)
    except IndexError:
        pass

def onClear(self):
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)

def onRefresh(self):
    self.studentList.delete(0,END)
    conn = sqlite3.connect('db_student_tracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM tbl_student_tracking")
        count = cursor.fetchone()[0]
        i = 0
        while i <count:
            cursor.execute("SELECT col_fullname FROM tbl_student_tracking")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.studentList.insert(0,str(item))
                i = i + 1
    conn.close()
    
if __name__ == "__main__":
    pass


























    




























    






        












    
