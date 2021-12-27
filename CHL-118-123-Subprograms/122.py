'''
Create the following menu:
  1) Add to file
  2) View all records
  3) Quit program
If the user selects 1, allow them to add to a file called Salaries.csv which will store their name
and salary. If they select 2 it should display all records in the Salaries.csv file. If they select 3
it should stop the program. If they select an incorrect option they should see an error message.
They should keep returning to the menu until they select option 3.
'''

import csv

def addtofile():
    file = open("Salaries.csv", "a")
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))
    newrecord = name + ", " + str(salary) + "\n"
    file.write(str(newrecord))
    file.close()

def viewrecords():
    file = open("Salaries.csv", "r")
    for row in file:
        print(row)
    file.close()

def main():
    tryagain = True
    while tryagain == True:
        print("1) Add to file")
        print("2) View all records")
        print("3) Quit program")
        print()
        selection = input("Enter the number of your selection: ")
        print()
        if selection == "1":
            addtofile()
        elif selection == "2":
            viewrecords()
        elif selection == "3":
            tryagain = False
        else:
            print("Incorrect option")

main()
