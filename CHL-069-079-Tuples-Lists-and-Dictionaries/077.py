'''
Change program 076 so that once the user has completed their list of names,
display the full list and ask them to type in one of the names on the list.
Display the position of that name in the list. Ask the user if they still
want that person to come to the party. If they answer “no”, delete that entry
from the list and display the list again.
'''
name1 = input("Enter a name of somebody you want to invite to your party: ")
name2 = input("Enter a another name: ")
name3 = input("Enter third name: ")
party = [name1, name2, name3]
for name in party:
    print(name)
pick = input("Pick a name: ")
print("{} is on the list index {}.".format(pick, party.index(pick)))
choice = input("Do you still want that person to come to the party? (y/n) ")

if choice == 'n':
    party.remove(pick)

for name in party:
    print(name)

    

