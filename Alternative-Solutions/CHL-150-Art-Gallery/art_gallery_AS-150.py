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
    artistList = []
    artistQuery = cursor.execute("""SELECT ArtistID, Name FROM Artists;""")
    for artist in artistQuery.fetchall():
        artistList.append('{} - {}'.format(artist[0], artist[1]))
    
    artistCombobox.config(values=artistList)

def clearNewArtistFields():
    nameEntry.delete(0, 'end')
    addressEntry.delete(0, 'end')
    townEntry.delete(0, 'end')
    countyEntry.delete(0, 'end')
    postcodeEntry.delete(0, 'end')


def clearNewArtworkFields():
    titleEntry.delete(0, 'end')
    mediumEntry.delete(0, 'end')
    priceEntry.delete(0, 'end')
    artistCombobox.set('')


def clearArtworkTree():
    for i in artworkFrame.get_children():
        artworkFrame.delete(i)

def displayArtist(artistKey):
    artistListBox.delete(0, 'end')
    if (artistKey == 0):
        artistListBox.insert('end', 'No Artist Selected')
    else:
        contentsOfArtistTable = cursor.execute("""SELECT Name, Address, County, Town, Postcode FROM artists WHERE ArtistID={};""".format(artistKey))
        name, address, county, town, postcode = contentsOfArtistTable.fetchone()
        artistListBox.insert('end', 'Artist Name : {}'.format(name))
        artistListBox.insert('end', '')
        artistListBox.insert('end', 'Artist Address : {}'.format(address))
        artistListBox.insert('end', 'County : {}'.format(county))
        if (town):
            artistListBox.insert('end', 'Town : {}'.format(town))
        artistListBox.insert('end', 'Postcode : {}'.format(postcode))



def displayArtwork(contentsOfPiecesOfArt):
    clearArtworkTree()
    if (contentsOfPiecesOfArt):
        for pieceOfArt in contentsOfPiecesOfArt:
            artworkFrame.insert('', 'end', text=pieceOfArt[0], values=(pieceOfArt[1], pieceOfArt[2], pieceOfArt[3]))
    else:
        artworkFrame.insert('', 'end', text='Empty', values=('No artwork exists', '', ''))


def loadAllArtwork():
    contentsOfPiecesOfArt = cursor.execute("""SELECT PieceID, Title, Medium, Price FROM PiecesOfArt""")
    displayArtwork(contentsOfPiecesOfArt)

def clearSearchFilter():
    searchCriteriaCombobox.set('')
    searchForEntry.delete(0, 'end')
    loadAllArtwork()

def artworkSelected(selection):
    if (artworkFrame.item(artworkFrame.focus())['text']):
        selectedArtist = cursor.execute("""SELECT ArtistID FROM PiecesOfArt WHERE PieceID={}""".format(artworkFrame.item(artworkFrame.focus())['text']))
        selectedArtistKey = selectedArtist.fetchone()[0]
    else:
        selectedArtistKey = 0
    
    displayArtist(artistKey=selectedArtistKey)

def addArtist():
    if (nameEntry.get() and addressEntry.get() and countyEntry.get() and postcodeEntry.get()):
        cursor.execute("""INSERT INTO Artists(Name, Address, Town, County, Postcode)
        VALUES('{}', '{}', '{}', '{}', '{}')""".format(nameEntry.get(), addressEntry.get(), townEntry.get(), countyEntry.get(), postcodeEntry.get()))
        db.commit()
        clearNewArtistFields()
        generateListOfArtists()
    else:
        tkinter.messagebox.showerror('Data Error', 'Incomplete Artist entry!')

def addPieceOfArt():
    if (titleEntry.get() and mediumEntry.get() and priceEntry.get() and artistCombobox.get()):
        artistID = artistCombobox.get().split()[0]
        cursor.execute("""INSERT INTO PiecesOfArt(ArtistID, Title, Medium, Price)
        VALUES('{}', '{}', '{}', '{}')""".format(int(artistID), titleEntry.get(), mediumEntry.get(), int(priceEntry.get())))
        db.commit()
        loadAllArtwork()
        clearNewArtistFields()
    else:
        tkinter.messagebox.showerror('Data Error', 'Incomplete Artwork entry!')



