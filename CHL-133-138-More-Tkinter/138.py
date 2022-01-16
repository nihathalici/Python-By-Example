"""
138
Save several images in the same folder as your program and call them 1.gif, 2.gif, 
3.gif, etc. Make sure they are all .gif files. Display one in a window and ask 
the user to enter a number. It should then use that number to choose the correct 
file name and display the correct image.
"""
from tkinter import *

def clicked():
    num = selection.get()
    artref = num + ".gif"
    photo = PhotoImage(file = artref)
    photobox.image = photo
    photobox["image"] = photo
    photobox.update()

window = Tk()
window.title("Art")
window.geometry("400x350")

art = PhotoImage(file = "1.gif")
photobox = Label(window, image = art)
photobox.image = art
photobox.place(x = 100, y = 20, width = 200, h = 150)

label = Label(text = "Select Art number:")
label.place(x = 50, y = 200, width = 120, h = 25)

selection = Entry(text = "")
selection.place(x = 200, y = 200, width = 100, h = 25)
selection.focus()

button = Button(text = "See Art", command = clicked)
button.place(x = 150, y = 250, width = 100, h = 25)

window.mainloop()
