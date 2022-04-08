'''
AS-122
Create the following menu:
  1) Add to file
  2) View all records
  3) Quit program
If the user selects 1, allow them to add to a file called Salaries.csv which will store their name
and salary. If they select 2 it should display all records in the Salaries.csv file. If they select 3
it should stop the program. If they select an incorrect option they should see an error message.
They should keep returning to the menu until they select option 3.
'''

#####
# Python By Example
# Exercise 122
# Christopher Hagan
#####

import sys, csv, os

fileName = 'salaries.csv'
columnHeaders = ['Name', 'Salary']
breakBetweenLines = '-------'

def addNameAndSalary():
    newEntry = {}
    newEntry[columnHeaders[0]] = input('Enter the new name to add: ')
    newEntry[columnHeaders[1]] = input('Enter the salary of this person ')
    FileExists = os.path.isfile(fileName)
    with open(fileName, 'a') as csvFile:
        fileWriter = csv.DictWriter(csvFile, fieldnames=columnHeaders)
        if not FileExists:
            fileWriter.writeheader()
        fileWriter.writerow(newEntry)


def viewFile():
    with open(fileName, 'r') as csvFile:
        fileReader = csv.DictReader(csvFile, fieldnames=columnHeaders)

        for row in fileReader:
            # Ignore the header
            if not (row[columnHeaders[0]] == columnHeaders[0]) and not (row[columnHeaders[1]] == columnHeaders[1]):
                print('{} has a salary of {}.'.format(row[columnHeaders[0]], row[columnHeaders[1]]))

def main():
    while True:
        print(breakBetweenLines)
        print('1) Add to file')
        print('2) View all records')
        print('3) Quit program')
        print(breakBetweenLines)
        selection = input('Select an operation: ')
        if selection == '1':
            addNameAndSalary()
        elif selection == '2':
            viewFile()
        elif selection == '3':
            print('Exiting...')
            sys.exit(0)
        else:
            print('Invalid operation selected...')


main()