def pieceOfArtSold():
    focusedItem = artworkFrame.item(artworkFrame.focus())
    if (focusedItem['text']):
        artworkToBeRemoved = cursor.execute("""SELECT PieceID, ArtistID, Title, Medium, Price FROM PiecesOfArt WHERE PieceID={}""".format(focusedItem['text']))
        pieceID, artistID, title, medium, price = artworkToBeRemoved.fetchone()
        artist = cursor.execute("""SELECT Name FROM Artists WHERE ArtistID={}""".format(artistID)).fetchone()[0]

        soldFileExists = os.path.isfile(soldArtworkFile)
        with open(soldArtworkFile, 'a') as csvFile:
            fileWriter = csv.DictWriter(csvFile, fieldnames=soldArtworkColumnHeaders)
            if not soldFileExists:
                fileWriter.writeheader()
            fileWriter.writerow({'PieceID': pieceID, 'Artist': artist, 'Title': title, 'Medium': medium, 'Price': price})
        
        cursor.execute("""DELETE FROM PiecesOfArt WHERE PieceID={}""".format(focusedItem['text']))
        db.commit()
        loadAllArtwork()
    else:
        tkinter.messagebox.showerror('Selection Error', 'No artwork selected!')

def searchArtwork():
    if (searchCriteriaCombobox.get() == 'Artist'):
        contentsOfPiecesOfArt = cursor.execute("""SELECT PieceID, Title, Medium, Price FROM PiecesOfArt WHERE ArtistID IN 
        (SELECT ArtistID FROM Artists WHERE Name='{}');""".format(searchForEntry.get())).fetchall()
    else:
        contentsOfPiecesOfArt = cursor.execute("""SELECT PieceID, Title, Medium, Price FROM PiecesOfArt WHERE {}='{}'""".format
        (searchCriteriaCombobox.get(), searchForEntry.get())).fetchall()

    displayArtwork(contentsOfPiecesOfArt)

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

artistListBox = Listbox()
artistListBox.place(x=150, y=75, width=300, height=150)
displayArtist(0)

# SUBFRAME: New Artist
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

# SECOND MAIN FRAME:Artwork Frame and Contents
artworkFrame = LabelFrame(text='Artwork')
artworkFrame.place(x=50, y=375, width=900, height=600)

artworkFrame = ttk.Treeview(show='headings', column=('Title', 'Medium', 'Price'), selectmode='browse')
artworkFrame.column('Title', width=300, anchor='w')
artworkFrame.heading('Title', text='Title')
artworkFrame.column('Medium', width=150, anchor='center')
artworkFrame.heading('Medium', text='Medium')
artworkFrame.column('Price', width=150, anchor='e')
artworkFrame.heading('Price', text='Price (£)')
artworkFrame.bind('<<TreeviewSelect>>', artworkSelected)
artworkFrame.place(x=75, y=400, width=600, height=400)
loadAllArtwork()

# SUBFRAME: FiltersFrame
filtersFrame = LabelFrame(text='Filter')
filtersFrame.place(x=750, y=400, width=150, height=225)

searchLabel = Label(text='Search criteria')
searchLabel.place(x=775, y=425, width=100, height=25)

searchCriteriaCombobox = ttk.Combobox(values=['Artist', 'Medium', 'Price'])
searchCriteriaCombobox.place(x=775, y=450, width=100, height=25)

searchForLabel = Label(text='Search for')
searchForLabel.place(x=775, y=475, width=100, height=25)

searchForEntry = Entry(text='')
searchForEntry.place(x=775, y=500, width=100, height=25)

searchButton = Button(text='Search', command=searchArtwork)
searchButton.place(x=775, y=545, width=100, height=25)

clearFilterButton = Button(text='Clear Filter', command=clearSearchFilter)
clearFilterButton.place(x=775, y=585, width=100, height=25)

sellArtworkButton = Button(text='Mark Artwork\n as sold', command=pieceOfArtSold)
sellArtworkButton.place(x=750, y=700, width=150, height=50)

# SUBFRAME: newArtworkFrame

newArtworkFrame = LabelFrame(text='Add new artwork')
newArtworkFrame.place(x=75, y=825, height=130, width=850)

titleLabel = Label(text='Title -')
titleLabel.place(x=100, y=850, width=75, height=25)
titleEntry = Entry(text='')
titleEntry.place(x=175, y=850, width=400, height=25)

mediumLabel = Label(text='Medium -')
mediumLabel.place(x=100, y=875, width=75, height=25)
mediumEntry = Entry(text='')
mediumEntry.place(x=175, y=875, width=100, height=25)

priceLabel = Label(text='Price (£) -')
priceLabel.place(x=100, y=900, width=75, height=25)
priceEntry = Entry(text='')
priceEntry.place(x=175, y=900, width=100, height=25)

artistLabel = Label(text='Artist -')
artistLabel.place(x=300, y=885, width=75, height=25)

artistCombobox = ttk.Combobox(values='')
artistCombobox.place(x=400, y=885, width=150, height=25)
generateListOfArtists()

addPieceOfArtButton = Button(text='Add Piece of\n  Art', command=addPieceOfArt)
addPieceOfArtButton.place(x=700, y=870, width=100, height=50)

window.mainloop()
db.close()
