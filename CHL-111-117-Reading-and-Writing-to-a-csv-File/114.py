'''
Using the Books.csv file, ask the user to enter a starting year and an end
year. Display all books released between those two years.
'''

import csv

start = int(input("Enter a starting year: "))
end = int(input("Enter an end year: "))

file = list(csv.reader(open("Books.csv", "r")))
tmp = []
for row in file:
    tmp.append(row)

x = 0
for row in tmp:
    if int(tmp[x][2]) >= start and int(tmp[x][2]) <= end:
        print(tmp[x])
    x = x + 1
