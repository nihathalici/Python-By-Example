Art Gallery
========================================================

A small art gallery is selling works from different artists and wants to keep track of the paintings using an SQL database. You need to create a user-friendly system to keep track of the art. This should include using a GUI.


art_gallery_AS-150.py
========================================================

```Python3
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

import os, sqlite3, tkinter.messagebox, csv

soldArtworkFile = 'soldArtwork.csv'
soldArtworkColumnHeaders = ['PieceID', 'Artist', 'Title', 'Medium', 'Price']

def generateListOfArtists():
    pass

def clearNewArtistFields():
    pass

def clearNewArtworkFields():
    pass

def clearArtworkTree():
    pass

def displayArtist(artistKey):
    pass

def displayArtwork(contentsOfPiecesOfArt):
    pass

def loadAllArtwork():
    pass

def clearSearchFilter():
    pass

def artworkSelected(selection):
    pass

def addArtist():
    pass

def addPieceOfArt():
    pass

def addPieceOfArtSold():
    pass

def searchArtwork():
    pass

with sqlite3.connect("ArtGallery.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Artists(
ArtistID INTEGER PRIMARY KEY,
Name text NOT NULL,
Address text NOT NULL,
Town text,
County text NOT NULL,
Postcode text NOT NULL);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS PiecesOfArt(
PieceID INTEGER PRIMARY KEY,
ArtistID INTEGER NOT NULL,
Title text NOT NULL,
Medium text NOT NULL,
Price INTEGER NOT NULL);""")

window = Tk()
window.geometry('1000x1000')
window.title('Art Gallery')

# Artist Frame and Contents
artistFrame = LabelFrame(text='Artists')
artistFrame.place(x=50, y=25, width=900, height=300)

artistListBox = Listbox()
artistListBox.place(x=150, y=75, width=300, height=150)
displayArtist(0)

# SUBFRAME: newArtistFrame

newArtistFrame = LabelFrame(text='Add new Artist')
newArtistFrame.place(x=600, y=50, width=330, height=230)

nameLabel = Label(text='Name: ')
nameLabel.place(x=610, y=75, width=75, height=25)
nameEntry = Entry(text='')
nameEntry.place(x=685, y=75, width=150, height=25)

addressLabel = Label(text='Address: ')
addressLabel.place(x=610, y=100, width=75, height=25)
addressEntry = Entry(text='')
addressEntry.place(x=685, y=100, width=150, height=25)

townLabel = Label(text='Town: ')
townLabel.place(x=610, y=125, width=75, height=25)
townEntry = Entry(text='')
townEntry.place(x=685, y=125, width=150, height=25)

countyLabel = Label(text='County: ')
countyLabel.place(x=610, y=150, width=75, height=25)
countyEntry = Entry(text='')
countyEntry.place(x=685, y=150, width=150, height=25)

postcodeLabel = Label(text='Postcode: ')
postcodeLabel.place(x=610, y=175, width=75, height=25)
postcodeEntry = Entry(text='')
postcodeEntry.place(x=685, y=175, width=150, height=25)

addArtistButton = Button(text='Add Artist', command=addArtist)
addArtistButton.place(x=740, y=215, width=75, height=50)

# Artwork frame and contents

window.mainloop()

db.close()


```

Sample Output
========================================================

![Sample output Art Gallery](https://github.com/nihathalici/Python-By-Example/blob/main/Alternative-Solutions/CHL-150-Art-Gallery/art_gallery_AS-150_sample_output.PNG)
