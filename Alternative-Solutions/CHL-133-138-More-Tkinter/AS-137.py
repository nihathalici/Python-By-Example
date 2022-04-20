"""
AS-137
Change program 136 so that when a new name and gender is added to the
list box it is also written to a text file. Add another button that will display
the entire text file in the main Python shell window.
"""
#####
# Python By Example
# Exercise 137
# Christopher Hagan
#####

from curses import window
from tkinter import *
import csv, os

fileName = 'nameGender.csv'
columnHeaders = ['Name', 'Gender']

def addToListbox():
    userBox.insert(END, '{}, {}'.format(nameEntry.get(), gender.get()))

    newEntry = {}
    newEntry[columnHeaders[0]] = nameEntry.get()
    newEntry[columnHeaders[1]] = gender.get()
    fileAlreadyExists = os.path.isfile(fileName)
    with open(fileName, 'a') as csvFile:
        fileWriter = csv.DictWriter(csvFile, fieldnames=columnHeaders)
        if not fileAlreadyExists:
            fileWriter.writeheader()

        fileWriter.writerow(newEntry)


def printContents():
    with open(fileName, 'r') as csvFile:
        fileReader = csv.DictReader(csvFile, fieldnames=columnHeaders)
        
        for row in fileReader:
            print(row)


window = Tk()
window.geometry('500x500')
window.title('Name list')

nameLabel = Label(text='Please enter a name: ')
nameLabel.place(x=100, y=50, width=150, height=25)

nameEntry = Entry(text='')
nameEntry.place(x=250, y=50, width=150, height=25)

gender = StringVar(window)
gender.set('Select Gender')
genderList = OptionMenu(window, gender, 'Male', 'Female')
genderList.place(x=100, y=100, width=300, height=25)

addToList = Button(text='Add to list', command=addToListbox)
addToList.place(x=100, y=150, width=300, height=50)

userBox = Listbox()
userBox.place(x=100, y=200, width=300, height=200)

printText = Button(text='Print text', command=printContents)
printText.place(x=100, y=450, width=300, height=25)


window.mainloop()





