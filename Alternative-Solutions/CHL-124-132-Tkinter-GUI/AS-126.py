'''
AS-126
Create a program that will ask the user to enter a number in a
box. When they click on a button it will add that number
to a total and display it in another box. This can be
repeated as many times as they want and keep adding to
the total. There should be another button that resets the
total back to 0 and empties the original text box, ready for
them to start again.
'''

#####
# Python By Example
# Exercise 126
# Christopher Hagan
#####

from tkinter import *

def displayTotal(total):
    totalValue['text'] = '{}'.format(total)

def addToTotal():
    newValue = int(userValue.get())
    currentTotal = int(totalValue['text'])
    currentTotal += newValue
    displayTotal(currentTotal)

def resetTotal():
    total = 0
    displayTotal(total)

total = 0
window = Tk()
window.title('Adding to total')
window.geometry('500x500')

instruction = Label(text = 'Please enter a number to add to the total: ')
instruction.place(x=30, y=50)

userValue = Entry(text='')
userValue.place(x=320, y=50, width=50, height=25)

totalLabel = Label(text='Total is ')
totalLabel.place(x=200, y=400, width=50, height=25)

totalValue = Message(text='0')
totalValue.place(x=250, y=400, width=100, height=25)
displayTotal(total)

addValue = Button(text='Add value to total', command=addToTotal)
addValue.place(x=150, y=200, width=200, height=50)

resetToZero = Button(text='Reset total to zero', command=resetTotal)
resetToZero.place(x=150, y=250, width=200, height=50)

window.mainloop()