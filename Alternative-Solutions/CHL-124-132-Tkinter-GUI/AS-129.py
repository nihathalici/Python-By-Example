"""
AS-129
Create a window that will ask the user to enter a number in a text box.
When they click on a button it will use the code variable.isdigit() to check
to see if it is a whole number. If it is a whole number, add it to a list box,
otherwise clear the entry box. Add another button that will clear the list.
"""

#####
# Python By Example
# Exercise 129
# Christopher Hagan
#####

from tkinter import *

def addValue():
    valueEntered = userValue.get()
    if (valueEntered.isdigit()):
        listOfNumbers.insert(END, int(valueEntered))
        messageValue['fg'] = 'green'
        messageValue['text'] = '{} was added to the list!'.format(valueEntered)
    else:
        messageValue['fg'] = 'red'
        messageValue['text'] = '{} is not a digit, so it was not added!'.format(valueEntered)

def clearValues():
    listOfNumbers.delete(0, END)
    messageValue['fg'] = 'green'
    messageValue['text'] = 'List has been cleared!'

window = Tk()
window.geometry('500x500')
window.title('Adding digits to a list')

instruction = Label(text = 'Enter a digit to add to the list: ')
instruction.place(x=30, y=50, width=250, height=25)

userValue = Entry(text='')
userValue.place(x=260, y=50, width=50, height=25)

messageValue = Message(text='')
messageValue.place(x=100, y=100, width=200, height=50)

addButton = Button(text = 'Add value to list', command=addValue)
addButton.place(x=150, y=150, width=200, height=25)

clearButton = Button(text='Clear list', command=clearValues)
clearButton.place(x=150, y=190, width=200, height=25)

listOfNumbers = Listbox()
listOfNumbers.place(x=150, y=250, width=200, height=200)

window.mainloop()
