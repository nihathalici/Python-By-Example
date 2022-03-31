'''
AS-110
Using the Names.txt file you created earlier, display the list of
names in Python. Ask the user to type in one of the names and then
save all the names except the one they entered into a new file called
Names2.txt.
'''
#####
# Python By Example
# Exercise 110
# Christopher Hagan
#####

namesContent = open('AS_Names.txt', 'r').readlines()

print('The current content of the "Names.txt" file is : \n')
for line in namesContent:
    print(line, end="")

validName = False
while not validName:
    nameToRemove = input('Which name should be removed when making "Names2.txt" : ')
    for line in namesContent:
        # Compensate for all the new lines
        if nameToRemove == line.replace('\n', ''):
            validName = True
            namesContent.remove(line)
    if not validName:
        print('This name was not present in the file "Names.txt", please try again...')

newFile = open('AS_Names2.txt', 'w')
for line in namesContent:
    newFile.write(line)

newFile.close()
