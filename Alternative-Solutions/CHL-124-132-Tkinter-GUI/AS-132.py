"""
AS-132
Using the .csv file you created for the last challenge, create a program 
that will allow people to add names and ages to the list and create a 
button that will display the contents of the .csv file by importing it to a
list box.
"""
#####
# Python By Example
# Exercise 132
# Christopher Hagan
#####

from tkinter import *
import csv

columnHeaders = ['name', 'age']
fileName = ''

def createFile():
    pass

def updateList():
    fileContents.delete(0, END)
    with open(fileName, 'r') as csvFile:
        fileReader = csv.DictReader(csvFile, fieldnames=columnHeaders)
        i = 0
        for entry in fileReader:
            fileContents.insert(i, '{}, {}'.format(entry[columnHeaders[0]], entry[columnHeaders[1]]))
            i += 1


def addEntryToFile():
    newEntry = {}
    newEntry[columnHeaders[0]] = nameValue.get()
    newEntry[columnHeaders[1]] = ageValue.get()
    with open(fileName, 'a') as csvFile:
        fileWriter = csv.DictWriter(csvFile, fieldnames=columnHeaders)
        fileWriter.writerow(newEntry)
    updateList()

window = Tk()
window.geometry('500x700')
window.title('Working with csv files')

nameInstruction = Label(text='Enter the name to add: ')
nameInstruction.place(x=50, y=250, width=150, height=25)

nameValue = Entry(text='')
nameValue.place(x=300, y=250, width=100, height=25)
nameValue.focus()

ageInstruction = Label(text='Enter the age of this person: ')
ageInstruction.place(x=50, y=300, width=200, height=25)

ageValue = Entry(text='')
ageValue.place(x=300, y=300, width=100, height=25)

addPerson = Button(text='Add person to .csv file', command=addEntryToFile)
addPerson.place(x=100, y=375, width=300, height=25)

updateListbox = Button(text='Update the Listbox with file contents', command=updateList)
updateListbox.place(x=100, y=425, width=300, height=25)

fileContents = Listbox()
fileContents.place(x=100, y=475, width=300, height=200)

window.mainloop()
