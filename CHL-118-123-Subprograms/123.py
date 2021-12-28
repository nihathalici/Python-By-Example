'''
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
import csv

def addtofile():
    file = open("Salaries.csv", "a")
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))
    newrecord = name + ", " + str(salary) + "\n"
    file.write(newrecord)
    file.close()

def viewrecords():
    file = open("Salaries.csv", "r")
    for row in file:
        print(row)
    file.close()

def deleterecord():
    file = open("Salaries.csv", "r")
    x = 0
    tmplist = []
    for row in file:
        tmplist.append(row)
    file.close()
    for row in tmplist:
        print(x, row)
        x += 1
    rowdelete = int(input("Enter the row number to delete: "))
    del tmplist[rowdelete]
    file = open("Salaries.csv", "w")
    for row in tmplist:
        file.write(row)
    file.close()

def main():
    tryagain = True
    while tryagain == True:
        print("1) Add to file")
        print("2) View all records")
        print("3) Delete a record")
        print("4) Quit program")
        print()
        selection = input("Enter the number of your selection: ")
        print()
        if selection == "1":
            addtofile()
        elif selection == "2":
            viewrecords()
        elif selection == "3":
            deleterecord()
        elif selection == "4":
            tryagain == "False"
        else:
            print("Incorrect option")

main()
