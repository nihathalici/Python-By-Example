"""
128
1 kilometre = 0.6214 miles and 1 mile = 1.6093 kilometres. 
Using these figures, make a program that will allow the 
user to convert between miles and kilometres.
"""
#####
# Python By Example
# Exercise 128
# Christopher Hagan
#####

from tkinter import *

mileInKilometres = 1.6093
kilometreInMiles = 0.6214

def displayValues(kms, miles):
    kmValue['text'] = 'Value in KMs\n\n{} kms'.format(kms)
    milesValue['text'] = 'Value in Miles\n\n{} miles'.format(miles)

def valueInKilometres():
    miles = float(userValue.get())
    kms = round(miles * mileInKilometres, 5)
    displayValues(kms=kms, miles=miles)

def valueInMiles():
    kms = float(userValue.get())
    miles = round(kms * kilometreInMiles, 5)
    displayValues(kms=kms, miles=miles)

window = Tk()
window.geometry('500x500')
window.title('Convert distance between kilometres and miles')

instruction = Label(text='Enter the value you wish to convert: ')
instruction.place(x=50, y=50, width=250, height=25)

userValue = Entry(text='')
userValue.place(x=300, y=50, width=50, height=25)

kmValue = Message(text='')
kmValue.place(x=100, y=150, width=100, height=50)

milesValue = Message(text='')
milesValue.place(x=300, y=150, width=100, height=50)

kmButton = Button(text='Convert To KM', command=valueInKilometres)
kmButton.place(x=150, y=300, width=200, height=50)

milesButton = Button(text='Convert To Miles', command=valueInMiles)
milesButton.place(x=150, y=400, width=200, height=50)

window.mainloop()