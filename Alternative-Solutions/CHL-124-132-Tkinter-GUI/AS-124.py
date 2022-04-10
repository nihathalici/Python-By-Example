'''
AS-124
Create a window that will ask the user to enter their
name. When they click on a button it should display
the message “Hello” and their name and change
the background colour and font colour of the
message box.
'''

#####
# Python By Example
# Exercise 124
# Christopher Hagan
#####

from tkinter import *
from urllib import response

def buttonPressed():
    name = entryBox.get()
    responseBox['text'] = 'Hello {}'.format(name)
    responseBox['bg'] = 'orange'
    responseBox['fg'] = 'black'

window = Tk()
window.title("Exercise 124")
window.geometry("400x250")

labelBox = Label(text='Enter your name: ')
labelBox.place(x=50, y=50)

entryBox = Entry(text='')
entryBox.place(x=175, y=50, width=125, height=25)

button = Button(text='Greeting', command=buttonPressed)
button.place(x=100, y=100, width=150, height=25)

responseBox = Message(text='')
responseBox.place(x=75, y=150, width=200, height=50)
responseBox['bg'] = 'blue'
responseBox['fg'] = 'white'

window.mainloop()