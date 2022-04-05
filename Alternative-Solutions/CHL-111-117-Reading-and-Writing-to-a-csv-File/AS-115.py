'''
AS-115
Using the Books.csv file, display the data in
the file along with the row number of each.
'''

#####
# Python By Example
# Exercise 115
# Christopher Hagan
#####

import csv 

columnHeaders = ['Book', 'Author', 'Year Released']

with open('AS_Books.csv', 'r') as csvFile:
    reader = csv.DictReader(csvFile, fieldnames=columnHeaders)

    count = 0
    for row in reader:
        if columnHeaders[2] not in row[columnHeaders[2]]:
            print('{} - {} by {} published in {}'.format(count, row['Book'], row['Author'], row['Year Released']))
        count += 1
