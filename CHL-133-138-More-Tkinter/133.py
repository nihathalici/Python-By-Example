"""
133
Create your own icon that consists of several
vertical multi-coloured lines. Create a logo
which measures 200 x 150, using Paint or
another graphics package. Create the
following window using your own icon and
logo.

When the user enters their name and clicks
on the Press Me button it should display
“Hello” and their name in the second text
box.
"""

from tkinter import *

def click():
    name = textbox1.get()
    message = str("Hello " + name)
    textbox2["text"] = message

window = Tk()
window.title("Names")
window.geometry("450x350")
window.wm_iconbitmap("MyIcon.ico")
window.configure(background="black")


logo = PhotoImage(file="Mylogo.gif")
logoimage = Label(image=logo)
logoimage.place(x = 100, y = 20, width= 200, height=150)

label1 = Label(text= "Enter your name:")
label1.place(x = 30, y = 200)
label1["bg"] = "black"
label1["fg"] = "white"

textbox1 = Entry(text = "")
textbox1.place(x = 150, y = 200, width= 200, height=25)
textbox1["justify"] = "center"
textbox1.focus()

button1 = Button(text = "Press me", command=click)
button1.place(x = 30, y = 250, width= 120, height=25)
button1["bg"] = "yellow"

textbox2 = Message(text = "")
textbox2.place(x = 150, y = 250, width= 200, height=25)
textbox2["bg"] = "white"
textbox2["fg"] = "black"

window.mainloop()
