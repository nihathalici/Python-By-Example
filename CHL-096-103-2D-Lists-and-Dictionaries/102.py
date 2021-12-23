'''
Ask the user to enter the name, age and shoe size for four people. Ask for the name
of one of the people in the list and display their age and shoe size.
'''
list = {}
for i in range(0, 4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe size: "))
    list[name] = {"Age": age, "Shoe size": shoe}

ask = input("Enter a name to see details: ")
print(list[ask])
