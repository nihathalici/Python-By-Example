'''
AS-111
Create a .csv file that will store the following data. Call it “Books.csv”.
'''

#####
# Python By Example
# Exercise 111
# Christopher Hagan
#####

import csv

columnHeaders = ['Book','Author','Year Released']
books = [{'Book': 'To Kill A Mockingbird', 'Author': 'Harper Lee', 'Year Released': '1960'},
         {'Book': 'A Brief History Of Time','Author': 'Stephen Hawking', 'Year Released': '1988'},
         {'Book': 'The Great Gatsby','Author': 'F.Scott Fitzgerald', 'Year Released': '1922'},
         {'Book': 'The Man Who Mistook His Wife For A Hat','Author':  'Oliver Sacks', 'Year Released': '1985'},
         {'Book': 'Pride and Prejudice','Author':  'Jane Austen', 'Year Released': '1813'}]

with open('AS_Books.csv', 'w') as csvFile:
    booksFile = csv.DictWriter(csvFile, delimiter=',', fieldnames=columnHeaders)

    booksFile.writeheader()
    for book in books:
        booksFile.writerow(book)
