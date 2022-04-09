'''
AS-123
In Python, it is not technically possible to directly
delete a record from a .csv file. Instead you need
to save the file to a temporary list in Python,
make the changes to the list and then overwrite
the original file with the temporary list.
Change the previous program to allow you to do
this. Your menu should now look like this:

  1) Add to file
  2) View all records
  3) Delete a record
  4) Quit program

  Enter the number of your selection:
'''
#####
# Python By Example
# Exercise 123
# Christopher Hagan
#####

import csv, os, sys

fileName = 'salaries.csv'
columnHeaders = ['Name', 'Salary']
breakBetweenLines = ('-------')

def addToFile():
    newEntry = {}
    newEntry[columnHeaders[0]] = input('Enter the new name to add : ')
    newEntry[columnHeaders[1]] = input('And their salary is : ')
    fileAlreadyExists = os.path.isfile(fileName)
    with open(fileName, 'a') as csvFile:
        fileWriter = csv.DictWriter(csvFile, fieldnames=columnHeaders)
        if not fileAlreadyExists:
            fileWriter.writeheader()
        fileWriter.writerow(newEntry)
    print(breakBetweenLines)
    print('{} was added to the file...'.format(newEntry[columnHeaders[0]]))


def viewFile():
    with open(fileName, 'r') as csvFile:
        fileReader = csv.DictReader(csvFile, fieldnames=columnHeaders)

        for row in fileReader:
            if not (row[columnHeaders[0]] == columnHeaders[0]) and not (row[columnHeaders[1]] == columnHeaders[1]):
                print('{} has a salary of {} per annum.'.format(row[columnHeaders[0]], row[columnHeaders[1]])) 


def deleteFromFile():
    listOfItems = []
    with open(fileName, 'r') as csvFile:
        fileReader = csv.DictReader(csvFile, fieldnames=columnHeaders)
        for row in fileReader:
            listOfItems.append(row)
    
    # Start at 1 because the header should be ignored
    for i in range(1, len(listOfItems)):
        print('{} - Name: {}, Salary: {}'.format(i, listOfItems[i][columnHeaders[0]], listOfItems[i][columnHeaders[1]]))
    
    print(breakBetweenLines)
    itemToDelete = input('Enter the number of the record to delete : ')
    print(breakBetweenLines)
    if itemToDelete.isdigit() and (int(itemToDelete) > 0) and (int(itemToDelete) < len(listOfItems)):
        userRemoved = listOfItems[int(itemToDelete)][columnHeaders[0]]
        del listOfItems[int(itemToDelete)]
        with open(fileName, 'w') as csvFile:
            fileWriter = csv.DictWriter(csvFile, fieldnames=columnHeaders)
            for row in listOfItems:
                fileWriter.writerow(row)
        print('{} was removed from the file...'.format(userRemoved))
    else:
        print('Invalid selection, nothing was removed from the file...')

def main():
    while True:
        print(breakBetweenLines)
        print('1) Add to file')
        print('2) View records in file')
        print('3) Delete a record from the file')
        print('4) Quit program')
        print(breakBetweenLines)
        selection = input('Please enter a valid selection: ')
        print(breakBetweenLines)
        if selection == '1':
            addToFile()
        elif selection == '2':
            viewFile()
        elif selection == '3':
            deleteFromFile()
        elif selection == '4':
            print('Exiting on user request...')
            sys.exit(0)
        else:
            print('Invalid selection, please try again!')

main()

