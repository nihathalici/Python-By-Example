"""
AS-136
Create a program that will ask the user to enter a name and then select 
the gender for that person from a drop-down list. It should then add 
the name and the gender (separated by a comma) to a list box 
when the user clicks on a button.
"""
#####
# Python By Example
# Exercise 136
# Christopher Hagan
#####
from tkinter import *

def addToListbox():
    userBox.insert(END, '{}, {}'.format(nameEntry.get(), gender.get()))

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
userBox.place(x=100, y=250, width=300, height=200)

window.mainloop()
