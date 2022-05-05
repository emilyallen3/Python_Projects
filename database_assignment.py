#Database Assignment Step 222
#Emily Allen

import sqlite3

#Connect to the assignment database
conn = sqlite3.connect('assignment.db')


#Open connection to the database and use the cursor to
#execute the creation of a table with 2 columns file_id and file_name
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_file(\
        file_id INTEGER PRIMARY KEY AUTOINCREMENT,\
        file_name TEXT\
        )")
    #Commit the changes
    conn.commit()
#Close the connection to the database
conn.close()

#Connect to the database
conn = sqlite3.connect('assignment.db')


#Tuple of file names
fileList = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#A For loop that iterates through the list of file names.
#If the file ends in .txt, connect to the databse and use the cursor
#to execute the insertion of the txt files into the database
for file in fileList:
    if file.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_file(file_name) VALUES(?)",(file,))
            conn.commit()
            print(file)
conn.close()



