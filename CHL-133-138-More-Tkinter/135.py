"""
135
Create a simple program that shows a drop-down list containing several
colours and a Click Me button. When the user selects a colour from the list
and clicks the button it should change the background of the
window to that colour. For an extra challenge, try to avoid using an if
statement to do this.
"""
from tkinter import *

def clicked():
    sel = selectcolour.get()
    window.configure(background = sel)

window = Tk()
window.title("background")
window.geometry("200x200")

selectcolour = StringVar(window)
selectcolour.set("Grey")

colourlist = OptionMenu(window, selectcolour, "Grey", "Red", "Blue", "Green", "Yellow")
colourlist.place(x = 50, y = 30)

clickme = Button(text = "Click Me", command= clicked)
clickme.place(x = 50, y = 150, width= 60, height = 30)

mainloop()