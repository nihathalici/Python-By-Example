'''
Display the following menu to the user:
    1) Create a new file
    2) Display the file
    3) Add a new item to the file
    Make a selection 1, 2 or 3:
    
Ask the user to enter 1, 2 or 3. If they select
anything other than 1, 2 or 3 it should display a
suitable error message.

If they select 1, ask the user to enter a school
subject and save it to a new file called
“Subject.txt”. It should overwrite any existing file
with a new file.

If they select 2, display the contents of the
“Subject.txt” file.

If they select 3, ask the user to enter a new
subject and save it to the file and then display
the entire contents of the file.

Run the program several times to test the
options.
'''

sel = int(input('''
    1) Create a new file
    2) Display the file
    3) Add a new item to the file
    Make a selection 1, 2 or 3:
'''))

if sel == 1:
    subj = input("Enter a school subject: ")
    file = open("Subject.txt", "w")
    file.write(subj)
    file.close()

elif sel == 2:
    file = open("Subject.txt", "r")
    print(file.read())

elif sel == 3:
    new_subj = input("Enter a new school subject: ")
    file = open("Subject.txt", "a")
    file.write(new_subj + "\n")
    file.close()

    file = open("Subject.txt", "r")
    print(file.read())
    file.close()

else:
    print("Error. Make a selection 1, 2 or 3. Try again!")
