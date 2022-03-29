'''
Adapt program 102 to display the names and ages of all the people in
the list but do not show their shoe size.
'''

list = {}
for i in range(0, 4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe size: "))
    list[name] = {"Age": age, "Shoe size": shoe}

ask = input("Enter a name to see details: ")

print( "{} is {} years old.".format(ask, list[ask]['Age'])  )
