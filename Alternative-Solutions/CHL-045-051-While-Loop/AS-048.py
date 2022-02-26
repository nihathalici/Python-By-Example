
'''
AS-048
Ask for the name of somebody the user wants to invite to a party.
After this, display the message “[name] has now been invited” and
add 1 to the count. Then ask if they want to invite somebody else.
Keep repeating this until they no longer want to invite anyone else
to the party and then display how many people they have coming to the party.
'''

#####
# Python By Example
# Exercise 048
# Christopher Hagan
#####

total = 0
addAnother = 'y'

while addAnother.lower().startswith('y'):
    name = input('Enter the name of someone who you would like to invite to your party: ')
    total += 1
    print('{} has been invited to your party'.format(name))
    addAnother = input('Would you like to invite someone else: ')

print('The total number of people coming to your party is {}.'.format(total))
