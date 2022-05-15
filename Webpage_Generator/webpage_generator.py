#Webpage Generator Assignment
#Emily Allen

#import needed modules
import tkinter as tk
from tkinter import *
import webbrowser

#Create the tkinter window
root = tk.Tk()
root.title("Webpage Generator")
root.geometry('500x500')

#Create the Text Widget for the user to input their webpage body
body_editor_lbl = tk.Label(root, text="Webpage Body Editor")
body_editor_lbl.pack()
body_editor = tk.Text(root, height=10)
body_editor.pack()
body_editor.insert('0.0',"Insert webpage body here....")

#function that puts together the html document with the new body information,
#writes the new html file and then opens the html file in the webbrowser
#in a new tab
def openWebpage():
    htmlString1 = """
            <!DOCTYPE html>
                <html>
                    <head>
                        <title>Your webpage here!</title>
                    </head>
                    <body>
                        <h1>"""
    htmlString2 = """
                        </h1>
                    </body>
                </html>
                """
    #this gets the text the user input
    updatedBody = body_editor.get('0.0','10.10')

    #this concatenates the strings that make up the html file
    fullText = htmlString1 + updatedBody + htmlString2

    #this creates and opens the html file
    createWrite = open('../Webpage_Generator/main.html', 'w')

    #this writes our html file with the updated body from the user
    createWrite.write(fullText)
    createWrite.close()

    #this opens our html file in a new tab in the browser
    webbrowser.open_new_tab('main.html')

#this is the button the user clicks to generate their webpage
open_page_button = Button(root, text="Open Updated Webpage", command=openWebpage)
open_page_button.pack()




root.mainloop()
