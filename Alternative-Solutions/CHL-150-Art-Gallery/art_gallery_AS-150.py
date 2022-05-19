#####
# Python By Example
# Exercise 150
# Christopher Hagan
##
#####

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

def pieceOfArtSold():
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

# FIRST MAIN FRAME: Artist Frame and Contents
artistFrame = LabelFrame(text='Artist')
artistFrame.place(x=50, y=25, width=900, height=300)

# SUBFRAME: New Artist
newArtistFrame = LabelFrame(text='Add new Artist')
newArtistFrame.place(x=600, y=50, width=330, height=230)

# SECOND MAIN FRAME:Artwork Frame and Contents
artworkFrame = LabelFrame(text='Artwork')
artworkFrame.place(x=50, y=375, width=900, height=600)

# SUBFRAME: FiltersFrame
FiltersFrame = LabelFrame(text='Filter')
FiltersFrame.place(x=750, y=400, width=150, height=225)

window.mainloop()
db.close()


