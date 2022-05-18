#####
# Python By Example
# Exercise 149
# Christopher Hagan
#####

"""
When the user enters a number in the first box and clicks on the
“View Times Table” button it should show the times table in
the list area. The “Clear” button should clear both boxes.
"""

from tkinter import *

def calculateTimesTables():
    multiplier = int(numberEntry.get())
    for i in range(1, 13):
        timesTableBox.insert('end', '{} x {} = {}'.format(i, multiplier, i*multiplier))
    numberEntry.delete(0, 'end')
    numberEntry.focus()

def clearEntryBoxes():
    numberEntry.delete(0, 'end')
    timesTableBox.delete(0, 'end')
    numberEntry.focus()

window = Tk()
window.geometry("500x500")
window.title('Times Tables')

numberLabel = Label(text='Enter a number:')
numberLabel.place(x=25, y=50, width=125, height=25)

numberEntry = Entry(text='')
numberEntry.place(x=150, y=50, width=150, height=25)

timesTableBox = Listbox()
timesTableBox.place(x=150, y=100, width=150, height=300)

viewTimesTableButton = Button(text='View Times Table', command=calculateTimesTables)
viewTimesTableButton.place(x=325, y=100, width=150, height=25)

clearButton = Button(text='Clear', command=clearEntryBoxes)
clearButton.place(x=325, y=150, width=150, height=25)

window.mainloop()
