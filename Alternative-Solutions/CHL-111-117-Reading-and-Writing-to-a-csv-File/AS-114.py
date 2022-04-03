'''
AS-114
Using the Books.csv file, ask the user to enter a starting year and an end
year. Display all books released between those two years.
'''

#####
# Python By Example
# Exercise 114
# Christopher Hagan
#####

import csv

columnHeaders = ['Book', 'Author', 'Year Released']

startYear = int(input('Enter the starting year: '))
endYear = int(input('Enter the ending year: '))

with open('AS_Books.csv', 'r') as csvFile:
    reader = csv.DictReader(csvFile, fieldnames=columnHeaders)

    for row in reader:
        if columnHeaders[2] not in row[columnHeaders[2]]:
            bookYear = int(row[columnHeaders[2]])
            if (bookYear >= startYear) and (bookYear <= endYear):
                print('{}, {}, {}'.format(row['Book'], row['Author'], row['Year Released']))
