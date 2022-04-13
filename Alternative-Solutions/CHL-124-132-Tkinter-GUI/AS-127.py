"""
AS-127
Create a window that will ask the user to enter a
name in a text box. When they click on a button it
will add it to the end of the list that is displayed on
the screen. Create another button which will clear
the list.
"""
#####
# Python By Example
# Exercise 127
# Christopher Hagan
#####


from tkinter import *

def addToList():
    newName = nameEntry.get()
    listOfNames.insert(listOfNames.size()+1, newName)

def clearList():
    listOfNames.delete(0, listOfNames.size())

window = Tk()
window.geometry('500x500')
window.title('Add name to list of names')

instruction = Label(text='Please enter a name to add to the list: ')
instruction.place(x=50, y=100, width=270, height=25)

nameEntry = Entry(text='')
nameEntry.place(x=320, y=100, width=100, height=25)

addButton = Button(text='Add to list', command=addToList)
addButton.place(x=200, y=200, width=100, height=25)

clearButton = Button(text='Clear list', command=clearList)
clearButton.place(x=200, y=250, width=100, height=25)

listOfNames = Listbox()
listOfNames.place(x=200, y=300, width=100, height=150)

window.mainloop()

