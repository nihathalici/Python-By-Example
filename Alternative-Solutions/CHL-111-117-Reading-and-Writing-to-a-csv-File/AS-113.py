'''
AS-113
Using the Books.csv file, ask the user how many records
they want to add to the list and then allow them to add
that many. After all the data has been added, ask for an
author and display all the books in the list by that author.
If there are no books by that author in the list, display a
suitable message.
'''

#####
# Python By Example
# Exercise 113
# Christopher Hagan
#####

import csv

columnHeaders = ['Book', 'Author', 'Year Released']

newBooks = int(input('How many new books would you like to add?: '))
newBooksList = []

for i in range(0, newBooks):
    newBook = input('Enter the name of a new book to add: ')
    newAuthor = input('Enter the author of this book: ')
    newYear = input('Enter the year this book was published: ')
    print('-----')

    newBooksList.append({'Book': newBook, 'Author': newAuthor, 'Year Released': newYear})

with open('AS_Books.csv', 'a') as csvFile:
    booksFile = csv.DictWriter(csvFile, delimiter=',', fieldnames=columnHeaders)
    for newBookEntry in newBooksList:
        booksFile.writerow(newBookEntry)

searchAuthor = input('Which Author would you like to view: ')

booksByAuthor = 0

with open('AS_Books.csv', 'r') as updatedCsvFile:
    reader = csv.DictReader(updatedCsvFile, fieldnames=columnHeaders)

    for row in reader:
        if searchAuthor.lower() in str(row['Author']).lower():
            print('{}, {}, {}'.format(row['Book'], row['Author'], row['Year Released']))
            booksByAuthor += 1

if booksByAuthor == 0:
    print('This Author did not write any of the available books!')
