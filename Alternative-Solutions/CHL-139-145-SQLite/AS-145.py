"""
AS-145
Create a program that displays the following screen: It should save the data to an SQL database called TestScores 
when the Add button is clicked. The Clear button should clear the window.
"""
#####
# Python By Example
# Exercise 145
# Christopher Hagan
#####

import sqlite3
from tkinter import *

def addToDB():
    name = nameEntry.get()
    score = int(gradeEntry.get())
    cursor.execute("""INSERT INTO Scores(Name, Score) 
        VALUES('{}', {});""".format(name, score))
    db.commit()
    clearFields()

def clearFields():
    nameEntry.delete(0, 'end')
    gradeEntry.delete(0, 'end')

with sqlite3.connect("AS-TestScores.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Scores(
    Name text PRIMARY KEY,
    Score INTEGER NOT NULL);""")

window = Tk()
window.geometry('500x250')
window.title('Test Scores')

nameLabel = Label(text='Enter student\'s name: ')
nameLabel.place(x=100, y=50, width=200, height=25)

nameEntry = Entry(text='')
nameEntry.place(x=300, y=50, width=150, height=25)

gradeLabel = Label(text='Enter the student\'s grade: ')
gradeLabel.place(x=100, y=100, width=200, height=25)

gradeEntry = Entry(text='')
gradeEntry.place(x=300, y=100, width=150, height=25)

addButton = Button(text='Add', command=addToDB)
addButton.place(x=200, y=175, width=50, height=50)

clearButton = Button(text='Clear', command=clearFields)
clearButton.place(x=350, y=175, width=50, height=50)

window.mainloop()

db.close()
