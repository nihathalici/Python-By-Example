"""
AS-130
Alter program 129 to add a third button that will save the list to a .csv file. The code
tmp_list = num_list.get(0,END) can be used to save the contents of a list box
as a tuple called tmp_list .
"""
#####
# Python By Example
# Exercise 130
# Christopher Hagan
#####

from email import message
from tkinter import *
import csv

fileName = 'AS_listOfNumbers.csv'

def addValue():
    valueEntered = userValue.get()
    if (valueEntered.isdigit()):
        listOfNumbers.insert(END, valueEntered)
        messageValue['fg'] = 'green'
        messageValue['text'] = '{} was added to the list!'.format(valueEntered)
    else:
        messageValue['fg'] = 'red'
        messageValue['text'] = '{} is not a digit, so it was not added!'.format(valueEntered)

def clearValues():
    listOfNumbers.delete(0, END)
    messageValue['fg'] = 'green'
    messageValue['text'] = 'List has been cleared!'

def saveList():
    tmp_list = listOfNumbers.get(0, END)
    with open(fileName, 'w') as csvFile:
        fileWriter = csv.writer(csvFile)

        for number in tmp_list:
            fileWriter.writerow([number])
    messageValue['fg'] = 'green'
    messageValue['text'] = '{} was saved!'.format(fileName)

window = Tk()
window.geometry('500x500')
window.title('Adding digits to a list')

instruction = Label(text='Enter a digit to add to the list: ')
instruction.place(x=30, y=50, width=250, height=25)

userValue = Entry(text='')
userValue.place(x=260, y=50, width=50, height=25)

messageValue = Message(text='')
messageValue.place(x=100, y=100, width=200, height=50)

addButton = Button(text='Add value to list', command=addValue)
addButton.place(x=150, y=150, width=200, height=25)

clearButton = Button(text='Clear list', command=clearValues)
clearButton.place(x=150, y=190, width=200, height=25)

saveButton = Button(text='Save list', command=saveList)
saveButton.place(x=150, y=230, width=200, height=25)

listOfNumbers = Listbox()
listOfNumbers.place(x=150, y=300, width=200, height=150)

window.mainloop()