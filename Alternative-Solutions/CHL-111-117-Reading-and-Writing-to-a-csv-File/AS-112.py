'''
AS-112
Using the Books.csv file from program 111, ask the user to enter another
record and add it to the end of the file. Display each row of the .csv file
on a separate line.
'''

#####
# Python By Example
# Exercise 112
# Christopher Hagan
#####

import csv

columnHeaders = ['Book', 'Author', 'Year Released']

newBook = input('Enter a new book to add: ')
newAuthor = input('Enter the Author of the book: ')
newYear = input('Enter the year the book was released: ')

newEntry = {'Book': newBook, 'Author': newAuthor, 'Year Released': newYear}

with open('AS_Books.csv', 'a') as csvFile:
    booksFile = csv.DictWriter(csvFile, delimiter=',', fieldnames=columnHeaders)
    booksFile.writerow(newEntry)

with open('AS_Books.csv', 'r') as updatedCsvFile:
    reader = csv.reader(updatedCsvFile)

    for row in reader:
        print(row)














