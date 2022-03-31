'''
AS-109
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

#####
# Python By Example
# Exercise 109
# Christopher Hagan
#####

fileName = 'AS_Subject.txt'

print("""Choose an operation:
1) Create a new file
2) Display the file
3) Add a new item to an existing file""")

operation = 0
while operation not in (1, 2, 3):
    operation = int(input('Make a selection 1, 2 or 3: '))
    if operation not in (1, 2, 3):
        print('Invalid selection, please try again!')

if operation == 1:
    subject = input('Please enter a school subject: ')
    file = open(fileName, 'w')
    file.write('{}\n'.format(subject))
if operation == 2:
    file = open(fileName, 'r')
    print('The contents of the file {} are: \n\n{}'.format(fileName, file.read()))
if operation == 3:
    newSubject = input('Please enter a new subject: ')
    file = open(fileName, 'a')
    file.write('{}\n'.format(newSubject))
    file.close()
    file = open(fileName, 'r')
    print('The contents of the file {} are: \n\n{}'.format(fileName, file.read()))
file.close()
