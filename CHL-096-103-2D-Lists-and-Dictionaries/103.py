'''
0
04
After gathering the four names, ages and shoe sizes, ask the
user to enter the name of the person they want to remove from
the list. Delete this row from the data and display the other rows
on separate lines.


'''
list = {}
for i in range(0, 4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe size: "))
    list[name] = {"Age": age, "Shoe size": shoe}

ask = input("Enter a name to see details: ")

print( "{} is {} years old.".format(ask, list[ask]['Age'])  )


