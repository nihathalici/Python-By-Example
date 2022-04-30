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
    pass

def clearFields():
    pass

with sqlite3.connect("AS-TestScores.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Scores(
    Name text PRIMARY KEY,
    Score INTEGER NOT NULL);""")

window = Tk()
window.geometry()
window.title('Test Scores')

window.mainloop()
db.close()

