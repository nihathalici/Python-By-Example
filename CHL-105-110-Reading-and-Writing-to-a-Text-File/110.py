'''
Using the Names.txt file you created earlier, display the list of
names in Python. Ask the user to type in one of the names and then
save all the names except the one they entered into a new file called
Names2.txt.
'''
file = open("Names.txt", "r")
print(file.read())
file.close()

file = open("Names.txt", "r")
selectedname = input("Enter a name from the list: ")
selectedname = selectedname + "\n"
for row in file:
    if row != selectedname:
        file = open("Names2.txt", "a")
        newrecord = row
        file.write(newrecord)
        file.close()
file.close()


