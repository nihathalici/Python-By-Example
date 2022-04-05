'''
Import the data from the Books.csv file into a list. Display the
list to the user. Ask them to select which row from the list
they want to delete and remove it from the list. Ask the user
which data they want to change and allow them to change it.
Write the data back to the original .csv file, overwriting the
existing data with the amended data.
'''

#####
# Python By Example
# Exercise 116
# Christopher Hagan
#####

import csv

columnHeaders = ['Book', 'Author', 'Year Released']

tmp = []
with open('AS_Books.csv', 'r') as csvFile:
    reader = csv.DictReader(csvFile, fieldnames=columnHeaders)

    count = 0
    for row in reader:
        tmp.append(row)
        if count != 0:
            print('{} - {}  by {} published in {}'.format(count, row['Book'], row['Author'], row['Year Released']))
        count += 1

# Row to remove entirely - process this last
rowToDelete = int(input('Which row should be deleted: '))

# Row to update the values in
rowToChange = int(input('Which row should be changed: '))
changedBook = input('Enter a new book name: ')
changedAuthor = input('Enter the author of the new book: ')
changedYear = input('Enter the year of the new book: ')

# Remove the row that needs to be updated then enter a new value
tmp.pop(rowToChange)
tmp.insert(rowToChange, {'Book': changedBook, 'Author': changedAuthor, 'Year Released': changedYear})

# Remove the value that needs to be removed entirely
tmp.pop(rowToDelete)

with open('AS_Books.csv', 'w') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=columnHeaders)

    writer.writeheader()
    for newEntry in tmp:
        # Ignore header row
        if not(newEntry['Book'] in columnHeaders[0] and newEntry['Author'] in columnHeaders[1] and
               newEntry['Year Released'] in columnHeaders[2]):
            writer.writerow(newEntry)