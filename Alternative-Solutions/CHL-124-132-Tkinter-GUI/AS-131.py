"""
AS-131
Create a program that will allow the user to create a new .csv file. It should
ask them to enter the name and age of a person and then allow them to add
this to the end of the file they have just created.
"""

#####
# Python By Example
# Exercise 131
# Christopher Hagan
#####

from tkinter import *
import csv

columnHeaders = ['name', 'age']

def newFile():
    name = fileName.get()
    if(name):
        with open(name, 'w') as csvFile:
            fileWriter = csv.DictWriter(csvFile, fieldnames=columnHeaders)
            fileWriter.writeheader()

def addEntryToFile():
    name = fileName.get()
    newEntry = {}
    newEntry[columnHeaders[0]] = nameValue.get()
    newEntry[columnHeaders[1]] = ageValue.get()
    with open(name, 'a') as csvFile:
        fileWriter = csv.DictWriter(csvFile, fieldnames=columnHeaders)
        fileWriter.writerow(newEntry)

window = Tk()
window.geometry('500x500')
window.title('Creating name/age csv files')

instruction = Label(text='Please enter a name for the new file: ')
instruction.place(x=50, y=100, width=250, height=25)

fileName = Entry(text='')
fileName.place(x=300, y=100, width=150, height=25)

newButton = Button(text='New CSV file...', command=newFile)
newButton.place(x=100, y=200, width=300, height=50)

nameInstruction = Label(text='Enter name: ')
nameInstruction.place(x=100, y=300, width=150, height=25)

nameValue = Entry(text='')
nameValue.place(x=250, y=300, width=100, height=25)

ageInstruction = Label(text='Enter age: ')
ageInstruction.place(x=100, y=350, width=100, height=25)

ageValue = Entry(text='')
ageValue.place(x=250, y=350, width=100, height=25)

addToFile = Button(text='Add entry to csv file....', command=addEntryToFile)
addToFile.place(x=100, y=400, width=300, height=25)

window.mainloop()

