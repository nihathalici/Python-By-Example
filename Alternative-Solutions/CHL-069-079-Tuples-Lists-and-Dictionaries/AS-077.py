'''
AS-077
Change program 076 so that once the user has completed their list of names,
display the full list and ask them to type in one of the names on the list.
Display the position of that name in the list. Ask the user if they still
want that person to come to the party. If they answer “no”, delete that entry
from the list and display the list again.
'''
#####
# Python By Example
# Exercise 077
# Christopher Hagan
#####

attendees = []
for i in range(0, 3):
    attendees.append(input('Enter the name of someone to invite to a party: '))

addAnother = 'y'
while addAnother.lower().startswith('y'):
    addAnother = input('Would you like to add another guest: ')
    if addAnother.startswith('y'):
        attendees.append(input('Enter the name of another guest to invite to the party: '))

print('You have invited {} people to your party!'.format(len(attendees)))
print(attendees)

choosenAttendee = input('Enter the name of a guest: ')
print('This guest has index {} in the list'.format(attendees.index(choosenAttendee)))
deleteAttendee = input('Would you still like this guest to attend the party? ')

if deleteAttendee.lower().startswith('n'):
    attendees.remove(choosenAttendee)

print(attendees)
        














